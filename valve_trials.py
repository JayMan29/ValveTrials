<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Tricuspid Valve Trials — ValveTrials.com</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@600;700;800&family=Inter:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<style>
:root{--ink:#0E262B;--page:#EAEFEE;--card:#FFFFFF;--line:#D2DEDB;--muted:#5B6E6B;
--accent:#C7402F;--r:12px;}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:var(--page);color:var(--ink);
font-family:"Inter",system-ui,-apple-system,Segoe UI,Roboto,sans-serif;font-size:15px;line-height:1.5;-webkit-font-smoothing:antialiased}
a{color:var(--accent)}
.mono{font-family:"IBM Plex Mono",ui-monospace,Menlo,monospace}
/* site header */
.site{display:flex;align-items:center;justify-content:space-between;gap:16px;padding:13px 24px;background:var(--ink);color:#fff;flex-wrap:wrap}
.brand{font-family:"Archivo",sans-serif;font-weight:800;font-size:19px;letter-spacing:-.01em;color:#fff;text-decoration:none}
.brand span{color:#E8846F}
.site-nav{display:flex;gap:4px;flex-wrap:wrap}
.site-nav a{color:#c7d3d1;text-decoration:none;font-size:14px;padding:7px 13px;border-radius:8px;transition:background .15s,color .15s}
.site-nav a:hover{background:rgba(255,255,255,.12);color:#fff}
.site-nav a.active{background:#fff;color:var(--ink);font-weight:600}
/* mast */
.mast{padding:40px 24px 20px;max-width:1080px;margin:0 auto;border-bottom:1px solid var(--line)}
.kicker{font-family:"IBM Plex Mono",monospace;font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:var(--muted);margin:0 0 10px}
.crumb{color:var(--muted);text-decoration:none}.crumb:hover{color:var(--accent)}
.mast h1{font-family:"Archivo",sans-serif;font-weight:800;font-size:clamp(28px,5vw,46px);line-height:1.02;letter-spacing:-.02em;margin:0 0 12px;max-width:16ch}
.mast .lede{max-width:64ch;color:#33474a;margin:0;font-size:16px}
.mast .meta{font-family:"IBM Plex Mono",monospace;font-size:12.5px;color:var(--muted);margin-top:14px}
.legend{display:flex;flex-wrap:wrap;gap:8px 14px;margin-top:16px;font-size:12.5px;color:var(--muted)}
.legend span{display:inline-flex;align-items:center;gap:5px}
/* home */
.home{max-width:1080px;margin:0 auto;padding:56px 24px 90px}
.home .kicker{font-family:"IBM Plex Mono",monospace;font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:var(--muted);margin:0 0 12px}
.home-h1{font-family:"Archivo",sans-serif;font-weight:800;font-size:clamp(32px,5.5vw,54px);line-height:1.02;letter-spacing:-.025em;margin:0 0 14px;max-width:17ch}
.home-lede{max-width:60ch;color:#33474a;font-size:17px;margin:0 0 42px}
.valve-cards{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}
.vcard{display:flex;flex-direction:column;gap:14px;padding:28px 26px;background:var(--card);border:1px solid var(--line);border-left:6px solid var(--vhue);border-radius:16px;text-decoration:none;color:var(--ink);transition:transform .16s,box-shadow .16s;min-height:250px}
.vcard:hover{transform:translateY(-4px);box-shadow:0 16px 40px rgba(14,38,43,.12)}
.vcard:focus-visible{outline:2px solid var(--accent);outline-offset:3px}
.vglyph{width:66px;height:66px}
.vcard h2{font-family:"Archivo",sans-serif;font-weight:800;font-size:27px;margin:0;letter-spacing:-.01em}
.vcard p{color:var(--muted);font-size:14px;margin:0;line-height:1.5;flex:1}
.vcard .pill{align-self:flex-start;font-size:11px;padding:4px 10px;border-radius:999px;background:#eef1f4;color:#455568;font-family:"IBM Plex Mono",monospace}
.vcard .go{font-family:"IBM Plex Mono",monospace;font-size:13px;color:var(--vhue);font-weight:600}
.vcard.soon{opacity:.96}
.vcard.soon .go{color:var(--muted)}
/* controls */
.controls{position:sticky;top:0;z-index:20;background:rgba(234,239,238,.92);backdrop-filter:blur(8px);border-bottom:1px solid var(--line);padding:12px 24px}
.controls-inner{max-width:1080px;margin:0 auto;display:flex;flex-direction:column;gap:11px}
.searchbar{display:flex;gap:10px;align-items:center;flex-wrap:wrap}
.searchbar input{flex:1;min-width:220px;padding:11px 14px;border:1px solid var(--line);border-radius:10px;background:var(--card);font-size:15px;color:var(--ink)}
.searchbar input:focus{outline:2px solid var(--accent);outline-offset:1px}
.seg{display:inline-flex;border:1px solid var(--line);border-radius:10px;overflow:hidden;background:var(--card)}
.seg button{border:0;background:transparent;padding:9px 13px;font-size:13px;cursor:pointer;color:var(--muted);font-family:inherit}
.seg button.active{background:var(--ink);color:#fff}
.actions{display:flex;gap:8px}
.actions button{border:1px solid var(--line);background:var(--card);color:#33474a;padding:9px 13px;border-radius:10px;font-size:13px;cursor:pointer;font-family:inherit}
.actions button:hover{border-color:var(--accent);color:var(--accent)}
.fchips{display:flex;flex-wrap:wrap;gap:8px}
.fchip{border:1px solid var(--line);background:var(--card);color:#33474a;padding:7px 12px;border-radius:999px;font-size:13px;cursor:pointer;font-family:inherit;display:inline-flex;align-items:center;gap:7px}
.fchip .fn{font-family:"IBM Plex Mono",monospace;font-size:11px;color:var(--muted)}
.fchip[data-filter="cat"]{border-left:4px solid var(--hue)}
.fchip.active{background:var(--ink);color:#fff;border-color:var(--ink)}
.fchip.active .fn{color:#cdd8d6}
.countline{font-family:"IBM Plex Mono",monospace;font-size:12px;color:var(--muted)}
/* list + dropdowns */
.list{max-width:1080px;margin:22px auto 80px;padding:0 24px}
details.group{margin-bottom:20px}
summary.grouphead{list-style:none;cursor:pointer;display:flex;align-items:center;gap:10px;margin:0;padding:8px 4px;font-family:"Archivo",sans-serif;font-weight:700;font-size:15px;letter-spacing:.02em;text-transform:uppercase;color:var(--hue);border-bottom:2px solid var(--hue)}
summary.grouphead::-webkit-details-marker{display:none}
summary.grouphead:hover{opacity:.85}
summary.grouphead:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
.grouphead .dot{width:9px;height:9px;border-radius:50%;background:var(--hue)}
.gcount{margin-left:auto;font-family:"IBM Plex Mono",monospace;font-size:12px;color:var(--muted);font-weight:400;letter-spacing:0}
.gchev{width:9px;height:9px;border-right:2px solid var(--hue);border-bottom:2px solid var(--hue);transform:rotate(-45deg);transition:transform .18s}
details.group[open] > summary .gchev{transform:rotate(45deg)}
.rows{display:flex;flex-direction:column;gap:8px;margin-top:12px}
details.row{background:var(--card);border:1px solid var(--line);border-left:5px solid var(--hue);border-radius:var(--r);overflow:hidden}
details.row[open]{box-shadow:0 8px 26px rgba(14,38,43,.09)}
summary{list-style:none;cursor:pointer;display:grid;grid-template-columns:20px minmax(190px,1.05fr) 1.5fr auto;gap:14px;align-items:center;padding:14px 18px}
summary::-webkit-details-marker{display:none}
summary:hover{background:#f6f9f8}
summary:focus-visible{outline:2px solid var(--accent);outline-offset:-2px}
.chev{width:9px;height:9px;border-right:2px solid var(--muted);border-bottom:2px solid var(--muted);transform:rotate(-45deg);transition:transform .18s;margin-left:4px}
details.row[open] > summary .chev{transform:rotate(45deg)}
.row-acr{font-family:"Archivo",sans-serif;font-weight:800;font-size:17px;letter-spacing:-.01em;display:block;line-height:1.15}
.row-name{font-size:12px;color:var(--muted);display:block;line-height:1.3;margin-top:1px}
.cav-dot{color:#B03A2E;font-size:12px}
.row-take{font-size:13.5px;color:#243b3e;line-height:1.4}
.row-meta{display:flex;flex-direction:column;align-items:flex-end;gap:5px;text-align:right}
.badge{font-size:10.5px;padding:3px 9px;border-radius:999px;border:1px solid transparent;white-space:nowrap;font-weight:500}
.status-published{background:#e6f4ec;color:#1c6b45;border-color:#c7e6d5}
.status-ongoing{background:#e7f0fa;color:#1f5c92;border-color:#cbe0f3}
.status-terminated{background:#f4e7e6;color:#9c3a2f;border-color:#eccdc9}
.dates{display:flex;flex-direction:column;align-items:flex-end;gap:1px;font-family:"IBM Plex Mono",monospace;font-size:11px;color:var(--muted);line-height:1.35}
.dates .d-pub{color:#33474a}
/* expanded body */
.body-inner{padding:2px 18px 20px;border-top:1px solid var(--line)}
.paperbar{display:flex;flex-wrap:wrap;align-items:center;gap:10px 16px;margin:14px 0 6px;padding:12px 14px;background:#f5f8f7;border:1px solid var(--line);border-radius:10px}
.paperbar.none{color:var(--muted);font-style:italic}
.plinks{display:flex;flex-wrap:wrap;gap:8px}
.plink{font-family:"IBM Plex Mono",monospace;font-size:12px;text-decoration:none;padding:6px 11px;border-radius:8px;border:1px solid var(--line);color:var(--accent);background:#fff}
.plink.primary{background:var(--accent);color:#fff;border-color:var(--accent)}
.plink.search{color:#33474a}
.plink:hover{filter:brightness(.96)}
.paper-cite{font-size:12.5px;color:#33474a;margin-left:auto}.paper-cite em{font-style:italic}
.d-caveat{margin:8px 0;font-size:13px;color:#9c3a2f;background:#faeeec;border:1px dashed #e6c3bd;border-radius:8px;padding:9px 12px}
.d-summary{color:#33474a;margin:8px 0 4px;font-size:14.5px}
.d-grid{display:grid;grid-template-columns:1fr 290px;gap:26px;padding-top:8px}
.d-main section{margin-bottom:18px}
.d-main h3{font-family:"Archivo",sans-serif;font-size:12.5px;text-transform:uppercase;letter-spacing:.06em;color:var(--hue);margin:0 0 7px;padding-bottom:5px;border-bottom:1px solid var(--line)}
.d-main p{margin:0}
.overview{width:100%;border-collapse:collapse;font-size:13.5px}
.overview th{text-align:left;width:38%;color:var(--muted);font-weight:500;padding:6px 10px 6px 0;vertical-align:top;border-bottom:1px solid #edf2f1}
.overview td{padding:6px 0;border-bottom:1px solid #edf2f1;vertical-align:top}
.bul{margin:0;padding-left:18px}.bul li{margin:3px 0}
.results{list-style:none;margin:0;padding:0}
.results li{position:relative;padding-left:22px;margin:6px 0}
.results li::before{content:"✔";position:absolute;left:0;color:var(--hue);font-size:12px;top:2px}
.empty{color:var(--muted);font-style:italic;margin:0}
.d-side{border-left:1px solid var(--line);padding-left:22px}
.qf{margin-bottom:18px}
.qf h4{font-family:"Archivo",sans-serif;font-size:11.5px;text-transform:uppercase;letter-spacing:.08em;margin:0 0 8px}
.qf dl{margin:0;display:grid;grid-template-columns:auto 1fr;gap:5px 12px;font-size:13px}
.qf dt{color:var(--muted)}.qf dd{margin:0;text-align:right}
.qf .lab{font-size:11px;text-transform:uppercase;letter-spacing:.05em;color:var(--muted);margin:8px 0 2px}
.qf p{margin:0 0 2px;font-size:13px}
.qf .bul{font-size:13px}
.noresults{text-align:center;color:var(--muted);padding:50px 20px;font-size:16px;display:none}
/* coming soon */
.soon-box{background:var(--card);border:1px solid var(--line);border-left:6px solid var(--hue);border-radius:16px;padding:28px 26px;max-width:640px}
.soon-box h2{font-family:"Archivo",sans-serif;font-weight:800;font-size:24px;margin:0 0 8px}
.soon-box p{color:#33474a;margin:0 0 16px}
.back{font-family:"IBM Plex Mono",monospace;font-size:13px;text-decoration:none}
.soon-head{font-family:"Archivo",sans-serif;font-size:12.5px;text-transform:uppercase;letter-spacing:.08em;color:var(--muted);margin:34px 0 12px}
.soon-sections{display:flex;flex-direction:column;gap:8px;max-width:640px}
.soon-sec{display:flex;align-items:center;gap:10px;background:var(--card);border:1px dashed var(--line);border-radius:10px;padding:13px 16px;font-family:"Archivo",sans-serif;font-weight:700;font-size:14px;text-transform:uppercase;letter-spacing:.02em;color:#7c8b89}
.soon-sec .dot{width:9px;height:9px;border-radius:50%;background:var(--hue);opacity:.5}
.soon-tag{margin-left:auto;font-family:"IBM Plex Mono",monospace;font-size:11px;font-weight:400;letter-spacing:0;color:var(--muted);text-transform:none}
footer.pagefoot{max-width:1080px;margin:0 auto;padding:22px 24px;border-top:1px solid var(--line);color:var(--muted);font-size:12.5px}
/* editor */
.site-nav a.editlink{border:1px solid rgba(255,255,255,.25)}
.editor{max-width:1180px;margin:0 auto;padding:30px 24px 80px}
.editor .kicker{font-family:"IBM Plex Mono",monospace;font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:var(--muted);margin:0 0 8px}
.editor h1{font-family:"Archivo",sans-serif;font-weight:800;font-size:clamp(26px,4vw,40px);margin:0 0 10px}
.editor .lede{max-width:70ch;color:#33474a;margin:0 0 16px}
.ed-actions{display:flex;flex-wrap:wrap;align-items:center;gap:10px;margin-bottom:8px}
.ed-btn{border:1px solid var(--line);background:var(--card);color:#243b3e;padding:9px 14px;border-radius:9px;font-size:13px;cursor:pointer;font-family:inherit}
.ed-btn:hover{border-color:var(--accent);color:var(--accent)}
.ed-btn.primary{background:var(--ink);color:#fff;border-color:var(--ink)}
.ed-btn.primary:hover{filter:brightness(1.1);color:#fff}
.ed-btn.danger{color:#9c3a2f;border-color:#e6c3bd}
.ed-count{font-family:"IBM Plex Mono",monospace;font-size:12px;color:var(--muted)}
.ed-dirty{font-family:"IBM Plex Mono",monospace;font-size:12px;color:var(--accent)}
.ed-cols{display:grid;grid-template-columns:290px 1fr;gap:22px;margin-top:14px}
.ed-side{position:sticky;top:14px;align-self:start}
.ed-search{width:100%;padding:10px 12px;border:1px solid var(--line);border-radius:9px;background:var(--card);font-size:14px;margin-bottom:10px}
.ed-listbox{max-height:70vh;overflow:auto;border:1px solid var(--line);border-radius:12px;background:var(--card);padding:6px}
.ed-group{font-family:"Archivo",sans-serif;font-size:11px;text-transform:uppercase;letter-spacing:.06em;color:var(--muted);padding:10px 8px 4px;display:flex;justify-content:space-between}
.ed-item{display:block;width:100%;text-align:left;border:0;background:transparent;border-radius:8px;padding:8px 10px;cursor:pointer;font-family:inherit}
.ed-item:hover{background:#f0f4f3}
.ed-item.active{background:var(--ink);color:#fff}
.ed-item b{display:block;font-family:"Archivo",sans-serif;font-size:14px}
.ed-item span{font-size:11px;color:var(--muted)}
.ed-item.active span{color:#cdd8d6}
.ed-empty{color:var(--muted);padding:16px;font-style:italic}
.ed-form{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:18px 20px}
.ed-formhead{display:flex;justify-content:space-between;align-items:center;gap:12px;margin-bottom:12px;padding-bottom:12px;border-bottom:1px solid var(--line)}
.ed-formhead h2{font-family:"Archivo",sans-serif;font-size:18px;margin:0}
.ed-formbtns{display:flex;gap:8px}
.ed-grid{display:grid;grid-template-columns:1fr 1fr;gap:12px 16px}
.ed-sec{grid-column:1/-1;font-family:"Archivo",sans-serif;font-size:12px;text-transform:uppercase;letter-spacing:.07em;color:var(--hue,#2C6E8F);margin:10px 0 2px;padding-top:8px;border-top:1px solid #eef2f1}
.ed-field{display:flex;flex-direction:column;gap:4px;font-size:12.5px;color:var(--muted)}
.ed-field.wide{grid-column:1/-1}
.ed-field input,.ed-field select,.ed-field textarea{border:1px solid var(--line);border-radius:8px;padding:8px 10px;font-size:14px;font-family:inherit;color:var(--ink);background:#fff}
.ed-field textarea{resize:vertical;line-height:1.4}
.ed-field input:focus,.ed-field select:focus,.ed-field textarea:focus{outline:2px solid var(--accent);outline-offset:1px}
.ed-check{grid-column:auto;display:flex;align-items:center;gap:8px;font-size:14px;color:var(--ink);padding-top:18px}
.ed-dialog{width:min(760px,94vw);border:0;border-radius:14px;padding:0 24px 24px;box-shadow:0 30px 80px rgba(10,30,34,.35)}
.ed-dialog::backdrop{background:rgba(11,28,31,.5)}
.ed-dialog h3{font-family:"Archivo",sans-serif;margin:18px 0 8px}
.ed-dialog textarea{width:100%;border:1px solid var(--line);border-radius:10px;padding:12px;font-family:"IBM Plex Mono",monospace;font-size:12px}
.ed-dialog-actions{margin-top:10px}
.ed-x{position:absolute;right:14px;top:14px;border:1px solid var(--line);background:#fff;border-radius:50%;width:32px;height:32px;cursor:pointer}
@media (max-width:820px){.ed-cols{grid-template-columns:1fr}.ed-side{position:static}.ed-grid{grid-template-columns:1fr}}
@media (max-width:820px){
  .valve-cards{grid-template-columns:1fr}
  summary{grid-template-columns:18px 1fr;gap:8px}
  .row-take,.row-meta{grid-column:2}
  .row-meta{align-items:flex-start;text-align:left}
  .dates{align-items:flex-start}
  .d-grid{grid-template-columns:1fr}
  .d-side{border-left:0;border-top:1px solid var(--line);padding-left:0;padding-top:16px}
  .qf dd{text-align:left}
  .paper-cite{margin-left:0;width:100%}
}
@media (prefers-reduced-motion:reduce){*{transition:none!important;scroll-behavior:auto!important}}
</style>
</head>
<body>
<header class="site">
  <a class="brand" href="index.html">Valve<span>Trials</span>.com</a>
  <nav class="site-nav"><a href='aortic.html' class=''>Aortic</a><a href='mitral.html' class=''>Mitral</a><a href='tricuspid.html' class='active'>Tricuspid</a><a href='editor.html' class='editlink '>✎ Editor</a></nav>
</header>

<header class="mast">
  <p class="kicker"><a class="crumb" href="index.html">ValveTrials.com</a> · Tricuspid</p>
  <h1>Tricuspid Valve Trials</h1>
  <p class="lede">Major transcatheter (and key comparator) tricuspid-valve trials, grouped into
     collapsible categories and ordered oldest to newest. Click any trial to read the full entry and open the paper.</p>
  <p class="meta">14 trials · 11 published · 3 ongoing · 0 negative-result trials excluded · antiplatelet/anticoagulant trials excluded by design</p>
  <div class="legend">
    <span>🟢 Published</span><span>🔵 Ongoing</span>
    <span>Sorted oldest → newest within each category</span><span>⚠ Caveat inside</span>
  </div>
</header>

<div class="controls">
  <div class="controls-inner">
    <div class="searchbar">
      <input id="search" type="search" placeholder="Search trial, device, NCT, population…" aria-label="Search trials">
      <div class="seg" data-group="status">
        <button class="active" data-value="all">All</button>
        <button data-value="published">Published</button>
        <button data-value="ongoing">Ongoing</button>
      </div>
      <div class="seg" data-group="pc">
        <button class="active" data-value="0">All</button>
        <button data-value="1">⭐ Practice changing</button>
      </div>
      <div class="actions">
        <button id="expandAll">Expand all</button>
        <button id="collapseAll">Collapse all</button>
      </div>
    </div>
    <div class="fchips"><button class='fchip active' data-filter='all'>All</button><button class='fchip' data-filter='cat' data-value="Tricuspid TEER" style='--hue:#6D5AB6'>Tricuspid TEER <span class='fn'>6</span></button><button class='fchip' data-filter='cat' data-value="Tricuspid Transcatheter Replacement (TTVR)" style='--hue:#4E63B6'>Tricuspid Transcatheter Replacement (TTVR) <span class='fn'>3</span></button><button class='fchip' data-filter='cat' data-value="Tricuspid Annuloplasty" style='--hue:#8E5AB6'>Tricuspid Annuloplasty <span class='fn'>2</span></button><button class='fchip' data-filter='cat' data-value="Tricuspid Heterotopic / Caval" style='--hue:#B65AA0'>Tricuspid Heterotopic / Caval <span class='fn'>2</span></button><button class='fchip' data-filter='cat' data-value="Tricuspid Frontier / Next-Gen Device" style='--hue:#5A78B6'>Tricuspid Frontier / Next-Gen Device <span class='fn'>1</span></button></div>
    <div class="countline"><span id="count">14 / 14 trials shown</span></div>
  </div>
</div>

<main class="list">
  <details class='group' data-cat="Tricuspid TEER" style='--hue:#6D5AB6' open><summary class='grouphead'><span class='gchev' aria-hidden='true'></span><span class='dot'></span>Tricuspid TEER<span class='gcount'>6</span></summary><div class='rows'><details class="row" style="--hue:#6D5AB6" data-cat="Tricuspid TEER"
         data-status="published" data-signal="descriptive"
         data-pc="0" data-search="triluminate trial to evaluate treatment with abbott transcatheter clip repair system in patients with moderate or greater tr (single-arm) abbott triclip none (single-arm) moderate or greater symptomatic tr, high surgical risk nct03227757 tricuspid teer triclip teer single-arm feasibility ce-mark">
  <summary>
    <span class="chev" aria-hidden="true"></span>
    <span class="row-id">
      <span class="row-acr">TRILUMINATE </span>
      <span class="row-name">Trial to Evaluate Treatment With Abbott Transcatheter Clip Repair System in Patients With Moderate or Greater TR (Single-Arm)</span>
    </span>
    <span class="row-take">Proved tricuspid TEER was feasible and safe, launching the modern T-TEER era.</span>
    <span class="row-meta"><span class='badge status-published'>🟢 Published</span><span class='dates'><span class='d-enr'>Enrolled 2017–2018</span><span class='d-pub'>Published 2019</span></span></span>
  </summary>
  <div class="body-inner">
  <div class='paperbar'><div class='plinks'><a class='plink search' href='https://pubmed.ncbi.nlm.nih.gov/?term=TRILUMINATE%20AND%20%22Nickenig%20G%22%5BAuthor%5D' target='_blank' rel='noopener'>Find on PubMed ↗</a><a class='plink registry' href='https://clinicaltrials.gov/study/NCT03227757' target='_blank' rel='noopener'>ClinicalTrials.gov ↗</a></div><span class='paper-cite'>Nickenig G, et al. · <em>The Lancet</em> · 2019</span></div>
  
  <p class="d-summary">The single-arm feasibility study that established transcatheter edge-to-edge repair of the tricuspid valve as feasible and safe, reducing TR and improving symptoms — the basis for CE mark.</p>
  <div class="d-grid">
    <div class="d-main">
      <section><h3>Study overview</h3><table class='overview'><tbody><tr><th>Device</th><td>Abbott TriClip</td></tr><tr><th>Intervention</th><td>TEER</td></tr><tr><th>Comparator</th><td>None (single-arm)</td></tr><tr><th>Population</th><td>Moderate or greater symptomatic TR, high surgical risk</td></tr><tr><th>Risk group</th><td>High surgical risk</td></tr><tr><th>Sample size</th><td>85</td></tr><tr><th>Enrollment</th><td>2017–2018</td></tr><tr><th>Follow-up</th><td>30 days, 1 year, 3 years</td></tr><tr><th>Trial type</th><td>Prospective single-arm, multicenter</td></tr></tbody></table></section>
      <section><h3>Inclusion criteria</h3><p class='empty'>—</p></section>
      <section><h3>Primary endpoint</h3><p>Safety and reduction in TR severity.</p></section>
      <section><h3>Secondary endpoints</h3><ul class='bul'><li>NYHA class</li><li>6-minute walk</li><li>Quality of life</li><li>Right-heart remodeling</li></ul></section>
      <section><h3>Key results</h3><ul class='results'><li>Significant TR reduction with a strong safety profile</li><li>Durable symptom and functional improvement through 3 years</li></ul></section>
      <section><h3>Why this trial matters</h3><p>First convincing tricuspid TEER dataset; led to CE mark (2020).</p></section>
      <section><h3>Clinical pearls</h3><ul class='bul'><li>Used the first-generation clip in a highly selected population.</li></ul></section>
      <section><h3>Limitations</h3><ul class='bul'><li>Single-arm</li><li>Selected anatomy</li><li>First-generation device</li></ul></section>
    </div>
    <aside class="d-side">
      <div class="qf"><h4>Quick facts</h4>
        <dl>
          <dt>Valve</dt><dd>Tricuspid</dd>
          <dt>Disease</dt><dd>Secondary tricuspid regurgitation</dd>
          <dt>Procedure</dt><dd>TEER</dd>
          <dt>Sample</dt><dd>85</dd>
          <dt>Follow-up</dt><dd>30 days, 1 year, 3 years</dd>
        </dl>
      </div>
      <div class="qf"><h4>Guidelines</h4>
        <p class="lab">ACC / AHA</p><p>Feasibility basis for T-TEER.</p>
        <p class="lab">ESC / EACTS</p><p>Supported CE mark.</p>
      </div>
      <div class="qf"><h4>FDA / regulatory</h4><p>CE mark 2020; precursor to the US pivotal.</p></div>
      <div class="qf"><h4>Timeline</h4><ul class='bul'><li>Enrollment: 2017–2018</li><li>Published: Lancet 2019</li><li>CE mark: 2020</li></ul></div>
    </aside>
  </div>
</div>
</details><details class="row" style="--hue:#6D5AB6" data-cat="Tricuspid TEER"
         data-status="published" data-signal="descriptive"
         data-pc="0" data-search="clasp tr efs edwards pascal tricuspid repair system early feasibility study edwards pascal / pascal ace none (single-arm) severe symptomatic tr, high surgical risk nct03745313 tricuspid teer pascal teer single-arm feasibility">
  <summary>
    <span class="chev" aria-hidden="true"></span>
    <span class="row-id">
      <span class="row-acr">CLASP TR EFS </span>
      <span class="row-name">Edwards PASCAL Tricuspid Repair System Early Feasibility Study</span>
    </span>
    <span class="row-take">PASCAL is the second viable tricuspid TEER platform.</span>
    <span class="row-meta"><span class='badge status-published'>🟢 Published</span><span class='dates'><span class='d-enr'>Enrolled 2019–2021</span><span class='d-pub'>Published 2021</span></span></span>
  </summary>
  <div class="body-inner">
  <div class='paperbar'><div class='plinks'><a class='plink search' href='https://pubmed.ncbi.nlm.nih.gov/?term=CLASP%20TR%20EFS%20AND%20%22Kodali%20S%22%5BAuthor%5D' target='_blank' rel='noopener'>Find on PubMed ↗</a><a class='plink registry' href='https://clinicaltrials.gov/study/NCT03745313' target='_blank' rel='noopener'>ClinicalTrials.gov ↗</a></div><span class='paper-cite'>Kodali S, Hahn RT, et al. · <em>Journal of the American College of Cardiology</em> · 2021</span></div>
  
  <p class="d-summary">Early feasibility of the PASCAL system for tricuspid TEER, showing durable TR reduction and functional improvement — the PASCAL counterpart to the TriClip program.</p>
  <div class="d-grid">
    <div class="d-main">
      <section><h3>Study overview</h3><table class='overview'><tbody><tr><th>Device</th><td>Edwards PASCAL / PASCAL Ace</td></tr><tr><th>Intervention</th><td>TEER</td></tr><tr><th>Comparator</th><td>None (single-arm)</td></tr><tr><th>Population</th><td>Severe symptomatic TR, high surgical risk</td></tr><tr><th>Risk group</th><td>High surgical risk</td></tr><tr><th>Sample size</th><td>early feasibility cohort</td></tr><tr><th>Enrollment</th><td>2019–2021</td></tr><tr><th>Follow-up</th><td>30 days, 1 year, 2 years</td></tr><tr><th>Trial type</th><td>Prospective single-arm (EFS)</td></tr></tbody></table></section>
      <section><h3>Inclusion criteria</h3><p class='empty'>—</p></section>
      <section><h3>Primary endpoint</h3><p>Safety and performance / TR reduction.</p></section>
      <section><h3>Secondary endpoints</h3><ul class='bul'><li>TR grade</li><li>NYHA / 6-minute walk</li><li>KCCQ</li></ul></section>
      <section><h3>Key results</h3><ul class='results'><li>Durable TR reduction and functional improvement with good safety</li></ul></section>
      <section><h3>Why this trial matters</h3><p>Feasibility basis for the PASCAL tricuspid pivotal (CLASP II TR).</p></section>
      <section><h3>Clinical pearls</h3><ul class='bul'><li>Independent leaflet grasping and a central spacer suit large tricuspid gaps.</li></ul></section>
      <section><h3>Limitations</h3><ul class='bul'><li>Single-arm</li><li>Small cohort</li></ul></section>
    </div>
    <aside class="d-side">
      <div class="qf"><h4>Quick facts</h4>
        <dl>
          <dt>Valve</dt><dd>Tricuspid</dd>
          <dt>Disease</dt><dd>Tricuspid regurgitation</dd>
          <dt>Procedure</dt><dd>TEER</dd>
          <dt>Sample</dt><dd>early feasibility cohort</dd>
          <dt>Follow-up</dt><dd>30 days, 1 year, 2 years</dd>
        </dl>
      </div>
      <div class="qf"><h4>Guidelines</h4>
        <p class="lab">ACC / AHA</p><p>Feasibility evidence.</p>
        <p class="lab">ESC / EACTS</p><p>Supported CE-mark program.</p>
      </div>
      <div class="qf"><h4>FDA / regulatory</h4><p>Precursor to CLASP II TR pivotal.</p></div>
      <div class="qf"><h4>Timeline</h4><ul class='bul'><li>Enrollment: 2019–2021</li><li>Published: JACC 2021 / JACC Cardiovasc Interv</li></ul></div>
    </aside>
  </div>
</div>
</details><details class="row" style="--hue:#6D5AB6" data-cat="Tricuspid TEER"
         data-status="published" data-signal="positive"
         data-pc="1" data-search="triluminate pivotal triluminate pivotal trial of tricuspid teer vs medical therapy abbott triclip guideline-directed medical therapy severe symptomatic tr, intermediate-or-greater surgical risk nct03904147 tricuspid teer triclip teer vs gdmt rct fda-approved 2024">
  <summary>
    <span class="chev" aria-hidden="true"></span>
    <span class="row-id">
      <span class="row-acr">TRILUMINATE Pivotal </span>
      <span class="row-name">TRILUMINATE Pivotal Trial of Tricuspid TEER vs Medical Therapy</span>
    </span>
    <span class="row-take">Established tricuspid TEER as an FDA-approved therapy; benefit is real but largely symptomatic/QoL.</span>
    <span class="row-meta"><span class='badge status-published'>🟢 Published</span><span class='dates'><span class='d-enr'>Enrolled 2019–2021</span><span class='d-pub'>Published 2023</span></span></span>
  </summary>
  <div class="body-inner">
  <div class='paperbar'><div class='plinks'><a class='plink primary' href='https://doi.org/10.1056/NEJMoa2300525' target='_blank' rel='noopener'>Read paper (DOI) ↗</a><a class='plink primary' href='https://pubmed.ncbi.nlm.nih.gov/36876753/' target='_blank' rel='noopener'>PubMed ↗</a><a class='plink registry' href='https://clinicaltrials.gov/study/NCT03904147' target='_blank' rel='noopener'>ClinicalTrials.gov ↗</a></div><span class='paper-cite'>Sorajja P, Whisenant B, Hamid N, et al. · <em>New England Journal of Medicine</em> · 2023</span></div>
  
  <p class="d-summary">The first randomized tricuspid TEER trial: TriClip beat medical therapy on a hierarchical composite driven mainly by quality-of-life improvement, with excellent safety and durable TR reduction — the basis for FDA approval.</p>
  <div class="d-grid">
    <div class="d-main">
      <section><h3>Study overview</h3><table class='overview'><tbody><tr><th>Device</th><td>Abbott TriClip</td></tr><tr><th>Intervention</th><td>TEER</td></tr><tr><th>Comparator</th><td>Guideline-directed medical therapy</td></tr><tr><th>Population</th><td>Severe symptomatic TR, intermediate-or-greater surgical risk</td></tr><tr><th>Risk group</th><td>Intermediate+ surgical risk</td></tr><tr><th>Sample size</th><td>350 (175 / 175) + single-arm</td></tr><tr><th>Enrollment</th><td>2019–2021</td></tr><tr><th>Follow-up</th><td>1 and 2 years</td></tr><tr><th>Trial type</th><td>Randomized, open-label</td></tr></tbody></table></section>
      <section><h3>Inclusion criteria</h3><p class='empty'>—</p></section>
      <section><h3>Primary endpoint</h3><p>Hierarchical composite (win ratio) of death/tricuspid surgery, HF hospitalization, and KCCQ change at 1 year.</p></section>
      <section><h3>Secondary endpoints</h3><ul class='bul'><li>TR grade ≤moderate</li><li>KCCQ</li><li>NYHA / 6-minute walk</li><li>Safety (MAE)</li></ul></section>
      <section><h3>Key results</h3><ul class='results'><li>Win ratio 1.48 (95% CI 1.06–2.13, P=0.02), driven by quality of life</li><li>TR reduced to moderate-or-less in ~90% at 30 days, sustained at 1 year</li><li>&gt;98% free from major adverse events at 30 days</li><li>No significant reduction in death or HF hospitalization</li></ul></section>
      <section><h3>Why this trial matters</h3><p>Practice-changing: basis for FDA approval of TriClip (April 2024).</p></section>
      <section><h3>Clinical pearls</h3><ul class='bul'><li>Benefit is predominantly symptomatic/QoL — counsel expectations accordingly.</li><li>TR reduction is durable and the procedure is remarkably safe.</li></ul></section>
      <section><h3>Limitations</h3><ul class='bul'><li>Open-label</li><li>Composite driven by KCCQ, not hard outcomes</li></ul></section>
    </div>
    <aside class="d-side">
      <div class="qf"><h4>Quick facts</h4>
        <dl>
          <dt>Valve</dt><dd>Tricuspid</dd>
          <dt>Disease</dt><dd>Secondary tricuspid regurgitation</dd>
          <dt>Procedure</dt><dd>TEER</dd>
          <dt>Sample</dt><dd>350 (175 / 175) + single-arm</dd>
          <dt>Follow-up</dt><dd>1 and 2 years</dd>
        </dl>
      </div>
      <div class="qf"><h4>Guidelines</h4>
        <p class="lab">ACC / AHA</p><p>Basis for FDA-approved T-TEER indication.</p>
        <p class="lab">ESC / EACTS</p><p>Supports TEER in selected severe TR.</p>
      </div>
      <div class="qf"><h4>FDA / regulatory</h4><p>TriClip FDA-approved April 2, 2024 (first tricuspid TEER); presented ACC.23.</p></div>
      <div class="qf"><h4>Timeline</h4><ul class='bul'><li>Enrollment: 2019–2021</li><li>Published: NEJM 2023 (ACC.23)</li><li>1-year: JACC 2025;85:235-246</li><li>2-year: Circulation 2025</li><li>FDA approval: Apr 2024</li></ul></div>
    </aside>
  </div>
</div>
</details><details class="row" style="--hue:#6D5AB6" data-cat="Tricuspid TEER"
         data-status="published" data-signal="positive"
         data-pc="1" data-search="tri-fr multicentric randomized evaluation of tricuspid teer in severe secondary tr (tri.fr) abbott triclip g4 gdmt alone severe isolated secondary tr, ineligible for surgery nct04646811 tricuspid teer triclip g4 teer vs gdmt rct investigator-led">
  <summary>
    <span class="chev" aria-hidden="true"></span>
    <span class="row-id">
      <span class="row-acr">TRI-FR </span>
      <span class="row-name">Multicentric Randomized Evaluation of Tricuspid TEER in Severe Secondary TR (Tri.Fr)</span>
    </span>
    <span class="row-take">Independent randomized confirmation that tricuspid TEER improves symptoms and functional status.</span>
    <span class="row-meta"><span class='badge status-published'>🟢 Published</span><span class='dates'><span class='d-enr'>Enrolled 2021–2023</span><span class='d-pub'>Published 2024</span></span></span>
  </summary>
  <div class="body-inner">
  <div class='paperbar'><div class='plinks'><a class='plink search' href='https://pubmed.ncbi.nlm.nih.gov/?term=TRI-FR%20AND%20%22Donal%20E%22%5BAuthor%5D' target='_blank' rel='noopener'>Find on PubMed ↗</a><a class='plink registry' href='https://clinicaltrials.gov/study/NCT04646811' target='_blank' rel='noopener'>ClinicalTrials.gov ↗</a></div><span class='paper-cite'>Donal E, et al. · <em>ESC 2024 (peer-reviewed publication)</em> · 2024</span></div>
  
  <p class="d-summary">A French/Belgian investigator-led RCT: tricuspid TEER plus medical therapy improved a clinical composite (symptoms, TR, functional status) versus medical therapy alone — the second positive randomized T-TEER trial.</p>
  <div class="d-grid">
    <div class="d-main">
      <section><h3>Study overview</h3><table class='overview'><tbody><tr><th>Device</th><td>Abbott TriClip G4</td></tr><tr><th>Intervention</th><td>TEER + GDMT</td></tr><tr><th>Comparator</th><td>GDMT alone</td></tr><tr><th>Population</th><td>Severe isolated secondary TR, ineligible for surgery</td></tr><tr><th>Risk group</th><td>High surgical risk</td></tr><tr><th>Sample size</th><td>300</td></tr><tr><th>Enrollment</th><td>2021–2023</td></tr><tr><th>Follow-up</th><td>1 year</td></tr><tr><th>Trial type</th><td>Randomized, open-label</td></tr></tbody></table></section>
      <section><h3>Inclusion criteria</h3><p class='empty'>—</p></section>
      <section><h3>Primary endpoint</h3><p>Packer clinical composite score (improved / unchanged / worse) at 1 year.</p></section>
      <section><h3>Secondary endpoints</h3><ul class='bul'><li>Patient global assessment</li><li>TR grade</li><li>6-minute walk</li><li>KCCQ</li></ul></section>
      <section><h3>Key results</h3><ul class='results'><li>Composite improvement 74.6% (TEER) vs 39.5% (GDMT); effect estimate 0.68 (P&lt;0.0001)</li><li>Technical success 97.3%; in-hospital mortality 0.6%</li><li>Most patients required 2 devices</li></ul></section>
      <section><h3>Why this trial matters</h3><p>Sponsor-independent confirmation of TRILUMINATE Pivotal&#x27;s QoL/functional benefit.</p></section>
      <section><h3>Clinical pearls</h3><ul class='bul'><li>Government-funded trial — reduces industry-sponsorship concerns.</li><li>Reinforces that the benefit is symptomatic/functional.</li></ul></section>
      <section><h3>Limitations</h3><ul class='bul'><li>Open-label</li><li>Composite is symptom/QoL-weighted</li></ul></section>
    </div>
    <aside class="d-side">
      <div class="qf"><h4>Quick facts</h4>
        <dl>
          <dt>Valve</dt><dd>Tricuspid</dd>
          <dt>Disease</dt><dd>Secondary tricuspid regurgitation</dd>
          <dt>Procedure</dt><dd>TEER</dd>
          <dt>Sample</dt><dd>300</dd>
          <dt>Follow-up</dt><dd>1 year</dd>
        </dl>
      </div>
      <div class="qf"><h4>Guidelines</h4>
        <p class="lab">ACC / AHA</p><p>Strengthens the T-TEER evidence base.</p>
        <p class="lab">ESC / EACTS</p><p>Supports TEER in secondary TR.</p>
      </div>
      <div class="qf"><h4>FDA / regulatory</h4><p>Not a US registration trial (European).</p></div>
      <div class="qf"><h4>Timeline</h4><ul class='bul'><li>Enrollment: 2021–2023</li><li>Presented: ESC 2024</li></ul></div>
    </aside>
  </div>
</div>
</details><details class="row" style="--hue:#6D5AB6" data-cat="Tricuspid TEER"
         data-status="published" data-signal="descriptive"
         data-pc="0" data-search="bright real-world outcomes of tricuspid teer with triclip (bright study) abbott triclip / triclip g4 registry severe symptomatic tr in routine practice  tricuspid teer triclip teer registry real-world">
  <summary>
    <span class="chev" aria-hidden="true"></span>
    <span class="row-id">
      <span class="row-acr">bRIGHT <span class='cav-dot' title='See caveat inside'>⚠</span></span>
      <span class="row-name">Real-World Outcomes of Tricuspid TEER With TriClip (bRIGHT Study)</span>
    </span>
    <span class="row-take">Real-world data confirm the safety and TR-reduction seen in the randomized trials.</span>
    <span class="row-meta"><span class='badge status-published'>🟢 Published</span><span class='dates'><span class='d-enr'>Enrolled 2020–2023</span><span class='d-pub'>Published 2024</span></span></span>
  </summary>
  <div class="body-inner">
  <div class='paperbar'><div class='plinks'><a class='plink primary' href='https://doi.org/10.1016/j.jacc.2024.05.006' target='_blank' rel='noopener'>Read paper (DOI) ↗</a></div><span class='paper-cite'>Lurz P, Rommel KP, Schmitz T, et al. · <em>Journal of the American College of Cardiology</em> · 2024</span></div>
  <div class='d-caveat'>⚠ Post-market registry (not a dedicated NCT here).</div>
  <p class="d-summary">A European post-market registry showing that tricuspid TEER reduces TR safely and durably across a broad range of real-world anatomies and centers.</p>
  <div class="d-grid">
    <div class="d-main">
      <section><h3>Study overview</h3><table class='overview'><tbody><tr><th>Device</th><td>Abbott TriClip / TriClip G4</td></tr><tr><th>Intervention</th><td>TEER</td></tr><tr><th>Comparator</th><td>Registry</td></tr><tr><th>Population</th><td>Severe symptomatic TR in routine practice</td></tr><tr><th>Risk group</th><td>Mixed / high risk</td></tr><tr><th>Sample size</th><td>registry cohort</td></tr><tr><th>Enrollment</th><td>2020–2023</td></tr><tr><th>Follow-up</th><td>30 days, 1 year, 2 years</td></tr><tr><th>Trial type</th><td>Prospective post-market registry</td></tr></tbody></table></section>
      <section><h3>Inclusion criteria</h3><p class='empty'>—</p></section>
      <section><h3>Primary endpoint</h3><p>Real-world safety and TR reduction.</p></section>
      <section><h3>Secondary endpoints</h3><ul class='bul'><li>NYHA / KCCQ</li><li>Durability</li><li>Procedural success</li></ul></section>
      <section><h3>Key results</h3><ul class='results'><li>Significant, durable TR reduction across broad anatomies</li><li>Safety consistent with the randomized trials</li></ul></section>
      <section><h3>Why this trial matters</h3><p>Provides generalizability for the RCT findings.</p></section>
      <section><h3>Clinical pearls</h3><ul class='bul'><li>Broader/less-selected patients and centers than TRILUMINATE.</li></ul></section>
      <section><h3>Limitations</h3><ul class='bul'><li>Non-randomized registry</li><li>Shorter-term outcomes</li></ul></section>
    </div>
    <aside class="d-side">
      <div class="qf"><h4>Quick facts</h4>
        <dl>
          <dt>Valve</dt><dd>Tricuspid</dd>
          <dt>Disease</dt><dd>Tricuspid regurgitation</dd>
          <dt>Procedure</dt><dd>TEER</dd>
          <dt>Sample</dt><dd>registry cohort</dd>
          <dt>Follow-up</dt><dd>30 days, 1 year, 2 years</dd>
        </dl>
      </div>
      <div class="qf"><h4>Guidelines</h4>
        <p class="lab">ACC / AHA</p><p>Supportive real-world evidence.</p>
        <p class="lab">ESC / EACTS</p><p>Generalizability data.</p>
      </div>
      <div class="qf"><h4>FDA / regulatory</h4><p>Real-world support for T-TEER.</p></div>
      <div class="qf"><h4>Timeline</h4><ul class='bul'><li>Published: JACC 2024;84:607-616 (1-year)</li></ul></div>
    </aside>
  </div>
</div>
</details><details class="row" style="--hue:#6D5AB6" data-cat="Tricuspid TEER"
         data-status="ongoing" data-signal="pending"
         data-pc="0" data-search="clasp ii tr edwards pascal tricuspid repair system pivotal trial edwards pascal gdmt alone severe symptomatic tr  tricuspid teer pascal teer pivotal ongoing">
  <summary>
    <span class="chev" aria-hidden="true"></span>
    <span class="row-id">
      <span class="row-acr">CLASP II TR <span class='cav-dot' title='See caveat inside'>⚠</span></span>
      <span class="row-name">Edwards PASCAL Tricuspid Repair System Pivotal Trial</span>
    </span>
    <span class="row-take">The key pivotal that could bring PASCAL to FDA approval for tricuspid TEER.</span>
    <span class="row-meta"><span class='badge status-ongoing'>🔵 Ongoing</span><span class='dates'><span class='d-enr'>Enrolled ongoing</span><span class='d-pub'>Not yet published</span></span></span>
  </summary>
  <div class="body-inner">
  <div class='paperbar none'>Not yet published — trial ongoing.</div>
  <div class='d-caveat'>⚠ NCT not confirmed here.</div>
  <p class="d-summary">The pivotal randomized trial of PASCAL tricuspid TEER plus medical therapy versus medical therapy — the trial that would confirm a second TEER platform for approval.</p>
  <div class="d-grid">
    <div class="d-main">
      <section><h3>Study overview</h3><table class='overview'><tbody><tr><th>Device</th><td>Edwards PASCAL</td></tr><tr><th>Intervention</th><td>TEER + GDMT</td></tr><tr><th>Comparator</th><td>GDMT alone</td></tr><tr><th>Population</th><td>Severe symptomatic TR</td></tr><tr><th>Risk group</th><td>High surgical risk</td></tr><tr><th>Sample size</th><td>pivotal target</td></tr><tr><th>Enrollment</th><td>ongoing</td></tr><tr><th>Follow-up</th><td>1 year+</td></tr><tr><th>Trial type</th><td>Randomized</td></tr></tbody></table></section>
      <section><h3>Inclusion criteria</h3><p class='empty'>—</p></section>
      <section><h3>Primary endpoint</h3><p>Safety/effectiveness vs medical therapy.</p></section>
      <section><h3>Secondary endpoints</h3><p class='empty'>—</p></section>
      <section><h3>Key results</h3><ul class='results'><li>Pending — trial ongoing</li></ul></section>
      <section><h3>Why this trial matters</h3><p>Would establish PASCAL as an approved T-TEER option.</p></section>
      <section><h3>Clinical pearls</h3><ul class='bul'><li>Watch how PASCAL vs TriClip outcomes compare in tricuspid anatomy.</li></ul></section>
      <section><h3>Limitations</h3><ul class='bul'><li>Not yet reporting</li><li>NCT unconfirmed here</li></ul></section>
    </div>
    <aside class="d-side">
      <div class="qf"><h4>Quick facts</h4>
        <dl>
          <dt>Valve</dt><dd>Tricuspid</dd>
          <dt>Disease</dt><dd>Tricuspid regurgitation</dd>
          <dt>Procedure</dt><dd>TEER</dd>
          <dt>Sample</dt><dd>pivotal target</dd>
          <dt>Follow-up</dt><dd>1 year+</dd>
        </dl>
      </div>
      <div class="qf"><h4>Guidelines</h4>
        <p class="lab">ACC / AHA</p><p>Pending.</p>
        <p class="lab">ESC / EACTS</p><p>Pending.</p>
      </div>
      <div class="qf"><h4>FDA / regulatory</h4><p>Potential PASCAL tricuspid approval.</p></div>
      <div class="qf"><h4>Timeline</h4><ul class='bul'><li>Status: ongoing</li></ul></div>
    </aside>
  </div>
</div>
</details></div></details><details class='group' data-cat="Tricuspid Transcatheter Replacement (TTVR)" style='--hue:#4E63B6' open><summary class='grouphead'><span class='gchev' aria-hidden='true'></span><span class='dot'></span>Tricuspid Transcatheter Replacement (TTVR)<span class='gcount'>3</span></summary><div class='rows'><details class="row" style="--hue:#4E63B6" data-cat="Tricuspid Transcatheter Replacement (TTVR)"
         data-status="ongoing" data-signal="descriptive"
         data-pc="0" data-search="lux-valve lux-valve / lux-valve plus transcatheter tricuspid replacement program jenscare lux-valve / lux-valve plus none (single-arm) severe symptomatic tr, high surgical risk  tricuspid transcatheter replacement (ttvr) lux-valve ttvr frontier">
  <summary>
    <span class="chev" aria-hidden="true"></span>
    <span class="row-id">
      <span class="row-acr">LuX-Valve <span class='cav-dot' title='See caveat inside'>⚠</span></span>
      <span class="row-name">LuX-Valve / LuX-Valve Plus Transcatheter Tricuspid Replacement Program</span>
    </span>
    <span class="row-take">A distinct TTVR design worth tracking as it moves toward transfemoral delivery and wider study.</span>
    <span class="row-meta"><span class='badge status-ongoing'>🔵 Ongoing</span><span class='dates'><span class='d-enr'>Enrolled late 2010s–ongoing</span><span class='d-pub'>Not yet published</span></span></span>
  </summary>
  <div class="body-inner">
  <div class='paperbar none'>Not yet published — trial ongoing.</div>
  <div class='d-caveat'>⚠ Primarily Chinese experience; Western pivotal data limited. NCT not confirmed here.</div>
  <p class="d-summary">A non-radial-force tricuspid replacement anchored to the interventricular septum; early (mainly Chinese) experience shows high TR elimination, with transfemoral (LuX-Valve Plus) iterations advancing.</p>
  <div class="d-grid">
    <div class="d-main">
      <section><h3>Study overview</h3><table class='overview'><tbody><tr><th>Device</th><td>Jenscare LuX-Valve / LuX-Valve Plus</td></tr><tr><th>Intervention</th><td>Transcatheter tricuspid replacement</td></tr><tr><th>Comparator</th><td>None (single-arm)</td></tr><tr><th>Population</th><td>Severe symptomatic TR, high surgical risk</td></tr><tr><th>Risk group</th><td>High surgical risk</td></tr><tr><th>Sample size</th><td>not fully extracted</td></tr><tr><th>Enrollment</th><td>late 2010s–ongoing</td></tr><tr><th>Follow-up</th><td>ongoing</td></tr><tr><th>Trial type</th><td>Single-arm / early studies</td></tr></tbody></table></section>
      <section><h3>Inclusion criteria</h3><p class='empty'>—</p></section>
      <section><h3>Primary endpoint</h3><p>Safety and TR reduction.</p></section>
      <section><h3>Secondary endpoints</h3><p class='empty'>—</p></section>
      <section><h3>Key results</h3><ul class='results'><li>High TR elimination in early series; broader/Western data still limited</li></ul></section>
      <section><h3>Why this trial matters</h3><p>Septal-anchoring design avoids radial force on the annulus.</p></section>
      <section><h3>Clinical pearls</h3><ul class='bul'><li>LuX-Valve Plus moves to transjugular/transfemoral delivery.</li></ul></section>
      <section><h3>Limitations</h3><ul class='bul'><li>Limited Western data</li><li>NCT unconfirmed here</li></ul></section>
    </div>
    <aside class="d-side">
      <div class="qf"><h4>Quick facts</h4>
        <dl>
          <dt>Valve</dt><dd>Tricuspid</dd>
          <dt>Disease</dt><dd>Tricuspid regurgitation</dd>
          <dt>Procedure</dt><dd>Transcatheter tricuspid replacement</dd>
          <dt>Sample</dt><dd>not fully extracted</dd>
          <dt>Follow-up</dt><dd>ongoing</dd>
        </dl>
      </div>
      <div class="qf"><h4>Guidelines</h4>
        <p class="lab">ACC / AHA</p><p>Investigational.</p>
        <p class="lab">ESC / EACTS</p><p>Investigational.</p>
      </div>
      <div class="qf"><h4>FDA / regulatory</h4><p>Not FDA-approved.</p></div>
      <div class="qf"><h4>Timeline</h4><ul class='bul'><li>Early series and iterations ongoing</li></ul></div>
    </aside>
  </div>
</div>
</details><details class="row" style="--hue:#4E63B6" data-cat="Tricuspid Transcatheter Replacement (TTVR)"
         data-status="published" data-signal="descriptive"
         data-pc="0" data-search="triscend edwards evoque tricuspid valve replacement early feasibility study edwards evoque none (single-arm) severe symptomatic tr, high surgical risk nct04221490 tricuspid transcatheter replacement (ttvr) evoque ttvr transfemoral single-arm">
  <summary>
    <span class="chev" aria-hidden="true"></span>
    <span class="row-id">
      <span class="row-acr">TRISCEND </span>
      <span class="row-name">Edwards EVOQUE Tricuspid Valve Replacement Early Feasibility Study</span>
    </span>
    <span class="row-take">EVOQUE showed that transcatheter tricuspid replacement can nearly abolish TR.</span>
    <span class="row-meta"><span class='badge status-published'>🟢 Published</span><span class='dates'><span class='d-enr'>Enrolled 2019–2021</span><span class='d-pub'>Published 2023</span></span></span>
  </summary>
  <div class="body-inner">
  <div class='paperbar'><div class='plinks'><a class='plink search' href='https://pubmed.ncbi.nlm.nih.gov/?term=TRISCEND%20AND%20%22Kodali%20S%22%5BAuthor%5D' target='_blank' rel='noopener'>Find on PubMed ↗</a><a class='plink registry' href='https://clinicaltrials.gov/study/NCT04221490' target='_blank' rel='noopener'>ClinicalTrials.gov ↗</a></div><span class='paper-cite'>Kodali S, Hahn RT, et al. · <em>Journal of the American College of Cardiology</em> · 2023</span></div>
  
  <p class="d-summary">The feasibility study of transfemoral EVOQUE tricuspid replacement showed near-elimination of TR with strong functional gains — establishing dedicated TTVR as viable.</p>
  <div class="d-grid">
    <div class="d-main">
      <section><h3>Study overview</h3><table class='overview'><tbody><tr><th>Device</th><td>Edwards EVOQUE</td></tr><tr><th>Intervention</th><td>Transcatheter tricuspid replacement</td></tr><tr><th>Comparator</th><td>None (single-arm)</td></tr><tr><th>Population</th><td>Severe symptomatic TR, high surgical risk</td></tr><tr><th>Risk group</th><td>High surgical risk</td></tr><tr><th>Sample size</th><td>132 (feasibility)</td></tr><tr><th>Enrollment</th><td>2019–2021</td></tr><tr><th>Follow-up</th><td>30 days, 6 months, 1 year</td></tr><tr><th>Trial type</th><td>Prospective single-arm (EFS)</td></tr></tbody></table></section>
      <section><h3>Inclusion criteria</h3><p class='empty'>—</p></section>
      <section><h3>Primary endpoint</h3><p>30-day safety and TR reduction.</p></section>
      <section><h3>Secondary endpoints</h3><ul class='bul'><li>TR grade ≤mild</li><li>NYHA / 6-minute walk</li><li>KCCQ</li></ul></section>
      <section><h3>Key results</h3><ul class='results'><li>~98% achieved TR ≤mild</li><li>Marked functional and quality-of-life improvement</li><li>Pacemaker implantation and bleeding are the main trade-offs</li></ul></section>
      <section><h3>Why this trial matters</h3><p>Established dedicated TTVR; basis for the TRISCEND II pivotal.</p></section>
      <section><h3>Clinical pearls</h3><ul class='bul'><li>Replacement abolishes TR more completely than repair — at the cost of anticoagulation/pacemakers.</li></ul></section>
      <section><h3>Limitations</h3><ul class='bul'><li>Single-arm</li><li>New-pacemaker and bleeding risk</li></ul></section>
    </div>
    <aside class="d-side">
      <div class="qf"><h4>Quick facts</h4>
        <dl>
          <dt>Valve</dt><dd>Tricuspid</dd>
          <dt>Disease</dt><dd>Tricuspid regurgitation</dd>
          <dt>Procedure</dt><dd>Transcatheter tricuspid replacement</dd>
          <dt>Sample</dt><dd>132 (feasibility)</dd>
          <dt>Follow-up</dt><dd>30 days, 6 months, 1 year</dd>
        </dl>
      </div>
      <div class="qf"><h4>Guidelines</h4>
        <p class="lab">ACC / AHA</p><p>Feasibility basis for TTVR.</p>
        <p class="lab">ESC / EACTS</p><p>Supported CE mark.</p>
      </div>
      <div class="qf"><h4>FDA / regulatory</h4><p>Breakthrough-device program; precursor to TRISCEND II.</p></div>
      <div class="qf"><h4>Timeline</h4><ul class='bul'><li>Enrollment: 2019–2021</li><li>Published: JACC 2023</li></ul></div>
    </aside>
  </div>
</div>
</details><details class="row" style="--hue:#4E63B6" data-cat="Tricuspid Transcatheter Replacement (TTVR)"
         data-status="published" data-signal="positive"
         data-pc="1" data-search="triscend ii edwards evoque tricuspid valve replacement pivotal trial edwards evoque optimal medical therapy severe or torrential tr, symptomatic nct04482062 tricuspid transcatheter replacement (ttvr) evoque ttvr vs gdmt rct fda-approved 2024">
  <summary>
    <span class="chev" aria-hidden="true"></span>
    <span class="row-id">
      <span class="row-acr">TRISCEND II </span>
      <span class="row-name">Edwards EVOQUE Tricuspid Valve Replacement Pivotal Trial</span>
    </span>
    <span class="row-take">EVOQUE is the first FDA-approved tricuspid replacement, with the strongest win ratio in the field.</span>
    <span class="row-meta"><span class='badge status-published'>🟢 Published</span><span class='dates'><span class='d-enr'>Enrolled 2021–2023</span><span class='d-pub'>Published 2025</span></span></span>
  </summary>
  <div class="body-inner">
  <div class='paperbar'><div class='plinks'><a class='plink search' href='https://pubmed.ncbi.nlm.nih.gov/?term=TRISCEND%20II%20AND%20%22Hahn%20RT%22%5BAuthor%5D' target='_blank' rel='noopener'>Find on PubMed ↗</a><a class='plink registry' href='https://clinicaltrials.gov/study/NCT04482062' target='_blank' rel='noopener'>ClinicalTrials.gov ↗</a></div><span class='paper-cite'>Hahn RT, Makkar R, Kodali S, et al. · <em>New England Journal of Medicine</em> · 2025</span></div>
  
  <p class="d-summary">The first randomized TTVR trial: EVOQUE plus medical therapy was superior to medical therapy on a hierarchical composite (win ratio ~2.0), with near-complete TR elimination — basis for the first FDA-approved tricuspid replacement.</p>
  <div class="d-grid">
    <div class="d-main">
      <section><h3>Study overview</h3><table class='overview'><tbody><tr><th>Device</th><td>Edwards EVOQUE</td></tr><tr><th>Intervention</th><td>TTVR + GDMT</td></tr><tr><th>Comparator</th><td>Optimal medical therapy</td></tr><tr><th>Population</th><td>Severe or torrential TR, symptomatic</td></tr><tr><th>Risk group</th><td>High surgical risk</td></tr><tr><th>Sample size</th><td>400 (392 randomized)</td></tr><tr><th>Enrollment</th><td>2021–2023</td></tr><tr><th>Follow-up</th><td>6 months primary; 1 year</td></tr><tr><th>Trial type</th><td>Randomized, open-label</td></tr></tbody></table></section>
      <section><h3>Inclusion criteria</h3><p class='empty'>—</p></section>
      <section><h3>Primary endpoint</h3><p>Hierarchical composite (win ratio) of death, RVAD/transplant, tricuspid intervention, HF hospitalization, KCCQ, NYHA, and 6-minute walk at 1 year.</p></section>
      <section><h3>Secondary endpoints</h3><ul class='bul'><li>TR grade ≤mild</li><li>KCCQ</li><li>NYHA / 6-minute walk</li><li>Safety (MAE)</li></ul></section>
      <section><h3>Key results</h3><ul class='results'><li>Win ratio 2.02 (95% CI 1.56–2.62, P&lt;0.001) favoring EVOQUE</li><li>~95–99% achieved TR ≤mild</li><li>More new pacemakers and bleeding with EVOQUE</li></ul></section>
      <section><h3>Why this trial matters</h3><p>Basis for the first FDA-approved transcatheter tricuspid replacement (Feb 2024).</p></section>
      <section><h3>Clinical pearls</h3><ul class='bul'><li>Largest treatment effect in tricuspid trials — but weigh pacemaker/anticoagulation trade-offs.</li><li>Approved without an FDA advisory panel, on a prespecified 6-month analysis of the first 150 patients.</li></ul></section>
      <section><h3>Limitations</h3><ul class='bul'><li>Open-label</li><li>Pacemaker and bleeding risk</li><li>Composite includes softer endpoints</li></ul></section>
    </div>
    <aside class="d-side">
      <div class="qf"><h4>Quick facts</h4>
        <dl>
          <dt>Valve</dt><dd>Tricuspid</dd>
          <dt>Disease</dt><dd>Tricuspid regurgitation</dd>
          <dt>Procedure</dt><dd>Transcatheter tricuspid replacement</dd>
          <dt>Sample</dt><dd>400 (392 randomized)</dd>
          <dt>Follow-up</dt><dd>6 months primary; 1 year</dd>
        </dl>
      </div>
      <div class="qf"><h4>Guidelines</h4>
        <p class="lab">ACC / AHA</p><p>Basis for FDA-approved TTVR indication.</p>
        <p class="lab">ESC / EACTS</p><p>EVOQUE CE mark (2023); supports replacement in selected severe TR.</p>
      </div>
      <div class="qf"><h4>FDA / regulatory</h4><p>EVOQUE FDA-approved February 2024 (first transcatheter tricuspid replacement); TCT 2023/2024.</p></div>
      <div class="qf"><h4>Timeline</h4><ul class='bul'><li>Enrollment: 2021–2023</li><li>6-month (first 150): TCT 2023</li><li>Full cohort: TCT 2024</li><li>Published: NEJM 2025</li><li>FDA approval: Feb 2024</li></ul></div>
    </aside>
  </div>
</div>
</details></div></details><details class='group' data-cat="Tricuspid Annuloplasty" style='--hue:#8E5AB6' open><summary class='grouphead'><span class='gchev' aria-hidden='true'></span><span class='dot'></span>Tricuspid Annuloplasty<span class='gcount'>2</span></summary><div class='rows'><details class="row" style="--hue:#8E5AB6" data-cat="Tricuspid Annuloplasty"
         data-status="published" data-signal="descriptive"
         data-pc="0" data-search="scout percutaneous tricuspid valve annuloplasty system for symptomatic chronic functional tr (trialign) mitralign trialign none (single-arm) symptomatic chronic functional tr nct02574650 tricuspid annuloplasty trialign direct annuloplasty single-arm early feasibility">
  <summary>
    <span class="chev" aria-hidden="true"></span>
    <span class="row-id">
      <span class="row-acr">SCOUT <span class='cav-dot' title='See caveat inside'>⚠</span></span>
      <span class="row-name">Percutaneous Tricuspid Valve Annuloplasty System for Symptomatic Chronic Functional TR (Trialign)</span>
    </span>
    <span class="row-take">An early proof-of-concept for suture-based tricuspid annuloplasty.</span>
    <span class="row-meta"><span class='badge status-published'>🟢 Published</span><span class='dates'><span class='d-enr'>Enrolled 2015–2016</span><span class='d-pub'>Published 2017</span></span></span>
  </summary>
  <div class="body-inner">
  <div class='paperbar'><div class='plinks'><a class='plink search' href='https://pubmed.ncbi.nlm.nih.gov/?term=SCOUT%20AND%20%22Hahn%20RT%22%5BAuthor%5D' target='_blank' rel='noopener'>Find on PubMed ↗</a><a class='plink registry' href='https://clinicaltrials.gov/study/NCT02574650' target='_blank' rel='noopener'>ClinicalTrials.gov ↗</a></div><span class='paper-cite'>Hahn RT, et al. · <em>Journal of the American College of Cardiology</em> · 2017</span></div>
  <div class='d-caveat'>⚠ Early device; limited ongoing clinical development.</div>
  <p class="d-summary">An early feasibility study of the Trialign system, which plicates the annulus to mimic a surgical Kay bicuspidization, showing reduced annular area and TR.</p>
  <div class="d-grid">
    <div class="d-main">
      <section><h3>Study overview</h3><table class='overview'><tbody><tr><th>Device</th><td>Mitralign Trialign</td></tr><tr><th>Intervention</th><td>Direct annuloplasty (bicuspidization)</td></tr><tr><th>Comparator</th><td>None (single-arm)</td></tr><tr><th>Population</th><td>Symptomatic chronic functional TR</td></tr><tr><th>Risk group</th><td>High surgical risk</td></tr><tr><th>Sample size</th><td>15 (SCOUT I)</td></tr><tr><th>Enrollment</th><td>2015–2016</td></tr><tr><th>Follow-up</th><td>30 days, 6 months</td></tr><tr><th>Trial type</th><td>Prospective single-arm (early feasibility)</td></tr></tbody></table></section>
      <section><h3>Inclusion criteria</h3><p class='empty'>—</p></section>
      <section><h3>Primary endpoint</h3><p>Feasibility, safety, and annular/TR reduction.</p></section>
      <section><h3>Secondary endpoints</h3><ul class='bul'><li>Annular area</li><li>TR grade</li><li>6-minute walk</li><li>Quality of life</li></ul></section>
      <section><h3>Key results</h3><ul class='results'><li>Reduced annular area and TR with functional improvement</li><li>Single-leaflet dehiscence observed in some patients</li></ul></section>
      <section><h3>Why this trial matters</h3><p>One of the first transcatheter tricuspid annuloplasty concepts.</p></section>
      <section><h3>Clinical pearls</h3><ul class='bul'><li>Recreates a surgical Kay-type annuloplasty percutaneously.</li></ul></section>
      <section><h3>Limitations</h3><ul class='bul'><li>Very small</li><li>Durability/dehiscence concerns</li><li>Limited ongoing development</li></ul></section>
    </div>
    <aside class="d-side">
      <div class="qf"><h4>Quick facts</h4>
        <dl>
          <dt>Valve</dt><dd>Tricuspid</dd>
          <dt>Disease</dt><dd>Functional tricuspid regurgitation</dd>
          <dt>Procedure</dt><dd>Direct transcatheter annuloplasty (bicuspidization)</dd>
          <dt>Sample</dt><dd>15 (SCOUT I)</dd>
          <dt>Follow-up</dt><dd>30 days, 6 months</dd>
        </dl>
      </div>
      <div class="qf"><h4>Guidelines</h4>
        <p class="lab">ACC / AHA</p><p>Historical proof-of-concept.</p>
        <p class="lab">ESC / EACTS</p><p>Early data.</p>
      </div>
      <div class="qf"><h4>FDA / regulatory</h4><p>Investigational.</p></div>
      <div class="qf"><h4>Timeline</h4><ul class='bul'><li>Enrollment: 2015–2016</li><li>Published: JACC 2017</li></ul></div>
    </aside>
  </div>
</div>
</details><details class="row" style="--hue:#8E5AB6" data-cat="Tricuspid Annuloplasty"
         data-status="published" data-signal="descriptive"
         data-pc="0" data-search="tri-repair tricuspid regurgitation repair with cardioband device study edwards cardioband (tricuspid) none (single-arm) symptomatic functional tr, high surgical risk nct02981953 tricuspid annuloplasty cardioband direct annuloplasty single-arm ce-mark">
  <summary>
    <span class="chev" aria-hidden="true"></span>
    <span class="row-id">
      <span class="row-acr">TRI-REPAIR </span>
      <span class="row-name">TrIcuspid Regurgitation RePAIr With Cardioband Device Study</span>
    </span>
    <span class="row-take">Direct annuloplasty can remodel the tricuspid annulus, but the evidence base is smaller than TEER.</span>
    <span class="row-meta"><span class='badge status-published'>🟢 Published</span><span class='dates'><span class='d-enr'>Enrolled 2016–2017</span><span class='d-pub'>Published 2019</span></span></span>
  </summary>
  <div class="body-inner">
  <div class='paperbar'><div class='plinks'><a class='plink search' href='https://pubmed.ncbi.nlm.nih.gov/?term=TRI-REPAIR%20AND%20%22Nickenig%20G%22%5BAuthor%5D' target='_blank' rel='noopener'>Find on PubMed ↗</a><a class='plink registry' href='https://clinicaltrials.gov/study/NCT02981953' target='_blank' rel='noopener'>ClinicalTrials.gov ↗</a></div><span class='paper-cite'>Nickenig G, et al. · <em>EuroIntervention</em> · 2019</span></div>
  
  <p class="d-summary">Direct transcatheter annuloplasty of the tricuspid annulus with Cardioband reduced annular size and TR with durable symptom improvement — a repair-based alternative to TEER and replacement.</p>
  <div class="d-grid">
    <div class="d-main">
      <section><h3>Study overview</h3><table class='overview'><tbody><tr><th>Device</th><td>Edwards Cardioband (tricuspid)</td></tr><tr><th>Intervention</th><td>Direct annuloplasty</td></tr><tr><th>Comparator</th><td>None (single-arm)</td></tr><tr><th>Population</th><td>Symptomatic functional TR, high surgical risk</td></tr><tr><th>Risk group</th><td>High surgical risk</td></tr><tr><th>Sample size</th><td>30</td></tr><tr><th>Enrollment</th><td>2016–2017</td></tr><tr><th>Follow-up</th><td>6 months, 1 year, 2 years</td></tr><tr><th>Trial type</th><td>Prospective single-arm, multicenter</td></tr></tbody></table></section>
      <section><h3>Inclusion criteria</h3><p class='empty'>—</p></section>
      <section><h3>Primary endpoint</h3><p>Safety and annular/TR reduction.</p></section>
      <section><h3>Secondary endpoints</h3><ul class='bul'><li>Septolateral annular diameter</li><li>TR grade</li><li>NYHA / 6-minute walk</li><li>KCCQ</li></ul></section>
      <section><h3>Key results</h3><ul class='results'><li>Significant annular reduction and TR improvement</li><li>Durable functional gains through 2 years</li></ul></section>
      <section><h3>Why this trial matters</h3><p>CE-mark tricuspid annuloplasty option; leaflet- and anatomy-preserving.</p></section>
      <section><h3>Clinical pearls</h3><ul class='bul'><li>Preserves future TEER/replacement options.</li><li>Right coronary artery course is a key procedural consideration.</li></ul></section>
      <section><h3>Limitations</h3><ul class='bul'><li>Small single-arm</li><li>Technically demanding</li></ul></section>
    </div>
    <aside class="d-side">
      <div class="qf"><h4>Quick facts</h4>
        <dl>
          <dt>Valve</dt><dd>Tricuspid</dd>
          <dt>Disease</dt><dd>Secondary tricuspid regurgitation</dd>
          <dt>Procedure</dt><dd>Direct transcatheter annuloplasty</dd>
          <dt>Sample</dt><dd>30</dd>
          <dt>Follow-up</dt><dd>6 months, 1 year, 2 years</dd>
        </dl>
      </div>
      <div class="qf"><h4>Guidelines</h4>
        <p class="lab">ACC / AHA</p><p>Not routine; anatomy-selected option.</p>
        <p class="lab">ESC / EACTS</p><p>CE-mark device.</p>
      </div>
      <div class="qf"><h4>FDA / regulatory</h4><p>Investigational in the US.</p></div>
      <div class="qf"><h4>Timeline</h4><ul class='bul'><li>Enrollment: 2016–2017</li><li>Published: EuroIntervention / JACC 2019–2021</li><li>CE mark obtained</li></ul></div>
    </aside>
  </div>
</div>
</details></div></details><details class='group' data-cat="Tricuspid Heterotopic / Caval" style='--hue:#B65AA0' open><summary class='grouphead'><span class='gchev' aria-hidden='true'></span><span class='dot'></span>Tricuspid Heterotopic / Caval<span class='gcount'>2</span></summary><div class='rows'><details class="row" style="--hue:#B65AA0" data-cat="Tricuspid Heterotopic / Caval"
         data-status="published" data-signal="descriptive"
         data-pc="0" data-search="hover heterotopic implantation of the sapien valve in the inferior vena cava for severe tr edwards sapien (in ivc) none (single-arm) severe tr, inoperable / very high risk nct02339974 tricuspid heterotopic / caval sapien ivc caval heterotopic off-label single-arm">
  <summary>
    <span class="chev" aria-hidden="true"></span>
    <span class="row-id">
      <span class="row-acr">HOVER <span class='cav-dot' title='See caveat inside'>⚠</span></span>
      <span class="row-name">Heterotopic Implantation of the SAPIEN Valve in the Inferior Vena Cava for Severe TR</span>
    </span>
    <span class="row-take">Proof-of-concept that an off-the-shelf valve in the IVC can palliate TR-related congestion.</span>
    <span class="row-meta"><span class='badge status-published'>🟢 Published</span><span class='dates'><span class='d-enr'>Enrolled 2015–2019</span></span></span>
  </summary>
  <div class="body-inner">
  <div class='paperbar'><div class='plinks'><a class='plink search' href='https://pubmed.ncbi.nlm.nih.gov/?term=Heterotopic%20Implantation%20of%20the%20SAPIEN%20Valve%20in%20the%20Inferior%20Vena%20Cava%20for%20Severe%20TR%20Tricuspid' target='_blank' rel='noopener'>Find on PubMed ↗</a><a class='plink registry' href='https://clinicaltrials.gov/study/NCT02339974' target='_blank' rel='noopener'>ClinicalTrials.gov ↗</a></div></div>
  <div class='d-caveat'>⚠ Off-label use of a commercially available valve; very small feasibility study.</div>
  <p class="d-summary">A feasibility study implanting a balloon-expandable SAPIEN valve in the inferior vena cava to palliate right-heart congestion from severe TR in inoperable patients.</p>
  <div class="d-grid">
    <div class="d-main">
      <section><h3>Study overview</h3><table class='overview'><tbody><tr><th>Device</th><td>Edwards SAPIEN (in IVC)</td></tr><tr><th>Intervention</th><td>Single-site caval valve implantation</td></tr><tr><th>Comparator</th><td>None (single-arm)</td></tr><tr><th>Population</th><td>Severe TR, inoperable / very high risk</td></tr><tr><th>Risk group</th><td>Prohibitive surgical risk</td></tr><tr><th>Sample size</th><td>15 (planned)</td></tr><tr><th>Enrollment</th><td>2015–2019</td></tr><tr><th>Follow-up</th><td>30 days, 6 months</td></tr><tr><th>Trial type</th><td>Prospective single-arm feasibility</td></tr></tbody></table></section>
      <section><h3>Inclusion criteria</h3><p class='empty'>—</p></section>
      <section><h3>Primary endpoint</h3><p>30-day safety; 6-month symptom palliation.</p></section>
      <section><h3>Secondary endpoints</h3><ul class='bul'><li>NYHA class</li><li>Congestion symptoms</li></ul></section>
      <section><h3>Key results</h3><ul class='results'><li>Feasible IVC implantation with symptom palliation in selected patients</li></ul></section>
      <section><h3>Why this trial matters</h3><p>Early demonstration of single-site caval valve implantation.</p></section>
      <section><h3>Clinical pearls</h3><ul class='bul'><li>Palliative — addresses congestion, not the tricuspid valve.</li></ul></section>
      <section><h3>Limitations</h3><ul class='bul'><li>Very small</li><li>Off-label device use</li><li>Palliative intent</li></ul></section>
    </div>
    <aside class="d-side">
      <div class="qf"><h4>Quick facts</h4>
        <dl>
          <dt>Valve</dt><dd>Tricuspid</dd>
          <dt>Disease</dt><dd>Severe tricuspid regurgitation</dd>
          <dt>Procedure</dt><dd>Single-site caval valve implantation (IVC)</dd>
          <dt>Sample</dt><dd>15 (planned)</dd>
          <dt>Follow-up</dt><dd>30 days, 6 months</dd>
        </dl>
      </div>
      <div class="qf"><h4>Guidelines</h4>
        <p class="lab">ACC / AHA</p><p>Historical proof-of-concept.</p>
        <p class="lab">ESC / EACTS</p><p>Early data.</p>
      </div>
      <div class="qf"><h4>FDA / regulatory</h4><p>Off-label.</p></div>
      <div class="qf"><h4>Timeline</h4><ul class='bul'><li>Enrollment: 2015–2019</li></ul></div>
    </aside>
  </div>
</div>
</details><details class="row" style="--hue:#B65AA0" data-cat="Tricuspid Heterotopic / Caval"
         data-status="published" data-signal="descriptive"
         data-pc="0" data-search="tricus euro safety and efficacy of the tricvalve transcatheter bicaval valves system (tricus euro) p+f tricvalve none (single-arm) severe symptomatic tr, high surgical risk, significant caval backflow nct04141137 tricuspid heterotopic / caval tricvalve bicaval / cavi heterotopic single-arm ce-mark">
  <summary>
    <span class="chev" aria-hidden="true"></span>
    <span class="row-id">
      <span class="row-acr">TRICUS EURO </span>
      <span class="row-name">Safety and Efficacy of the TricValve Transcatheter Bicaval Valves System (TRICUS EURO)</span>
    </span>
    <span class="row-take">Caval valve implantation palliates congestion when the valve itself can&#x27;t be repaired or replaced.</span>
    <span class="row-meta"><span class='badge status-published'>🟢 Published</span><span class='dates'><span class='d-enr'>Enrolled 2019–2021</span><span class='d-pub'>Published 2022</span></span></span>
  </summary>
  <div class="body-inner">
  <div class='paperbar'><div class='plinks'><a class='plink primary' href='https://doi.org/10.1016/j.jcin.2022.05.022' target='_blank' rel='noopener'>Read paper (DOI) ↗</a><a class='plink registry' href='https://clinicaltrials.gov/study/NCT04141137' target='_blank' rel='noopener'>ClinicalTrials.gov ↗</a></div><span class='paper-cite'>Estévez-Loureiro R, et al. · <em>JACC: Cardiovascular Interventions</em> · 2022</span></div>
  
  <p class="d-summary">A dedicated bicaval valve system (SVC + IVC) that treats the congestive consequences of severe TR rather than the valve itself; improved symptoms and quality of life at 6–12 months in high-risk patients — the basis for CE mark.</p>
  <div class="d-grid">
    <div class="d-main">
      <section><h3>Study overview</h3><table class='overview'><tbody><tr><th>Device</th><td>P+F TricValve</td></tr><tr><th>Intervention</th><td>Bicaval valve implantation (CAVI)</td></tr><tr><th>Comparator</th><td>None (single-arm)</td></tr><tr><th>Population</th><td>Severe symptomatic TR, high surgical risk, significant caval backflow</td></tr><tr><th>Risk group</th><td>High surgical risk</td></tr><tr><th>Sample size</th><td>35 (44 pooled with first-in-human)</td></tr><tr><th>Enrollment</th><td>2019–2021</td></tr><tr><th>Follow-up</th><td>30 days, 6 months, 1 year</td></tr><tr><th>Trial type</th><td>Prospective single-arm, multicenter</td></tr></tbody></table></section>
      <section><h3>Inclusion criteria</h3><p class='empty'>—</p></section>
      <section><h3>Primary endpoint</h3><p>30-day safety; 6-month quality-of-life and functional status.</p></section>
      <section><h3>Secondary endpoints</h3><ul class='bul'><li>NYHA class</li><li>KCCQ</li><li>Caval backflow</li><li>Right-heart congestion markers</li></ul></section>
      <section><h3>Key results</h3><ul class='results'><li>Significant quality-of-life and functional improvement at 6–12 months</li><li>Does not reduce true tricuspid TR — treats caval backflow/congestion</li><li>Mortality aligned with baseline TRI-SCORE</li></ul></section>
      <section><h3>Why this trial matters</h3><p>Offers a palliative option for patients unsuitable for TEER or orthotopic replacement.</p></section>
      <section><h3>Clinical pearls</h3><ul class='bul'><li>Treats symptoms of congestion, not the regurgitation — set expectations accordingly.</li><li>Useful when coaptation gaps or anatomy preclude TEER/replacement.</li></ul></section>
      <section><h3>Limitations</h3><ul class='bul'><li>Small single-arm</li><li>Does not correct TR</li><li>Palliative intent</li></ul></section>
    </div>
    <aside class="d-side">
      <div class="qf"><h4>Quick facts</h4>
        <dl>
          <dt>Valve</dt><dd>Tricuspid</dd>
          <dt>Disease</dt><dd>Severe tricuspid regurgitation</dd>
          <dt>Procedure</dt><dd>Bicaval valve implantation (CAVI)</dd>
          <dt>Sample</dt><dd>35 (44 pooled with first-in-human)</dd>
          <dt>Follow-up</dt><dd>30 days, 6 months, 1 year</dd>
        </dl>
      </div>
      <div class="qf"><h4>Guidelines</h4>
        <p class="lab">ACC / AHA</p><p>Niche palliative option.</p>
        <p class="lab">ESC / EACTS</p><p>CE mark (May 2021).</p>
      </div>
      <div class="qf"><h4>FDA / regulatory</h4><p>Investigational in the US.</p></div>
      <div class="qf"><h4>Timeline</h4><ul class='bul'><li>Enrollment: 2019–2021</li><li>Published: JACC Cardiovasc Interv 2022;15:1366-1377</li><li>CE mark: May 2021</li></ul></div>
    </aside>
  </div>
</div>
</details></div></details><details class='group' data-cat="Tricuspid Frontier / Next-Gen Device" style='--hue:#5A78B6' open><summary class='grouphead'><span class='gchev' aria-hidden='true'></span><span class='dot'></span>Tricuspid Frontier / Next-Gen Device<span class='gcount'>1</span></summary><div class='rows'><details class="row" style="--hue:#5A78B6" data-cat="Tricuspid Frontier / Next-Gen Device"
         data-status="ongoing" data-signal="pending"
         data-pc="0" data-search="tandem i (croívalve) european feasibility study of the croívalve duo transcatheter tricuspid coaptation valve system croívalve duo none (single-arm) severe symptomatic tr nct05296148 tricuspid frontier / next-gen device croívalve duo coaptation valve single-arm ongoing">
  <summary>
    <span class="chev" aria-hidden="true"></span>
    <span class="row-id">
      <span class="row-acr">TANDEM I (CroíValve) </span>
      <span class="row-name">European Feasibility Study of the CroíValve DUO Transcatheter Tricuspid Coaptation Valve System</span>
    </span>
    <span class="row-take">A novel coaptation-valve concept to watch in the crowded tricuspid frontier.</span>
    <span class="row-meta"><span class='badge status-ongoing'>🔵 Ongoing</span><span class='dates'><span class='d-enr'>Enrolled 2022–ongoing</span><span class='d-pub'>Not yet published</span></span></span>
  </summary>
  <div class="body-inner">
  <div class='paperbar'><div class='plinks'><a class='plink registry' href='https://clinicaltrials.gov/study/NCT05296148' target='_blank' rel='noopener'>ClinicalTrials.gov ↗</a></div></div>
  
  <p class="d-summary">An early feasibility study of a coaptation-valve system that anchors in the SVC and places a spacer at the tricuspid annulus — a hybrid concept between caval and orthotopic approaches.</p>
  <div class="d-grid">
    <div class="d-main">
      <section><h3>Study overview</h3><table class='overview'><tbody><tr><th>Device</th><td>CroíValve DUO</td></tr><tr><th>Intervention</th><td>Transcatheter tricuspid coaptation valve</td></tr><tr><th>Comparator</th><td>None (single-arm)</td></tr><tr><th>Population</th><td>Severe symptomatic TR</td></tr><tr><th>Risk group</th><td>High surgical risk</td></tr><tr><th>Sample size</th><td>early feasibility</td></tr><tr><th>Enrollment</th><td>2022–ongoing</td></tr><tr><th>Follow-up</th><td>ongoing</td></tr><tr><th>Trial type</th><td>Prospective single-arm (EFS)</td></tr></tbody></table></section>
      <section><h3>Inclusion criteria</h3><p class='empty'>—</p></section>
      <section><h3>Primary endpoint</h3><p>Safety and performance.</p></section>
      <section><h3>Secondary endpoints</h3><p class='empty'>—</p></section>
      <section><h3>Key results</h3><ul class='results'><li>Pending — early feasibility ongoing</li></ul></section>
      <section><h3>Why this trial matters</h3><p>Represents the diversity of next-generation tricuspid approaches.</p></section>
      <section><h3>Clinical pearls</h3><ul class='bul'><li>Combines a caval anchor with an annular coaptation element.</li></ul></section>
      <section><h3>Limitations</h3><ul class='bul'><li>Very early stage</li><li>Not yet reporting</li></ul></section>
    </div>
    <aside class="d-side">
      <div class="qf"><h4>Quick facts</h4>
        <dl>
          <dt>Valve</dt><dd>Tricuspid</dd>
          <dt>Disease</dt><dd>Tricuspid regurgitation</dd>
          <dt>Procedure</dt><dd>Transcatheter tricuspid coaptation valve</dd>
          <dt>Sample</dt><dd>early feasibility</dd>
          <dt>Follow-up</dt><dd>ongoing</dd>
        </dl>
      </div>
      <div class="qf"><h4>Guidelines</h4>
        <p class="lab">ACC / AHA</p><p>Pending.</p>
        <p class="lab">ESC / EACTS</p><p>Pending.</p>
      </div>
      <div class="qf"><h4>FDA / regulatory</h4><p>Early feasibility.</p></div>
      <div class="qf"><h4>Timeline</h4><ul class='bul'><li>Started: 2022</li><li>Status: ongoing</li></ul></div>
    </aside>
  </div>
</div>
</details></div></details>
  <p id="noresults" class="noresults">No trials match those filters. Clear the search or pick “All”.</p>
</main>

<footer class="pagefoot">
  ValveTrials.com — a cardiology valve-trial reference. Paper links point to the verified DOI or PubMed
  record; where none was verified, a “Find on PubMed” search link is provided instead of a fabricated one.
  Negative-result trials are excluded from list views (still present in <span class="mono">trials_data.py</span>).
  ⚠ flags provisional or context items. A reference aid, not clinical advice.
</footer>
<script>
const $ = s => document.querySelector(s);
const rows = Array.from(document.querySelectorAll('details.row'));
const groups = Array.from(document.querySelectorAll('details.group'));
const search = $('#search');
const count = $('#count');
let state = {text:'',cat:'all',status:'all',pc:false};
function apply(){
  let shown=0;
  rows.forEach(r=>{
    const okText=!state.text||r.dataset.search.includes(state.text);
    const okCat=state.cat==='all'||r.dataset.cat===state.cat;
    const okStatus=state.status==='all'||r.dataset.status===state.status;
    const okPc=!state.pc||r.dataset.pc==='1';
    const vis=okText&&okCat&&okStatus&&okPc;
    r.style.display=vis?'':'none';r.dataset.vis=vis?'1':'0';if(vis)shown++;
  });
  const filterActive=!!(state.text||state.cat!=='all'||state.status!=='all'||state.pc);
  groups.forEach(g=>{
    const visRows=g.querySelectorAll('details.row[data-vis="1"]').length;
    const catOk=state.cat==='all'||g.dataset.cat===state.cat;
    g.style.display=(visRows>0&&catOk)?'':'none';
    if(filterActive&&visRows>0&&catOk)g.open=true;
  });
  count.textContent=shown+' / '+rows.length+' trials shown';
  $('#noresults').style.display=shown?'none':'block';
}
search.addEventListener('input',e=>{state.text=e.target.value.trim().toLowerCase();apply();});
document.querySelectorAll('.fchip').forEach(c=>c.addEventListener('click',()=>{
  document.querySelectorAll('.fchip').forEach(x=>x.classList.remove('active'));
  c.classList.add('active');state.cat=c.dataset.filter==='all'?'all':c.dataset.value;apply();
}));
document.querySelectorAll('.seg[data-group]').forEach(seg=>{
  const group=seg.dataset.group;
  seg.querySelectorAll('button').forEach(b=>b.addEventListener('click',()=>{
    seg.querySelectorAll('button').forEach(x=>x.classList.remove('active'));
    b.classList.add('active');
    if(group==='pc')state.pc=b.dataset.value==='1';else state[group]=b.dataset.value;apply();
  }));
});
$('#expandAll').addEventListener('click',()=>{groups.forEach(g=>g.open=true);rows.forEach(r=>{if(r.style.display!=='none')r.open=true;});});
$('#collapseAll').addEventListener('click',()=>{rows.forEach(r=>r.open=false);groups.forEach(g=>g.open=false);});
apply();
</script>
</body>
</html>
