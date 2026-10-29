(function () {
  'use strict';
  var root = document.documentElement;
  var header = document.querySelector('.site-header');

  // Home: transparent header turns solid once the page scrolls
  if (document.body.classList.contains('home') && header) {
    var onScroll = function () { header.classList.toggle('is-scrolled', window.scrollY > 40); };
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }

  // Mobile menu: no scrolling while open, hamburger becomes an X
  var btn = document.querySelector('.nav-toggle');
  var nav = document.querySelector('.main-nav');
  if (btn && nav) {
    var setOpen = function (open) {
      if (open) root.style.setProperty('--menu-top', header.getBoundingClientRect().bottom + 'px');
      nav.classList.toggle('open', open);
      root.classList.toggle('menu-open', open);
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
      btn.setAttribute('aria-label', open ? 'Close menu' : 'Menu');
    };
    btn.addEventListener('click', function () { setOpen(!nav.classList.contains('open')); });
    nav.addEventListener('click', function (e) { if (e.target.closest('a')) setOpen(false); });
    nav.addEventListener('touchmove', function (e) { e.preventDefault(); }, { passive: false });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') setOpen(false); });
    window.addEventListener('resize', function () { if (window.innerWidth > 960) setOpen(false); });
  }

  // Exclusive accordions (only one open at a time)
  var accs = document.querySelectorAll('details.acc');
  accs.forEach(function (d) {
    d.addEventListener('toggle', function () {
      if (d.open) accs.forEach(function (o) { if (o !== d) o.open = false; });
    });
  });

  // Carousels
  document.querySelectorAll('[data-carousel]').forEach(function (c) {
    var viewport = c.querySelector('.carousel-viewport');
    var track = c.querySelector('.carousel-track');
    var slides = Array.prototype.slice.call(track.children);
    var dots = c.querySelector('.carousel-dots');
    var i = 0;
    slides.forEach(function (_, n) {
      var b = document.createElement('button');
      b.type = 'button';
      b.setAttribute('aria-label', 'Show testimonial ' + (n + 1));
      b.addEventListener('click', function () { go(n); });
      dots.appendChild(b);
    });
    var fit = function () { viewport.style.height = slides[i].offsetHeight + 'px'; };
    var go = function (n) {
      i = (n + slides.length) % slides.length;
      track.style.transform = 'translateX(' + (-100 * i) + '%)';
      slides.forEach(function (s, k) {
        var on = k === i;
        s.setAttribute('aria-hidden', on ? 'false' : 'true');
        if (on) s.removeAttribute('inert'); else s.setAttribute('inert', '');
      });
      Array.prototype.forEach.call(dots.children, function (d, k) { d.setAttribute('aria-current', k === i ? 'true' : 'false'); });
      fit();
    };
    c.querySelector('.prev').addEventListener('click', function () { go(i - 1); });
    c.querySelector('.next').addEventListener('click', function () { go(i + 1); });
    c.querySelectorAll('details').forEach(function (d) { d.addEventListener('toggle', fit); });
    window.addEventListener('resize', fit);
    window.addEventListener('load', fit);
    if (window.ResizeObserver) { var ro = new ResizeObserver(fit); slides.forEach(function (s) { ro.observe(s); }); }
    if (document.fonts && document.fonts.ready) document.fonts.ready.then(fit);
    go(0);
  });

  // Video popup
  var modal = document.querySelector('.modal');
  if (modal) {
    var frame = modal.querySelector('.modal-inner');
    var close = function () { modal.classList.remove('open'); frame.querySelector('iframe') && frame.removeChild(frame.querySelector('iframe')); };
    document.querySelectorAll('[data-video-popup]').forEach(function (b) {
      b.addEventListener('click', function () {
        var f = document.createElement('iframe');
        f.src = 'https://www.youtube-nocookie.com/embed/' + b.getAttribute('data-video-popup') + '?autoplay=1&rel=0';
        f.allow = 'autoplay; encrypted-media; picture-in-picture; fullscreen';
        f.allowFullscreen = true;
        f.title = 'Vaughn Company video';
        frame.appendChild(f);
        modal.classList.add('open');
      });
    });
    modal.addEventListener('click', function (e) { if (e.target === modal || e.target.closest('.modal-close')) close(); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') close(); });
  }

  // Click-to-load YouTube embeds
  document.querySelectorAll('.video-embed[data-video]').forEach(function (v) {
    v.addEventListener('click', function () {
      if (v.querySelector('iframe')) return;
      var f = document.createElement('iframe');
      f.src = 'https://www.youtube-nocookie.com/embed/' + v.getAttribute('data-video') + '?autoplay=1&rel=0';
      f.allow = 'autoplay; encrypted-media; picture-in-picture; fullscreen';
      f.allowFullscreen = true;
      f.title = v.getAttribute('data-title') || 'Video';
      v.innerHTML = '';
      v.appendChild(f);
    });
  });

  var y = document.querySelector('[data-year]');
  if (y) y.textContent = new Date().getFullYear();
})();
