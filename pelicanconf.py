# -*- coding: utf-8 -*- #
'''pelican configurations.
'''
from __future__ import unicode_literals

AUTHOR = 'Satoru SATOH'
SITENAME = "ssato's blog"
# SITEURL = 'https://ssato.github.io/blog'

PATH = 'content'
# OUTPUT_PATH = 'docs'

THEME = 'themes/pelican-simplegrey'

TIMEZONE = 'Asia/Tokyo'

DEFAULT_LANG = 'ja'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'), )

# Social widget
SOCIAL = (('Github', 'https://github.com/ssato/'),
          ('Instagram', 'https://www.instagram.com/satoh.satoru/'),
          ('Twitter', 'https://twitter.com/satoru_satoh'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
