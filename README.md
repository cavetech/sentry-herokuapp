# Sentry on Heroku

This is a starting point for running
[Sentry](https://github.com/getsentry/sentry "Sentry") on
[Heroku](https://www.heroku.com/ "Heroku").

## Features

* Automatic database configuration via
  [dj-database-url](https://github.com/kennethreitz/dj-database-url "dj-database-url")
* SENTRY_KEY set via environment variable
* Emails stored in database via
  [django-database-email-backend](https://github.com/stefanfoulis/django-database-email-backend "django-database-email-backend")

## To do

* Support static assets on S3
* Support Twitter/Facebook/Google/GitHub/Trello credentials for OAuth
* Support caching with memcached
* Support queuing with a Celery broker
* Support buffering with Redis
