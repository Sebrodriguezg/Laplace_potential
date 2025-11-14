# conf.py

import os
import sys
# Añadir la carpeta raíz del proyecto a sys.path
BASE_DIR = os.path.abspath(os.path.join(__file__, "../../"))
sys.path.insert(0, BASE_DIR)

project = 'Campo Estatico MDF'
copyright = '2025, Rodriguez-Huertas-Avila'
author = 'Sebastian Rodriguez, Camilo Huertas, Julian Avila'
release = '0.1'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.autosummary',  # genera resúmenes automáticos
    'sphinx.ext.viewcode',     # agrega enlaces al código fuente
]

autosummary_generate = True

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'es'

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_title = "Documentación – Campo Estático MDF"
html_theme_options = {
    'navigation_depth': 4,
    'collapse_navigation': False,
    'sticky_navigation': True,
    'titles_only': False
}

