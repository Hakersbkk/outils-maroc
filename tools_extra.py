#!/usr/bin/env python3
"""Extra tool batch 2 — merges into generate.py's JS_TOOLS. Client-side only."""
EXTRA = {
    "convertisseur-texte": ("Convertisseur de texte : MAJUSCULES, minuscules, Titre, camelCase",
        "Transformez votre texte en un clic : majuscules, minuscules, Première Lettre, camelCase, inverse.",
        """<h1>Convertisseur de texte</h1>
<textarea id="t" rows="6" placeholder="Collez votre texte..."></textarea>
<button onclick="f('up')">MAJUSCULES</button> <button onclick="f('lo')">minuscules</button>
<button onclick="f('ti')">Première Lettre</button> <button onclick="f('ca')">camelCase</button>
<button onclick="f('rv')">Inverser</button>
<div class="out" id="r" style="font-family:monospace;white-space:pre-wrap"></div>
<script>function f(m){const t=document.getElementById('t');let v=t.value;
if(m==='up')v=v.toUpperCase();if(m==='lo')v=v.toLowerCase();
if(m==='ti')v=v.toLowerCase().replace(/(^|\\s)(\\S)/g,(a,b,c)=>b+c.toUpperCase());
if(m==='ca')v=v.toLowerCase().replace(/[^a-z0-9]+(.)/g,(a,c)=>c.toUpperCase());
if(m==='rv')v=[...v].reverse().join('');
document.getElementById('r').textContent=v;}</script>""",),

    "formateur-json": ("Formateur et validateur JSON en ligne (beautifier)",
        "Collez du JSON : indentez-le, validez-le, corrigez les erreurs signalées. Local, rien n'est envoyé.",
        """<h1>Formateur JSON</h1>
<textarea id="t" rows="7" placeholder='{"exemple": [1,2,3]}' style="font-family:monospace"></textarea>
<button onclick="fmt()">Formater / Valider</button>
<div class="out" id="r"></div>
<script>function fmt(){const s=document.getElementById('t').value,r=document.getElementById('r');
try{r.textContent=JSON.stringify(JSON.parse(s),null,2);r.style.color='#1d7a46'}catch(e){r.textContent='❌ Erreur JSON : '+e.message;r.style.color='#b3261e'}}</script>""",),

    "base64-encode-decode": ("Encodeur / décodeur Base64 en ligne",
        "Encodez ou décodez du texte en Base64 instantanément, directement dans votre navigateur.",
        """<h1>Base64 encode / decode</h1>
<textarea id="t" rows="5" placeholder="Votre texte..."></textarea>
<button onclick="e(1)">Encoder →</button> <button onclick="e(0)">← Décoder</button>
<div class="out" id="r" style="font-family:monospace;white-space:pre-wrap"></div>
<script>function e(en){const t=document.getElementById('t').value,r=document.getElementById('r');
try{r.textContent=en?btoa(unescape(encodeURIComponent(t))):decodeURIComponent(escape(atob(t.trim())))}catch(x){r.textContent='❌ Entrée Base64 invalide';}}</script>""",),

    "hachage-sha256": ("Générateur de hash SHA-256 en ligne",
        "Calculez l'empreinte SHA-256 d'un texte. Calculée localement via l'API WebCrypto.",
        """<h1>Hash SHA-256</h1>
<textarea id="t" rows="4" placeholder="Votre texte..."></textarea>
<button onclick="h()">Calculer le hash</button>
<div class="out" id="r" style="font-family:monospace;word-break:break-all"></div>
<script>async function h(){const d=new TextEncoder().encode(document.getElementById('t').value);
const b=await crypto.subtle.digest('SHA-256',d);
document.getElementById('r').textContent=[...new Uint8Array(b)].map(x=>x.toString(16).padStart(2,'0')).join('');}</script>""",),

    "convertisseur-unites": ("Convertisseur d'unités : longueur, poids, température",
        "Convertissez m/km/miles, kg/livres, °C/°F et plus, en un calcul instantané.",
        """<h1>Convertisseur d'unités</h1>
<label>Valeur <input id="v" type="number" value="10"></label>
<label>Catégorie <select id="c" onchange="units()"><option value="len">Longueur</option><option value="w">Poids</option><option value="t">Température</option></select></label>
<label>De <select id="a"></select> vers <select id="b"></select></label>
<button onclick="calc()">Convertir</button><div class="out" id="r"></div>
<script>const U={len:{m:1,km:1000,cm:.01,'mile':1609.344,'pied (ft)':.3048,'pouce (in)':.0254},
w:{kg:1,g:.001,'livre (lb)':.453592,'tonne':1000},t:{'°C':0,'°F':1}};
function units(){const c=document.getElementById('c').value;const o=Object.keys(U[c]);
document.getElementById('a').innerHTML=document.getElementById('b').innerHTML=o.map(u=>`<option>${u}</option>`).join('');calc()}
function calc(){const v=+document.getElementById('v').value||0,c=document.getElementById('c').value,a=document.getElementById('a').value,b=document.getElementById('b').value;
let r;if(c==='t'){let cc=a==='°C'?v:(v-32)*5/9;r=b==='°C'?cc:cc*9/5+32}
else r=v*U[c][a]/U[c][b];
document.getElementById('r').innerHTML=`<b>${v} ${a} = ${r.toFixed(4)} ${b}</b>`}
units();</script>""",),

    "calculateur-pourboire": ("Calculateur de pourboire et addition partagée",
        "Calculez le pourboire et divisez l'addition entre amis en un clic.",
        """<h1>Pourboire & addition</h1>
<label>Addition (DH) <input id="b" type="number" value="250"></label>
<label>Pourboire % <input id="p" type="number" value="10"></label>
<label>Personnes <input id="n" type="number" value="4" min="1"></label>
<button onclick="calc()">Calculer</button><div class="out" id="r"></div>
<script>function calc(){const b=+document.getElementById('b').value||0,p=+document.getElementById('p').value||0,n=Math.max(1,+document.getElementById('n').value||1);
const tip=b*p/100,tot=b+tip;
document.getElementById('r').innerHTML=`Pourboire : <b>${tip.toFixed(0)} DH</b> · Total : <b>${tot.toFixed(0)} DH</b><br>Par personne : <b>${(tot/n).toFixed(0)} DH</b>`;}</script>""",),

    "calculateur-dates": ("Calculateur de dates : différence et échéances",
        "Combien de jours entre deux dates ? Ajoutez ou retirez des jours d'une date.",
        """<h1>Calculateur de dates</h1>
<label>Date 1 <input id="d1" type="date"></label>
<label>Date 2 <input id="d2" type="date"></label>
<button onclick="diff()">Différence</button>
<div class="out" id="r"></div>
<script>function diff(){const a=new Date(document.getElementById('d1').value),b=new Date(document.getElementById('d2').value);
if(!a||!b||isNaN(a)||isNaN(b)){return}
document.getElementById('r').innerHTML=`Différence : <b>${Math.abs(Math.round((b-a)/86400000))}</b> jours (${(Math.abs(b-a)/31557600000).toFixed(2)} années)`;}</script>""",),

    "tirage-au-sort": ("Tirage au sort : nombre aléatoire ou liste",
        "Lancez un dé, tirez un gagnant dans une liste, ou générez un nombre aléatoire.",
        """<h1>Tirage au sort</h1>
<label>Min <input id="a" type="number" value="1"></label>
<label>Max <input id="b" type="number" value="100"></label>
<label>Liste (un nom par ligne — optionnel)</label>
<textarea id="l" rows="4" placeholder="Karim\\nSara\\nYoussef"></textarea>
<button onclick="pick()">Tirer au sort</button>
<div class="out" id="r" style="font-size:1.4rem;font-weight:700"></div>
<script>function pick(){const l=document.getElementById('l').value.split('\\n').map(x=>x.trim()).filter(Boolean);
if(l.length){const w=l[Math.floor(Math.random()*l.length)];document.getElementById('r').textContent='🏆 '+w;return}
const a=+document.getElementById('a').value,b=+document.getElementById('b').value;
document.getElementById('r').textContent='🎲 '+String(Math.floor(Math.random()*(b-a+1))+a);}</script>""",),

    "convertisseur-couleurs": ("Convertisseur de couleurs : HEX ⇄ RGB",
        "Convertissez une couleur hexadécimale en RGB et voyez le résultat.",
        """<h1>HEX ⇄ RGB</h1>
<input id="c" type="color" value="#e2552b" style="width:100%;height:44px">
<div class="out" id="r"></div>
<script>const c=document.getElementById('c');function upd(){const v=c.value;
const r=parseInt(v.slice(1,3),16),g=parseInt(v.slice(3,5),16),b=parseInt(v.slice(5,7),16);
document.getElementById('r').innerHTML=`HEX <b>${v.toUpperCase()}</b> · RGB <b>rgb(${r}, ${g}, ${b})</b>`;}
c.addEventListener('input',upd);upd();</script>""",),

    "generateur-facture-simple": ("Générateur de facture simple (PDF à imprimer) — Maroc",
        "Créez une facture propre en 2 minutes avec TVA, puis imprimez-la en PDF. Aucun compte.",
        """<h1>Générateur de facture simple</h1>
<label>Votre nom / société <input id="from" placeholder="Yassine KCHAIT"></label>
<label>Client <input id="to" placeholder="Nom du client"></label>
<label>Description <input id="desc" placeholder="Site web one-page + hébergement"></label>
<label>Montant HT (DH) <input id="amt" type="number" value="490"></label>
<label>TVA % <input id="tva" type="number" value="0"></label>
<button onclick="make()">Générer l'aperçu</button> <button onclick="window.print()">🖨️ Imprimer / PDF</button>
<div class="out" id="r" style="display:none;background:#fff"></div>
<script>function make(){const g=id=>document.getElementById(id).value||'—';
const amt=+document.getElementById('amt').value||0,tva=+document.getElementById('tva').value||0;
const tt=amt*tva/100,tot=amt+tt,d=new Date().toLocaleDateString('fr-FR');
const r=document.getElementById('r');r.style.display='block';
r.innerHTML=`<h2 style="margin:0 0 8px">FACTURE</h2><p style="color:#667380">N° ${Date.now().toString().slice(-6)} · ${d}</p>
<p><b>De :</b> ${g('from')}<br><b>À :</b> ${g('to')}</p>
<table style="width:100%;border-collapse:collapse;margin:10px 0"><tr style="border-bottom:2px solid #333"><th align="left">Description</th><th align="right">Montant</th></tr>
<tr><td>${g('desc')}</td><td align="right">${amt.toFixed(2)} DH</td></tr>
<tr><td>TVA ${tva}%</td><td align="right">${tt.toFixed(2)} DH</td></tr>
<tr style="border-top:2px solid #333;font-weight:700"><td>TOTAL</td><td align="right">${tot.toFixed(2)} DH</td></tr></table>
<p style="color:#667380">Payable par virement bancaire ou Cash Plus. Merci !</p>`;
r.classList.add('printable');}
</script>""",),

    "supprimer-doublons-lignes": ("Supprimer les doublons de lignes d'un texte",
        "Collez une liste : supprimez les doublons, videz les lignes, triez alphabétiquement.",
        """<h1>Anti-doublons de lignes</h1>
<textarea id="t" rows="6" placeholder="Une valeur par ligne..."></textarea>
<button onclick="go(1)">Supprimer doublons</button> <button onclick="go(2)">Trier A→Z</button> <button onclick="go(3)">Retirer lignes vides</button>
<div class="out" id="r" style="font-family:monospace;white-space:pre-wrap"></div>
<script>function go(m){const t=document.getElementById('t').value.split('\\n');
let v=m===1?[...new Set(t)]:m===2?[...new Set(t)].sort((a,b)=>a.localeCompare(b)):t.filter(x=>x.trim());
v=v.filter(x=>x!=='');
document.getElementById('r').textContent=v.join('\\n');
document.getElementById('r').innerHTML+=`<br><small>${t.length} → ${v.length} lignes</small>`;}</script>""",),

    "mailto-generator": ("Générateur de lien e-mail (mailto) prêt à partager",
        "Créez un lien mailto avec sujet et message pré-remplis pour votre site ou signature.",
        """<h1>Générateur mailto</h1>
<label>Adresse e-mail <input id="to" placeholder="contact@exemple.com"></label>
<label>Sujet <input id="s" placeholder="Demande de devis"></label>
<label>Message <textarea id="m" rows="3" placeholder="Bonjour, ..."></textarea></label>
<button onclick="gen()">Générer</button>
<div class="out" id="r" style="font-family:monospace;word-break:break-all"></div>
<script>function gen(){const u=document.getElementById('to').value.trim();
document.getElementById('r').textContent=`mailto:${u}?subject=${encodeURIComponent(document.getElementById('s').value)}&body=${encodeURIComponent(document.getElementById('m').value)}`;}</script>""",),

    "calendrier-prayer-horaire-priere": ("Horaire de prière au Maroc (aujourd'hui, votre ville)",
        "Horaires de prière du jour pour les grandes villes du Maroc, via l'API Aladhan.",
        """<h1>Horaire de prière — Maroc</h1>
<label>Ville <select id="c"><option>Casablanca</option><option>Rabat</option><option>Marrakech</option><option>Fès</option><option>Tanger</option><option>Agadir</option><option>Oujda</option></select></label>
<button onclick="load()">Afficher</button><div class="out" id="r">Choisissez votre ville…</div>
<script>async function load(){const c=document.getElementById('c').value;
document.getElementById('r').textContent='Chargement…';
try{const d=await(await fetch(`https://api.aladhan.com/v1/timingsByCity?city=${encodeURIComponent(c)}&country=Morocco&method=21`)).json();
const t=d.data.timings;document.getElementById('r').innerHTML=
Object.entries(t).filter(([k])=>['Fajr','Sunrise','Dhuhr','Asr','Maghrib','Isha'].includes(k)).map(([k,v])=>`<b>${k}:</b> ${v}`).join(' · ');}
catch(e){document.getElementById('r').textContent='Indisponible, réessayez.'}}</script>""",),
}
