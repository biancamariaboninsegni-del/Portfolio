with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

import re

# === FIX 1: PONTORMO TEXT ===
old_pontormo_text = 'Pontormo painted the <em>Deposition</em> in 1528 with colours no one had used before: an acid pink that looked almost synthetic, an apple green, a burnt orange. It was not naturalism. It was psychology.'
new_pontormo_text = 'Pontormo painted the <em>Deposition</em> in 1528 with colours no one had used before: an acid pink, an apple green, an orange that had no name. John Shearman, writing at Harvard, described the work as \u201can extraordinarily imaginative renewal\u201d \u2014 but what he meant, precisely, was this: Pontormo understood that colour is not description. It is pressure. The figures float in a space with no ground, no cross, no blood. Only colour, doing the work that gravity cannot.'

old_pontormo_cite = 'Pontormo \u00b7 Florence \u00b7 1528'
new_pontormo_cite = 'Pontormo \u00b7 Santa Felicita, Florence \u00b7 1528 \u00b7 cf. Shearman, <em>Mannerism</em>, Penguin, 1967'

if old_pontormo_text in content:
    content = content.replace(old_pontormo_text, new_pontormo_text, 1)
    print('OK: testo Pontormo aggiornato.')
else:
    print('SKIP: testo Pontormo non trovato (forse gia aggiornato).')

if old_pontormo_cite in content:
    content = content.replace(old_pontormo_cite, new_pontormo_cite, 1)
    print('OK: citazione Pontormo aggiornata.')
else:
    print('SKIP: citazione Pontormo non trovata.')

# === FIX 2: WADA — add images + Albers reference ===
old_wada = 'Sanz\u014d Wada published his dictionary in 1933: 348 colour combinations with traditional Japanese names. He did not study colours alone. He studied how they behave together.'
new_wada = 'Sanz\u014d Wada published his dictionary in 1933: 348 colour combinations built from 159 carefully selected colours, each assembled by hand. He did not study colours alone. He studied how they behave together. Thirty years later, Josef Albers would arrive at the same conclusion at Yale: <em>\u201cIn visual perception, a colour is almost never seen as it really is.\u201d</em> Wada had already known this. He just never wrote it down as theory.'

old_wada_cite = 'Sanz\u014d Wada \u00b7 Tokyo \u00b7 1933'
new_wada_cite = 'Sanz\u014d Wada \u00b7 Tokyo \u00b7 1933 \u00b7 cf. Albers, <em>Interaction of Color</em>, Yale Press, 1963'

if old_wada in content:
    content = content.replace(old_wada, new_wada, 1)
    print('OK: testo Wada aggiornato.')
else:
    print('SKIP: testo Wada non trovato (forse gia aggiornato).')

if old_wada_cite in content:
    content = content.replace(old_wada_cite, new_wada_cite, 1)
    print('OK: citazione Wada aggiornata.')
else:
    print('SKIP: citazione Wada non trovata.')

# === FIX 3: add Wada images if not already there ===
if 'img/colors/wada.jpg' not in content:
    # Find the Wada div and prepend images
    old_wada_div = '          <p style="font-family:\'Plus Jakarta Sans\',sans-serif;font-size:0.95rem;font-weight:400;color:#1a1a1a;line-height:1.7;margin-bottom:0.8rem;">\n            Sanz\u014d Wada'
    new_wada_div = '          <img src="img/colors/wada.jpg" style="width:100%;border-radius:2px;margin-bottom:0.5rem;opacity:0.92;" alt="Sanzo Wada, Dictionary of Color Combinations, 1933" />\n          <img src="img/colors/wada2.jpg" style="width:100%;border-radius:2px;margin-bottom:0.8rem;opacity:0.92;" alt="Sanzo Wada, colour combinations detail" />\n          <p style="font-family:\'Plus Jakarta Sans\',sans-serif;font-size:0.88rem;font-weight:400;color:#1a1a1a;line-height:1.7;margin-bottom:0.8rem;">\n            Sanz\u014d Wada'
    if old_wada_div in content:
        content = content.replace(old_wada_div, new_wada_div, 1)
        print('OK: immagini Wada aggiunte.')
    else:
        print('SKIP: div Wada non trovato per immagini.')
else:
    print('SKIP: immagini Wada gia presenti.')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('\nDone.')
