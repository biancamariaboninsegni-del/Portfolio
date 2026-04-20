
import os, base64

desktop = os.path.expanduser('~/Desktop/')
src = desktop + 'index_backup.html'
dst = desktop + 'index.html'

with open(src, 'r', encoding='utf-8') as f:
    content = f.read()

with open(desktop + 'micro_AM.jpg', 'rb') as f:
    am_b64 = 'data:image/jpeg;base64,' + base64.b64encode(f.read()).decode()
with open(desktop + 'micro_PM.jpg', 'rb') as f:
    pm_b64 = 'data:image/jpeg;base64,' + base64.b64encode(f.read()).decode()

img_vars = 'window.IMG_AM = "' + am_b64 + '";' + chr(10) + 'window.IMG_PM = "' + pm_b64 + '";' + chr(10)
content = content.replace('</script>' + chr(10) + '</body>', img_vars + '</script>' + chr(10) + '</body>', 1)

toggle_css = chr(10) + '#toggle-ampm { position: fixed; top: 4.5rem; right: 1.5rem; z-index: 500; display: none; }' + chr(10) + '#toggle-ampm-btn { font-family: Courier Prime, monospace; font-size: 0.65rem; letter-spacing: 0.15em; color: rgba(245,234,214,0.6); cursor: pointer; border: 1px solid rgba(245,234,214,0.25); padding: 0.3rem 0.7rem; border-radius: 2px; background: transparent; text-transform: uppercase; }' + chr(10)
content = content.replace('</style>', toggle_css + '</style>', 1)

content = content.replace('<div id="header">', '<div id="toggle-ampm"><span id="toggle-ampm-btn" onclick="toggleAMPM()">\u2600 day</span></div>' + chr(10) + '<div id="header">')

toggle_fn = chr(10) + 'var _isDay = false;' + chr(10) + 'function toggleAMPM() {' + chr(10) + '  _isDay = !_isDay;' + chr(10) + '  const room = document.getElementById("room");' + chr(10) + '  const btn = document.getElementById("toggle-ampm-btn");' + chr(10) + '  if (_isDay) {' + chr(10) + '    room.style.backgroundImage = "url(" + window.IMG_AM + ")";' + chr(10) + '    btn.textContent = "\u263e night";' + chr(10) + '  } else {' + chr(10) + '    room.style.backgroundImage = "url(" + window.IMG_PM + ")";' + chr(10) + '    btn.textContent = "\u2600 day";' + chr(10) + '  }' + chr(10) + '}' + chr(10)
content = content.replace('function enterRoom()', toggle_fn + chr(10) + 'function enterRoom()', 1)

content = content.replace("setTimeout(() => document.getElementById('curtain').style.display = 'none', 1500);", "setTimeout(() => document.getElementById('curtain').style.display = 'none', 1500);" + chr(10) + "  setTimeout(() => { const t = document.getElementById('toggle-ampm'); if(t) t.style.display='block'; }, 1800);")

old = '<div id="sudoku-hint">complete to unlock the drawers</div>'
btn = '<div style="text-align:center;margin-top:0.8rem"><span onclick="surrenderSudoku()" style="font-family:monospace;font-size:0.65rem;color:rgba(245,234,214,0.4);cursor:pointer;text-decoration:underline">i surrender</span></div>'
content = content.replace(old, old + chr(10) + '          ' + btn)

with open(dst, 'w', encoding='utf-8') as f:
    f.write(content)

print('Fatto! File:', os.path.getsize(dst)//1024, 'KB')
print('IMG_AM count:', content.count('window.IMG_AM'))
print('surrenderSudoku:', 'surrenderSudoku' in content)
