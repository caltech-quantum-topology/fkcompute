# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

# -- Path setup ---------------------------------------------------------------
# Make the package importable so autodoc can import it.
sys.path.insert(0, os.path.abspath("../src"))

# -- Project information ------------------------------------------------------
project = "fkcompute"
copyright = "2026, Paul Orland, Davide Passaro, Lara San Martin Suarez, Toby Saunders-A'Court, Josef Svoboda"
author = "Paul Orland, Davide Passaro, Lara San Martin Suarez, Toby Saunders-A'Court, Josef Svoboda"
release = "0.2.20"
version = "0.2"

# -- General configuration ----------------------------------------------------
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.githubpages",
    "sphinx_copybutton",
    "sphinx_design",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# -- Autodoc configuration ----------------------------------------------------
autodoc_default_options = {
    "members": True,
    "undoc-members": True,
    "show-inheritance": True,
    "member-order": "bysource",
}
autosummary_generate = True
napoleon_google_docstring = False
napoleon_numpy_docstring = True
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = False

# -- Intersphinx --------------------------------------------------------------
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
    "sympy": ("https://docs.sympy.org/latest/", None),
}

# -- Options for HTML output --------------------------------------------------
html_theme = "furo"
html_static_path = ["_static"]
html_css_files = ["quantum_topology.css"]

_font_stack = '"Space Grotesk", system-ui, -apple-system, BlinkMacSystemFont, "SF Pro Text", sans-serif'
_mono_stack = '"IBM Plex Mono", "SFMono-Regular", Menlo, Consolas, monospace'

html_theme_options = {
    "light_css_variables": {
        "font-stack": _font_stack,
        "font-stack--monospace": _mono_stack,
        "color-brand-primary": "#d55a2b",
        "color-brand-content": "#d55a2b",
        "color-background-primary": "#f8f9fc",
        "color-background-secondary": "#ffffff",
        "color-foreground-primary": "#1a1a2e",
        "color-foreground-secondary": "#5a5a7a",
        "color-foreground-muted": "#5a5a7a",
        "color-link": "#0066cc",
        "color-link--hover": "#d55a2b",
        "color-link-underline": "transparent",
        "color-link-underline--hover": "#d55a2b",
        "color-sidebar-background": "#ffffff",
        "color-sidebar-link-text": "#5a5a7a",
        "color-sidebar-link-text--top-level": "#1a1a2e",
        "color-sidebar-item-background--current": "rgba(213,90,43,0.08)",
        "color-sidebar-item-background--hover": "rgba(213,90,43,0.04)",
        "color-sidebar-brand-text": "#1a1a2e",
        "color-sidebar-caption-text": "#5a5a7a",
        "color-code-background": "#f0f1f5",
        "color-code-foreground": "#1a1a2e",
        "color-highlighted-background": "rgba(213,90,43,0.12)",
        "color-admonition-background": "rgba(213,90,43,0.04)",
        "color-header-background": "rgba(248,249,252,0.95)",
        "color-header-border": "rgba(0,0,0,0.08)",
        "color-header-text": "#1a1a2e",
    },
    "dark_css_variables": {
        "font-stack": _font_stack,
        "font-stack--monospace": _mono_stack,
        "color-brand-primary": "#ff6c39",
        "color-brand-content": "#ff6c39",
        "color-background-primary": "#050611",
        "color-background-secondary": "#07081a",
        "color-foreground-primary": "#f5f7ff",
        "color-foreground-secondary": "#9aa0c4",
        "color-foreground-muted": "#9aa0c4",
        "color-link": "#ffe182",
        "color-link--hover": "#ff6c39",
        "color-link-underline": "transparent",
        "color-link-underline--hover": "#ff6c39",
        "color-sidebar-background": "#07081a",
        "color-sidebar-link-text": "#9aa0c4",
        "color-sidebar-link-text--top-level": "#f5f7ff",
        "color-sidebar-item-background--current": "rgba(255,108,57,0.1)",
        "color-sidebar-item-background--hover": "rgba(255,108,57,0.06)",
        "color-sidebar-brand-text": "#f5f7ff",
        "color-sidebar-caption-text": "#9aa0c4",
        "color-code-background": "#0a0a20",
        "color-code-foreground": "#f5f7ff",
        "color-highlighted-background": "rgba(255,108,57,0.18)",
        "color-admonition-background": "rgba(255,108,57,0.06)",
        "color-header-background": "rgba(5,6,17,0.92)",
        "color-header-border": "rgba(255,255,255,0.04)",
        "color-header-text": "#f5f7ff",
    },
    "navigation_with_keys": True,
    "top_of_page_button": "edit",
    "source_repository": "https://github.com/caltech-quantum-topology/fkcompute/",
    "source_branch": "main",
    "source_directory": "docs/",
}

# -- Options for LaTeX output -------------------------------------------------
latex_elements = {
    "preamble": r"""
\usepackage{amsmath}
\usepackage{amssymb}
""",
}
