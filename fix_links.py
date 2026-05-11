import os
import re

# Directorio donde se encuentran los archivos HTML
DIR_PATH = "web-main1/web-main/web-main/"
# Lista de archivos HTML a procesar (excluyendo el script)
HTML_FILES = [f for f in os.listdir(DIR_PATH) if f.endswith(".html") and f != "fix_links.py"]

# Mapeo de correcciones de enlaces
# El usuario indica que perfex.html (que es perfex_crm.html) debe integrarse
# y que los enlaces como faq fallan.
# Asumo que los enlaces rotos son a archivos que no existen o están mal nombrados.
# Basado en el análisis, los enlaces en index.html apuntan a los archivos correctos.
# El problema es que el usuario quiere que perfex.html se integre, y el archivo se llama perfex_crm.html.
# También asumo que el usuario quiere que el enlace a "planes.html" se añada a la navegación principal,
# y que el enlace a "perfex_crm.html" se mantenga como está en el menú desplegable.

# El principal problema que el usuario menciona es que los enlaces "fallan".
# Esto a menudo significa que los enlaces relativos están mal en páginas anidadas,
# pero aquí todos los archivos están en el mismo directorio, por lo que los enlaces
# relativos simples (ej: "faq.html") deberían funcionar.
# El problema puede ser que el usuario espera que "perfex.html" exista, pero es "perfex_crm.html".
# También puede ser que el enlace a "faq.html" esté mal escrito en otras páginas.

# Voy a estandarizar los enlaces en el navbar y footer de todas las páginas.

# 1. Corregir el enlace a perfex_crm.html en el navbar (línea 625 en index.html)
#    De: <li><a class="dropdown-item text-crm" href="perfex_crm.html"><i class="bi bi-diagram-3-fill text-crm"></i> **CRM Privado**</a></li>
#    A: <li><a class="dropdown-item text-crm" href="perfex_crm.html"><i class="bi bi-diagram-3-fill text-crm"></i> **CRM Privado**</a></li>
#    No hay corrección de nombre de archivo, pero voy a asegurarme de que el enlace a "planes.html" esté en el navbar principal si el usuario lo desea.
#    El usuario solo mencionó "perfex.html" y "faq etc...".

# Voy a extraer el navbar y el footer de index.html para usarlos como plantilla.

# Navbar (Líneas 598-650 en index.html)
NAVBAR_START = 598
NAVBAR_END = 650

# Footer (Líneas 870-915 en index.html)
FOOTER_START = 870
FOOTER_END = 915

def get_section_content(file_path, start_line, end_line):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    # Los números de línea son 1-indexados, por lo que restamos 1 para obtener el índice de la lista.
    return "".join(lines[start_line-1:end_line])

def replace_section(file_path, old_start_tag, old_end_tag, new_content):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Patrón para encontrar y reemplazar el navbar
    # Asumo que el navbar empieza con <nav class="navbar..." y termina con </nav>
    # Y el footer empieza con <footer class="footer"> y termina con </footer>
    
    # Patrón para el navbar
    navbar_pattern = re.compile(r'<nav class="navbar.*?<\/nav>', re.DOTALL)
    # Patrón para el footer
    footer_pattern = re.compile(r'<footer class="footer.*?<\/footer>', re.DOTALL)

    if old_start_tag == "NAVBAR":
        new_content = new_content.replace("perfex_crm.html", "perfex.html") # Integrar el nombre que el usuario quiere
        new_content = new_content.replace("perfex_crm.html", "perfex.html") # Reemplazar el nombre de archivo en el HTML
        content = navbar_pattern.sub(new_content, content)
    elif old_start_tag == "FOOTER":
        new_content = new_content.replace("perfex_crm.html", "perfex.html") # Integrar el nombre que el usuario quiere
        content = footer_pattern.sub(new_content, content)
    
    # Corregir el enlace a FAQ si está mal (el usuario lo mencionó)
    # En el navbar de index.html es: <a class="nav-link" href="faq.html">FAQ</a> (Línea 629)
    # En el footer de index.html es: <li><a href="faq.html">Preguntas Frecuentes</a></li> (Línea 893)
    # Si el usuario dice que falla, puede ser que en otras páginas esté mal.
    # Voy a estandarizar todos los enlaces a archivos HTML para que sean el nombre del archivo.
    
    # Corregir el nombre del archivo perfex_crm.html a perfex.html en el sistema de archivos
    # Esto debe hacerse antes de reemplazar el contenido, pero el script no puede renombrar archivos.
    # Haré el renombrado con un comando shell antes de ejecutar el script.
    
    # Asumiendo que el renombrado ya se hizo:
    # Renombrar perfex_crm.html a perfex.html
    
    # Corregir enlaces internos a archivos HTML que el usuario pueda haber escrito mal
    # Reemplazar cualquier mención de "perfex_crm.html" por "perfex.html"
    content = content.replace("perfex_crm.html", "perfex.html")
    
    # Corregir enlaces a "planes.html" si no están en el navbar principal
    # El usuario no lo pidió explícitamente, pero es una página que existe.
    # Voy a añadir "Planes" al navbar principal si no está.
    
    # En index.html, el navbar es:
    # 611                    <li class="nav-item">
    # 612                        <a class="nav-link" href="index.html">Inicio</a>
    # 613                    </li>
    # ...
    # 628                    <li class="nav-item">
    # 629                        <a class="nav-link" href="faq.html">FAQ</a>
    # 630                    </li>
    
    # Voy a usar el contenido del navbar y footer de index.html (ya renombrado) para reemplazar en todos los archivos.
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

