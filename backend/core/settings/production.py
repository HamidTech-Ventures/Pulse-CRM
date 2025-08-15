from .base import *  # noqa

DEBUG = False
ALLOWED_HOSTS = env('ALLOWED_HOSTS')

# Database
DATABASE_URL = env('DATABASE_URL')
import dj_database_url  # type: ignore
DATABASES = {
    'default': dj_database_url.parse(DATABASE_URL, conn_max_age=600),
}

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = env.bool('SECURE_SSL_REDIRECT', default=True)
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = env.int('SECURE_HSTS_SECONDS', default=3600)
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

CORS_ALLOW_ALL_ORIGINS = False