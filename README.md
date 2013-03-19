# ChromeFiddle

A site to track experimental settings for Google's Chrome browser.

## Pip

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

## Django

Run development web server
```
$ python manage.py runserver <IP>:<PORT>
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

Dump all Flag objects to JSON file
```
$ python manage.py dumpdata flags  > fixtures/flags_list.json
```

Collect static files to static directory
```
$ python manage.py collectstatic
```

## Provisioning vanilla Ubuntu server

Use the scripts in my [ubuntu-setup](https://github.com/peterfschaadt/ubuntu-setup) repository to prepare server for [Chef](http://www.opscode.com/chef) configuration and dependency management.

## Fabric

+ **setup** = apt-get update/upgrade, install Python tools, Git, and Nginx, reset_permissions
+ **_virtualenv** = activate virtual environment
+ **create_virtualenv** = creates virtual environment
+ **remove_pyc_files** = remove compiled Python files
+ **restart_gunicorn_nginx** = restart Gunicorn and Nginx servers
+ **start_gunicorn** / **restart_gunicorn**
+ **start_nginx** / **restart_nginx**
+ **update_project** = git pull, install_requirements, perform_migration, collect_static
+ **deploy** = update_project, restart_gunicorn_nginx
+ **install_requirements** = install pip requirements from requirements.txt
+ **perform_migration** = perform database migration with South
+ **collect_static** = collect static files
+ **test** = run test suite
+ **dump_db_json** = Dump backup of database to JSON
+ **reset_permissions** = reset permissions
+ **find_todo** = find all TODO references in source code

## PostgreSQL

Run PostgreSQL shell
```
$ psql -U <POSTGRES_USER>
```

Create database
```
$ createdb -U <POSTGRES_USER> -E utf8 -O <POSTGRES_USER> <POSTGRES_DB_NAME> -T template0
```

Connect to database
```
$ psql -d chromefiddle_prod -U django
```

Start PostgreSQL process (for Mac development only)
```
$ lunchy start postgres
```

Stop PostgreSQL process
```
$ lunchy stop postgres
```
