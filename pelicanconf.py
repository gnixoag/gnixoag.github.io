#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = '高星'
SITENAME = '高星的博客'
#SITEURL = 'https://gnix_oag.coding.me/home'

PATH = 'content'

#插件
PLUGIN_PATHS = ['D:\\webpage\\pelican-plugins']
PLUGINS = ['i18n_subsites','plantuml','tipue_search','neighbors','series',
	    'render_math',
	    'extract_toc','summary','sitemap','gzip_cache']

#主题设置
THEME = 'D:\\webpage\\pelican-themes\\pelican-bootstrap3'
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}
I18N_TEMPLATES_LANG = 'en'
BOOTSTRAP_THEME =  'darkly'

#显示文章作者、分类、修改日期
SHOW_ARTICLE_AUTHOR = True
SHOW_ARTICLE_CATEGORY = True
SHOW_DATE_MODIFIED = True

#代码显示风格
PYGMENTS_STYLE =  'vim'


DISPLAY_TAGS_ON_SIDEBAR = True
DISPLAY_CATEGORIES_ON_SIDEBAR = True
DISPLAY_RECENT_POSTS_ON_SIDEBAR = True
DISPLAY_ARCHIVE_ON_SIDEBAR = True
DISPLAY_AUTHORS_ON_SIDEBAR  = True

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
LINKS = (('国内博客', 'http://gnix_oag.coding.me/home/'),
         ('国外博客', 'http://gnixoag.github.io/'),
         ('工作单位', 'http://www.hnxxjsxy.com'),)

# Social widget
SOCIAL = (('Email', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

