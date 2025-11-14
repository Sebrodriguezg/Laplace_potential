# conf.py

import os
import sys

# ============================================================
# CONFIGURACIÓN DE RUTAS
# ============================================================

# Añadir la carpeta raíz del proyecto a sys.path
BASE_DIR = os.path.abspath(os.path.join(__file__, "../../"))
sys.path.insert(0, BASE_DIR)

# ============================================================
# METADATOS
# ============================================================

project = 'Campo Estatico MDF'
copyright = '2025, Rodriguez-Huertas-Avila'
author = 'Sebastian Rodriguez, Camilo Huertas, Julian Avila'
release = '0.1'

# ============================================================
# EXTENSIONES
# ============================================================

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.autosummary',
    'sphinx.ext.viewcode',
]

autosummary_generate = True

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'es'

# ============================================================
# THEME
# ============================================================

html_theme = 'sphinx_rtd_theme'
html_title = "Documentación – Campo Estático MDF"

html_theme_options = {
    'navigation_depth': 4,
    'collapse_navigation': False,
    'sticky_navigation': True,
    'titles_only': False
}

# ============================================================
# ARCHIVOS ESTÁTICOS
# ============================================================

html_static_path = ['_static']

# ============================================================
# CONFIG ESPECIAL PARA GITHUB PAGES
# ============================================================

# 1. HABILITAR RUTAS RELATIVAS
html_use_index = True
html_copy_source = True

# ESTA LÍNEA ES LA MÁS IMPORTANTE:
html_use_relative_paths = True

# 2. CONFIGURAR html_baseurl
# CAMBIA "USUARIO" Y "REPO" POR LOS TUYOS
html_baseurl ="https://sebrodriguezg.github.io/Laplace_potential/"

# 3. EVITAR QUE GITHUB PAGES ROMPA LAS CARPETAS _static, _sources, etc.
html_extra_path = ['.nojekyll']
