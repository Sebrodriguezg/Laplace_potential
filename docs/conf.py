# conf.py

import os
import sys
sys.path.insert(0, os.path.abspath('..'))

project = 'Campo Estatico MDF'
copyright = '2024, Jules'
author = 'Jules'
release = '0.1'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon', # Soporte para docstrings de Google y NumPy
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

language = 'es'

html_theme = 'alabaster'
html_static_path = ['_static']
