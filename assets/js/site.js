/* Salt & Slate Cleaning Company — site behaviour (vanilla JS, no dependencies) */
(function () {
  'use strict';

  /* ------------------------------------------------------------------ nav */
  function initNav() {
    var burger = document.querySelector('.burger');
    var drawer = document.getElementById('mobile-drawer');
    if (!burger || !drawer) return;

    function open() {
      drawer.classList.add('is-open');
      burger.setAttribute('aria-expanded', 'true');
      document.documentElement.style.overflow = 'hidden';
      var first = drawer.querySelector('.drawer__close');
      if (first) first.focus();
    }
    function close() {
      drawer.classList.remove('is-open');
      burger.setAttribute('aria-expanded', 'false');
      document.documentElement.style.overflow = '';
    }
    burger.addEventListener('click', function () {
      drawer.classList.contains('is-open') ? close() : open();
    });
    drawer.addEventListener('click', function (e) {
      if (e.target === drawer || e.target.closest('.drawer__close') || e.target.closest('a')) close();
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && drawer.classList.contains('is-open')) close();
    });
  }

  /* ----------------------------------------------------- hero slideshow */
  function initHero() {
    var frame = document.querySelector('[data-hero-slides]');
    if (!frame) return;
    var slides = Array.prototype.slice.call(frame.querySelectorAll('.hero__slide'));
    var dots = Array.prototype.slice.call(document.querySelectorAll('.hero__dot'));
    if (slides.length < 2) return;
    var i = 0;
    var timer = null;
    var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    function show(n) {
      i = (n + slides.length) % slides.length;
      slides.forEach(function (s, idx) { s.classList.toggle('is-active', idx === i); });
      dots.forEach(function (d, idx) {
        d.classList.toggle('is-active', idx === i);
        d.setAttribute('aria-selected', idx === i ? 'true' : 'false');
      });
    }
    function play() { if (!reduce) timer = window.setInterval(function () { show(i + 1); }, 5200); }
    function stop() { if (timer) { window.clearInterval(timer); timer = null; } }

    dots.forEach(function (d, idx) {
      d.addEventListener('click', function () { stop(); show(idx); play(); });
    });
    frame.addEventListener('mouseenter', stop);
    frame.addEventListener('mouseleave', play);
    document.addEventListener('visibilitychange', function () {
      document.hidden ? stop() : play();
    });
    show(0);
    play();
  }

  /* ------------------------------------------------- before/after slider */
  function initBeforeAfter() {
    document.querySelectorAll('.ba').forEach(function (ba) {
      var range = ba.querySelector('.ba__range');
      var stage = ba.querySelector('.ba__stage');
      if (!range || !stage) return;
      function apply() { stage.style.setProperty('--pos', range.value + '%'); }
      range.addEventListener('input', apply);
      range.addEventListener('change', apply);
      apply();
    });
  }

  /* ------------------------------------------- review marquee duplication */
  function initMarquee() {
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    document.querySelectorAll('.rev-track').forEach(function (track) {
      if (track.dataset.cloned === '1') return;
      track.dataset.cloned = '1';
      Array.prototype.slice.call(track.children).forEach(function (child) {
        var clone = child.cloneNode(true);
        clone.setAttribute('aria-hidden', 'true');
        track.appendChild(clone);
      });
    });
  }

  /* ------------------------------------------------------------- forms */
  function initForms() {
    var params = new URLSearchParams(window.location.search);
    var submitted = params.get('submitted') === '1';

    document.querySelectorAll('form[data-leadr]').forEach(function (form) {
      var pageField = form.querySelector('input[name="_page"]');
      if (pageField) pageField.value = window.location.href;

      var alertBox = form.parentNode.querySelector('.alert');
      if (submitted && alertBox) {
        alertBox.hidden = false;
        form.reset();
        if (pageField) pageField.value = window.location.href;
      }

      form.addEventListener('submit', function (e) {
        if (!window.fetch || !form.reportValidity) return; /* plain POST fallback */
        if (!form.reportValidity()) { e.preventDefault(); return; }
        e.preventDefault();

        var btn = form.querySelector('button[type="submit"]');
        var label = btn ? btn.textContent : '';
        if (btn) { btn.disabled = true; btn.textContent = 'Sending…'; }

        var data = {};
        new FormData(form).forEach(function (value, key) { data[key] = value; });
        data._page = window.location.href;

        fetch(form.action, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json', 'Accept': 'application/json' },
          body: JSON.stringify(data)
        }).then(function (res) {
          return res.json().catch(function () { return { ok: res.ok }; });
        }).then(function (json) {
          if (json && json.ok) {
            form.reset();
            if (pageField) pageField.value = window.location.href;
            if (alertBox) {
              alertBox.hidden = false;
              alertBox.scrollIntoView({ behavior: 'smooth', block: 'center' });
            }
            if (btn) { btn.disabled = false; btn.textContent = label; }
          } else {
            throw new Error('submit failed');
          }
        }).catch(function () {
          /* fall back to a normal browser POST so the lead is never lost */
          if (btn) { btn.disabled = false; btn.textContent = label; }
          form.removeAttribute('data-leadr');
          HTMLFormElement.prototype.submit.call(form);
        });
      });
    });
  }

  /* --------------------------------------------------- reveal on scroll */
  function initReveal() {
    if (!('IntersectionObserver' in window)) return;
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    var targets = document.querySelectorAll('[data-reveal]');
    if (!targets.length) return;
    targets.forEach(function (el) {
      el.style.opacity = '0';
      el.style.transform = 'translateY(14px)';
      el.style.transition = 'opacity .6s ease, transform .6s ease';
    });
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        entry.target.style.opacity = '1';
        entry.target.style.transform = 'none';
        io.unobserve(entry.target);
      });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.06 });
    targets.forEach(function (el) { io.observe(el); });
  }

  function ready(fn) {
    if (document.readyState !== 'loading') fn();
    else document.addEventListener('DOMContentLoaded', fn);
  }

  ready(function () {
    initNav();
    initHero();
    initBeforeAfter();
    initMarquee();
    initForms();
    initReveal();
  });
})();
