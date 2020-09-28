#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'ht_song@163.com'
SITENAME = "涛声依旧"
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

# site's frame
DEFAULT_PAGINATION = 10
DIRECT_TEMPLATES = ('index', 'categories', 'authors', 'archives')
THEME = "themes/pelican-blueidea"
STATIC_PATHS = ["images"]

# Display pages list on the top menu
DISPLAY_PAGES_ON_MENU = True
# Display categories list on the top menu
DISPLAY_CATEGORIES_ON_MENU = True
# Display categories list as a submenu of the top menu
DISPLAY_CATEGORIES_ON_SUBMENU = False
# Display the category in the article's info
DISPLAY_CATEGORIES_ON_POSTINFO = False
# Display the author in the article's info
DISPLAY_AUTHOR_ON_POSTINFO = True
# Display the search form
DISPLAY_SEARCH_FORM = False
# Sort pages list by a given attribute
PAGES_SORT_ATTRIBUTE = 'Title'
# Display the "Fork me on Github" banner
# GITHUB_URL = ('https://github.com/htsong')
# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('www.scut.edu.cn', 'http://www.scut.edu.cn'),)
# Social widget
SOCIAL = (('腾讯课堂', 'https://ke.qq.com/course/934385?taid=1857780&tuin=3da8917f'),
          ('GITHUB', 'https://github.com/htsong'),
          ('Email: ht_song@163.com','mailto: ht_song@163.com'),
          ('QQ: 1034457471','mailto: 1034457471@qq.com'),
         )

# plugins
PLUGIN_PATHS = ['./plugins']
PLUGINS = ['static_comments','toy','render_math']

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
STATIC_COMMENTS = True   # enable static comments, the output path default is 'comments'

# from embedly_cards import EmbedlyCardExtension
# MD_EXTENSIONS = ['codehilite(css_class=highlight)', 'extra', EmbedlyCardExtension()]
