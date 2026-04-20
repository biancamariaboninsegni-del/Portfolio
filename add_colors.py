with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add icon after baseball icon
old_icon = '''        <!-- Baseball -->
        <div class="folder-icon" onclick="openModal('modal-baseball')" style="cursor:pointer;">
          <img src="img/baseball_icon.png" style="width:52px;height:52px;object-fit:cover;border-radius:50%;opacity:0.85;"/>
          <span class="folder-label">Baseball</span>
        </div>'''

new_icon = '''        <!-- Baseball -->
        <div class="folder-icon" onclick="openModal('modal-baseball')" style="cursor:pointer;">
          <img src="img/baseball_icon.png" style="width:52px;height:52px;object-fit:cover;border-radius:50%;opacity:0.85;"/>
          <span class="folder-label">Baseball</span>
        </div>
        <!-- Colors -->
        <div class="folder-icon" onclick="openModal('modal-colors')" style="cursor:pointer;">
          <img src="img/colors/ikb.jpg" style="width:52px;height:52px;object-fit:cover;border-radius:50%;opacity:0.92;"/>
          <span class="folder-label">Colours</span>
        </div>'''

# 2. Colors modal HTML
colors_modal = '''
<div class="modal-backdrop" id="modal-colors">
  <div class="parchment-window" style="max-width:960px;background:#0d0b08;color:#e8e2d9;border:1px solid rgba(255,255,255,0.07);">
    <div class="parchment-header" style="border-bottom:1px solid rgba(255,255,255,0.08);">
      <span class="parchment-title" style="font-family:'Cormorant Garamond',serif;color:#e8e2d9;font-style:italic;">Atlante dei Colori</span>
      <span class="parchment-close" onclick="closeModal('modal-colors')" style="color:rgba(232,226,217,0.4);">close \u00d7</span>
    </div>
    <div class="parchment-body" style="padding:2rem 2.5rem 3rem;">

      <!-- SPECTRUM -->
      <div style="margin-bottom:2.5rem;">
        <div style="font-family:'Courier Prime',monospace;font-size:0.55rem;letter-spacing:0.25em;color:rgba(232,226,217,0.28);text-transform:uppercase;margin-bottom:0.8rem;">electromagnetic spectrum</div>
        <div style="position:relative;width:100%;">
          <div style="height:22px;width:100%;border-radius:2px;background:linear-gradient(to right,#1a0030,#3b0080,#0000ff,#00a8ff,#00ff88,#aaff00,#ffee00,#ff8800,#ff2200,#800000);opacity:0.85;"></div>
          <div style="display:flex;justify-content:space-between;margin-top:6px;font-family:'Courier Prime',monospace;font-size:0.52rem;color:rgba(232,226,217,0.28);letter-spacing:0.06em;">
            <span>gamma</span><span>X-ray</span><span>UV</span><span style="color:rgba(232,226,217,0.55);">380nm \u2192 700nm</span><span>IR</span><span>microwave</span><span>radio</span>
          </div>
          <!-- Visible light label -->
          <div style="position:absolute;top:0;left:28%;right:38%;height:22px;border:1px solid rgba(255,255,255,0.25);border-radius:2px;pointer-events:none;">
            <span style="position:absolute;top:-1.3rem;left:50%;transform:translateX(-50%);font-family:'Courier Prime',monospace;font-size:0.5rem;color:rgba(232,226,217,0.45);white-space:nowrap;letter-spacing:0.1em;">visible light</span>
          </div>
        </div>
        <div style="display:flex;justify-content:space-between;margin-top:1rem;font-family:'Courier Prime',monospace;font-size:0.5rem;color:rgba(232,226,217,0.25);letter-spacing:0.08em;">
          <span>380 nm</span><span>violet</span><span>blue</span><span>green</span><span>yellow</span><span>orange</span><span>red</span><span>700 nm</span>
        </div>
      </div>

      <!-- INTRO -->
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:2rem;margin-bottom:2.5rem;padding-bottom:2rem;border-bottom:1px solid rgba(255,255,255,0.06);">
        <div>
          <p style="font-family:'Cormorant Garamond',serif;font-size:1.05rem;font-weight:300;font-style:italic;color:rgba(232,226,217,0.7);line-height:1.7;margin-bottom:0.8rem;">
            Pontormo dipinse il <em>Compianto</em> nel 1528 con colori che nessuno aveva usato prima: un rosa acido che sembrava sintetico, un verde mela, un arancio bruciato. Non era naturalismo. Era psicologia.
          </p>
          <p style="font-family:'Courier Prime',monospace;font-size:0.6rem;color:rgba(232,226,217,0.28);letter-spacing:0.1em;">Pontormo \u00b7 Firenze \u00b7 1528</p>
        </div>
        <div>
          <p style="font-family:'Cormorant Garamond',serif;font-size:1.05rem;font-weight:300;font-style:italic;color:rgba(232,226,217,0.7);line-height:1.7;margin-bottom:0.8rem;">
            Sanz\u014d Wada pubblica il suo dizionario nel 1933: 348 combinazioni cromatiche con nomi tradizionali giapponesi. Non studia i colori da soli. Studia come si comportano insieme.
          </p>
          <p style="font-family:'Courier Prime',monospace;font-size:0.6rem;color:rgba(232,226,217,0.28);letter-spacing:0.1em;">Sanz\u014d Wada \u00b7 Tokyo \u00b7 1933</p>
        </div>
      </div>
      <div style="margin-bottom:2.5rem;padding-bottom:2rem;border-bottom:1px solid rgba(255,255,255,0.06);">
        <p style="font-family:'Cormorant Garamond',serif;font-size:1rem;font-weight:300;color:rgba(232,226,217,0.55);line-height:1.75;max-width:640px;">
          Kassia St Clair scrive che ogni colore ha una vita: nasce, cresce, muore, e a volte ha seconde e terze vite. Il bianco di piombo usato dai pittori rinascimentali li avvelenava lentamente attraverso la pelle. Il verde arsenico nel Settecento uccideva chi indossava abiti alla moda. I colori non sono mai stati innocenti.
        </p>
        <p style="font-family:'Courier Prime',monospace;font-size:0.6rem;color:rgba(232,226,217,0.28);letter-spacing:0.1em;margin-top:0.6rem;">Kassia St Clair \u00b7 The Secret Lives of Color \u00b7 2016</p>
      </div>

      <!-- COLOR FAMILIES -->
      <div style="margin-bottom:2rem;">
        <div style="font-family:'Courier Prime',monospace;font-size:0.55rem;letter-spacing:0.25em;color:rgba(232,226,217,0.28);text-transform:uppercase;margin-bottom:1.2rem;">ten families</div>
        <div style="display:flex;flex-wrap:wrap;gap:1rem;" id="color-families">
          <div class="col-family" data-family="whites" onclick="showColorFamily('whites')" style="cursor:pointer;display:flex;flex-direction:column;align-items:center;gap:0.4rem;">
            <div style="width:44px;height:44px;border-radius:50%;background:#f0ede8;border:1px solid rgba(255,255,255,0.15);transition:transform 0.2s;"></div>
            <span style="font-family:'Courier Prime',monospace;font-size:0.55rem;color:rgba(232,226,217,0.45);letter-spacing:0.1em;">whites</span>
          </div>
          <div class="col-family" data-family="yellows" onclick="showColorFamily('yellows')" style="cursor:pointer;display:flex;flex-direction:column;align-items:center;gap:0.4rem;">
            <div style="width:44px;height:44px;border-radius:50%;background:#e8c84a;border:1px solid rgba(255,255,255,0.1);transition:transform 0.2s;"></div>
            <span style="font-family:'Courier Prime',monospace;font-size:0.55rem;color:rgba(232,226,217,0.45);letter-spacing:0.1em;">yellows</span>
          </div>
          <div class="col-family" data-family="oranges" onclick="showColorFamily('oranges')" style="cursor:pointer;display:flex;flex-direction:column;align-items:center;gap:0.4rem;">
            <div style="width:44px;height:44px;border-radius:50%;background:#d4651a;border:1px solid rgba(255,255,255,0.1);transition:transform 0.2s;"></div>
            <span style="font-family:'Courier Prime',monospace;font-size:0.55rem;color:rgba(232,226,217,0.45);letter-spacing:0.1em;">oranges</span>
          </div>
          <div class="col-family" data-family="pinks" onclick="showColorFamily('pinks')" style="cursor:pointer;display:flex;flex-direction:column;align-items:center;gap:0.4rem;">
            <div style="width:44px;height:44px;border-radius:50%;background:#e8829a;border:1px solid rgba(255,255,255,0.1);transition:transform 0.2s;"></div>
            <span style="font-family:'Courier Prime',monospace;font-size:0.55rem;color:rgba(232,226,217,0.45);letter-spacing:0.1em;">pinks</span>
          </div>
          <div class="col-family" data-family="reds" onclick="showColorFamily('reds')" style="cursor:pointer;display:flex;flex-direction:column;align-items:center;gap:0.4rem;">
            <div style="width:44px;height:44px;border-radius:50%;background:#b8231e;border:1px solid rgba(255,255,255,0.1);transition:transform 0.2s;"></div>
            <span style="font-family:'Courier Prime',monospace;font-size:0.55rem;color:rgba(232,226,217,0.45);letter-spacing:0.1em;">reds</span>
          </div>
          <div class="col-family" data-family="purples" onclick="showColorFamily('purples')" style="cursor:pointer;display:flex;flex-direction:column;align-items:center;gap:0.4rem;">
            <div style="width:44px;height:44px;border-radius:50%;background:#6b3fa0;border:1px solid rgba(255,255,255,0.1);transition:transform 0.2s;"></div>
            <span style="font-family:'Courier Prime',monospace;font-size:0.55rem;color:rgba(232,226,217,0.45);letter-spacing:0.1em;">purples</span>
          </div>
          <div class="col-family" data-family="blues" onclick="showColorFamily('blues')" style="cursor:pointer;display:flex;flex-direction:column;align-items:center;gap:0.4rem;">
            <div style="width:44px;height:44px;border-radius:50%;background:#1c2fd4;border:1px solid rgba(255,255,255,0.1);transition:transform 0.2s;"></div>
            <span style="font-family:'Courier Prime',monospace;font-size:0.55rem;color:rgba(232,226,217,0.45);letter-spacing:0.1em;">blues</span>
          </div>
          <div class="col-family" data-family="greens" onclick="showColorFamily('greens')" style="cursor:pointer;display:flex;flex-direction:column;align-items:center;gap:0.4rem;">
            <div style="width:44px;height:44px;border-radius:50%;background:#2a7a4a;border:1px solid rgba(255,255,255,0.1);transition:transform 0.2s;"></div>
            <span style="font-family:'Courier Prime',monospace;font-size:0.55rem;color:rgba(232,226,217,0.45);letter-spacing:0.1em;">greens</span>
          </div>
          <div class="col-family" data-family="browns" onclick="showColorFamily('browns')" style="cursor:pointer;display:flex;flex-direction:column;align-items:center;gap:0.4rem;">
            <div style="width:44px;height:44px;border-radius:50%;background:#7a4a28;border:1px solid rgba(255,255,255,0.1);transition:transform 0.2s;"></div>
            <span style="font-family:'Courier Prime',monospace;font-size:0.55rem;color:rgba(232,226,217,0.45);letter-spacing:0.1em;">browns</span>
          </div>
          <div class="col-family" data-family="blacks" onclick="showColorFamily('blacks')" style="cursor:pointer;display:flex;flex-direction:column;align-items:center;gap:0.4rem;">
            <div style="width:44px;height:44px;border-radius:50%;background:#1a1a1a;border:1px solid rgba(255,255,255,0.2);transition:transform 0.2s;"></div>
            <span style="font-family:'Courier Prime',monospace;font-size:0.55rem;color:rgba(232,226,217,0.45);letter-spacing:0.1em;">blacks</span>
          </div>
        </div>
      </div>

      <!-- MOODBOARD AREA -->
      <div id="color-moodboard" style="display:none;">
        <div style="display:flex;align-items:baseline;gap:1rem;margin-bottom:1.5rem;padding-top:1.5rem;border-top:1px solid rgba(255,255,255,0.06);">
          <span id="moodboard-title" style="font-family:'Cormorant Garamond',serif;font-size:1.5rem;font-weight:300;font-style:italic;color:#e8e2d9;"></span>
          <span id="moodboard-subtitle" style="font-family:'Courier Prime',monospace;font-size:0.55rem;color:rgba(232,226,217,0.3);letter-spacing:0.15em;text-transform:uppercase;"></span>
        </div>
        <p id="moodboard-story" style="font-family:'Cormorant Garamond',serif;font-size:0.95rem;font-weight:300;color:rgba(232,226,217,0.6);line-height:1.75;max-width:640px;margin-bottom:2rem;"></p>
        <div id="moodboard-grid" style="columns:3;column-gap:10px;"></div>
        <p style="font-family:'Courier Prime',monospace;font-size:0.52rem;color:rgba(232,226,217,0.18);letter-spacing:0.1em;margin-top:1.5rem;font-style:italic;" id="moodboard-coming-soon"></p>
      </div>

    </div>
  </div>
</div>

<script>
var colorData = {
  whites: {
    title: 'Isabella',
    subtitle: 'the whites',
    story: 'Nel 1601, Isabella d\'Austria giur\u00f2 di non cambiare la camicia fino alla resa di Ostenda. La citt\u00e0 resist\u00e9 tre anni. Il colore che ne nacque \u2014 un bianco sporco, giallastro, consumato \u2014 porta ancora il suo nome. I pittori rinascimentali usavano la biacca, bianco di piombo, sapendo che li avrebbe uccisi attraverso la pelle. Lo usavano lo stesso.',
    images: ['white1.jpeg','white2.jpeg','white3.jpeg','white4.jpeg','white5.jpeg','white6.jpeg','white7.jpg','white8.jpg','white9.jpg'],
    comingSoon: ''
  },
  blues: {
    title: 'International Klein Blue',
    subtitle: 'the blues',
    story: 'Yves Klein brevett\u00f2 il suo blu nel 1960: IKB 191. Non era una sfumatura ma un atto. Il lapislazzuli afgano nel Medioevo costava pi\u00f9 dell\'oro e trasform\u00f3 i cieli medievali in oltremare rinascimentale. Il blu non esiste in natura come pigmento \u2014 ogni blu che vediamo \u00e8 stato conquistato.',
    images: ['ikb.jpg'],
    comingSoon: 'More images coming soon.'
  },
  yellows: { title: 'Orpiment', subtitle: 'the yellows', story: '', images: [], comingSoon: 'Coming soon.' },
  oranges: { title: 'Minium', subtitle: 'the oranges', story: '', images: [], comingSoon: 'Coming soon.' },
  pinks: { title: 'Rose Madder', subtitle: 'the pinks', story: '', images: [], comingSoon: 'Coming soon.' },
  reds: { title: 'Vermillion', subtitle: 'the reds', story: '', images: [], comingSoon: 'Coming soon.' },
  purples: { title: 'Tyrian Purple', subtitle: 'the purples', story: '', images: [], comingSoon: 'Coming soon.' },
  greens: { title: 'Scheele\'s Green', subtitle: 'the greens', story: '', images: [], comingSoon: 'Coming soon.' },
  browns: { title: 'Mummy Brown', subtitle: 'the browns', story: '', images: [], comingSoon: 'Coming soon.' },
  blacks: { title: 'Vantablack', subtitle: 'the blacks', story: '', images: [], comingSoon: 'Coming soon.' }
};

function showColorFamily(family) {
  var data = colorData[family];
  if (!data) return;

  document.querySelectorAll('.col-family div').forEach(function(el) {
    el.style.transform = 'scale(1)';
    el.style.boxShadow = 'none';
  });
  var active = document.querySelector('[data-family="' + family + '"] div');
  if (active) { active.style.transform = 'scale(1.15)'; active.style.boxShadow = '0 0 12px rgba(255,255,255,0.2)'; }

  document.getElementById('moodboard-title').textContent = data.title;
  document.getElementById('moodboard-subtitle').textContent = data.subtitle;
  document.getElementById('moodboard-story').textContent = data.story;
  document.getElementById('moodboard-coming-soon').textContent = data.comingSoon;

  var grid = document.getElementById('moodboard-grid');
  grid.innerHTML = '';
  if (data.images.length > 0) {
    data.images.forEach(function(img, i) {
      var el = document.createElement('div');
      el.style.cssText = 'break-inside:avoid;margin-bottom:10px;';
      el.innerHTML = '<img src="img/colors/' + img + '" style="width:100%;display:block;border-radius:2px;opacity:0;transition:opacity 0.5s ease ' + (i * 0.08) + 's;" onload="this.style.opacity=\'1\'" />';
      grid.appendChild(el);
    });
  }

  var board = document.getElementById('color-moodboard');
  board.style.display = 'block';
  board.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
}
</script>
'''

# Insert icon
if old_icon in content:
    content = content.replace(old_icon, new_icon, 1)
    print('OK: icona aggiunta.')
else:
    print('ERRORE: icona baseball non trovata.')

# Insert modal before baseball modal
old_baseball_modal = '<div class="modal-backdrop" id="modal-baseball">'
if old_baseball_modal in content:
    content = content.replace(old_baseball_modal, colors_modal + '\n' + old_baseball_modal, 1)
    print('OK: modal colori aggiunto.')
else:
    print('ERRORE: modal baseball non trovato.')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
