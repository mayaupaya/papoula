# App Papoula: onde está cada coisa

Atualizado em 18/11/2026.

- **App:** https://app.escolapapoula.com
- **Hospedagem:** Cloudflare Pages, projeto `app-papoula` (também em https://app-papoula.pages.dev). Direct Upload com zip: index.html, manifest.webmanifest, sw.js, assets. Plano grátis: 500 publicações por mês.
- **Domínio:** escolapapoula.com, DNS na HostGator. Registro `CNAME app -> app-papoula.pages.dev`, TTL 14400. Não mexer nos outros registros.
- **Endereço antigo:** https://app-papoula.netlify.app (Netlify). Não aceita publicações até 7/12 (créditos esgotados). Não publicar mais lá.
- **Banco e login:** Supabase, projeto "Papoula" (`abeowvxyikewcbiqoxkl`), região us-west-2, plano grátis. Site URL em Authentication > URL Configuration: https://app.escolapapoula.com
- **Tabelas:** `gestantes` (id, owner, nome, dpp, dados jsonb), `config` (owner, dados jsonb), `push_subs` (owner, endpoint, sub, ultimo). RLS ligado em todas: owner = auth.uid().
- **`config.dados`:** capacidade, link, contrato, pix, perfil, termo, backupEm, resumo, carimbos, leads.
- **Login:** e-mail e senha. Cadastro aberto desligado; acesso por convite ou conta criada em Authentication > Users > Add user.
- **Chave no app:** publishable key (pública por design; o RLS protege os dados). Nunca colocar a secret key no app.

## Avisos no celular (push)
- **Service worker:** `sw.js` na raiz do app. A inscrição vale por endereço: ao trocar de endereço, reinstalar o ícone e reativar os avisos. Apagar a inscrição antiga (Netlify) de `push_subs`.
- **Edge Function `lembretes`:** "Verify JWT" desligado de propósito. Modo diário (`{}`): no máximo 1 envio por dia por aparelho, só se houver lembretes. Modo teste (`{"teste":true}`): envia só para quem chamou.
- **Segredo:** `VAPID_PRIVATE` em Edge Functions > Secrets (fora do repositório).
- **Agendamento:** pg_cron, job `papoula-8h`, `0 11 * * *` (8h em Brasília), chama a função via pg_net.
- **iPhone:** só com o app instalado na tela inicial (iOS 16.4+), em Ajustes > Ativar avisos.

## Limites conhecidos
- O projeto grátis do Supabase pausa com pouca atividade (Resume project). Sem backup automático: usar Ajustes > Baixar backup.
- E-mails padrão do Supabase saem em inglês e com poucos envios por hora.
- A importação da planilha lê as colunas do formulário da Roberta.
- A mensagem longa de pós-parto ainda é o texto da Roberta.
- O termo de teste não teve revisão jurídica.
