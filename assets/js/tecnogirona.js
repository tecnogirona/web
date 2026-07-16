/* TecnoGirona — JS compartido (unificado)
   Dependencias: Bootstrap 5 bundle, AOS (cargados en cada página).
   Usar en TODAS las páginas para consistencia de comportamiento. */
(function () {
  'use strict';

  // Navbar: efecto al hacer scroll
  var navbar = document.querySelector('.navbar-custom');
  if (navbar) {
    var onScroll = function () {
      if (window.scrollY > 50) navbar.classList.add('scrolled');
      else navbar.classList.remove('scrolled');
    };
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }

  // AOS (animaciones de entrada)
  if (window.AOS) {
    AOS.init({ duration: 800, easing: 'ease-in-out', once: true, offset: 100 });
  }

  // Año dinámico en el footer
  var yearEl = document.querySelector('[data-year]');
  if (yearEl) yearEl.textContent = new Date().getFullYear();
})();