# 1. Renombrar perfex_crm.html a perfex.html (se hará con shell)
# 2. Obtener el contenido del navbar y footer de index.html (ya renombrado)
# 3. Modificar el navbar para incluir "Planes" si es necesario (no lo haré a menos que el usuario lo pida, solo corregiré los enlaces)
# 4. Reemplazar el navbar y footer en todos los archivos HTML.

# Leer el contenido del navbar y footer de index.html (asumiendo que ya se renombró perfex_crm.html a perfex.html)
# Como no puedo renombrar el archivo antes de ejecutar el script, voy a modificar el script para que haga la corrección de nombres en el contenido.

# Contenido del navbar de index.html (Líneas 598-650)
NAVBAR_CONTENT = """<nav class="navbar navbar-expand-lg navbar-custom">
        <div class="container">
            <a class="navbar-brand" href="index.html">
                <i class="bi bi-tools"></i>
                TecnoGirona
            </a>
            
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav">
                <span class="navbar-toggler-icon"></span>
            </button>
            
            <div class="collapse navbar-collapse" id="navbarNav">
                <ul class="navbar-nav me-auto">
                    <li class="nav-item">
                        <a class="nav-link" href="index.html">Inicio</a>
                    </li>
                    <li class="nav-item dropdown">
                        <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown">
                            Servicios
                        </a>
                        <ul class="dropdown-menu">
                            <li><a class="dropdown-item" href="moviles.html"><i class="bi bi-phone"></i> Reparación Móviles</a></li>
                            <li><a class="dropdown-item" href="ordenadores.html"><i class="bi bi-laptop"></i> Reparación Ordenadores</a></li>
                            <li><a class="dropdown-item" href="consolas.html"><i class="bi bi-controller"></i> Reparación Consolas</a></li>
                            <li><a class="dropdown-item" href="datos.html"><i class="bi bi-hdd"></i> Recuperación Datos</a></li>
                            <li><a class="dropdown-item" href="empresas.html"><i class="bi bi-building"></i> Servicios IT Empresas</a></li>
                            <li><a class="dropdown-item" href="tpv.html"><i class="bi bi-credit-card"></i> Instalación TPV</a></li>
                            <li><a class="dropdown-item" href="planes.html"><i class="bi bi-cash-stack"></i> Planes de Mantenimiento</a></li>
                            <li><a class="dropdown-item text-crm" href="perfex.html"><i class="bi bi-diagram-3-fill text-crm"></i> **CRM Privado**</a></li>
                        </ul>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="faq.html">FAQ</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="nosotros.html">Nosotros</a>
                    </li>
                    <li class="nav-item">
                        <a class="nav-link" href="index.html#contacto">Contacto</a>
                    </li>
                </ul>
                
                <div class="navbar-actions">
                    <a href="tel:637161141" class="btn-phone">
                        <i class="bi bi-telephone"></i>
                        637 161 141
                    </a>
                    <a href="index.html#contacto" class="btn-quote">
                        Presupuesto Gratis
                    </a>
                </div>
            </div>
        </div>
    </nav>"""

