#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'ht_song@163.com'
SITENAME = "Hts' Blog"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'zh_CN'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = "themes/pelican-blueidea"

PLUGIN_PATHS = ['plugins']
PLUGINS = ['static_comments']

from embedly_cards import EmbedlyCardExtension
MD_EXTENSIONS = ['codehilite(css_class=highlight)',
                 'extra',
                 EmbedlyCardExtension()]
