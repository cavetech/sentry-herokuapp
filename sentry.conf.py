import os

import dj_database_url


CONF_ROOT = os.path.dirname(__file__)

DATABASES = {
    'default': dj_database_url.config(),
}

# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
#         'LOCATION': ['127.0.0.1:11211'],
#     }
# }

# SENTRY_USE_QUEUE = True
# BROKER_URL = 'redis://localhost:6379'

# SENTRY_BUFFER = 'sentry.buffer.redis.RedisBuffer'
# SENTRY_BUFFER_OPTIONS = {
#     'hosts': {
#         0: {
#             'host': '127.0.0.1',
#             'port': 6379,
#         }
#     }
# }

SENTRY_KEY = os.getenv('SENTRY_KEY')

# Set this to false to require authentication
SENTRY_PUBLIC = False

# SENTRY_URL_PREFIX = 'http://sentry.example.com'  # No trailing slash!

SENTRY_WEB_HOST = '0.0.0.0'
SENTRY_WEB_PORT = os.getenv('PORT')
SENTRY_WEB_OPTIONS = {
    'workers': 3,
}

ALLOWED_HOSTS = [
    '.herokuapp.com',
]

# Mail server configuration
EMAIL_BACKEND = 'database_email_backend.backend.DatabaseEmailBackend'

# http://twitter.com/apps/new
TWITTER_CONSUMER_KEY = ''
TWITTER_CONSUMER_SECRET = ''

# http://developers.facebook.com/setup/
FACEBOOK_APP_ID = ''
FACEBOOK_API_SECRET = ''

# http://code.google.com/apis/accounts/docs/OAuth2.html#Registering
GOOGLE_OAUTH2_CLIENT_ID = ''
GOOGLE_OAUTH2_CLIENT_SECRET = ''

# https://github.com/settings/applications/new
GITHUB_APP_ID = ''
GITHUB_API_SECRET = ''

# https://trello.com/1/appKey/generate
TRELLO_API_KEY = ''
TRELLO_API_SECRET = ''
