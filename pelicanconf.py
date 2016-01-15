#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Namit Kewat'
SITENAME = u"Namit Kewat's Blog"
SITEURL = 'http://namitkewat.github.io/'
SITELOGO = 'https://avatars1.githubusercontent.com/u/1215126?v=3&s=460'
SITESUBTITLE = 'Python, XBRL, Finance, MongoDB'
SITEDESCRIPTION = 'Namit kewat\'s Thoughts and Writings'

PATH = 'content'

TIMEZONE = 'Asia/Kolkata'

DEFAULT_LANG = u'en'

THEME = 'Flex'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('blog', '/blog'),
#         ('about', '/pages/about.html#about'),
#         ('contact', 'pages/about.html#contact'),)

# Social widget
SOCIAL = (('linkedin', 'https://in.linkedin.com/in/namitkewat'),
          ('github', 'https://github.com/namitkewat'),
          ('stack-overflow', 'http://stackoverflow.com/users/1283171/namit'),
          ('twitter', 'https://twitter.com/namitkewat'),)

DEFAULT_PAGINATION = 5

DISQUS_SITENAME = 'namitkewatgithubio'
ROBOTS = 'index, follow'

YEAR_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/index.html'
# MONTH_ARCHIVE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/index.html'
# DIRECT_TEMPLATES = ['index', 'categories', 'authors', 'archives']

MAIN_MENU = True
MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'))

COPYRIGHT_YEAR = 2016

MD_EXTENSIONS = ['codehilite(pygments_style=colorful, linenums=True)', 'extra']
## Details of codehilite are given at: https://github.com/waylan/Python-Markdown/blob/master/markdown/extensions/codehilite.py


# code blocks with line numbers
# PYGMENTS_RST_OPTIONS = {'linenos': 'table'}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
