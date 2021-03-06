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
sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('..'))
sys.path.insert(0, os.path.abspath('../src/'))

from pyH2A import __version__


# -- Project information -----------------------------------------------------

project = 'pyH2A'
copyright = '2022, Jacob Schneidewind'
author = 'Jacob Schneidewind'

# The full version, including alpha/beta/rc tags
release = __version__
version = __version__

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc',
			  'sphinx.ext.autosummary',
   			  'sphinx.ext.todo',
    		  'sphinx.ext.coverage',
    		  'sphinx.ext.viewcode',
    		  'numpydoc',
    		  'autodocsumm'
]

autodoc_default_options = {
    'autosummary': True,
}

numpydoc_show_class_members = False

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

source_suffix = '.rst'

master_doc = 'index'

pygments_style = 'sphinx'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

todo_include_todos = True


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.

html_theme = 'furo'  #sphinx_rtd_theme

# These paths are either relative to html_static_path
# or fully qualified paths (eg. https://...)

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".

html_static_path    = ['style']        # folders to include in output
html_css_files      = ['custom.css']   # extra style files to apply
html_logo = './_static/pyH2A.svg'


