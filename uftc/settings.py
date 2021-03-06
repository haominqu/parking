"""
Django settings for uftc project.

Generated by 'django-admin startproject' using Django 1.11.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2paj^l#lgg&l4e6(i(8!q^4!xx-fp!g*(-@t3w%&hnl3)fei(w'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

from corsheaders.defaults import default_headers
CORS_ALLOW_HEADERS = default_headers + (
'Content-Type',
)
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'userinfo',
    'parking',
    'pay',
    'backend',
    'parkbackend',
    'corsheaders',
    'rest_framework',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'uftc.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'uftc.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'uftc_db',
        'USER': 'root',
        'HOST': 'localhost',
        'POST': 3306,
        'PASSWORD': '123456',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

# STATIC_ROOT = os.path.join(BASE_DIR, "collected static")
#
# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, 'static'),
# )

MEDIA_ROOT = os.path.join(BASE_DIR, '').replace('\\', '/')
MEDIA_URL = '/'

AUTH_USER_MODEL = 'userinfo.AdminInfo'


from datetime import datetime, timedelta
SECRET_KEY = "quscsacascascashmxiaobao"

JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': timedelta(seconds=36000),
    'JWT_REFRESH_EXPIRATION_DELTA': timedelta(days=1),
    'JWT_SECRET_KEY' :"quhmxiaobao",
    'JWT_SECRET_KEY': SECRET_KEY,

}

# import logging
# import django.utils.log
# import logging.handlers
#
# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': True,
#     'formatters': {
#         'standard': {
#             'format': '%(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] [%(module)s:%(funcName)s] [%(levelname)s]- %(message)s'}
#     # 日志格式
#     },
#     'filters': {
#     },
#     'handlers': {
#         'mail_admins': {
#             'level': 'ERROR',
#             'class': 'django.utils.log.AdminEmailHandler',
#             'include_html': True,
#         },
#         'default': {
#             'level': 'DEBUG',
#             'class': 'logging.handlers.RotatingFileHandler',
#             'filename': './sourceDns/log/all.log',  # 日志输出文件
#             'maxBytes': 1024 * 1024 * 5,  # 文件大小
#             'backupCount': 5,  # 备份份数
#             'formatter': 'standard',  # 使用哪种formatters日志格式
#         },
#         'error': {
#             'level': 'ERROR',
#             'class': 'logging.handlers.RotatingFileHandler',
#             'filename': './sourceDns/log/error.log',
#             'maxBytes': 1024 * 1024 * 5,
#             'backupCount': 5,
#             'formatter': 'standard',
#         },
#         'console': {
#             'level': 'DEBUG',
#             'class': 'logging.StreamHandler',
#             'formatter': 'standard'
#         },
#         'request_handler': {
#             'level': 'DEBUG',
#             'class': 'logging.handlers.RotatingFileHandler',
#             'filename': './sourceDns/log/script.log',
#             'maxBytes': 1024 * 1024 * 5,
#             'backupCount': 5,
#             'formatter': 'standard',
#         },
#         'scprits_handler': {
#             'level': 'DEBUG',
#             'class': 'logging.handlers.RotatingFileHandler',
#             'filename': './sourceDns/log/script.log',
#             'maxBytes': 1024 * 1024 * 5,
#             'backupCount': 5,
#             'formatter': 'standard',
#         }
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['default', 'console'],
#             'level': 'DEBUG',
#             'propagate': False
#         },
#         'django.request': {
#             'handlers': ['request_handler'],
#             'level': 'DEBUG',
#             'propagate': False,
#         },
#         'scripts': {
#             'handlers': ['scprits_handler'],
#             'level': 'INFO',
#             'propagate': False
#         },
#         'sourceDns.webdns.views': {
#             'handlers': ['default', 'error'],
#             'level': 'DEBUG',
#             'propagate': True
#         },
#         'sourceDns.webdns.util': {
#             'handlers': ['error'],
#             'level': 'ERROR',
#             'propagate': True
#         }
#     }
# }

BAIDUAK = 'GqohPozNne3cPFtPhkEu0KM4urYPZlTF'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "collected_static")

STATICFILES_DIRS = (
        os.path.join(BASE_DIR,'static'),
)


# alipayhm
ALIPAY_APP = {
    'ALIPAY_APP_ID': '2018080360972019',
    'ALIPAY_APP_PRIVATE_KEY': 'MIIEpQIBAAKCAQEAwBMs45iyxcIVC3kYAFnjCpWCjN1N0wiYXE2WWmQsK69VMfP5Xd0wUHxOqX2+LcSDJhrJPF9/0/LO5kc5OKsS5wOY9GAFSA7RxQ4KwG6LbzIkuxQPzEJLXHI5ZahKpMz3korEdAWz/aWXQXJRz7rHR2PQ07Rpxh4tF8Gm47BKs4tm8iKGK1dD75GAGY1gMJdXI7hbEOUyQvAPtm4BTQjm6Uvu9NFT+biKf47xRt+ibrFyQTl/KTcRyl4XKe1pafsA2FYeL31yazgqw+lRTyu2AYFWqAmmYHfAzw8cthD1MBIfeJwPV2MYiBmU2QUe45TUWJtb/ovJ4cVGZTt4gvwaDwIDAQABAoIBAHu5HlYw2x8lqHaudvZq8CO2MNTaDLJeO/5g//OTyRwOobs+o6eBvghqOiVVWPaUOcKGyI96GJYHNp0Azewhzlg+af0oCN7kpNzg8a4IxwpGa4CSKKbzISYYcb54zDQhz2t2tZrivZEqZCcFI4vCjXD/69kiwmuaroM5+2149nV1vHT2CQd+gMLQryfW1O4dqHlt0itB8NP+HWPO4c4SazL/M7evlXKmkYOlVk3aWo295nwBvkYoC4pHv/sNPEyn2dS14E0kWEo6mOQN5HfgaJyk9KwdwdfKkOpY8U8vVpdXSTzLoOIZ+ITOOfRy+Dj+AS8yaD+MInFUsXLFy6k1upECgYEA8oXfbLZyTUT30FZGTk727+bD5PE1HNRZeRGQcaobml4WIWr6ahLhDxDtpGRU+OIY1fJ/USmK2PGjaN+tGXQXwoLJGgO4UcCR04LbwgPUv7/7XOgMQn3qmZjYIf/MUJnVD+i4cvo97d4FzjCKsdUgINC28RcWMznlIaUg5ZBjCTcCgYEAyr+hMpbpSrVJ77+/kqekqzxDBoetDRT9dxer0Z8ISgGlxJH2tRr81itd7vlBDwbgvJsifogmzjfHFJzHDPIb1/9bLLKodzFwdz6u5P0khFoS5kV1y4ZZT+i7wDvzC2ILc8ETnGCrW4NHsvg6mjLVZl5o2dGMDOL1S/ug4yJsgekCgYEAjjdA6IAokPUzmOEuwzb9CXs6PqPPsIM5oIxTNsQ5AZHQynHwPImrnmkf4fnP9k6nn7ZfQJnqyQMR/yrDWBzC3hZRlUa/LHmPSgf/lEso0/Thkv6kSc2K591ASNe22UEMNxMSLqJd9IHwx5OhkVzYRUX/MWuHYiy+F7e8jcHYwYsCgYEAnOT7/iUQNVLi+1ecDQYUBLqmd3gorzXuCunTeWyiwnpR6DK4Al/3Blka4KIb+V/uK6W1ZMtBlFVPhqDn3BnC+DxQNt+uREaK7IwiVWubhZwagf2AcVXu6UqFd/YsV0Ow7wubfGjGUhPeOR2kY80wnH40j1J8GUDMZ9c6ImpyI3kCgYEAkDC+6l014MHpiZK1wr/qqv1r6LnFN4oi/EO4qKgxV+7aLk43egsTg8ChBhzj78Cfl4HpMHbJRprOghrnmnDOT6fK9GjLgQkBAXxymCpqaEbSqgrhrMFqraRGB/P/K1Ep3onpqh6hAFrT4RM+2oUtsW00w8292E4N6DWMgC88g6k=',
    'ALIPAY_ALI_PUBLIC_KEY': 'MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEA7PV8NWNEeZTX7/ZSFWUe+iwv8WwDnEY1PFLA8mY0D1q5uANY7yJlpcKflCgYS61Gze85q9S2ZY48rkV1gSFjm5YSAOc2v+gnznYJiNau7VsD6xWE6fccCrMgZwSb9PqacAenjt7sxcpP86GfqfkDohVf1ZXGy3v3nn+rSnWS8cfKbBODyMdcKObYZ+3wQnKf2cwE5i1w8J4jyabXZMMH8TJ/MiH1s9OvCAjZNBqGq6pUGAXOuwu/UMUMCRJZodMr8bwWbhwcLd4MxKkjIkX2ClXyH+Tsnc+jQ3tCMdRlvAIcWDShr/E3g/zRmsdKHX2SHlg0dWV/Mgi0F3uwIDaBMwIDAQAB',
    'ALIPAY_TIMEOUT_EXPRESS': '90m',
    'ALIPAY_NOTIFY_URL': 'http://39.106.16.34:8080/api/pay/confirmcharge/',
}

# wxpayhm
WX_APP = {
    'WX_APP_ID': 'wxe950bea6bf500e6b',
    'WX_MCH_ID': '1523323611',
    'WX_NOTIFY_URL': '',
    'WX_SELF_KEY':'',
}
