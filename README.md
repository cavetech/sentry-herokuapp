# Sentry on Heroku

This is a starting point for running
[Sentry](https://github.com/getsentry/sentry "Sentry") on
[Heroku](https://www.heroku.com/ "Heroku").

## Instructions

```bash
$ git clone https://github.com/grosskur/sentry-herokuapp.git
$ cd sentry-herokuapp
$ heroku create your-sentry
$ heroku addons:add heroku-postgresql:dev
$ heroku pg:promote $(heroku config -s | awk -F= '$1 ~ /^HEROKU_POSTGRESQL_[A-Z]+_URL$/ {print $1}')
$ heroku run sentry --config=sentry.conf.py migrate
$ git push heroku master
```

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
