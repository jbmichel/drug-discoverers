#!/usr/bin/env python3
"""Render questions.yaml as a browsable page. Regenerate after editing the bank."""
import html, json, pathlib, sys
import yaml

HERE = pathlib.Path(__file__).parent
bank = yaml.safe_load((HERE / "questions.yaml").read_text())

def esc(s): return html.escape((s or "").strip())

cards = []
for c in bank["cards"]:
    cards.append({
        "id": c["id"], "gate": c.get("gate"), "dim": c["dimension"],
        "dimLabel": bank["dimensions"][c["dimension"]],
        "q": esc(c["question"]), "persona": esc(c["persona"]),
        "principle": esc(c.get("principle", "")),
        "evidence": [esc(e) for e in c.get("evidence", [])],
        "good": esc(c.get("good_evidence", "")),
        "absence": esc(c.get("absence_means", "")),
        "tells": [esc(t) for t in c.get("weak_answer_tells", [])],
        "source": esc(c["source"]),
        "fires": [f.lower() for f in c.get("fires_when", [])],
    })

DATA = json.dumps({"cards": cards, "dimensions": bank["dimensions"],
                   "tree": bank.get("tag_tree", {})}, ensure_ascii=False)

TPL = r"""<title>Discoverer Question Bank</title>
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Serif:wght@400;500;600&display=swap">
<style>
:root{
 --ground:#EEF1F0;--surface:#FFF;--surface2:#F6F8F7;
 --ink:#141F1E;--ink2:#394B49;--muted:#5F706E;
 --rule:#D7DEDC;--rule2:#BFCAC8;
 --accent:#1B4D4B;--accent-soft:#E2EDEB;
 --gate:#9B3A22;--gate-soft:#F7E7E1;
 --shadow:0 1px 2px rgba(20,31,30,.05),0 10px 26px -14px rgba(20,31,30,.22);
}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){
 --ground:#0A1211;--surface:#121C1B;--surface2:#172221;
 --ink:#E7EDEB;--ink2:#BCC9C7;--muted:#83958F;
 --rule:#223130;--rule2:#324644;
 --accent:#63B3AA;--accent-soft:#10302E;
 --gate:#DD8163;--gate-soft:#331812;
 --shadow:0 1px 2px rgba(0,0,0,.45),0 12px 30px -16px rgba(0,0,0,.8);
}}
:root[data-theme="dark"]{
 --ground:#0A1211;--surface:#121C1B;--surface2:#172221;
 --ink:#E7EDEB;--ink2:#BCC9C7;--muted:#83958F;
 --rule:#223130;--rule2:#324644;
 --accent:#63B3AA;--accent-soft:#10302E;
 --gate:#DD8163;--gate-soft:#331812;
 --shadow:0 1px 2px rgba(0,0,0,.45),0 12px 30px -16px rgba(0,0,0,.8);
}
*{box-sizing:border-box}
body{margin:0;background:var(--ground);color:var(--ink);
 font-family:"IBM Plex Sans",system-ui,sans-serif;font-size:16px;line-height:1.6;
 -webkit-font-smoothing:antialiased}
.wrap{max-width:860px;margin:0 auto;padding:0 20px 96px}
.mono{font-family:"IBM Plex Mono",ui-monospace,monospace}
.lbl{font-family:"IBM Plex Mono",monospace;font-size:.67rem;letter-spacing:.13em;
 text-transform:uppercase;color:var(--muted)}
header{padding:34px 0 8px}
h1{font-family:"IBM Plex Serif",Georgia,serif;font-weight:600;font-size:1.95rem;
 margin:0 0 6px;letter-spacing:-.015em}
.sub{color:var(--ink2);max-width:62ch;margin:0}
.stats{display:flex;flex-wrap:wrap;gap:22px;margin:20px 0 0;padding:14px 0;
 border-top:1px solid var(--rule);border-bottom:1px solid var(--rule)}
.stat b{font-family:"IBM Plex Serif",serif;font-size:1.35rem;font-weight:600;
 display:block;line-height:1.1;font-variant-numeric:tabular-nums}
.note{margin:18px 0 0;padding:12px 14px;background:var(--surface2);
 border:1px solid var(--rule);border-radius:2px;font-size:.87rem;color:var(--ink2)}
.controls{position:sticky;top:0;z-index:9;background:color-mix(in srgb,var(--ground) 94%,transparent);
 backdrop-filter:blur(9px);border-bottom:1px solid var(--rule);
 padding:12px 0;margin:22px 0 0;display:flex;flex-wrap:wrap;gap:8px;align-items:center}
.chip{font-family:inherit;font-size:.78rem;padding:5px 11px;border-radius:2px;cursor:pointer;
 border:1px solid var(--rule2);background:var(--surface);color:var(--ink2)}
.chip[aria-pressed="true"]{border-color:var(--accent);color:var(--accent);background:var(--accent-soft);font-weight:500}
.chip:focus-visible,input:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
input[type=search]{flex:1;min-width:170px;padding:6px 11px;border-radius:2px;
 border:1px solid var(--rule2);background:var(--surface);color:var(--ink);
 font-family:inherit;font-size:.82rem}
.count{margin-left:auto;font-size:.72rem;color:var(--muted);font-family:"IBM Plex Mono",monospace}
h2.sec{font-family:"IBM Plex Serif",serif;font-size:1.28rem;font-weight:600;
 margin:38px 0 4px;letter-spacing:-.01em}
.secnote{color:var(--muted);font-size:.87rem;margin:0 0 14px;max-width:60ch}
/* gate ladder: a real ordered sequence, so it is numbered and railed */
.gate-group{position:relative;padding-left:44px;margin-top:18px}
.gate-group::before{content:"";position:absolute;left:15px;top:6px;bottom:6px;
 width:2px;background:linear-gradient(var(--gate),var(--rule))}
.gate-num{position:absolute;left:0;top:0;width:32px;height:32px;border-radius:50%;
 display:grid;place-items:center;background:var(--gate-soft);color:var(--gate);
 border:1.5px solid var(--gate);font-family:"IBM Plex Serif",serif;font-weight:600;font-size:.95rem}
.gate-title{font-size:.86rem;color:var(--gate);font-weight:500;margin:6px 0 12px}
.card{background:var(--surface);border:1px solid var(--rule);border-radius:3px;
 box-shadow:var(--shadow);padding:20px 22px;margin:0 0 14px}
.card.gate{border-left:3px solid var(--gate)}
.q{font-family:"IBM Plex Serif",Georgia,serif;font-size:1.13rem;line-height:1.42;
 font-weight:500;margin:0 0 10px;text-wrap:balance}
.attr{display:flex;flex-wrap:wrap;gap:8px;align-items:baseline;margin-bottom:12px}
.persona{font-family:"IBM Plex Mono",monospace;font-size:.75rem;color:var(--accent);
 background:var(--accent-soft);padding:2px 8px;border-radius:2px;
 border:1px solid color-mix(in srgb,var(--accent) 28%,transparent)}
.dimtag{font-family:"IBM Plex Mono",monospace;font-size:.67rem;letter-spacing:.09em;
 text-transform:uppercase;color:var(--muted)}
.principle{color:var(--ink2);font-size:.93rem;margin:0 0 14px}
.field{margin-top:13px}
.field .lbl{display:block;margin-bottom:5px}
.field p{margin:0;font-size:.92rem;color:var(--ink2)}
.evid{display:flex;flex-wrap:wrap;gap:5px}
.evid span{font-family:"IBM Plex Mono",monospace;font-size:.71rem;padding:3px 8px;
 border-radius:2px;background:var(--surface2);border:1px solid var(--rule);color:var(--ink2)}
/* the field that matters most gets the only coloured rule in the card */
.absence{border-left:2px solid var(--gate);padding-left:12px;background:var(--gate-soft);
 padding:10px 12px;border-radius:0 2px 2px 0}
.absence .lbl{color:var(--gate)}
.absence p{color:var(--ink)}
ul.tells{margin:0;padding-left:18px}
ul.tells li{font-size:.89rem;color:var(--ink2);margin-bottom:3px}
.src{margin-top:15px;padding-top:11px;border-top:1px solid var(--rule);
 font-family:"IBM Plex Mono",monospace;font-size:.69rem;color:var(--muted);word-break:break-word}
.fires{font-family:"IBM Plex Mono",monospace;font-size:.67rem;color:var(--gate);
 letter-spacing:.06em;text-transform:uppercase}
.empty{padding:40px 0;text-align:center;color:var(--muted)}
footer{margin-top:44px;padding-top:20px;border-top:1px solid var(--rule);
 font-size:.83rem;color:var(--muted)}
@media (prefers-reduced-motion:reduce){*{transition:none!important}}
@media (max-width:560px){.wrap{padding:0 14px 70px}h1{font-size:1.6rem}
 .gate-group{padding-left:34px}.gate-group::before{left:11px}
 .gate-num{width:24px;height:24px;font-size:.8rem}.card{padding:16px}}
</style>

<div class="wrap">
<header>
  <div class="lbl">Persona question bank &middot; v0</div>
  <h1>Discoverer Question Bank</h1>
  <p class="sub">Questions 31 named drug discoverers would ask of a new indication &mdash;
  used as the research agenda that builds the dossier, not as a critique of one that exists.</p>
  <div class="stats">
    <div class="stat"><b id="s-cards">0</b><span class="lbl">questions</span></div>
    <div class="stat"><b id="s-gates">0</b><span class="lbl">kill gates</span></div>
    <div class="stat"><b id="s-dims">0</b><span class="lbl">dimensions</span></div>
    <div class="stat"><b id="s-people">0</b><span class="lbl">personas</span></div>
  </div>
  <p class="note"><b>Personas are reconstructions from public writing, not the people.</b>
  Every card carries its source so any attribution can be checked &mdash; an unattributed
  card is a generic checklist item and gets deleted. This v0 is hand-built from the
  Grade&nbsp;A source manifest, before any crawling; it is a schema test, not a finished bank.</p>
</header>

<div class="controls">
  <button class="chip" data-tag="" aria-pressed="true">All modalities</button>
  <button class="chip" data-tag="oncology" aria-pressed="false">Oncology</button>
  <button class="chip" data-tag="antibacterial" aria-pressed="false">Antibacterial</button>
  <button class="chip" data-tag="genetic medicine" aria-pressed="false">Genetic medicine</button>
  <button class="chip" data-tag="cell therapy" aria-pressed="false">Cell therapy</button>
  <button class="chip" id="gatesOnly" aria-pressed="false">Gates only</button>
  <input type="search" id="q" placeholder="Search question, persona, source&hellip;" aria-label="Search">
  <span class="count" id="count"></span>
</div>

<main id="out"></main>

<footer>
  Generated from <span class="mono">dossier/questions.yaml</span> by
  <span class="mono">dossier/build_page.py</span>. Editing the bank and re-running
  regenerates this page.
</footer>
</div>

<script id="bank" type="application/json">__DATA__</script>
<script>
(function(){
"use strict";
var B=JSON.parse(document.getElementById("bank").textContent);
var CARDS=B.cards, DIMS=B.dimensions, TREE=B.tree;
var tag="", gatesOnly=false, query="";

function norm(s){return s.trim().toLowerCase().replace(/[_-]/g," ");}
function close(tags){
  var kids={},parents={};
  Object.keys(TREE||{}).forEach(function(p){
    kids[norm(p)]=(TREE[p]||[]).map(norm);
    kids[norm(p)].forEach(function(c){parents[c]=norm(p);});
  });
  var out={};
  tags.map(norm).forEach(function(t){
    out[t]=1;(kids[t]||[]).forEach(function(k){out[k]=1;});
    while(parents[t]){t=parents[t];out[t]=1;}
  });
  return out;
}
function fires(c){
  if(!c.fires||!c.fires.length) return true;
  if(!tag) return true;
  var a=close(c.fires), b=close([tag]);
  return Object.keys(a).some(function(k){return b[k];});
}
function matches(c){
  if(gatesOnly && !c.gate) return false;
  if(!fires(c)) return false;
  if(!query) return true;
  var hay=(c.q+" "+c.persona+" "+c.source+" "+c.principle+" "+c.dimLabel).toLowerCase();
  return hay.indexOf(query)>-1;
}
function el(t,cls,txt){var e=document.createElement(t);if(cls)e.className=cls;
  if(txt!==undefined)e.innerHTML=txt;return e;}

function card(c){
  var d=el("div","card"+(c.gate?" gate":""));
  d.appendChild(el("p","q",c.q));
  var attr=el("div","attr");
  attr.appendChild(el("span","persona",c.persona));
  attr.appendChild(el("span","dimtag",c.dim.replace("_"," ")));
  if(c.fires.length) attr.appendChild(el("span","fires","fires: "+c.fires.join(" / ")));
  d.appendChild(attr);
  if(c.principle) d.appendChild(el("p","principle",c.principle));
  if(c.evidence.length){
    var f=el("div","field");f.appendChild(el("span","lbl","Where to look"));
    var ev=el("div","evid");
    c.evidence.forEach(function(e){ev.appendChild(el("span",null,e));});
    f.appendChild(ev);d.appendChild(f);
  }
  if(c.good){var f2=el("div","field");f2.appendChild(el("span","lbl","What would count"));
    f2.appendChild(el("p",null,c.good));d.appendChild(f2);}
  if(c.absence){var f3=el("div","field absence");
    f3.appendChild(el("span","lbl","If nothing is found"));
    f3.appendChild(el("p",null,c.absence));d.appendChild(f3);}
  if(c.tells.length){var f4=el("div","field");
    f4.appendChild(el("span","lbl","Weak-answer tells"));
    var ul=el("ul","tells");
    c.tells.forEach(function(t){ul.appendChild(el("li",null,t));});
    f4.appendChild(ul);d.appendChild(f4);}
  d.appendChild(el("div","src","source: "+c.source));
  return d;
}

function render(){
  var out=document.getElementById("out");out.textContent="";
  var vis=CARDS.filter(matches);
  document.getElementById("count").textContent=vis.length+" of "+CARDS.length+" shown";

  var gates=vis.filter(function(c){return c.gate;});
  if(gates.length){
    out.appendChild(el("h2","sec","Kill gates"));
    out.appendChild(el("p","secnote","Answered in order, cheapest disqualifying question first. Abandoning at a gate is a successful outcome &mdash; the ordering exists so a dead indication costs a day instead of a quarter."));
    var nums=[];gates.forEach(function(c){if(nums.indexOf(c.gate)<0)nums.push(c.gate);});
    nums.sort(function(a,b){return a-b;}).forEach(function(n){
      var g=el("div","gate-group");
      g.appendChild(el("div","gate-num",String(n)));
      var inGate=gates.filter(function(c){return c.gate===n;});
      g.appendChild(el("div","gate-title",inGate[0].dimLabel));
      inGate.forEach(function(c){g.appendChild(card(c));});
      out.appendChild(g);
    });
  }
  var body=vis.filter(function(c){return !c.gate;});
  if(body.length){
    out.appendChild(el("h2","sec","Dossier body"));
    out.appendChild(el("p","secnote","Grouped by dimension. Each becomes a section of the dossier, with its evidence and confidence filled in &mdash; or an explicit statement that nothing was found."));
    Object.keys(DIMS).forEach(function(k){
      var grp=body.filter(function(c){return c.dim===k;});
      if(!grp.length) return;
      var h=el("h2","sec",DIMS[k]);h.style.fontSize="1.05rem";out.appendChild(h);
      grp.forEach(function(c){out.appendChild(card(c));});
    });
  }
  if(!vis.length) out.appendChild(el("div","empty","No questions match that filter."));
}

document.querySelectorAll(".chip[data-tag]").forEach(function(b){
  b.addEventListener("click",function(){
    tag=b.dataset.tag;
    document.querySelectorAll(".chip[data-tag]").forEach(function(o){
      o.setAttribute("aria-pressed",String(o===b));});
    render();
  });
});
document.getElementById("gatesOnly").addEventListener("click",function(){
  gatesOnly=!gatesOnly;this.setAttribute("aria-pressed",String(gatesOnly));render();
});
document.getElementById("q").addEventListener("input",function(){
  query=this.value.trim().toLowerCase();render();
});

document.getElementById("s-cards").textContent=CARDS.length;
document.getElementById("s-gates").textContent=
  Object.keys(CARDS.reduce(function(a,c){if(c.gate)a[c.gate]=1;return a;},{})).length;
document.getElementById("s-dims").textContent=Object.keys(DIMS).length;
document.getElementById("s-people").textContent=
  Object.keys(CARDS.reduce(function(a,c){a[c.persona]=1;return a;},{})).length;
render();
})();
</script>
"""

out = HERE / "question-bank.html"
out.write_text(TPL.replace("__DATA__", DATA), encoding="utf-8")
print(f"{len(cards)} cards -> {out} ({out.stat().st_size//1024} KB)")
