#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Thomas Boquet'
SITENAME = u'MacGRython'
SITEURL = 'http://tboquet.github.io'
PATH = 'content'

TIMEZONE = 'America/Montreal'

DEFAULT_LANG = u'en'

# ipynb setup
MARKUP = ['md', 'ipynb']
IPYNB_USE_META_SUMMARY = True
PLUGIN_PATHS = ['./plugins']
PLUGINS = ['render_math', 'ipynb']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
MD_EXTENSIONS = ['codehilite(css_class=highlight)']

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         )

# Social widget
SOCIAL = (('Linkedin', 'https://ca.linkedin.com/in/tboquet'),
          ('Twitter', 'https://twitter.com/thomasboquet'),
          ('github', 'https://github.com/tboquet/'))

DEFAULT_PAGINATION = 5
ADDTHIS_PROFILE = "ra-56576a95c573c6a9"
ADDTHIS_DATA_TRACK_ADDRESSBAR = True
ADDTHIS_FACEBOOK_LIKE = True
ADDTHIS_TWEET = True
OPEN_GRAPH_IMAGE = "https://github.com/tboquet.github.io/content/images/mcplaceholdermin.jpg"
OPEN_GRAPH_FB_APP_ID = '457522324431057'
# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = False
PYGMENTS_STYLE = 'emacs'
PYGMENTS_RST_OPTIONS = {'linenos': 'none'}
THEME = "../pelican-themes/pelican-bootstrap3/"
BOOTSTRAP_THEME = "cosmo"
SITELOGO = "images/transwhite.png"
DISPLAY_TAGS_ON_SIDEBAR = False
STATIC_PATHS = ['images']
SUMMARY_MAX_LENGTH = 50
SITELOGO_SIZE = 24
BANNER = "images/bandcut2.jpg"
BANNER_SUBTITLE = "Data Science & Machine Learning with paper clips"
BANNER_ALL_PAGES = False
SHOW_DATE_MODIFIED = True
# ABOUT_ME = "Data Scientist at R2, juggling with machine learning and statistical tools in Python and R to tackle business challenges."
# AVATAR = "images/profile.jpg"
