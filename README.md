# ChromeFiddle

## A site to track experimental settings for Google's Chrome browser.

View installed and available versions of pip packages with [pip-tools](https://github.com/nvie/pip-tools)
```
$ pip-review
```

Update pip packages interactively
```
$ pip-review --interactive
```

Backup list of environment's installed pip packages to requirements.txt
```
$ pip-dump
```

Run development web server
```
$ python manage.py runserver
```

Run interactive Django shell
```
$ python manage.py shell
```

Create Django database schema
```
$ python manage.py syncdb
```

Save schema with [South](http://south.aeracode.org/)
```
$ python manage.py schemamigration flags --auto
```

Apply schema migration
```
$ python manage.py migrate flags
```
