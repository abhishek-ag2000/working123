"""
Django settings for src project.

Generated by 'django-admin startproject' using Django 2.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
TEMPLATE_DIR = os.path.join(BASE_DIR,'templates')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'jdc#ewbwngw0nbdxj6il05f2pdbr75fhjni@j_ut+o2ev8(fm$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["www.bracketline.com","35.200.221.172","bracketline.com"]

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY ='954744097986-2c65ubrgiggh2nbb532es23go3a30s8c.apps.googleusercontent.com'  #Paste CLient Key
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'TBPj7U1_ieD5Ge8YKslwqeFj'

SOCIAL_AUTH_FACEBOOK_KEY = '837109483127908'
SOCIAL_AUTH_FACEBOOK_SECRET = '82c10c3f0e510e88aa285bccb9f69b6a'

CSRF_FAILURE_VIEW = 'ecommerce_integration.views.csrf_failure'


# Application definition

INSTALLED_APPS = [
########## Third Party Apps ###########

    'social_django',                            #pip install social-auth-app-django
    'bootstrap3',                               #pip install django-bootstrap3
    "sslserver",                                #pip install django-sslserver
    'crispy_forms',                             #pip install --upgrade django-crispy-forms
    'bootstrap_datepicker_plus',                #pip install django-bootstrap-datepicker-plus
    'mathfilters',                              #pip install django-mathfilters
    'pagedown',                                 #pip install django-pagedown                               
    'ckeditor',                                 #pip install django-ckeditor
    'ckeditor_uploader',                        #pip install django-ckeditor
    'sorl.thumbnail',                           #pip install sorl-thumbnail
    'import_export',                            #pip install django-import-export
    'django_celery_beat',                       #pip install django-celery-beat
    'django_celery_results',                    #pip install django-celery-results
    'star_ratings',                             #pip install django-star-ratings

    # argon2 = pip install django[argon2]
    # bcrypt = pip install bcrypt
    # pillow = pip install pillow
    # xhtml2pdf = pip install --pre xhtml2pdf
    # pip install social-auth-app-django
    # pip install sorl-thumbnail



######### Django Inbuild Apps ########

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize', 

######### My Apps ##############  
  
    'accounts',
    'company',
    'accounting_double_entry',
    'todogst',
    'userprofile',
    'blog',
    'consultancy',
    'stockkeeping',
    'pdf',
    'ecommerce_integration',
    'ecommerce_cart',
    'messaging',
    'Gst',
    'aggrement',
    'company_accounts',
    'helpandsupport',

]

IMPORT_EXPORT_USE_TRANSACTIONS = True

CKEDITOR_UPLOAD_PATH = "uploads/"

CKEDITOR_CONFIGS = {
    'special': {
        'toolbar': 'Special',
        'width' : 'auto',
        'toolbar_Special': [
            ['Styles', 'Format', 'Bold', 'Italic', 'Underline', 'Strike', 'SpellChecker', 'Undo'],
            ['Link', 'Unlink', 'Anchor'],
            ['Image', 'Flash', 'Table', 'HorizontalRule'],
            ['TextColor', 'BGColor'],
            ['Smiley', 'SpecialChar'], ['Source'],
        ],
        
    }
}



EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # During development only


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'src.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR,],
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

AUTHENTICATION_BACKENDS = (
 'social_core.backends.open_id.OpenIdAuth',  # for Google authentication
 'social_core.backends.google.GoogleOpenId',  # for Google authentication
 'social_core.backends.google.GoogleOAuth2',  # for Google authentication
 'social_core.backends.facebook.FacebookOAuth2',  # for Facebook authentication
 
 'django.contrib.auth.backends.ModelBackend',
)


WSGI_APPLICATION = 'src.wsgi.application'


from django.contrib.messages import constants as messages

MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
]


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = TIME_ZONE

CRISPY_TEMPLATE_PACK = 'bootstrap4'

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static-root")



MEDIA_URL = '/media/'

MEDIA_DIR = os.path.join(BASE_DIR,'media')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "media-root")


LOGIN_URL = 'login'
LOGOUT_URL = 'logout'
LOGIN_REDIRECT_URL = "ecommerce_integration:productlist"
LOGOUT_REDIRECT_URL = "home"
