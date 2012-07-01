from fabric.api import env, run, prefix, cd, sudo, local

env.user = 'malene'
env.hosts = ['tango.johan.cc']
env.directory = '/home/malene/srv/malenebichel'
env.activate = 'source /home/malene/.virtualenvs/malenebichel/bin/activate'

def deploy():
    local('git push')
    with cd(env.directory):
        with prefix(env.activate):
            run('git pull')
            run('pip install -r requirements.txt')
            run('python manage.py migrate')
            run('python manage.py cleanup')
            run('touch malenebichel/wsgi.py') # this triggers a gracefull reload
