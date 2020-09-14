#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'ht_song@163.com'
SITENAME = "涛声依旧 (ht_song@163.com)"
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
         ('www.scut.edu.cn', 'http://www.scut.edu.cn'),)

# Social widget
SOCIAL = (('腾讯课堂', 'https://ke.qq.com/course/934385?taid=1857780&tuin=3da8917f'),
          ('GITHUB', 'https://github.com/htsong'),
          ('Email','mailto: ht_song@163.com'),
         )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
STATIC_COMMENTS = True   # enable static comments, the output path default is 'comments'

THEME = "themes/pelican-blueidea"

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['static_comments','toy']

# from embedly_cards import EmbedlyCardExtension
# MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra', EmbedlyCardExtension()]
