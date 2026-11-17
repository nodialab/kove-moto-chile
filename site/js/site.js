(() => {
  const $ = (s, r = document) => r.querySelector(s), $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const nav = $('#nav');
  const onScroll = () => nav.classList.toggle('solid', scrollY > 40);
  onScroll(); addEventListener('scroll', onScroll, { passive: true });
  const b = $('#burger'), l = $('#links');
  b?.addEventListener('click', () => { const o = l.classList.toggle('open'); b.setAttribute('aria-expanded', o); document.body.style.overflow = o ? 'hidden' : ''; });
  $$('#links a').forEach(a => a.addEventListener('click', () => { l.classList.remove('open'); b.setAttribute('aria-expanded', false); document.body.style.overflow = ''; }));

  // reveal
  const io = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } }), { threshold: .12 });
  $$('.reveal').forEach(el => io.observe(el));

  // counters
  const co = new IntersectionObserver(es => es.forEach(e => {
    if (!e.isIntersecting) return; co.unobserve(e.target);
    const el = e.target, end = +el.dataset.count, pre = el.dataset.prefix || '', n = el.dataset.fmt === 'n', t0 = performance.now();
    const f = t => { const p = Math.min(1, (t - t0) / 1600), v = Math.round(end * (1 - Math.pow(1 - p, 3))); el.textContent = pre + (n ? v : v.toLocaleString('es-CL')); if (p < 1) requestAnimationFrame(f); };
    requestAnimationFrame(f);
  }), { threshold: .6 });
  $$('[data-count]').forEach(el => co.observe(el));

  // hero slider
  const sl = $$('#slides .slide'), dots = $$('#dots button');
  if (sl.length) {
    let i = 0, t; const go = n => { sl[i].classList.remove('on'); dots[i].classList.remove('on'); i = (n + sl.length) % sl.length; sl[i].classList.add('on'); dots[i].classList.add('on'); };
    const run = () => { clearInterval(t); t = setInterval(() => go(i + 1), 6500); };
    dots.forEach((d, k) => d.addEventListener('click', () => { go(k); run(); })); run();
  }

  // rails con arrastre
  $$('[data-rail]').forEach(r => {
    let down = false, sx = 0, sl0 = 0, moved = false;
    r.addEventListener('pointerdown', e => { if (e.pointerType !== 'mouse') return; down = true; moved = false; sx = e.clientX; sl0 = r.scrollLeft; });
    addEventListener('pointerup', () => { down = false; r.classList.remove('drag'); });
    r.addEventListener('pointermove', e => { if (!down) return; const d = e.clientX - sx; if (Math.abs(d) > 5) { moved = true; r.classList.add('drag'); } r.scrollLeft = sl0 - d; });
    r.addEventListener('click', e => { if (moved) { e.preventDefault(); moved = false; } }, true);
  });

  // carrusel
  $$('[data-carousel]').forEach(c => {
    const tr = $('.car-track', c), sl = $$('.car-slide', c), dt = $$('.car-dots button', c);
    const cur = () => { const m = tr.scrollLeft + tr.clientWidth / 2; let k = 0, best = 1e9; sl.forEach((s, j) => { const d = Math.abs(s.offsetLeft + s.offsetWidth / 2 - m); if (d < best) { best = d; k = j; } }); return k; };
    const to = k => { k = Math.max(0, Math.min(sl.length - 1, k)); tr.scrollTo({ left: sl[k].offsetLeft - (tr.clientWidth - sl[k].offsetWidth) / 2, behavior: 'smooth' }); };
    const mark = () => { const k = cur(); dt.forEach((d, j) => d.classList.toggle('on', j === k)); };
    $('.car-prev', c).onclick = () => to(cur() - 1); $('.car-next', c).onclick = () => to(cur() + 1);
    dt.forEach((d, j) => d.onclick = () => to(j)); tr.addEventListener('scroll', () => requestAnimationFrame(mark), { passive: true }); mark();
    let down = false, sx = 0, s0 = 0, mv = false;
    tr.addEventListener('pointerdown', e => { if (e.pointerType !== 'mouse') return; down = true; mv = false; sx = e.clientX; s0 = tr.scrollLeft; tr.style.scrollSnapType = 'none'; });
    addEventListener('pointerup', () => { if (!down) return; down = false; tr.style.scrollSnapType = ''; if (mv) to(cur()); });
    tr.addEventListener('pointermove', e => { if (!down) return; const d = e.clientX - sx; if (Math.abs(d) > 5) mv = true; tr.scrollLeft = s0 - d; });
    tr.addEventListener('click', e => { if (mv) { e.preventDefault(); e.stopPropagation(); mv = false; } }, true);
  });

  // selector de color + giro 360 (arrastrar)
  const cut = $('#cut'), hint = $('#spinhint'); let frames = [], fi = 0;
  const setFrames = s => { frames = s ? s.split('|').filter(Boolean) : []; fi = 0; frames.forEach(u => { new Image().src = u; }); if (hint) hint.hidden = !frames.length; if (cut) cut.style.cursor = frames.length ? 'grab' : ''; };
  if (cut) setFrames(cut.dataset.frames);
  $$('[data-swap]').forEach(s => s.addEventListener('click', () => {
    if (!cut || s.classList.contains('on')) return;
    $$('[data-swap]').forEach(x => x.classList.toggle('on', x === s)); const nm = $('#swname'); if (nm) nm.textContent = s.title;
    cut.classList.add('swap'); const im = new Image(); im.onload = () => { cut.src = s.dataset.swap; setFrames(s.dataset.frames); requestAnimationFrame(() => cut.classList.remove('swap')); }; im.src = s.dataset.swap;
  }));
  if (cut) {
    let down = false, sx = 0, f0 = 0;
    const stage = cut.parentElement, show = k => { fi = ((k % frames.length) + frames.length) % frames.length; cut.src = frames[fi]; };
    stage.addEventListener('pointerdown', e => { if (!frames.length) return; down = true; sx = e.clientX; f0 = fi; stage.setPointerCapture(e.pointerId); cut.style.cursor = 'grabbing'; if (hint) hint.hidden = true; });
    stage.addEventListener('pointermove', e => { if (down) show(f0 - Math.round((e.clientX - sx) / (stage.clientWidth / frames.length / 1.4))); });
    const up = () => { down = false; if (frames.length) cut.style.cursor = 'grab'; };
    stage.addEventListener('pointerup', up); stage.addEventListener('pointercancel', up);
    addEventListener('keydown', e => { if (frames.length && /^Arrow(Left|Right)$/.test(e.key) && lb.hidden) show(fi + (e.key === 'ArrowRight' ? 1 : -1)); });
  }

  // filtros
  $$('[data-filter-group]').forEach(g => {
    const target = $('[data-filter-target]'), btns = $$('button', g);
    const apply = f => { btns.forEach(x => x.classList.toggle('on', x.dataset.f === f)); $$('[data-cat]', target).forEach(el => el.hidden = !(f === 'all' || f === 'Todas' || el.dataset.cat === f)); };
    btns.forEach(x => x.addEventListener('click', () => apply(x.dataset.f)));
    const q = new URLSearchParams(location.search).get('cat'); if (q && btns.some(x => x.dataset.f === q)) apply(q);
  });

  // tabs de galería
  $$('[data-tabs]').forEach(g => $$('button', g).forEach(b => b.addEventListener('click', () => {
    $$('button', g).forEach(x => x.classList.toggle('on', x === b));
    $$('[data-panel]', g.closest('section')).forEach(p => p.hidden = p.dataset.panel !== b.dataset.t);
  })));

  // lightbox
  const lb = $('#lb'), li = $('img', lb), lc = $('figcaption', lb); let group = [], gi = 0;
  const show = k => { gi = (k + group.length) % group.length; li.src = group[gi].dataset.full; lc.textContent = group[gi].dataset.cap || ''; };
  const open = (g, k) => { group = g; lb.hidden = false; document.body.style.overflow = 'hidden'; show(k); };
  const close = () => { lb.hidden = true; document.body.style.overflow = ''; };
  $$('[data-lightbox]').forEach(c => c.addEventListener('click', e => { const a = e.target.closest('a[data-full]'); if (!a) return; e.preventDefault(); const g = $$('a[data-full]', c).filter(x => !x.hidden); open(g, g.indexOf(a)); }));
  $('.lb-x', lb).onclick = close; $('.lb-p', lb).onclick = () => show(gi - 1); $('.lb-n', lb).onclick = () => show(gi + 1);
  lb.addEventListener('click', e => { if (e.target === lb) close(); });
  addEventListener('keydown', e => { if (lb.hidden) return; if (e.key === 'Escape') close(); if (e.key === 'ArrowLeft') show(gi - 1); if (e.key === 'ArrowRight') show(gi + 1); });

  // ?m=Modelo preselecciona el select
  const pm = new URLSearchParams(location.search).get('m'); if (pm) $$('.quote select[name=m]').forEach(x => { x.value = pm; });

  // botones "Cotizar X": fijan el modelo en el select cada vez
  $$('[data-quote]').forEach(b => b.addEventListener('click', () => $$('.quote select[name=m]').forEach(x => { x.value = b.dataset.quote; })));

  // cotizador -> WhatsApp
  $$('.quote').forEach(f => f.addEventListener('submit', e => {
    e.preventDefault(); const d = new FormData(f);
    const msg = `Hola, soy ${d.get('n')}${d.get('c') ? ' (' + d.get('c') + ')' : ''}. Quiero cotizar la Kove ${d.get('m')} en ${d.get('ci')}.`;
    open_ = window.open(`https://wa.me/${f.dataset.wa}?text=${encodeURIComponent(msg)}`, '_blank', 'noopener');
  }));
})();
