from fabric.api import cd, env, prefix, run, sudo, local, settings
from contextlib import contextmanager

__author__ = 'Peter Schaadt'
__repository__ = 'https://github.com/peterfschaadt/chromefiddle.git'

# User/host
env.user = 'django'
env.host = ['198.144.185.175']

# Paths
env.root_dir = '/web'
env.virtualenv = '%s/chromefiddle/env' % env.root_dir
env.activate = 'source %s/bin/activate' % env.virtualenv
env.code_dir = '%s/chromefiddle' % env.root_dir
env.static_dir = '%s/src' % env.root_dir


def setup():
    """
    Initial configuration
    """
    # Update/upgrade
    sudo('apt-get update')
    sudo('apt-get upgrade')
    # Install python tools
    sudo('apt-get install -y python-setuptools')
    sudo('easy_install pip')
    sudo('pip install virtualenv')
    # Install Git
    sudo('apt-get install git-core')
    # Install Nginx
    sudo('apt-get install nginx')
    # Install Curl
    sudo('apt-get install libcurl3')
    # Reset permissions
    reset_permissions()


@contextmanager
def _virtualenv():
    """
    Activate virtualenv
    """
    with prefix(env.activate):
        yield


def create_virtualenv():
    """
    Create virtualenv
    """
    with cd(env.root_dir):
        sudo('virtualenv env --no-site-packages')


def remove_pyc_files():
    """
    Remove all compiled python files
    """
    with settings(warn_only=True):
        with cd(env.code_dir):
            sudo('find . -name "*.pyc" -exec rm {} \;')


def restart_gunicorn_nginx():
    """
    Restart Gunicorn and Nginx servers
    """
    restart_gunicorn()
    restart_nginx()


def start_gunicorn():
    """
    Start Gunicorn WSGI server
    """
    with cd(env.code_dir):
            with _virtualenv():
                sudo('gunicorn_django -c gunicorn.py '
                     '--daemon prod_settings.py & sleep 3')


def restart_gunicorn():
    """
    Restart Gunicorn WSGI server
    """
    with settings(warn_only=True):
        with cd(env.code_dir):
            pid = sudo('cat gunicorn.pid')
            remove_pyc_files()
            if not pid.succeeded:
                start_gunicorn()
            else:
                sudo('kill -HUP %s' % pid)


def start_nginx():
    """
    Start Nginx HTTP server
    """
    sudo('/etc/init.d/nginx start')


def restart_nginx():
    """
    Restart Nginx HTTP server
    """
    sudo('/etc/init.d/nginx restart')


def update_project():
    with cd(env.code_dir):
        with _virtualenv():
            run('git pull')
            install_requirements()
            perform_migration()
            collect_static()


def deploy():
    """
    Deploy Django project
    """
    update_project()
    restart_gunicorn_nginx()


def install_requirements():
    """
    Install pip dependencies from freeze files
    """
    with cd(env.code_dir):
        with _virtualenv():
            sudo('pip install -r requirements.txt', pty=True)


def perform_migration():
    """
    Perform database migration with South
    """
    with cd(env.code_dir):
        with _virtualenv():
            sudo('python manage.py migrate --settings=prod_settings', pty=True)


def collect_static():
    """
    Collect static files
    """
    with cd(env.code_dir):
        with _virtualenv():
            sudo('python manage.py collectstatic --settings=prod_settings', pty=True)


def test():
    """
    Run test suite
    """
    with cd(env.code_dir):
        with _virtualenv():
            local('python manage.py test', fail='abort')


def dump_db_json():
    """
    Dump backup of database to JSON
    """
    with cd(env.code_dir):
        with _virtualenv():
            sudo('python manage.py dumpdata > data/data.chromefiddle.json', pty=True)


def reset_permissions():
    """
    Reset user permissions
    """
    sudo('chown %s -R %s' % (env.user, env.root_dir))
    sudo('chgrp %s -R %s' % (env.user, env.root_dir))


def find_todo():
    """
    Find all TODO references
    """
    remove_pyc_files()
    local('grep -ir "TODO" *')
