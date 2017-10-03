import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
SITE_ROOT = os.path.abspath(os.path.dirname(__file__))
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join( SITE_ROOT, 'static')
SITE_STATIC_ROOT = os.path.join( SITE_ROOT, 'local_static')
STATICFILES_DIRS = (    ('', SITE_STATIC_ROOT),)

SECRET_KEY = '$v_ret!^a=4_+)y*n_^k%7b(@8gq7*e1$5+pdyd+l-rfi%g$wu'
DEBUG = True
ALLOWED_HOSTS = []

EMAIL_HOST = ''
EMAIL_PORT = 25
EMAIL_SUBJECT_PREFIX = ''

INSTALLED_APPS = (
  'django.contrib.admin',
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.messages',
  'django.contrib.staticfiles',
  'account',
  'main',
  'cart',
  'sorl.thumbnail',
)
MIDDLEWARE_CLASSES = (
  'django.contrib.sessions.middleware.SessionMiddleware',
  'django.middleware.common.CommonMiddleware',
  'django.middleware.csrf.CsrfViewMiddleware',
  'django.contrib.auth.middleware.AuthenticationMiddleware',
  'django.contrib.auth.middleware.RemoteUserMiddleware',
  'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
  'django.contrib.messages.middleware.MessageMiddleware',
  'django.middleware.clickjacking.XFrameOptionsMiddleware',
  'django.middleware.security.SecurityMiddleware',
)
ROOT_URLCONF = 'u-sport.urls'

THUMBNAIL_DEBUG = True

TEMPLATES = [    
  {
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [],
    #'APP_DIRS': True,
    'OPTIONS': {
      'context_processors': [
        'django.template.context_processors.debug',
        'django.template.context_processors.request',
        'django.contrib.auth.context_processors.auth',
        'django.contrib.messages.context_processors.messages',
      ],
      'loaders':[
        #'admin_tools.template_loaders.Loader',
        #'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
      ],
    },
  },
]

WSGI_APPLICATION = 'u-sport.wsgi.application'
AUTH_USER_MODEL = 'account.User' 

AUTHENTICATION_BACKENDS = (
  'django.contrib.auth.backends.RemoteUserBackend',
  'django.contrib.auth.backends.ModelBackend', 
)
DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': 'u-sport',
    'USER': 'postgres',
    'PASSWORD': '1111',
    'HOST': '',# Set to empty string for localhost.    
    'PORT': '', # Set to empty string for default.    
  }
}

DATETIME_FORMAT = 'd F Y l'
DATE_FORMAT = 'd F Y l'
FIRST_DAY_OF_WEEK = '1'
DATE_INPUT_FORMATS = ('%d %m %Y',)

LANGUAGE_CODE = 'ru'
LOCALE_PATHS = (    'main/locale',)

#TIME_ZONE = 'UTC+3'
USE_I18N = True
#USE_L10N = True
USE_TZ = True
