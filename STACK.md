# TecnoGirona — Stack Técnico y Estándar de Desarrollo

## Stack unificado (OBLIGATORIO para toda página nueva)
- **HTML5** estático (sin framework de build; se sirve tal cual).
- **Bootstrap 5.3** vía CDN (`bootstrap@5.3.2`).
- **Bootstrap Icons** vía CDN (`bootstrap-icons@1.11.1`).
- **Google Fonts**: Inter.
- **AOS** (animaciones de scroll) vía CDN (`aos@2.3.1`).
- **CSS compartido**: `assets/css/tecnogirona.css` (design system: navbar, hero, servicios, contacto, footer, whatsapp).
- **JS compartido**: `assets/js/tecnogirona.js` (navbar scroll + AOS init + año footer).

## NO usar
- ❌ Tailwind CDN inline (hay 10 páginas legadas con esto; migrar progresivamente a `tecnogirona.css`).
- ❌ CSS `<style>` inline duplicado por página (extraer a `tecnogirona.css`).
- ❌ Redirecciones `*.html` con underscore (`_`) — ya son stubs SEO que apuntan a las versiones kebab-case.

## Estructura de carpetas
```
/
├── index.html                      (home)
├── *.html                          (páginas de servicio, kebab-case)
├── assets/
│   ├── css/tecnogirona.css         (design system unificado)
│   └── js/tecnogirona.js           (comportamiento unificado)
├── images/                         (activos)
├── CNAME                           (tecnogirona.es)
├── sitemap.xml
└── robots.txt
```

## Convenciones SEO
- URLs en `kebab-case` (guiones medios), no `_` (guiones bajos).
- Cada página: `<link rel="canonical">` + `og:url` apuntando a `https://tecnogirona.es/<archivo>.html`.
- Dominio oficial: **tecnogirona.es** (nunca tecnogirona.com).
- Páginas de utilidad (formularios, 404) llevan `robots: noindex,follow`.

## Despliegue
⚠️ El DNS de `tecnogirona.es` apunta a un servidor nginx externo (213.158.94.183), NO a GitHub Pages.
Para ver los cambios en producción hay que subirlos a ese servidor (SFTP/SSH) o re-apuntar el DNS a GitHub Pages.
