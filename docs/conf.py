# -*- coding: utf-8 -*-

extensions = ["sphinx.ext.viewcode", "sphinx.ext.mathjax"]
templates_path = ["_templates"]
source_suffix = ".rst"

master_doc = "index"
project = "BMDS webserver"
copyright = "2016, Andy Shapiro"
author = "Andy Shapiro"
version = "0.5.0"
release = "0.5.0"

language = None
exclude_patterns = []
pygments_style = "sphinx"
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------
html_theme = "alabaster"
html_theme_options = {
    "show_powered_by": False,
    "description": "A windows webserver for executing EPA's BMDS software",
    "github_user": "shapiromatron",
    "github_repo": "bmds-server",
    "github_count": False,
    "show_related": False,
    "sidebar_includehidden": False,
}
html_static_path = ["_static"]
html_sidebars = {
    "**": ["about.html", "navigation.html", "relations.html", "searchbox.html", "donate.html"]
}
htmlhelp_basename = "BMDSdoc"
