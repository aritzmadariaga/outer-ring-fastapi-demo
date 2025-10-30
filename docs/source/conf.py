# Configuration file for the Sphinx documentation builder.


# -- Path setup --------------------------------------------------------------
import os
import sys
from pathlib import Path

# Ensure the project `src` directory is on sys.path so autodoc can import `app`.
# Resolve the path relative to this conf.py file (more robust inside containers/CI).
HERE = Path(__file__).resolve().parent
SRC_PATH = (HERE / '..' / '..' / 'src').resolve()
sys.path.insert(0, str(SRC_PATH))

# Helpful debug output in CI logs if autodoc cannot import modules.
print(f"[sphinx.conf] inserted src to sys.path: {SRC_PATH}")

project = 'Outer Ring FastAPI Base'
copyright = '2025, Aritz Madariaga'
author = 'Aritz Madariaga <aritzmadariaga@deusto.es>'
release = '0.1.0'

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'myst_parser',
    'sphinx_autodoc_typehints',
    'sphinx.ext.viewcode',
    'sphinx_copybutton',
    'sphinx.ext.intersphinx',
    'sphinxcontrib.mermaid'
]
intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
    'fastapi': ('https://fastapi.tiangolo.com/', None),
}

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'sphinx_rtd_theme'
