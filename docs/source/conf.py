# Configuration file for the Sphinx documentation builder.


# -- Path setup --------------------------------------------------------------
import os
import sys
sys.path.insert(0, os.path.abspath('../../src'))

project = 'Outer Ring FastAPI Base'
copyright = '2025, Aritz Madariaga'
author = 'Aritz Madariaga <aritzmadariaga@deusto.es>'
release = '0.1.0'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'myst_parser',
]

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'sphinx_rtd_theme'
