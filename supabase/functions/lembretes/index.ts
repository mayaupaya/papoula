// Papoula: resumo diário de lembretes por push (08h de Brasília)
import { createClient } from "npm:@supabase/supabase-js@2";
import webpush from "npm:web-push@3.6.7";

const VAPID_PUBLIC = "BJmW3nhjERoub6f99eOPLwHvV0JmtIj3PTVESteEwuy5hAG9FHwiyuxmYHOAvKC8WZ-uot27Al6SfTBtQc7n6fI";
const cors = {
  "Access-Control-Allow-Origin": "*",
  "Access-Control-Allow-Headers": "authorization, x-client-info, apikey, content-type",
  "Access-Control-Allow-Methods": "POST, OPTIONS",
};
const json = (o: unknown, status = 200) =>
  new Response(JSON.stringify(o), { status, headers: { ...cors, "Content-Type": "application/json" } });

Deno.serve(async (req) => {
  if (req.method === "OPTIONS") return new Response("ok", { headers: cors });
  const priv = Deno.env.get("VAPID_PRIVATE");
  if (!priv) return json({ erro: "Falta o segredo VAPID_PRIVATE" }, 500);
  webpush.setVapidDetails("mailto:avisos@papoula.app", VAPID_PUBLIC, priv);
  let key = Deno.env.get("SUPABASE_SERVICE_ROLE_KEY") ?? Deno.env.get("SUPABASE_SECRET_KEY") ?? "";
  if (!key) { try { const k = JSON.parse(Deno.env.get("SUPABASE_SECRET_KEYS") ?? "{}"); key = Object.values(k)[0] as string ?? ""; } catch (_) { /* nada */ } }
  if (!key) return json({ erro: "Sem chave de servidor no ambiente" }, 500);
  console.log("chave:", key.slice(0, 9));
  const db = createClient(Deno.env.get("SUPABASE_URL")!, key, { auth: { persistSession: false } });

  let body: Record<string, unknown> = {};
  try { body = await req.json(); } catch (_) { /* vazio */ }
  const teste = body.teste === true;
  let dona: string | null = null;
  if (teste) {
    const jwt = (req.headers.get("authorization") ?? "").replace(/^Bearer\s+/i, "");
    if (!jwt || jwt.startsWith("sb_")) { console.log("teste sem sessão: header", jwt ? jwt.slice(0, 14) : "vazio"); return json({ erro: "Sem sessão no pedido" }, 401); }
    let uid: string | null = null;
    // 1) Confere a assinatura do token pelo próprio banco (RLS) e pega a dona dos aparelhos dela
    let pub = Deno.env.get("SUPABASE_ANON_KEY") ?? "";
    try { const k = JSON.parse(Deno.env.get("SUPABASE_PUBLISHABLE_KEYS") ?? "{}"); pub = (Object.values(k)[0] as string) || pub; } catch (_) { /* nada */ }
    const dela = createClient(Deno.env.get("SUPABASE_URL")!, pub, { auth: { persistSession: false }, global: { headers: { Authorization: `Bearer ${jwt}` } } });
    const r0 = await dela.from("push_subs").select("owner").limit(1);
    if (r0.data && r0.data.length) uid = r0.data[0].owner; else console.log("rls sem linhas:", r0.error?.message ?? "0 linhas");
    const r1 = uid ? { data: { user: { id: uid } }, error: null } : await db.auth.getUser(jwt);
    if (r1.data?.user) uid = r1.data.user.id; else console.log("getUser falhou:", r1.error?.message);
    if (!uid) {
      const r2 = await fetch(`${Deno.env.get("SUPABASE_URL")}/auth/v1/user`, { headers: { apikey: pub, Authorization: `Bearer ${jwt}` } });
      if (r2.ok) uid = (await r2.json()).id; else console.log("auth/v1/user falhou:", r2.status, (await r2.text()).slice(0, 200));
    }
    if (!uid) return json({ erro: "Faça login de novo" }, 401);
    dona = uid;
  }

  const hoje = new Intl.DateTimeFormat("en-CA", { timeZone: "America/Sao_Paulo" }).format(new Date());
  let q = db.from("push_subs").select("id, owner, sub, ultimo");
  if (dona) q = q.eq("owner", dona);
  const { data: subs, error } = await q;
  if (error) return json({ erro: error.message }, 500);

  const donas = [...new Set((subs ?? []).map((s) => s.owner))];
  const { data: cfgs } = donas.length
    ? await db.from("config").select("owner, dados").in("owner", donas)
    : { data: [] };
  const contagem: Record<string, [number, number]> = {};
  for (const c of cfgs ?? []) {
    const dias: Record<string, number> = c.dados?.resumo?.dias ?? {};
    let h = 0, a = 0;
    for (const [d, n] of Object.entries(dias)) {
      if (d === hoje) h += n; else if (d < hoje) a += n;
    }
    contagem[c.owner] = [h, a];
  }

  let enviados = 0, removidos = 0, pulados = 0;
  for (const s of subs ?? []) {
    if (!teste && s.ultimo === hoje) { pulados++; continue; }
    const [h, a] = contagem[s.owner] ?? [0, 0];
    if (!teste && h + a === 0) { pulados++; continue; }
    const partes = [];
    if (h) partes.push(`${h} ${h === 1 ? "lembrete" : "lembretes"} para hoje`);
    if (a) partes.push(`${a} ${a === 1 ? "atrasado" : "atrasados"}`);
    const texto = teste
      ? `Teste: os avisos estão funcionando. ${partes.length ? "Agora: " + partes.join(" e ") + "." : "Nada pendente agora."}`
      : `Bom dia! Você tem ${partes.join(" e ")}.`;
    try {
      await webpush.sendNotification(s.sub, JSON.stringify({ title: "Papoula", body: texto, tag: teste ? "papoula-teste" : "papoula-dia" }), { TTL: 6 * 3600 });
      enviados++;
      if (!teste) await db.from("push_subs").update({ ultimo: hoje }).eq("id", s.id);
    } catch (e) {
      const code = (e as { statusCode?: number }).statusCode;
      if (code === 404 || code === 410) { await db.from("push_subs").delete().eq("id", s.id); removidos++; }
      else console.error("push falhou", code, String(e));
    }
  }
  return json({ hoje, enviados, removidos, pulados });
});
