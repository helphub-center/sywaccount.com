# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Path setup --------------------------------------------------------------

# Add any custom paths here if modules are outside the root
# sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------

project = 'SYW Account Login Guide'
copyright = '2025, SYW'
author = 'SYW Support Team'

# Full version
release = '1.0.0'

# -- General configuration ---------------------------------------------------

# Add Sphinx extensions here if needed
extensions = []

# Enable raw HTML inside RST files
raw_enabled = True

# Templates directory
templates_path = ['_templates']

# Ignore system and build files
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

# Page titles (full + short)
html_title = "How to Log In to SYW Account Online Easily – Complete Guide"
html_short_title = "SYW Login Guide"

# Favicon (place favicon.ico in root or /_static)
html_favicon = 'favicon.ico'

# Hide “View page source”
html_show_sourcelink = False

# Allow raw HTML in .rst files
html_allow_unsafe = True

# Theme options (minimal clean UI)
html_theme_options = {
    'show_powered_by': False,
}

# Static directory (uncomment if using CSS/JS/images)
# html_static_path = ['_static']
