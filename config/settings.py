"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 4.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

import os
from pathlib import Path
from dotenv import load_dotenv

#dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
#load_dotenv(dotenv_path)
load_dotenv(override=True)
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = str(os.getenv('SECRET_KEY'))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv('DEBUG', 'False').lower() in ('true', '1', 't')
#PRODUCTION = os.getenv('PRODUCTION', 'False').lower() in ('true', '1', 't')

ALLOWED_HOSTS = [str(os.getenv('ALLOWED_HOSTS'))]

# Application definition

INSTALLED_APPS = [
    'data_support',
    'account',
    'dashboard',
    'landing',
    'koordinator',
    'klerus',
    'parokia',
    'member',
    'baptis',
    'nikah',
    'imagekit',
    #'django_crontab',
    #'django_google_maps',
    'wagtail.contrib.forms',
    'wagtail.contrib.redirects',
    'wagtail.embeds',
    'wagtail.sites',
    'wagtail.users',
    'wagtail.snippets',
    'wagtail.documents',
    'wagtail.images',
    'wagtail.search',
    'wagtail.admin',
    'wagtail',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'dbbackup',
    'modelcluster',
    'taggit',
    'wagtailgeowidget',
    'wagtail_modeladmin',
    'axes',
]

DBBACKUP_STORAGE = 'django.core.files.storage.FileSystemStorage'
DBBACKUP_STORAGE_OPTIONS = {'location': BASE_DIR / 'backup'}

AUTHENTICATION_BACKENDS = [
    # AxesStandaloneBackend should be the first backend in the AUTHENTICATION_BACKENDS list.
    'axes.backends.AxesStandaloneBackend',

    # Django ModelBackend is the default authentication backend.
    'django.contrib.auth.backends.ModelBackend',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

MIDDLEWARE += ['wagtail.contrib.redirects.middleware.RedirectMiddleware']
MIDDLEWARE += ('crum.CurrentRequestUserMiddleware',)
MIDDLEWARE += ('axes.middleware.AxesMiddleware',)

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, "templates"),
            ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': str(os.getenv('ENGINE')),
        'NAME': str(os.getenv('NAME')),
        'USER': str(os.getenv('DBUSER')),
        'PASSWORD': str(os.getenv('DBPASSWORD')),
        'HOST': str(os.getenv('DBHOST')),
        'PORT': str(os.getenv('DBPORT')),
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'id-id'

TIME_ZONE = 'Asia/Jakarta'

USE_I18N = True

USE_TZ = True

AUTH_USER_MODEL = 'account.User'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
#STATIC_ROOT = 'static/'
# Upload File
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = 'media/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# MAP
GOOGLE_MAPS_API_KEY = str(os.getenv(('GOOGLE_MAPS_API_KEY')))
MAPS_CENTER = 'lat: -1.233982000061532, lng: 116.83728437200422'

# Upload File
#MEDIA_URL = 'media/'
#MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
WAGTAIL_USER_EDIT_FORM = 'account.forms.CustomUserEditForm'
WAGTAIL_USER_CREATION_FORM = 'account.forms.CustomUserCreationForm'
WAGTAIL_USER_CUSTOM_FIELDS = ['parokia', 'komox']

WAGTAIL_SITE_NAME = 'Gereja Orthodox Indonesia'
#WAGTAILADMIN_BASE_URL = str(os.getenv('WAGTAILADMIN_BASE_URL', 'http://localhost:8001'))
WAGTAILADMIN_BASE_URL = str(os.getenv('WAGTAILADMIN_BASE_URL', 'https://data.gerejaorthodox.id'))

# Only Django 4.0
CSRF_TRUSTED_ORIGINS = ['https://*.gerejaorthodox.id', 'http://127.0.0.1:8000', 'http://localhost:8000']

# Conjob
#CRONJOBS = [
#    ('0 0 * * *', 'config.cron.dbbackup_job')
#]

# MAP
GOOGLE_MAPS_V3_APIKEY = str(os.getenv('GOOGLE_MAPS_V3_APIKEY'))
GOOGLE_MAPS_V3_LANGUAGE = 'id'
GEO_WIDGET_ZOOM = int(os.getenv('GEO_WIDGET_ZOOM', 15))
GEO_WIDGET_DEFAULT_LOCATION = {'lat': -6.268851912051042, 'lng': 106.65501443906547}

# AXES
AXES_COOLOFF_TIME = float(os.getenv('AXES_COOLOFF_TIME', 2))
AXES_RESET_ON_SUCCESS = True
#AXES_LOCKOUT_PARAMETERS = ['ip_address', 'username']
AXES_LOCKOUT_PARAMETERS = ['username']
AXES_LOCKOUT_TEMPLATE = 'axes/block.html'
AXES_IPWARE_PROXY_COUNT = int(os.getenv('AXES_IPWARE_PROXY_COUNT', 0))

