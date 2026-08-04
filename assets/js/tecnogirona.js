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

  // Vercel Speed Insights - Inicialización
  // Carga el script de Speed Insights desde el CDN de jsDelivr
  (function() {
    // Solo cargar en producción (cuando el dominio es tecnogirona.es)
    var isProd = window.location.hostname === 'tecnogirona.es' || 
                 window.location.hostname === 'www.tecnogirona.es';
    
    if (!isProd) {
      console.log('[Speed Insights] Deshabilitado en desarrollo');
      return;
    }

    // Crear y cargar el módulo de Speed Insights
    var script = document.createElement('script');
    script.type = 'module';
    script.async = true;
    script.textContent = 
      'import { injectSpeedInsights } from "https://cdn.jsdelivr.net/npm/@vercel/speed-insights@1/+esm";' +
      'injectSpeedInsights();';
    
    script.onerror = function() {
      console.error('[Speed Insights] Error al cargar el script');
    };
    
    document.head.appendChild(script);
  })();
})();
