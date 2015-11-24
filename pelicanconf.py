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
# MARKUP = ['md', 'ipynb']

# PLUGIN_PATHS = './plugins'
# PLUGINS = ['ipynb']

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         )

# Social widget
SOCIAL = (('Linkedin Profile', 'https://ca.linkedin.com/in/tboquet'),
          ('Twitter Profile', 'https://twitter.com/thomasboquet'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = False

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
# ABOUT_ME = "Data Scientist at R2, juggling with machine learning and statistical tools in Python and R to tackle business challenges."
# AVATAR = "images/profile.jpg"
