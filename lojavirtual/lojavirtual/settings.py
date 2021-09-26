"""
Django settings for lojavirtual project.

Generated by 'django-admin startproject' using Django 3.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
#BASE_DIR = Path(__file__).resolve().parent.parent
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-u$x)p0_-69!jbg_&n-@du3kns@b*rm$tiye^(d)%y&cwwffj&6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'main.apps.MainConfig',
    'carrinho.apps.CarrinhoConfig',
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

ROOT_URLCONF = 'lojavirtual.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug', #guarda as variáveis booleana debug e sql_queries
                'django.template.context_processors.request', #guarda a requisição no contexto, permitindo que o objeto de request seja acessado em qualquer lugar da aplicação
                'django.contrib.auth.context_processors.auth', #guarda a variável user
                'django.contrib.messages.context_processors.messages', #guarda uma variavel messages no contexto, gerenciando as mensagens dos usuários
                'carrinho.context_processors.carrinho',
            ],
        },
    },
]

TEMPLATE_DIRS=(
    os.path.join(BASE_DIR, 'templates'),
    )

WSGI_APPLICATION = 'lojavirtual.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        #'NAME': BASE_DIR / 'db.sqlite3',
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
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_DIRS=(
    os.path.join(BASE_DIR,'static'),
    ) #armazenando arquivos estaticos
STATIC_ROOT=os.path.join(BASE_DIR, 'staticfiles') #arquivos estaticos do projeto no momento de distribuir a aplicacao para um webserver

LOGGING={
    'version':1,
    'disable_existing_loggers': False,
    'formatters':{
        'simple':{
            'format': 'Mensagem: %(levelname)s%(message)s'
        },
    },
    'handlers':{
        'console':{
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
    },
    'loggers':{
        'lojavirtual':{
            'handlers':['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

EMAIL_FALE_CONOSCO='email@teste.com.br' #constante para especificar o endereço de email que receberá os emails da aplicação
EMAIL_BACKEND='django.core.mail.backends.console.EmailBackend' #classe que gerencia os emails da aplicação

#Em produção é praxe usar um servidor web para entregar conteúdos estáticos
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'imagens-produtos')

ID_CARRINHO = 'carrinho' #identificador da sessão