"""Generate triage.html — a card-by-card review UI for the roster.

Reads discoverers.py, emits a self-contained page. Verdicts are stored in
the artifact `db` at triage/verdicts so they can be read back and merged
into discoverers.py.
"""

import json
import pathlib
import urllib.parse
from dataclasses import asdict

from discoverers import PEOPLE

SHORT_CATEGORY = {
    "commentary": "COMMENTARY",
    "foundational": "FOUNDATIONAL",
    "medchem": "MED CHEM",
    "oncology": "ONCOLOGY / CHEM BIO",
    "biologics": "BIOLOGICS",
    "genetic_medicine": "GENETIC MEDICINE",
    "antiviral": "ANTIVIRAL",
    "metabolic_cv": "METABOLIC / CV",
    "cns": "CNS",
    "computational": "COMPUTATIONAL",
    "strategy": "R&D STRATEGY",
}

GRADE_GLOSS = {
    "A": "Large corpus of explicit reasoning",
    "B": "Talks, reviews, interviews",
    "C": "Mostly primary papers",
}


def links_for(person):
    """Verification links. Only `url` is a verified address; the rest are
    search queries, which is the honest thing to hand a triager."""
    q = urllib.parse.quote_plus(person.name)
    out = []
    if person.url:
        host = person.url.split("//", 1)[-1].split("/", 1)[0].replace("www.", "")
        out.append({"label": host, "href": person.url, "primary": True})
    out += [
        {"label": "Wikipedia",
         "href": f"https://en.wikipedia.org/w/index.php?search={q}"},
        {"label": "Scholar",
         "href": f"https://scholar.google.com/scholar?q={q}"},
        {"label": "PubMed",
         "href": "https://pubmed.ncbi.nlm.nih.gov/?term="
                 + urllib.parse.quote_plus(person.name + "[Author]")},
        {"label": "Web",
         "href": "https://duckduckgo.com/?q="
                 + urllib.parse.quote_plus(person.name + " drug discovery")},
    ]
    return out


def build_records():
    records = []
    for i, p in enumerate(PEOPLE, start=1):
        d = asdict(p)
        d["id"] = str(i)
        d["cat_label"] = SHORT_CATEGORY.get(p.category, p.category.upper())
        d["gloss"] = GRADE_GLOSS.get(p.richness, "")
        d["artifact_tags"] = [a.replace("_", " ") for a in p.artifacts.split(";")]
        d["links"] = links_for(p)
        records.append(d)
    return records


