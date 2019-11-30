#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = '高星'
SITENAME = '高星的博客'
#SITEURL = 'https://gnix_oag.coding.me/home'

PATH = 'content'

PLUGIN_PATHS = ['D:\\webpage\\pelican-plugins']
PLUGINS = ['i18n_subsites']
THEME = 'D:\\webpage\\pelican-themes\\pelican-bootstrap3'
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
I18N_TEMPLATES_LANG = 'en'
BOOTSTRAP_THEME =  'darkly'
#BOOTSTRAP_THEME =  'abc'
SHOW_ARTICLE_AUTHOR = True
SHOW_ARTICLE_CATEGORY = True
SHOW_DATE_MODIFIED = True
PYGMENTS_STYLE =  'vim'
#BOOTSTRAP_NAVBAR_INVERSE = True
DISPLAY_TAGS_ON_SIDEBAR = True
DISPLAY_CATEGORIES_ON_SIDEBAR = True
DISPLAY_RECENT_POSTS_ON_SIDEBAR = True
#DISPLAY_ARCHIVE_ON_SIDEBAR = True
#DISPLAY_AUTHORS_ON_SIDEBAR  = True

USE_FOLDER_AS_CATEGORY = True
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True
GITHUB_URL = 'http://gnixoag.github.io'


TIMEZONE = 'Asia/Shanghai'

#DEFAULT_LANG = 'Chinese (Simplified)'

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
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True