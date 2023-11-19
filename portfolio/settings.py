from pathlib import Path
import environ
import os
import dj_database_url
# import firebase_admin
# from firebase_admin import credentials,storage

env=environ.Env()
environ.Env.read_env()


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Use the downloaded JSON file with your Firebase Admin SDK credentials
# service_account=env('SERVICE_ACCOUNT')
# firebase_storage=env('FIREBASE_STORAGE')

# cred = credentials.Certificate(os.path.join(BASE_DIR,service_account))
# firebase_admin.initialize_app(cred, {'storageBucket':firebase_storage},name='media_upload_app')

# # Configure the storage bucket
# FIREBASE_BUCKET = storage.bucket(app=firebase_admin.get_app(name='media_upload_app'))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY =env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
if DEBUG:
    ALLOWED_HOSTS = ['localhost','127.0.0.1','devme-c78b91affa17.herokuapp.com','www.devme-c78b91affa17.herokuapp.com']
else:
    ALLOWED_HOSTS = ['localhost','127.0.0.1','devme-c78b91affa17.herokuapp.com','www.devme-c78b91affa17.herokuapp.com']

SITE_ID=2
AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]
# Application definition

INSTALLED_APPS = [
    'whitenoise.runserver_nostatic',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    # 'storages',
    'django.contrib.staticfiles',
    'installation.apps.InstallationConfig',
    'django.contrib.humanize',
    'phonenumber_field',
    'mathfilters',
    'rest_framework',
    'errors.apps.ErrorsConfig',
    'manager.apps.ManagerConfig',
    'django.contrib.sites', #social app 
    'allauth', #social app
    'allauth.account', #social app
    'allauth.socialaccount', #social app
    'notifications.apps.NotificationsConfig',
    'allauth.socialaccount.providers.google', #social app
    'allauth.socialaccount.providers.twitter', #social app
    'allauth.socialaccount.providers.github', #social app
    'django_cleanup.apps.CleanupConfig',
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'portfolio.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'portfolio.site_constants.export_vars',
            ],
        },
    },
]


WSGI_APPLICATION = 'portfolio.wsgi.application'
ASGI_APPLICATION = 'portfolio.asgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

db_name=env('AWS_DATABASE_NAME')
db_user=env('AWS_DATABASE_USER')
db_password=env('AWS_DATABASE_PASSWORD')
db_host=env('AWS_DATABASE_HOST')
db_port=env('AWS_DATABASE_PORT')

if DEBUG:

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
   
    
    # DATABASES = {
    #     'default': {

    #         'ENGINE': 'django.db.backends.postgresql',
    #         'NAME':db_name,
    #         'USER':db_user,
    #         'PASSWORD':db_password,
    #         'HOST':db_host,
    #         'PORT':db_port,
    #     }
    # }
    
else:
	# DATABASES = {
    #     'default': dj_database_url.config(
    #         default=env('DATABASE_URL'),
    #         conn_max_age=600, 
    #     )
	# }
 
    DATABASES = {
        'default': {

            'ENGINE': 'django.db.backends.postgresql',
            'NAME':db_name,
            'USER':db_user,
            'PASSWORD':db_password,
            'HOST':db_host,
            'PORT':db_port,
        }
    }




# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS':
        {
            'min_length':6,
        },
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
    {
        'NAME':'manager.validators.NumberValidator',
        'OPTIONS':
        {
            'min_length':2,
        },
    },
    #{
    #    'NAME':'manager.validators.UpperCaseValidator',
    #},
    {
        'NAME':'manager.validators.LowerCaseValidator',
    },
]


#login
LOGIN_URL='/accounts/login'
LOGIN_REDIRECT_URL='/dashboard'
LOGOUT_REDIRECT_URL='/accounts/login'
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL='/media/'

#STATICFILES_STORAGE='whitenoise.storage.CompressedManifestStaticFilesStorage'
# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

if DEBUG:
    STATICFILES_DIRS=[os.path.join(BASE_DIR,'static')]
else:
    STATIC_ROOT=os.path.join(BASE_DIR,'static')


MEDIA_ROOT=os.path.join(BASE_DIR,'media')


BASE_URL=env('BASE_URL')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


email_host=env('EMAIL_HOST')
email_user=env('EMAIL_USER')
email_password=env('EMAIL_PASSWORD')
email_port=env('EMAIL_PORT')


EMAIL_HOST=email_host
EMAIL_HOST_USER=email_user
EMAIL_HOST_PASSWORD=email_password
EMAIL_USE_TLS=True
EMAIL_PORT=email_port
DEFAULT_FROM_EMAIL=EMAIL_HOST_USER


#SESSION_ENGINE='django.contrib.sessions.backends.cache'
SESSION_CACHE_ALIAS='default'
CACHE_TTL = 60 * 45

#cache
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        #"LOCATION": os.environ.get('REDIS_URL','redis-12648.c263.us-east-1-2.ec2.cloud.redislabs.com:12648'),
        "LOCATION":"redis://default:KevyKibbz@redis-12648.c263.us-east-1-2.ec2.cloud.redislabs.com:12648/studirre",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