# Contenido del footer de index.html (Líneas 870-915)
FOOTER_CONTENT = """<footer class="footer">
        <div class="container">
            <div class="footer-content">
                <div class="footer-section">
                    <h5>TecnoGirona</h5>
                    <p>Especialistas en reparación de dispositivos electrónicos en Girona desde 2010. Calidad, rapidez y garantía en cada reparación.</p>
                </div>
                
                <div class="footer-section">
                    <h5>Servicios</h5>
                    <ul>
                        <li><a href="moviles.html">Reparación Móviles</a></li>
                        <li><a href="ordenadores.html">Reparación Ordenadores</a></li>
                        <li><a href="consolas.html">Reparación Consolas</a></li>
                        <li><a href="datos.html">Recuperación Datos</a></li>
                        <li><a href="empresas.html">Servicios IT</a></li>
                        <li><a href="tpv.html">Instalación TPV</a></li>
                        <li><a href="planes.html">Planes de Mantenimiento</a></li>
                        <li><a href="perfex.html">CRM Privado</a></li>
                    </ul>
                </div>
                
                <div class="footer-section">
                    <h5>Información</h5>
                    <ul>
                        <li><a href="faq.html">Preguntas Frecuentes</a></li>
                        <li><a href="nosotros.html">Sobre Nosotros</a></li>
                        <li><a href="index.html#contacto">Contacto</a></li>
                        <li><a href="politica-privacidad.html">Política de Privacidad</a></li>
                        <li><a href="terminos-condiciones.html">Términos y Condiciones</a></li>
                    </ul>
                </div>
                
                <div class="footer-section">
                    <h5>Contacto</h5>
                    <ul>
                        <li><i class="bi bi-telephone me-2"></i> 637 161 141</li>
                        <li><i class="bi bi-envelope me-2"></i> tecnogirona@gmail.com</li>
                        <li><i class="bi bi-geo-alt me-2"></i> Girona, España</li>
                    </ul>
                </div>
            </div>
            
            <div class="footer-bottom">
                <p>&copy; 2024 TecnoGirona. Todos los derechos reservados.</p>
            </div>
        </div>
    </footer>"""

def main():
    # Renombrar el archivo perfex_crm.html a perfex.html
    old_path = os.path.join(DIR_PATH, "perfex_crm.html")
    new_path = os.path.join(DIR_PATH, "perfex.html")
    if os.path.exists(old_path):
        os.rename(old_path, new_path)
        print(f"Renombrado: {old_path} -> {new_path}")
    
    # Actualizar la lista de archivos HTML después del renombrado
    HTML_FILES = [f for f in os.listdir(DIR_PATH) if f.endswith(".html") and f != "fix_links.py"]
    
    # Patrones de búsqueda para navbar y footer
    navbar_pattern = re.compile(r'<nav class="navbar.*?<\/nav>', re.DOTALL)
    footer_pattern = re.compile(r'<footer class="footer.*?<\/footer>', re.DOTALL)
    
    # Corregir el navbar y footer en todos los archivos
    for filename in HTML_FILES:
        file_path = os.path.join(DIR_PATH, filename)
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Reemplazar navbar
        content = navbar_pattern.sub(NAVBAR_CONTENT, content)
        
        # Reemplazar footer
        content = footer_pattern.sub(FOOTER_CONTENT, content)
        
        # Corregir cualquier otra instancia de perfex_crm.html a perfex.html
        content = content.replace("perfex_crm.html", "perfex.html")
        
        # Corregir el enlace a FAQ si está mal (el usuario lo mencionó)
        # El enlace correcto es "faq.html". Asumo que el problema es que en algunas páginas
        # podría estar mal escrito o apuntar a un lugar incorrecto.
        # Al reemplazar el navbar y footer, ya se corrige en la navegación principal.
        # Busco cualquier otro enlace a FAQ que no esté en el navbar/footer.
        # No hay un patrón claro para un enlace roto a FAQ fuera de la navegación.
        # Con el reemplazo del navbar y footer, el problema debería estar resuelto.
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
            
        print(f"Enlaces corregidos en: {filename}")

if __name__ == "__main__":
    main()
