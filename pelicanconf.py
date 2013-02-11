#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = u'Staff'
SITENAME = u'LeafLabs'
SITEURL = 'http://leaflabs.com'

TIMEZONE = 'UTC'

DEFAULT_LANG = u'en'

DEFAULT_PAGINATION = False

ARTICLE_URL = '{date:%Y}/{date:%b}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%b}/{slug}/index.html'
ARTICLE_LANG_URL = '{lang}/{date:%Y}/{date:%b}/{slug}/'
ARTICLE_LANG_SAVE_AS = '{lang}/{date:%Y}/{date:%b}/{slug}/index.html'

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
PAGE_LANG_URL = '{lang}/{slug}/'
PAGE_LANG_SAVE_AS = '{lang}/{slug}/index.html'

AUTHOR_SAVE_AS = False
CATEGORY_SAVE_AS = False
TAG_SAVE_AS = False

PATH = '.'
ARTICLE_DIR = ('posts')
PAGE_DIR = ('pages')
#FILES_TO_COPY = (('style', 'style'), )
STATIC_PATHS = ['style']

#DIRECT_TEMPLATES = ('archives')

FEED_ALL_RSS = 'main.xml'
FEED_MAX_ITEMS = '20'

THEME = "leaflabs_theme"
THEME_STATIC_PATHS = ['style', ]

MARKUP = ('rst', 'md', 'html')