TEMPLATE = r"""<title>Drug Discoverer Triage</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Serif:wght@500;600&display=swap">
<style>
:root {
  --ground:#F1F4F3; --surface:#FFFFFF; --surface-2:#F7F9F8;
  --ink:#121A1C; --ink-2:#3B4A4D; --muted:#637376;
  --rule:#DCE2E1; --rule-strong:#C3CDCC;
  --accent:#0E4E63; --accent-soft:#E4EFF3;
  --keep:#2E6B4A; --keep-soft:#E3F0E8;
  --unsure:#8A6512; --unsure-soft:#F5EBD8;
  --drop:#9E3B2E; --drop-soft:#F6E3E0;
  --grid:rgba(14,78,99,.05);
  --shadow:0 1px 2px rgba(18,26,28,.05), 0 8px 24px -12px rgba(18,26,28,.18);
  --step--1:.78rem; --step-0:1rem; --step-1:1.19rem; --step-2:1.5rem; --step-3:2.15rem;
}
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    --ground:#0C1113; --surface:#141B1E; --surface-2:#182124;
    --ink:#E9EEED; --ink-2:#BCC8C9; --muted:#87989B;
    --rule:#232F32; --rule-strong:#33454A;
    --accent:#63B7D3; --accent-soft:#12303B;
    --keep:#79C295; --keep-soft:#15301F;
    --unsure:#DCAE5C; --unsure-soft:#332711;
    --drop:#E38878; --drop-soft:#3A1C16;
    --grid:rgba(99,183,211,.055);
    --shadow:0 1px 2px rgba(0,0,0,.4), 0 10px 28px -14px rgba(0,0,0,.7);
  }
}
:root[data-theme="dark"] {
  --ground:#0C1113; --surface:#141B1E; --surface-2:#182124;
  --ink:#E9EEED; --ink-2:#BCC8C9; --muted:#87989B;
  --rule:#232F32; --rule-strong:#33454A;
  --accent:#63B7D3; --accent-soft:#12303B;
  --keep:#79C295; --keep-soft:#15301F;
  --unsure:#DCAE5C; --unsure-soft:#332711;
  --drop:#E38878; --drop-soft:#3A1C16;
  --grid:rgba(99,183,211,.055);
  --shadow:0 1px 2px rgba(0,0,0,.4), 0 10px 28px -14px rgba(0,0,0,.7);
}
* { box-sizing:border-box; }
body {
  margin:0; background:var(--ground); color:var(--ink);
  font-family:"IBM Plex Sans",system-ui,-apple-system,sans-serif;
  font-size:var(--step-0); line-height:1.55;
  background-image:linear-gradient(var(--grid) 1px,transparent 1px),
                   linear-gradient(90deg,var(--grid) 1px,transparent 1px);
  background-size:26px 26px;
  -webkit-font-smoothing:antialiased;
}
.wrap { max-width:780px; margin:0 auto; padding:0 20px 168px; }
.mono { font-family:"IBM Plex Mono",ui-monospace,monospace; }

/* ---------- masthead ---------- */
header.masthead { padding:26px 0 14px; }
.mast-row { display:flex; align-items:baseline; justify-content:space-between; gap:16px; flex-wrap:wrap; }
h1 {
  font-family:"IBM Plex Serif",Georgia,serif; font-weight:600;
  font-size:var(--step-2); margin:0; letter-spacing:-.01em;
}
.mast-sub { font-size:var(--step--1); color:var(--muted); margin:2px 0 0; max-width:52ch; }
.tallies { display:flex; gap:14px; font-size:var(--step--1); }
.tally { display:flex; align-items:center; gap:6px; }
.tally b { font-variant-numeric:tabular-nums; font-weight:600; }
.dot { width:9px; height:9px; border-radius:2px; display:inline-block; }
.dot.keep{background:var(--keep)} .dot.unsure{background:var(--unsure)}
.dot.drop{background:var(--drop)} .dot.todo{background:var(--rule-strong)}

/* ---------- progress rail ---------- */
.rail { display:flex; gap:1px; margin:16px 0 0; height:22px; align-items:stretch; }
.tick {
  flex:1 1 0; min-width:0; padding:0; border:0; cursor:pointer;
  background:var(--rule-strong); border-radius:1px; opacity:.5;
  transition:opacity .12s, transform .12s;
}
.tick:hover { opacity:1; transform:scaleY(1.14); }
.tick[data-v="yes"]{background:var(--keep); opacity:.85}
.tick[data-v="maybe"]{background:var(--unsure); opacity:.85}
.tick[data-v="no"]{background:var(--drop); opacity:.85}
.tick.current {
  opacity:1; position:relative; z-index:1; transform:scaleY(1.3);
  box-shadow:0 0 0 1.5px var(--ground), 0 0 0 3px var(--accent);
}
.tick:focus-visible { outline:2px solid var(--accent); outline-offset:2px; }
.rail-legend { display:flex; justify-content:space-between; margin-top:7px;
  font-size:.7rem; letter-spacing:.09em; color:var(--muted); text-transform:uppercase; }

/* ---------- card ---------- */
.card {
  background:var(--surface); border:1px solid var(--rule); border-radius:3px;
  box-shadow:var(--shadow); margin-top:22px; overflow:hidden;
}
.card-head { padding:20px 26px 0; }
.eyebrow {
  display:flex; align-items:center; gap:10px; flex-wrap:wrap;
  font-size:.7rem; letter-spacing:.11em; text-transform:uppercase; color:var(--muted);
}
.eyebrow .reg { color:var(--accent); font-weight:500; }
.eyebrow .sep { color:var(--rule-strong); }
.verdict-stamp {
  margin-left:auto; padding:2px 8px; border-radius:2px; font-weight:500;
  letter-spacing:.11em; border:1px solid currentColor;
}
.verdict-stamp[data-v="yes"]{color:var(--keep); background:var(--keep-soft)}
.verdict-stamp[data-v="maybe"]{color:var(--unsure); background:var(--unsure-soft)}
.verdict-stamp[data-v="no"]{color:var(--drop); background:var(--drop-soft)}
.verdict-stamp[data-v=""]{display:none}
h2.name {
  font-family:"IBM Plex Serif",Georgia,serif; font-weight:600;
  font-size:var(--step-3); line-height:1.16; margin:10px 0 0;
  letter-spacing:-.02em; text-wrap:balance;
}
.lede { font-size:var(--step-1); color:var(--ink-2); margin:10px 0 0; max-width:60ch; }

.grade-row { display:flex; align-items:center; gap:12px; margin:18px 0 0;
  padding:10px 12px; background:var(--surface-2); border:1px solid var(--rule); border-radius:2px; }
.grade-badge {
  width:34px; height:34px; flex:none; display:grid; place-items:center;
  font-family:"IBM Plex Serif",serif; font-size:1.15rem; font-weight:600;
  border-radius:2px; color:var(--accent); background:var(--accent-soft);
  border:1px solid color-mix(in srgb, var(--accent) 30%, transparent);
}
.grade-text { font-size:var(--step--1); }
.grade-text b { font-weight:600; }
.grade-text span { color:var(--muted); }

.fields { padding:4px 26px 22px; }
.field { padding:16px 0 0; border-top:1px solid var(--rule); margin-top:16px; }
.field:first-child { border-top:0; margin-top:6px; }
.flabel { font-size:.68rem; letter-spacing:.13em; text-transform:uppercase;
  color:var(--muted); margin-bottom:6px; }
.fvalue { font-size:.95rem; color:var(--ink-2); }
.tags { display:flex; flex-wrap:wrap; gap:6px; }
.tag { font-size:.72rem; letter-spacing:.04em; padding:3px 8px; border-radius:2px;
  background:var(--surface-2); border:1px solid var(--rule); color:var(--ink-2); }

.links { display:flex; flex-wrap:wrap; gap:8px; padding:0 26px 22px; }
.link {
  display:inline-flex; align-items:center; gap:6px; text-decoration:none;
  font-size:.8rem; padding:6px 11px; border-radius:2px;
  border:1px solid var(--rule-strong); color:var(--ink-2); background:var(--surface);
  transition:border-color .12s, color .12s, background .12s;
}
.link:hover { border-color:var(--accent); color:var(--accent); background:var(--accent-soft); }
.link:focus-visible { outline:2px solid var(--accent); outline-offset:2px; }
.link.primary { border-color:var(--accent); color:var(--accent); background:var(--accent-soft); font-weight:500; }
.link .arw { opacity:.55; font-size:.9em; }
.link-note { padding:0 26px 20px; font-size:.72rem; color:var(--muted); }

/* ---------- action bar ---------- */
.bar {
  position:fixed; left:0; right:0; bottom:0; z-index:20;
  background:color-mix(in srgb, var(--ground) 92%, transparent);
  backdrop-filter:blur(10px); border-top:1px solid var(--rule);
}
.bar-inner { max-width:780px; margin:0 auto; padding:12px 20px 14px;
  display:flex; align-items:center; gap:10px; }
.verdict-btns { display:flex; gap:8px; flex:1; }
button.v {
  flex:1; display:flex; flex-direction:column; align-items:center; gap:1px;
  padding:9px 6px; border-radius:3px; cursor:pointer; background:var(--surface);
  border:1px solid var(--rule-strong); color:var(--ink); font-size:.9rem; font-weight:500;
  font-family:inherit; transition:transform .1s, border-color .12s, background .12s;
}
button.v kbd { font-family:"IBM Plex Mono",monospace; font-size:.64rem; letter-spacing:.06em;
  color:var(--muted); background:none; }
button.v:hover { transform:translateY(-1px); }
button.v:focus-visible { outline:2px solid var(--accent); outline-offset:2px; }
button.v.keep:hover, button.v.keep[aria-pressed="true"] { border-color:var(--keep); background:var(--keep-soft); color:var(--keep); }
button.v.unsure:hover, button.v.unsure[aria-pressed="true"] { border-color:var(--unsure); background:var(--unsure-soft); color:var(--unsure); }
button.v.drop:hover, button.v.drop[aria-pressed="true"] { border-color:var(--drop); background:var(--drop-soft); color:var(--drop); }
button.v[aria-pressed="true"] kbd { color:inherit; opacity:.7; }
button.nav {
  padding:9px 12px; border-radius:3px; cursor:pointer; background:transparent;
  border:1px solid var(--rule-strong); color:var(--muted); font-family:"IBM Plex Mono",monospace;
  font-size:.78rem;
}
button.nav:hover { color:var(--ink); border-color:var(--ink-2); }
button.nav:focus-visible { outline:2px solid var(--accent); outline-offset:2px; }

/* ---------- toolbar ---------- */
.toolbar { display:flex; align-items:center; gap:10px; flex-wrap:wrap;
  margin-top:18px; font-size:var(--step--1); color:var(--muted); }
.toolbar .spacer { flex:1; }
.chip {
  padding:5px 10px; border-radius:2px; border:1px solid var(--rule-strong);
  background:var(--surface); color:var(--ink-2); cursor:pointer;
  font-family:inherit; font-size:.78rem;
}
.chip[aria-pressed="true"] { border-color:var(--accent); color:var(--accent); background:var(--accent-soft); }
.chip:focus-visible { outline:2px solid var(--accent); outline-offset:2px; }
.status { font-family:"IBM Plex Mono",monospace; font-size:.72rem; }
.status.saved { color:var(--keep); }
.status.local { color:var(--unsure); }

dialog {
  border:1px solid var(--rule); border-radius:3px; background:var(--surface);
  color:var(--ink); max-width:640px; width:calc(100% - 40px); padding:22px;
  box-shadow:var(--shadow);
}
dialog::backdrop { background:rgba(10,16,18,.55); }
dialog h3 { font-family:"IBM Plex Serif",serif; margin:0 0 8px; font-size:var(--step-1); }
dialog p { font-size:var(--step--1); color:var(--muted); margin:0 0 12px; }
textarea {
  width:100%; height:230px; font-family:"IBM Plex Mono",monospace; font-size:.74rem;
  background:var(--surface-2); color:var(--ink); border:1px solid var(--rule);
  border-radius:2px; padding:10px; resize:vertical;
}
.dlg-actions { display:flex; gap:8px; justify-content:flex-end; margin-top:12px; }
@media (prefers-reduced-motion: reduce) { * { transition:none !important; animation:none !important; } }
@media (max-width:560px) {
  h2.name { font-size:1.7rem; }
  .card-head,.fields,.links,.link-note { padding-left:18px; padding-right:18px; }
  button.v { font-size:.82rem; }
}
</style>

<div class="wrap">
  <header class="masthead">
    <div class="mast-row">
      <div>
        <h1>Drug Discoverer Triage</h1>
        <p class="mast-sub">One card per candidate. Keep, mark unsure, or drop &mdash; decisions save as you go.</p>
      </div>
      <div class="tallies mono">
        <span class="tally"><i class="dot keep"></i><b id="t-keep">0</b> keep</span>
        <span class="tally"><i class="dot unsure"></i><b id="t-unsure">0</b> unsure</span>
        <span class="tally"><i class="dot drop"></i><b id="t-drop">0</b> drop</span>
        <span class="tally"><i class="dot todo"></i><b id="t-todo">0</b> left</span>
      </div>
    </div>
    <div class="rail" id="rail" role="group" aria-label="Jump to candidate"></div>
    <div class="rail-legend">
      <span id="legend-left">Candidate 1</span>
      <span id="legend-right">120 total</span>
    </div>
  </header>

  <main class="card" id="card" aria-live="polite">
    <div class="card-head">
      <div class="eyebrow mono">
        <span class="reg" id="c-reg"></span>
        <span class="sep">/</span><span id="c-cat"></span>
        <span class="sep">/</span><span id="c-status"></span>
        <span class="verdict-stamp" id="c-stamp" data-v=""></span>
      </div>
      <h2 class="name" id="c-name"></h2>
      <p class="lede" id="c-known"></p>
      <div class="grade-row">
        <div class="grade-badge" id="c-grade"></div>
        <div class="grade-text">
          <b id="c-gradelabel"></b> &mdash; <span id="c-gloss"></span>
        </div>
      </div>
    </div>
    <div class="fields">
      <div class="field">
        <div class="flabel">Affiliation</div>
        <div class="fvalue" id="c-aff"></div>
      </div>
      <div class="field">
        <div class="flabel">Where the reasoning lives</div>
        <div class="fvalue" id="c-where"></div>
      </div>
      <div class="field">
        <div class="flabel">Artifact types</div>
        <div class="tags" id="c-tags"></div>
      </div>
    </div>
    <div class="links" id="c-links"></div>
    <p class="link-note" id="c-linknote"></p>
  </main>

  <div class="toolbar">
    <button class="chip" id="f-all" aria-pressed="true">All __N__</button>
    <button class="chip" id="f-todo" aria-pressed="false">Undecided only</button>
    <span class="spacer"></span>
    <span class="status mono" id="save-status">connecting&hellip;</span>
    <button class="chip" id="btn-export">Export decisions</button>
  </div>
</div>

<div class="bar">
  <div class="bar-inner">
    <button class="nav" id="btn-prev" title="Previous (left arrow)">&larr;</button>
    <div class="verdict-btns">
      <button class="v drop" id="btn-no" aria-pressed="false">Drop<kbd>N</kbd></button>
      <button class="v unsure" id="btn-maybe" aria-pressed="false">Unsure<kbd>SPACE</kbd></button>
      <button class="v keep" id="btn-yes" aria-pressed="false">Keep<kbd>Y</kbd></button>
    </div>
    <button class="nav" id="btn-next" title="Skip (right arrow)">&rarr;</button>
  </div>
</div>

<dialog id="dlg">
  <h3>Decisions</h3>
  <p>Copied to your clipboard if the browser allowed it. Either way, the JSON below is the record &mdash; and Claude can read the same data straight from this page's store.</p>
  <textarea id="dlg-text" readonly></textarea>
  <div class="dlg-actions">
    <button class="chip" id="dlg-copy">Copy again</button>
    <button class="chip" id="dlg-close">Close</button>
  </div>
</dialog>

<script id="roster" type="application/json">__DATA__</script>
<script>
(function () {
  "use strict";
  var PEOPLE = JSON.parse(document.getElementById("roster").textContent);
  var N = PEOPLE.length;
  var LS_KEY = "dd-triage-v1";

  var verdicts = {};           // id -> "yes" | "maybe" | "no"
  var idx = 0;                 // index into PEOPLE
  var todoOnly = false;
  var dbDoc = null;            // set once the db capability resolves
  var docReady = false;

  // ---------- storage ----------
  function loadLocal() {
    try { return JSON.parse(localStorage.getItem(LS_KEY) || "{}"); }
    catch (e) { return {}; }
  }
  function saveLocal() {
    try { localStorage.setItem(LS_KEY, JSON.stringify(verdicts)); } catch (e) {}
  }
  function setStatus(text, cls) {
    var el = document.getElementById("save-status");
    el.textContent = text;
    el.className = "status mono " + (cls || "");
  }

  function persist(id, value) {
    saveLocal();
    if (!dbDoc) return;
    var patch = { v: {}, updatedAt: new Date().toISOString() };
    patch.v[id] = value;
    var write = docReady
      ? dbDoc.update(patch)
      : dbDoc.set({ v: verdicts, updatedAt: patch.updatedAt });
    write.then(function () {
      docReady = true;
      setStatus("saved", "saved");
    }).catch(function (err) {
      if (err && err.code === "invalid_argument" && docReady) {
        docReady = false;
        return dbDoc.set({ v: verdicts, updatedAt: patch.updatedAt })
          .then(function () { docReady = true; setStatus("saved", "saved"); });
      }
      setStatus("saved on this device only", "local");
    });
  }

  // ---------- render ----------
  var rail = document.getElementById("rail");
  var ticks = PEOPLE.map(function (p, i) {
    var b = document.createElement("button");
    b.className = "tick";
    b.type = "button";
    b.dataset.v = "";
    b.title = p.name;
    b.setAttribute("aria-label", p.name);
    b.addEventListener("click", function () { go(i); });
    rail.appendChild(b);
    return b;
  });

  function tallyAndRail() {
    var c = { yes: 0, maybe: 0, no: 0 };
    PEOPLE.forEach(function (p, i) {
      var v = verdicts[p.id] || "";
      ticks[i].dataset.v = v;
      ticks[i].classList.toggle("current", i === idx);
      if (v) c[v]++;
    });
    document.getElementById("t-keep").textContent = c.yes;
    document.getElementById("t-unsure").textContent = c.maybe;
    document.getElementById("t-drop").textContent = c.no;
    document.getElementById("t-todo").textContent = N - c.yes - c.maybe - c.no;
  }

  function text(id, value) { document.getElementById(id).textContent = value; }

  function render() {
    var p = PEOPLE[idx];
    text("c-reg", "REG-" + String(idx + 1).padStart(3, "0"));
    text("c-cat", p.cat_label);
    text("c-status", p.status.toUpperCase());
    text("c-name", p.name);
    text("c-known", p.known_for);
    text("c-grade", p.richness);
    text("c-gradelabel", "Grade " + p.richness);
    text("c-gloss", p.gloss);
    text("c-aff", p.affiliation);
    text("c-where", p.where);

    var tags = document.getElementById("c-tags");
    tags.textContent = "";
    p.artifact_tags.forEach(function (t) {
      var s = document.createElement("span");
      s.className = "tag";
      s.textContent = t;
      tags.appendChild(s);
    });

    var links = document.getElementById("c-links");
    links.textContent = "";
    p.links.forEach(function (l) {
      var a = document.createElement("a");
      a.className = "link" + (l.primary ? " primary" : "");
      a.href = l.href;
      a.target = "_blank";
      a.rel = "noopener noreferrer";
      a.textContent = l.label;
      var arw = document.createElement("span");
      arw.className = "arw";
      arw.textContent = "↗";
      a.appendChild(arw);
      links.appendChild(a);
    });
    text("c-linknote", p.url
      ? "First link is a verified address; the rest are searches."
      : "No verified address yet — these are searches to check the person against.");

    var v = verdicts[p.id] || "";
    var stamp = document.getElementById("c-stamp");
    stamp.dataset.v = v;
    stamp.textContent = v === "yes" ? "Keep" : v === "maybe" ? "Unsure" : v === "no" ? "Drop" : "";
    document.getElementById("btn-yes").setAttribute("aria-pressed", String(v === "yes"));
    document.getElementById("btn-maybe").setAttribute("aria-pressed", String(v === "maybe"));
    document.getElementById("btn-no").setAttribute("aria-pressed", String(v === "no"));

    text("legend-left", "Candidate " + (idx + 1) + " of " + N);
    text("legend-right", p.cat_label);
    tallyAndRail();
  }

  // ---------- navigation ----------
  function go(i) {
    idx = Math.max(0, Math.min(N - 1, i));
    render();
    window.scrollTo({ top: 0, behavior: "smooth" });
  }
  function advance() {
    if (todoOnly) {
      for (var step = 1; step <= N; step++) {
        var j = (idx + step) % N;
        if (!verdicts[PEOPLE[j].id]) { go(j); return; }
      }
      return;               // nothing undecided left; stay put
    }
    if (idx < N - 1) go(idx + 1); else render();
  }
  function decide(value) {
    var p = PEOPLE[idx];
    if (verdicts[p.id] === value) { delete verdicts[p.id]; value = ""; }
    else { verdicts[p.id] = value; }
    persist(p.id, value);
    render();
    if (value) setTimeout(advance, 130);
  }

  document.getElementById("btn-yes").addEventListener("click", function () { decide("yes"); });
  document.getElementById("btn-maybe").addEventListener("click", function () { decide("maybe"); });
  document.getElementById("btn-no").addEventListener("click", function () { decide("no"); });
  document.getElementById("btn-prev").addEventListener("click", function () { go(idx - 1); });
  document.getElementById("btn-next").addEventListener("click", advance);

  document.addEventListener("keydown", function (e) {
    if (e.metaKey || e.ctrlKey || e.altKey) return;
    if (document.getElementById("dlg").open) return;
    var k = e.key.toLowerCase();
    if (k === "y" || k === "k") { e.preventDefault(); decide("yes"); }
    else if (k === "n" || k === "d") { e.preventDefault(); decide("no"); }
    else if (k === "u" || e.key === " ") { e.preventDefault(); decide("maybe"); }
    else if (e.key === "ArrowRight") { e.preventDefault(); advance(); }
    else if (e.key === "ArrowLeft") { e.preventDefault(); go(idx - 1); }
  });

  var fAll = document.getElementById("f-all");
  var fTodo = document.getElementById("f-todo");
  function setFilter(only) {
    todoOnly = only;
    fAll.setAttribute("aria-pressed", String(!only));
    fTodo.setAttribute("aria-pressed", String(only));
    if (only && verdicts[PEOPLE[idx].id]) advance();
  }
  fAll.addEventListener("click", function () { setFilter(false); });
  fTodo.addEventListener("click", function () { setFilter(true); });

  // ---------- export ----------
  function exportPayload() {
    return JSON.stringify({
      exportedAt: new Date().toISOString(),
      keep: PEOPLE.filter(function (p) { return verdicts[p.id] === "yes"; }).map(function (p) { return p.name; }),
      unsure: PEOPLE.filter(function (p) { return verdicts[p.id] === "maybe"; }).map(function (p) { return p.name; }),
      drop: PEOPLE.filter(function (p) { return verdicts[p.id] === "no"; }).map(function (p) { return p.name; }),
      byId: verdicts
    }, null, 2);
  }
  var dlg = document.getElementById("dlg");
  function copyText(t) {
    if (navigator.clipboard) { navigator.clipboard.writeText(t).catch(function () {}); }
  }
  document.getElementById("btn-export").addEventListener("click", function () {
    var payload = exportPayload();
    document.getElementById("dlg-text").value = payload;
    copyText(payload);
    dlg.showModal();
  });
  document.getElementById("dlg-copy").addEventListener("click", function () {
    copyText(document.getElementById("dlg-text").value);
  });
  document.getElementById("dlg-close").addEventListener("click", function () { dlg.close(); });

  // ---------- boot ----------
  verdicts = loadLocal();
  render();
  setStatus("saving to this device", "local");

  var useCap = (window.claude && typeof window.claude.use === "function")
    ? window.claude.use("db")
    : Promise.resolve(null);
  useCap.then(function (db) {
    if (!db) { setStatus("saving to this device", "local"); return; }
    dbDoc = db.doc("triage/verdicts");
    dbDoc.onSnapshot(function (snap) {
      docReady = snap.exists;
      var remote = (snap.exists && snap.data() && snap.data().v) || {};
      var merged = {};
      Object.keys(remote).forEach(function (k) { if (remote[k]) merged[k] = remote[k]; });
      Object.keys(verdicts).forEach(function (k) { if (verdicts[k] && !merged[k]) merged[k] = verdicts[k]; });
      verdicts = merged;
      saveLocal();
      setStatus(snap.exists ? "saved" : "ready to save", "saved");
      render();
    }, function () {
      setStatus("saving to this device", "local");
    });
  }).catch(function () {
    setStatus("saving to this device", "local");
  });
})();
</script>
"""


def main():
    here = pathlib.Path(__file__).parent
    records = build_records()
    html = TEMPLATE.replace("__DATA__", json.dumps(records, ensure_ascii=False))
    html = html.replace("120 total", f"{len(records)} total")
    html = html.replace("All __N__", f"All {len(records)}")
    out = here / "triage.html"
    out.write_text(html, encoding="utf-8")
    print(f"{len(records)} cards -> {out} ({out.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
