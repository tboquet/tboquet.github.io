#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Thomas Boquet'
SITENAME = u'MacGython'
SITEURL = ''
PATH = 'content'

TIMEZONE = 'America/Montreal'

DEFAULT_LANG = u'en'

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
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('Linkedin Profile', 'https://ca.linkedin.com/in/tboquet'),
          ('Twitter Profile', '#'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = "theme"
BOOTSTRAP_THEME = "cosmo"
SITELOGO = "images/transwhite.png"
DISPLAY_TAGS_ON_SIDEBAR = False
STATIC_PATHS = ['images']
SUMMARY_MAX_LENGTH = 50
SITELOGO_SIZE = 24
BANNER = "images/bandcut2.jpg"
BANNER_SUBTITLE = "Data Science & Machine Learning with paper clips"
BANNER_ALL_PAGES = False
