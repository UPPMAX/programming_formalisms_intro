# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
#sys.path.insert(0, os.path.abspath('exts'))


# -- Project information -----------------------------------------------------

project = 'Programming formalism intro'
copyright = '2023, UPPMAX'
author = 'UPPMAX'
github_user = "UPPMAX"
github_repo_name = "programming_formalisms_intro"  # auto-detected from dirname if blank
github_version = "main/doc/"
conf_py_path = "/doc/" 

# The full version, including alpha/beta/rc tags
release = '0.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ["sphinx_lesson",
    "sphinx.ext.githubpages",
    "sphinx_rtd_theme_ext_color_contrast",
    "sphinxemoji.sphinxemoji",
    'sphinx-prompt',
    'sphinxcontrib.plantuml',
    'sphinx.ext.graphviz',
    'sphinxcontrib.mermaid',
    'sphinx_copybutton',
]
#plantuml = 'java -jar plantuml.jar'
#plantuml = 'java -Djava.awt.headless=true -jar %s' % os.path.join(os.path.dirname(os.path.abspath(__file__)), "plantuml.jar")

#plantuml = 'java -Djava.awt.headless=true -jar %s' % os.path.join(os.path.dirname(os.path.abspath(__file__)), "plantuml.jar")

mermaid_output_format = 'raq'
mermaid_params = [
    "--theme",
    "forest",
    "--width",
    "600",
    "--backgroundColor",
    "transparent",
]

jupyter_execute_notebooks = "cache"

myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "deflist",
    "dollarmath",
    "html_admonition",
    "html_image",
    "replacements",
    "smartquotes",
    "substitution",
    "tasklist",
]
copybutton_exclude = '.linenos, .gp, .go'

source_suffix = ['.rst', '.md','.dot','.uml','.gv']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
#exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
exclude_patterns = [
    "README*",
    "_build",
    "Thumbs.db",
    ".DS_Store",
    "jupyter_execute",
    "*venv*",
]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
#html_theme = 'alabaster'
html_theme = 'sphinx_rtd_theme'
#html_logo = "img/UU_logo.svg"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# HTML context:
from os.path import basename, dirname, realpath

html_context = {
    "display_github": True,
    "github_user": github_user,
    # Auto-detect directory name.  This can break, but
    # useful as a default.
    "github_repo": github_repo_name or basename(dirname(realpath(__file__))),
    "github_version": github_version,
    "conf_py_path": conf_py_path,
}
