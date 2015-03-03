from fabric.api import *

#env.use_ssh_config = True
env.hosts = ["52.10.69.37"]
env.user = "ubuntu"
env.key_filename = "/home/sam/Desktop/keys/nutwo.pem"
env.password = ""
env.port = 22

def testlive():
  run("ls")


def update_django_project():
    """ Updates the remote django project.
    """
    with cd('/home/sam/Desktop/tor/complete/client'):
        run('git pull')
        with prefix('source /home/sam/Desktop/tor/complete/bin/activate'):
            run('pip install -r require.txt')
            run('python manage.py syncdb')
            run('python manage.py migrate') # if you use south
            run('python manage.py collectstatic --noinput')
