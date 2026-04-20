// Gestione visibilità tab
let isVisible = true;
document.addEventListener('visibilitychange', () => {
  if (document.hidden) {
    isVisible = false;
    if(window._dustAnim) cancelAnimationFrame(window._dustAnim);
  } else {
    isVisible = true;
    const dustCanvas = document.getElementById('dust-canvas');
    if(dustCanvas && dustCanvas.style.display !== 'none' && typeof startDustAnim === 'function') {
      startDustAnim();
    }
  }
});

// Rispetta preferenze utente
if(window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
  window._dustDisabled = true;
}

// Dust particles animation v2
window._dustAnim = null;
function startDustAnim(){
  if(window._dustDisabled) return;
  const canvas = document.getElementById('dust-canvas');
  if(!canvas) return;
  canvas.style.display = 'block';
  canvas.style.position = 'absolute';
  canvas.style.inset = '0';
  canvas.style.width = '100%';
  canvas.style.height = '100%';
  canvas.style.pointerEvents = 'none';
  canvas.style.zIndex = '3';
  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight;
  const ctx = canvas.getContext('2d');
  const pts = Array.from({length:90}, ()=>({
    x: Math.random()*canvas.width,
    y: Math.random()*canvas.height,
    r: Math.random()*2.2+0.6,
    op: Math.random()*0.55+0.15,
    vx: (Math.random()-0.5)*0.25,
    vy: -(Math.random()*0.35+0.05),
    t: Math.random()*Math.PI*2
  }));
  function frame(){
    ctx.clearRect(0,0,canvas.width,canvas.height);
    pts.forEach(p=>{
      p.t += 0.012;
      p.x += p.vx + Math.sin(p.t)*0.2;
      p.y += p.vy;
      if(p.y < -5) { p.y = canvas.height+5; p.x = Math.random()*canvas.width; }
      if(p.x < -5) p.x = canvas.width+5;
      if(p.x > canvas.width+5) p.x = -5;
      ctx.beginPath();
      ctx.arc(p.x, p.y, p.r, 0, Math.PI*2);
      ctx.fillStyle = `rgba(255,225,140,${p.op})`;
      ctx.fill();
    });
    window._dustAnim = requestAnimationFrame(frame);
  }
  frame();
}

function stopDustAnim(){
  const canvas = document.getElementById('dust-canvas');
  if(canvas) canvas.style.display = 'none';
  if(window._dustAnim){ 
    cancelAnimationFrame(window._dustAnim); 
    window._dustAnim = null; 
  }
}
