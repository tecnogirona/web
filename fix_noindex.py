#!/usr/bin/env python3
"""
Script para remover etiquetas 'noindex' de todos los archivos HTML
y reemplazarlas con 'index, follow' para mejorar la indexación en buscadores.

Uso:
    python3 fix_noindex.py
"""

import os
import re
from pathlib import Path

def fix_noindex_in_file(filepath):
    """
    Remueve o reemplaza etiquetas noindex en un archivo HTML.
    
    Args:
        filepath: Ruta del archivo HTML
        
    Returns:
        bool: True si se realizó algún cambio
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Reemplazar diferentes variantes de noindex
        # Patrón 1: <meta name="robots" content="noindex">
        content = re.sub(
            r'<meta\s+name="robots"\s+content="noindex"\s*>',
            '<meta name="robots" content="index, follow">',
            content,
            flags=re.IGNORECASE
        )
        
        # Patrón 2: <meta name="robots" content="noindex, nofollow">
        content = re.sub(
            r'<meta\s+name="robots"\s+content="noindex,\s*nofollow"\s*>',
            '<meta name="robots" content="index, follow">',
            content,
            flags=re.IGNORECASE
        )
        
        # Patrón 3: <meta name="robots" content="noindex, follow">
        content = re.sub(
            r'<meta\s+name="robots"\s+content="noindex,\s*follow"\s*>',
            '<meta name="robots" content="index, follow">',
            content,
            flags=re.IGNORECASE
        )
        
        # Si hubo cambios, guardar el archivo
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        
        return False
        
    except Exception as e:
        print(f"❌ Error procesando {filepath}: {e}")
        return False

def main():
    """Procesa todos los archivos HTML en el directorio actual."""
    
    html_files = list(Path('.').glob('*.html'))
    
    if not html_files:
        print("❌ No se encontraron archivos HTML")
        return
    
    print(f"📝 Procesando {len(html_files)} archivos HTML...\n")
    
    fixed_count = 0
    
    for html_file in sorted(html_files):
        if fix_noindex_in_file(str(html_file)):
            print(f"✅ {html_file.name} - Corregido")
            fixed_count += 1
        else:
            print(f"⏭️  {html_file.name} - Sin cambios necesarios")
    
    print(f"\n{'='*50}")
    print(f"✨ Proceso completado:")
    print(f"   - Total archivos: {len(html_files)}")
    print(f"   - Corregidos: {fixed_count}")
    print(f"   - Sin cambios: {len(html_files) - fixed_count}")
    print(f"{'='*50}\n")
    
    if fixed_count > 0:
        print("✅ Las etiquetas 'noindex' han sido eliminadas/reemplazadas")
        print("📊 Próximos pasos:")
        print("   1. Commit los cambios en GitHub")
        print("   2. Espera a que Google reindexe (24-48 horas)")
        print("   3. Verifica en Google Search Console")

if __name__ == '__main__':
    main()
