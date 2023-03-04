"""Sphinx configuration."""
project = "stixx"
author = "Mauricio Guerrero"
copyright = "2023, Mauricio Guerrero"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
