# Papoula

App de gestão de prática para Roberta Albuquerque (enfermeira obstétrica, doula e artista gestacional), mais a marca e o case de design.

## Estrutura
- `app/`: PWA em um arquivo (index.html, manifest, sw.js, assets). Publicado no Cloudflare Pages, projeto `app-papoula`, em https://app.escolapapoula.com
- `supabase/functions/lembretes/`: Edge Function dos avisos push diários (08h de Brasília)
- `docs/infra.md`: onde está cada coisa (hospedagem, domínio, banco, agendamento)
- `case/`: dados e imagens do case de portfólio (brand.upaya.design) e o gerador dos diagramas

## Publicar o app
Zip com `index.html`, `manifest.webmanifest`, `sw.js` e `assets` e envio por Direct Upload no Cloudflare Pages.
```
cd app && zip -qr ../papoula-app.zip index.html manifest.webmanifest sw.js assets
```

## Segredos
Nada secreto neste repositório. A chave do Supabase no app é a publishable key (pública por design, protegida por RLS). `VAPID_PRIVATE` fica só em Edge Functions > Secrets no Supabase.

## Dados de clientes
Nunca versionar conversas, planilhas ou exportações de gestantes. Ver `.gitignore`.
