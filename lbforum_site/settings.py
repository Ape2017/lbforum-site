# Django settings for lbforum_site project.
import os
HERE = os.path.dirname(os.path.abspath(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': os.path.join(HERE, 'lbforum.sqlite'),                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(HERE, 'media/')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/admin_media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'm_wh2yga#6hp#6b3(f1)r90#%je9ikx4t5%$igdy+a#oy9y$q6'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.locale.LocaleMiddleware',

    #'debug_toolbar.middleware.DebugToolbarMiddleware',
    'pagination.middleware.PaginationMiddleware',
    'onlineuser.middleware.OnlineUserMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
        "django.core.context_processors.auth",
        "django.core.context_processors.debug",
        "django.core.context_processors.i18n",
        "django.core.context_processors.media",
        "django.core.context_processors.request",

        "djangohelper.context_processors.ctx_config",
)


ROOT_URLCONF = 'urls'

TEMPLATE_DIRS = (
        os.path.join(HERE, 'templates_plus'),
        os.path.join(HERE, 'templates'),
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

FIXTURE_DIRS = (
        os.path.join(HERE, 'fixtures'),
)
 

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.messages',

    'pagination',
    #'sorl.thumbnail',
    #'debug_toolbar',
    'registration',    
    'south',

    'lbforum',
    'simpleavatar',
    'djangohelper',
    'onlineuser',
    'attachments',

    'lbregistration',
)

LBFORUM_MEDIA_PREFIX = '%slbforum/' % MEDIA_URL

ROOT_URL = '/'
LOGIN_REDIRECT_URL = ROOT_URL
LOGIN_URL = "%saccounts/login/" % ROOT_URL
LOGOUT_URL = "%saccounts/logout/" % ROOT_URL
REGISTER_URL = '%saccounts/register/' % ROOT_URL#registration_register

CTX_CONFIG = {
        'LBFORUM_TITLE': 'LBForum',
        'LBFORUM_SUB_TITLE': 'A forum engine written in Python using Django',
        'FORUM_PAGE_SIZE': 50,
        'TOPIC_PAGE_SIZE': 20,

        #URLS....
        'LBFORUM_MEDIA_PREFIX': LBFORUM_MEDIA_PREFIX,
        'LOGIN_URL': LOGIN_URL,
        'LOGOUT_URL': LOGOUT_URL,
        'REGISTER_URL': REGISTER_URL,
        }

BBCODE_AUTO_URLS = True
#HTML safe filter
HTML_SAFE_TAGS = ['embed']
HTML_SAFE_ATTRS = ['allowscriptaccess', 'allowfullscreen', 'wmode']
HTML_UNSAFE_TAGS = []
HTML_UNSAFE_ATTRS = []
"""
#default html safe settings 
acceptable_elements = ['a', 'abbr', 'acronym', 'address', 'area', 'b', 'big',
      'blockquote', 'br', 'button', 'caption', 'center', 'cite', 'code', 'col',
      'colgroup', 'dd', 'del', 'dfn', 'dir', 'div', 'dl', 'dt', 'em',
      'font', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'hr', 'i', 'img', 
      'ins', 'kbd', 'label', 'legend', 'li', 'map', 'menu', 'ol', 
      'p', 'pre', 'q', 's', 'samp', 'small', 'span', 'strike',
      'strong', 'sub', 'sup', 'table', 'tbody', 'td', 'tfoot', 'th',
      'thead', 'tr', 'tt', 'u', 'ul', 'var']

acceptable_attributes = ['abbr', 'accept', 'accept-charset', 'accesskey',
  'action', 'align', 'alt', 'axis', 'border', 'cellpadding', 'cellspacing',
  'char', 'charoff', 'charset', 'checked', 'cite', 'clear', 'cols',
  'colspan', 'color', 'compact', 'coords', 'datetime', 'dir', 
  'enctype', 'for', 'headers', 'height', 'href', 'hreflang', 'hspace',
  'id', 'ismap', 'label', 'lang', 'longdesc', 'maxlength', 'method',
  'multiple', 'name', 'nohref', 'noshade', 'nowrap', 'prompt', 
  'rel', 'rev', 'rows', 'rowspan', 'rules', 'scope', 'shape', 'size',
  'span', 'src', 'start', 'summary', 'tabindex', 'target', 'title', 'type',
  'usemap', 'valign', 'value', 'vspace', 'width', 'style']
"""

#TODO add a config model
try:
    from local_settings import *
    CTX_CONFIG.update(CTX_CONFIG_)
except Exception, e:
    pass
