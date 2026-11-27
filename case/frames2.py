INK='#111111';G='#55554F';L='#E0DFDA';BG='#F3F3F1';RED='#111111';PRED='#AB0018';CREAM='#F4F0EC'
F="font-family:Inter,Helvetica,Arial,sans-serif;font-weight:400"
def phone(src,w=230): return f'<div style="width:{w}px;border-radius:{w*0.15:.0f}px;padding:{w*0.025:.0f}px;background:#fff;border:1px solid #DAD9D4;box-shadow:none"><img src="{src}" style="display:block;width:100%;border-radius:{w*0.125:.0f}px"></div>'
def frame(id,inner,bg=BG,pad='72px 64px',h=None): return f'<section id="{id}" style="width:1064px;box-sizing:border-box;background:{bg};padding:{pad};{F};color:{INK};{"height:"+str(h)+"px;" if h else ""}overflow:hidden;position:relative">{inner}</section>'
lab=lambda t,c=G: f'<div style="font-size:11px;font-weight:500;letter-spacing:.08em;text-transform:uppercase;color:{c}">{t}</div>'
arrowR=f'<div style="display:flex;align-items:center;justify-content:center;width:40px;flex:0 0 40px"><svg width="34" height="14" viewBox="0 0 34 14"><path d="M0 7h31M25 1l6 6-6 6" fill="none" stroke="{G}" stroke-width="1.5"/></svg></div>'
S=[]
# COVER 1064x665
S.append(frame('cover',f'''<img src="flor.png" style="position:absolute;right:-110px;top:-120px;width:430px;opacity:.95">
<div style="position:absolute;left:0;right:0;bottom:-170px;display:flex;justify-content:center;gap:34px;align-items:flex-end">
<div style="transform:translateY(40px)">{phone('ph_shot_ficha.png',250)}</div>{phone('ph_s_hoje.png',280)}<div style="transform:translateY(40px)">{phone('ph_shot_parto2.png',250)}</div></div>''',CREAM,'0',665))
# PROBLEM
nodes=[('Memory','exam windows, on-call weeks'),('WhatsApp','every message typed again'),('Intake sheet','client data no one revisits'),('Paper','labor notes by hand'),('Bank notes','installments checked one by one')]
S.append(frame('problem',f'''<div style="display:flex;justify-content:center"><div style="background:{INK};color:#fff;padding:14px 22px;border-radius:999px;font-size:15px;font-weight:600">One professional, between births</div></div>
<svg width="936" height="56" style="display:block"><path d="M468 0V28M93 28H843M93 28v28M281 28v28M468 28v28M655 28v28M843 28v28" fill="none" stroke="{L}" stroke-width="1.5"/></svg>
<div style="display:grid;grid-template-columns:repeat(5,1fr);gap:14px">{''.join(f'<div style="background:#fff;border:1px dashed #CFCEC8;border-radius:14px;padding:20px 16px;min-height:110px"><div style="font-size:23px;font-family:\'Instrument Serif\',Georgia,serif;font-weight:400;letter-spacing:0">{a}</div><div style="margin-top:8px;font-size:13px;line-height:1.45;color:{G}">{b}</div></div>' for a,b in nodes)}</div>
<div style="margin-top:34px;display:flex;justify-content:center;gap:10px;flex-wrap:wrap">{''.join(f'<div style="border:1px solid {L};background:#fff;border-radius:999px;padding:8px 14px;font-size:13px;color:{INK}">{t}</div>' for t in ['Missed exam windows','Repeated messages','No view of on-call load'])}</div>'''))
# JOURNEY
ph=[('Contract','Form, plan, contract, installments'),('Prenatal','Exams by due date, meetings, birth plan'),('Birth','On call from 37 weeks, labor record, PDF'),('Postpartum','Day 0 to 40 messages, review request')]
S.append(frame('journey',f'''<div style="display:grid;grid-template-columns:120px repeat(4,1fr);gap:0;align-items:stretch">
<div></div>{''.join(f'<div style="padding:0 10px 18px"><div style="display:flex;align-items:center;gap:10px"><span style="width:28px;height:28px;border-radius:50%;background:{INK};color:#fff;font-size:13px;font-weight:700;display:flex;align-items:center;justify-content:center">{i+1}</span><span style="font-size:24px;font-family:\'Instrument Serif\',Georgia,serif;font-weight:400;letter-spacing:0">{a}</span></div></div>' for i,(a,b) in enumerate(ph))}
<div style="padding:16px 0;border-top:1px solid {L}">{lab('She')}</div>{''.join(f'<div style="padding:16px 10px;border-top:1px solid {L};font-size:13.5px;line-height:1.45;color:{G}">{t}</div>' for t in ['Sends the intake form, agrees the plan','Keeps exam windows in her head','Goes on call, writes labor notes by hand','Follows up for 40 days, by memory'])}
<div style="padding:16px 0;border-top:1px solid {L}">{lab('The app',RED)}</div>{''.join(f'<div style="padding:16px 10px;border-top:1px solid {L};font-size:13.5px;line-height:1.45;color:{INK};font-weight:500">{b}</div>' for a,b in ph)}
<div style="padding:16px 0;border-top:1px solid {L}">{lab('Screen')}</div>{''.join(f'<div style="padding:16px 10px;border-top:1px solid {L}"><span style="display:inline-block;border:1px solid {L};background:#fff;border-radius:999px;padding:6px 12px;font-size:12.5px">{t}</span></div>' for t in ['New client · Contract','Prenatal tab','Labor tab · Partograph','Postpartum tab'])}
</div>'''))
# IA
def box(t,dark=False,w=None): return f'<div style="{"width:"+str(w)+"px;" if w else ""}background:{INK if dark else "#fff"};color:{"#fff" if dark else INK};border:1px solid {INK if dark else L};border-radius:12px;padding:12px 16px;font-size:14px;font-weight:{600 if dark else 500};text-align:center">{t}</div>'
tabs=['Today','Clients','+ New','On call','Cash']
subs={'Today':['Overdue','This week','Agenda · week / month','Leads'],'Clients':['Client file'],'+ New':['Intake link','Plan + contract'],'On call':['Load per week','Who is due'],'Cash':['Next 6 months','Late installments']}
file=['Summary','Labor','Prenatal / Postpartum','Payments','Contract']
S.append(frame('ia',f'''<div style="display:flex;justify-content:center">{box('App',True,140)}</div>
<svg width="936" height="44" style="display:block"><path d="M468 0V22M94 22H842M94 22v22M281 22v22M468 22v22M655 22v22M842 22v22" fill="none" stroke="{L}" stroke-width="1.5"/></svg>
<div style="display:grid;grid-template-columns:repeat(5,1fr);gap:14px;align-items:start">{''.join(f'<div style="display:flex;flex-direction:column;gap:8px">{box(t,True)}{"".join(f"<div style=\"font-size:12.5px;color:{G};padding:6px 10px;border-left:1.5px solid {L};margin-left:14px\">{s}</div>" for s in subs[t])}</div>' for t in tabs)}</div>
<div style="margin-top:34px;background:#fff;border:1px solid {L};border-radius:16px;padding:20px 22px">{lab('Client file · one place for everything')}<div style="margin-top:14px;display:flex;gap:8px;flex-wrap:wrap">{''.join(f'<span style="border-radius:999px;padding:8px 14px;font-size:13px;background:{INK if i==1 else BG};color:{"#fff" if i==1 else INK}">{t}</span>' for i,t in enumerate(file))}</div></div>'''))
# FLOW
st=[('ph_shot_nova.png','Intake','Form link, client fills her data'),('ph_shot_pag.png','Plan and contract','Contract and installments generated'),('ph_shot_ficha.png','Exams','Windows calculated from the due date'),('ph_s_hoje.png','Reminder','Lands on Today, message ready')]
S.append(frame('flow',f'''<div style="display:flex;align-items:flex-start;justify-content:space-between">{arrowR.join(f'<div style="width:196px;display:flex;flex-direction:column;align-items:center;gap:16px">{phone(s,196)}<div style="text-align:center"><div style="font-size:12px;font-weight:700;color:{RED}">0{i+1}</div><div style="margin-top:4px;font-size:22px;font-family:\'Instrument Serif\',Georgia,serif;font-weight:400;letter-spacing:0">{a}</div><div style="margin-top:4px;font-size:12.5px;line-height:1.4;color:{G}">{b}</div></div></div>' for i,(s,a,b) in enumerate(st))}</div>''',BG,'64px 48px'))
# PATTERN (loop)
pt=[('App flags it','in the week it matters'),('Message ready','her words, client’s number'),('She sends','from her own WhatsApp'),('Done or swiped','with undo')]
S.append(frame('pattern',f'''<div style="display:flex;align-items:center;justify-content:space-between">{arrowR.join(f'<div style="flex:1;background:#fff;border:1px solid {L};border-radius:16px;padding:22px 18px;min-height:120px;box-sizing:border-box"><div style="width:30px;height:30px;border-radius:50%;background:{RED if i==2 else INK};color:#fff;font-size:13px;font-weight:700;display:flex;align-items:center;justify-content:center">{i+1}</div><div style="margin-top:14px;font-size:22px;font-family:\'Instrument Serif\',Georgia,serif;font-weight:400;letter-spacing:0">{a}</div><div style="margin-top:4px;font-size:12.5px;color:{G}">{b}</div></div>' for i,(a,b) in enumerate(pt))}</div>
<div style="margin-top:22px;display:flex;justify-content:center;gap:24px;font-size:12.5px;color:{G}"><span><b style="color:{INK}">The system</b> prepares</span><span>·</span><span><b style="color:{RED}">The person</b> acts</span></div>''',BG,'56px 48px'))
# UI rows
def uirow(id,items,bg=BG): return frame(id,f'<div style="display:flex;justify-content:center;gap:44px;align-items:flex-start">{"".join(f"<div style=\"display:flex;flex-direction:column;align-items:center;gap:14px;{"margin-top:44px" if i==1 else ""}\">{phone(s,250)}<div style=\"font-size:13px;color:{G}\">{c}</div></div>" for i,(s,c) in enumerate(items))}</div>',bg,'64px 48px')
S.append(uirow('ui-daily',[('ph_shot_gest.png','Clients'),('ph_s_hoje.png','Today'),('ph_mes2.png','Agenda, month')]))
S.append(frame('ui-labor',f'''<div style="display:flex;justify-content:center;gap:44px;align-items:flex-start">
<div style="display:flex;flex-direction:column;align-items:center;gap:14px">{phone('ph_shot_parto.png',250)}<div style="font-size:13px;color:{G}">Labor record</div></div>
<div style="display:flex;flex-direction:column;align-items:center;gap:14px;margin-top:44px">{phone('ph_shot_parto2.png',250)}<div style="font-size:13px;color:{G}">Partograph</div></div>
<div style="display:flex;flex-direction:column;align-items:center;gap:14px"><img src="app-pdf.jpg" style="width:300px;border:1px solid {L};border-radius:8px;box-shadow:none"><div style="font-size:13px;color:{G}">PDF report, made on the phone</div></div></div>''',BG,'64px 48px'))
S.append(uirow('ui-practice',[('ph_shot_caixa.png','Cash forecast'),('ph_s_sobre.png','On-call load'),('ph_lead2.png','Leads')]))
S.append(uirow('ui-care',[('ph_shot_pos.png','Postpartum plan'),('ph_sw1.png','Swipe, with undo'),('ph_car1.png','Placenta prints')]))
# VALIDATION
ba=[('Reminders','Single dates piled up on Today','Weekly windows, one tap to move'),('Labor record','Heart rate inside the contraction entry','Two records, alert outside 110–160 bpm'),('Voice','Messages from an “app assistant”','Her own first person, sent from her WhatsApp')]
S.append(frame('validation',f'''<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:16px">{''.join(f'<div style="background:#fff;border:1px solid {L};border-radius:16px;overflow:hidden"><div style="padding:16px 18px;border-bottom:1px solid {L};font-size:22px;font-family:\'Instrument Serif\',Georgia,serif;font-weight:400;letter-spacing:0">{t}</div><div style="padding:16px 18px;border-bottom:1px solid {L}">{lab("Before")}<div style="margin-top:8px;font-size:13.5px;line-height:1.45;color:{G};text-decoration:line-through;text-decoration-color:#C9C4BF">{b}</div></div><div style="padding:16px 18px;background:#FAFAF8">{lab("After",RED)}<div style="margin-top:8px;font-size:13.5px;line-height:1.45;font-weight:600">{a}</div></div></div>' for t,b,a in ba)}</div>
<div style="margin-top:22px;display:flex;gap:10px;flex-wrap:wrap;justify-content:center">{''.join(f'<span style="border:1px solid {L};background:#fff;border-radius:999px;padding:7px 13px;font-size:12.5px;color:{INK}">{t}</span>' for t in ['Labor tab moved to 2nd','Week and month agenda','Swipe to dismiss','Leads with follow-ups'])}</div>'''))
# ARCHITECTURE
S.append(frame('arch',f'''<div style="display:flex;align-items:center;justify-content:space-between">
<div style="width:250px;background:#fff;border:1px solid {L};border-radius:16px;padding:20px">{lab('Phone')}<div style="margin-top:10px;font-size:22px;font-family:\'Instrument Serif\',Georgia,serif;font-weight:400;letter-spacing:0">Installable web app</div><div style="margin-top:6px;font-size:12.5px;line-height:1.45;color:{G}">iOS and Android. PDFs made on the device.</div></div>
{arrowR}
<div style="width:250px;background:{INK};color:#fff;border-radius:16px;padding:20px">{lab('Access','#A9A9A9')}<div style="margin-top:10px;font-size:22px;font-family:\'Instrument Serif\',Georgia,serif;font-weight:400;letter-spacing:0">Invite only</div><div style="margin-top:6px;font-size:12.5px;line-height:1.45;color:#CFCFCF">Email and password. No open sign-up.</div></div>
{arrowR}
<div style="width:250px;background:#fff;border:1px solid {L};border-radius:16px;padding:20px">{lab('Database')}<div style="margin-top:10px;font-size:22px;font-family:\'Instrument Serif\',Georgia,serif;font-weight:400;letter-spacing:0">Owner-only rows</div><div style="margin-top:6px;font-size:12.5px;line-height:1.45;color:{G}">Each professional reads and writes only her own records.</div></div></div>
<div style="margin-top:16px;display:grid;grid-template-columns:repeat(3,1fr);gap:16px">{''.join(f'<div style="border:1px dashed #CFCEC8;border-radius:14px;padding:16px 18px"><div style="font-size:20px;font-family:\'Instrument Serif\',Georgia,serif;font-weight:400;letter-spacing:0">{a}</div><div style="margin-top:6px;font-size:12.5px;line-height:1.45;color:{G}">{b}</div></div>' for a,b in [('8 am reminder','Carries counts, never client names'),('Backup','One-tap export to a file she keeps'),('Zero hosting cost','Managed services on free tiers')])}</div>
<div style="margin-top:16px;border-left:3px solid {RED};background:#fff;border-radius:0 12px 12px 0;padding:14px 18px;font-size:13.5px;line-height:1.5"><b>Clinical safety.</b> The app records and reminds; it does not diagnose. Ranges were set and reviewed by the obstetric nurse who uses it.</div>'''))
# BRAND
S.append(frame('brand-logo',f'''<div style="display:grid;grid-template-columns:1.25fr 1fr;gap:14px">
<div style="background:{CREAM};border-radius:12px;height:300px;display:flex;align-items:center;justify-content:center"><img src="logo-completa.png" style="width:320px"></div>
<div style="background:{PRED};border-radius:12px;height:300px;display:flex;align-items:center;justify-content:center"><img src="logo-empilhada-creme.png" style="width:190px"></div>
<div style="background:{INK};border-radius:12px;height:180px;display:flex;align-items:center;justify-content:center"><img src="logo-reduzida-creme.png" style="width:220px"></div>
<div style="background:#fff;border-radius:12px;height:180px;position:relative;overflow:hidden"><img src="flor.png" style="position:absolute;right:-50px;bottom:-90px;width:280px"></div></div>''',BG,'48px'))
S.append(frame('brand-system',f'''<div style="display:flex;height:140px;border-radius:12px;overflow:hidden;border:1px solid {L}">{''.join(f'<div style="flex:{fl};background:{hx};color:{fg};padding:14px;display:flex;flex-direction:column;justify-content:space-between;font-size:12px"><b style="letter-spacing:.06em;text-transform:uppercase;font-size:11px">{n}</b><span>{hx}</span></div>' for hx,n,fg,fl in [('#FFFFFF','Paper 50%',INK,5),('#AB0018','Red 20%','#fff',2),('#171313','Ink 20%','#fff',2),('#F4F0EC','Cream 10%',INK,1)])}</div>
<div style="margin-top:14px;display:grid;grid-template-columns:1fr 1fr;gap:14px">
<div style="background:#fff;border-radius:12px;padding:26px 28px;height:230px;box-sizing:border-box;display:flex;flex-direction:column;justify-content:space-between">{lab('Inter 900')}<div style="font-size:120px;line-height:.8;font-weight:900;letter-spacing:-.07em">Aa</div></div>
<div style="background:#fff;border-radius:12px;padding:26px 28px;height:230px;box-sizing:border-box;display:flex;flex-direction:column;justify-content:space-between">{lab('Georgia Italic')}<div style="font-family:Georgia,serif;font-style:italic;font-size:120px;line-height:.8;color:{PRED}">Aa</div></div></div>''',BG,'48px'))
html='<html><head><meta charset="utf-8"><style>@font-face{font-family:Inter;src:url(inter400.woff2);font-weight:400}@font-face{font-family:Inter;src:url(inter500.woff2);font-weight:500}@font-face{font-family:Inter;src:url(inter600.woff2);font-weight:600 900}@font-face{font-family:\'Instrument Serif\';src:url(is.woff2)}body{margin:0;background:#fff}section{margin:0 0 40px}</style></head><body>'+''.join(S)+'</body></html>'
open('frames.html','w').write(html)
from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    b=p.chromium.launch();pg=b.new_page(viewport={'width':1100,'height':900},device_scale_factor=2)
    pg.goto('file:///home/claude/pf/frames.html');pg.wait_for_timeout(1500)
    for id in ['cover','problem','journey','ia','flow','pattern','ui-daily','ui-labor','ui-practice','ui-care','validation','arch','brand-logo','brand-system']:
        el=pg.locator('#'+id);el.screenshot(path=f'out/{id}.png')
    b.close()
from PIL import Image
import glob
for f in glob.glob('out/*.png'):
    im=Image.open(f).convert('RGB');im.save(f[:-4]+'.jpg',quality=88);print(f,im.size)
