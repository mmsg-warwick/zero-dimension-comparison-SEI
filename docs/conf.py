# Configuration file for the Sphinx documentation builder.
#
# This file contains an opinionated list of extensions and configuration options
# used by the PyBaMM documentation.
#
# For a full list, see the Sphinx documentation for configuration options at
# https://www.sphinx-doc.org/en/master/config
#
# More information about the configuration options used here can be found in the
# configuration file for the PyBaMM documentation at
# https://github.com/pybamm-team/PyBaMM/blob/develop/docs/conf.py
#
# The configuration options to adjust the PyData Sphinx Theme with can be found at
# https://pydata-sphinx-theme.readthedocs.io/en/stable/user_guide/index.html


import importlib.metadata
import sys
from pathlib import Path

# ---- Project information ------------------------------------------------------------
project = "zero-dimension-comparison-SEI"
copyright = "2024, Kawa Manmi"
author = "Kawa Manmi"
version = release = importlib.metadata.version("zero_dimension_comparison_sei")

# ---- Path configuration -------------------------------------------------------------

# Path for repository root
sys.path.insert(0, Path("../").resolve())

# Path for local Sphinx extensions
sys.path.append(Path("./sphinxext/").resolve())

# ---- General configuration ----------------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.

# needs_sphinx = '1.0'

# The suffix(es) of source filenames. You may specify multiple suffixes as
# a list of strings.
source_suffix = [".rst", ".md"]

# List of patterns relative to the source directory that match files and
# directories to ignore when looking for source files. This pattern also
# affects the html_static_path and html_extra_path configuration options.
exclude_patterns = [
    "_build",
    "**.ipynb_checkpoints",
    "Thumbs.db",
    ".DS_Store",
]

html_theme = "pydata_sphinx_theme"
html_title = f"{project} v{version} Manual"
html_last_updated_fmt = "%Y-%m-%d"
html_static_path = ["_static"]
html_file_suffix = ".html"

# For edit button
html_context = {
    "github_user": "mmsg-warwick",
    "github_repo": "zero-dimension-comparison-SEI",
    "github_version": "main",
    "doc_path": "docs/",
}
# Add any logos and favicons for your hosted documentation here. The logo and the favicon
# should be placed in the html_static_path directory listed above.
# html_logo = "_static/logo.png"
# html_favicon = "_static/favicon.png"

# Add any paths that contain custom static files (such as style sheets or JavaScript scripts)
# in the html_static_path listed above. They are copied after the builtin static files, so a
# file named "default.css" will overwrite the builtin "default.css".
# html_css_files = ["custom.css"]
# html_js_files = ["custom.js"]

# Suppress any warnings generated by Sphinx and/or by Sphinx extensions as
# a list of strings. The following warnings are suppressed by default:
suppress_warnings = ["git.too_shallow"]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The language for content autogenerated by Sphinx. Refer to the Sphinx documentation
# for a list of supported language codes according to the IETF BCP 47 standard.
language = "en"

# Add any Sphinx extension module names here in a list of strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones. The
# custom ones must be placed under the path specified for local Sphinx extensions
# in the system path configuration above.

extensions = [
    # Sphinx extensions
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.napoleon",
    # Local extensions under ./sphinxext/
    # Third-party extensions
    "myst_parser",
    "sphinx_design",
    "sphinx_copybutton",
    "sphinx_inline_tabs",
    "sphinxcontrib.bibtex",
    "sphinx_last_updated_by_git",
    "pydata_sphinx_theme",
    "nbsphinx",
    "IPython.sphinxext.ipython_console_highlighting",
]

# Configure references
bibtex_bibfiles = ['refs.bib']
# ---- Options for EPUB output --------------------------------------------------------

# Bibliographic Dublin Core information
epub_title = project

# The unique identifier of the text. This can be a ISBN number or the project homepage
# epub_identifier = ''

# A unique identification for the text
# epub_uid = ''

# A list of files that should not be packed into the EPUB file
epub_exclude_files = ["search.html"]

# ---- HTML theme configuration -------------------------------------------------------

# Theme options are theme-specific and customize the look and feel of a theme further.
# For a list of options available for each theme, see the documentation for the theme.

# For a list of options available for the PyData Sphinx Theme, see the documentation at
# https://pydata-sphinx-theme.readthedocs.io/en/stable/user_guide/index.html

html_theme_options = {
    # "logo": {
    #     "image_light": "logo.png",
    #     "image_dark": "logo.png",
    # },
    "icon_links": [
        {
            "name": "GitHub",
            "icon": "fa-brands fa-square-github",
            "url": "https://github.com/mmsg-warwick/zero-dimension-comparison-SEI",
        },
        {
            "name": "PyPI",
            "url": "https://pypi.org/project/zero-dimension-comparison-SEI/",
            "icon": "fa-solid fa-box",
        },
    ],
    "collapse_navigation": True,
    "navbar_end": ["theme-switcher", "navbar-icon-links"],
    "use_edit_page_button": True,
    "pygment_light_style": "xcode",
    "pygment_dark_style": "monokai",
    "footer_start": [
        "copyright",
        "sphinx-version",
    ],
    "footer_end": [
        "theme-version",
        "last-updated",
    ],
}

# ---- Extension configuration --------------------------------------------------------

# Add any configuration options for Sphinx extensions here as per the documentation for
# each extension. See the PyBaMM documentation at
# https://github.com/pybamm-team/PyBaMM/blob/develop/docs/conf.py for examples of how
# to configure Sphinx extensions for your project.

myst_enable_extensions = [
    "colon_fence",
]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
    "scipy": ("https://docs.scipy.org/doc/scipy/reference", None),
    "matplotlib": ("https://matplotlib.org/stable", None),
    "pybamm": ("https://docs.pybamm.org/en/latest/", None),
}

always_document_param_types = True
napoleon_use_rtype = True
napoleon_google_docstring = False
