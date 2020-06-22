"""Local file local enviroment."""
from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('DATABASE_NAME_1'),
        'USER': os.getenv('DATABASE_USER_1'),
        'PASSWORD': os.getenv('DATABASE_PASSWORD_1'),
        'HOST': os.getenv('DATABASE_HOST_1'),
        'PORT': os.getenv('DATABASE_PORT_1'),
    },
    'data1_db': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('DATABASE_NAME_2'),
        'USER': os.getenv('DATABASE_USER_2'),
        'PASSWORD': os.getenv('DATABASE_PASSWORD_2'),
        'HOST': os.getenv('DATABASE_HOST_2'),
        'PORT': os.getenv('DATABASE_PORT_2'),
    },
    'data2_db': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('DATABASE_NAME_3'),
        'HOSTNAME': os.getenv('DATABASE_HOST_3'),
        'USER': os.getenv('DATABASE_USER_3'),
        'PASSWORD': os.getenv('DATABASE_PASSWORD_3'),
        'OPTIONS': {
            'autocommit': True,
        }
    },
    'data3_db': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('DATABASE_NAME_4'),
        'HOSTNAME': os.getenv('DATABASE_HOST_4'),
        'USER': os.getenv('DATABASE_USER_4'),
        'PASSWORD': os.getenv('DATABASE_PASSWORD_4'),
        'OPTIONS': {
            'autocommit': True,
        }
    },
    'data4_db': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('DATABASE_NAME_5'),
        'HOSTNAME': os.getenv('DATABASE_HOST_5'),
        'USER': os.getenv('DATABASE_USER_5'),
        'PASSWORD': os.getenv('DATABASE_PASSWORD_5'),
        'OPTIONS': {
            'autocommit': True,
        }
    },
}
