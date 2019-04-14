import os
import socket

from sunpy_sphinx_theme import get_html_theme_path

try:
    from urllib.parse import urljoin
except ImportError:
    from urlparse import urljoin


html_theme_path = get_html_theme_path()
html_theme = "sunpy"
html_static_path = [os.path.join(html_theme_path[0], html_theme, "static")]
templates_path = [os.path.join(html_theme_path[0], html_theme, "templates")]
html_favicon = os.path.join(html_static_path[0], "img", "favicon-32.ico")

on_rtd = os.environ.get("READTHEDOCS", False) == "True"

if on_rtd:
    sunpy_website_url_base = "https://sunpy.org"
else:
    sunpy_website_url_base = socket.gethostname()


def page_url(page):
    return urljoin(sunpy_website_url_base, page)


html_sidebars = {"**": ["docsidebar.html"]}
html_theme_options = {
    "navbar_links": [  # About and documentation is hard coded due to drop down
        ("Blog", page_url("blog.html"), 1),
        ("Support Us", page_url("contribute.html"), 1),
        ("Get Help", page_url("help.html"), 1),
        ("SunPy Project", page_url("team.html"), 1),
    ],
    "navbar_docs": [  # About and documentation is hard coded due to drop down
        ("SunPy", "https://docs.sunpy.org/en/stable/", 1),
        ("ndcube", "https://docs.sunpy.org/projects/ndcube", 1),
        ("drms", "https://docs.sunpy.org/projects/drms", 1),
        ("radiospectra", "https://docs.sunpy.org/projects/radiospectra/en/latest/index.html", 1),
        ("IRISPy", "https://docs.sunpy.org/projects/irispy/en/latest/", 1),
    ],
    "on_rtd": on_rtd,
}
