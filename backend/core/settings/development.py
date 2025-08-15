from .base import *  # noqa

# Database
DATABASES = {}
DATABASE_URL = env('DATABASE_URL', default='')
if DATABASE_URL:
    import dj_database_url  # type: ignore
    DATABASES['default'] = dj_database_url.parse(DATABASE_URL, conn_max_age=600)
else:
    DATABASES['default'] = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }

# Dev specific
DEBUG = True
ALLOWED_HOSTS = ['*']
CORS_ALLOW_ALL_ORIGINS = True