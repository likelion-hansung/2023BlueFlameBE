# 배포 서버
from .base import *

# DEBUG = True

DEBUG = False

ALLOWED_HOSTS = ['3.39.71.133']

DJANGO_APPS += []
    
PROJECT_APPS += []
    
THIRD_PARTY_APPS += []
    
INSTALLED_APPS = DJANGO_APPS + PROJECT_APPS + THIRD_PARTY_APPS

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_ROOT = [
    BASE_DIR / 'static' 
]