/* Vercel Speed Insights - Script independiente
   Carga automáticamente Speed Insights cuando se incluye en una página.
   Uso: <script src="assets/js/speed-insights.js"></script> */
(function() {
  'use strict';
  
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
