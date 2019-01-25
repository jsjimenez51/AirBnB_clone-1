#!/usr/bin/python3
'''Fabric script that will generate a .tgz archive from a folder'''
from fabric.api import local, env, put, sudo, runs_once
from datetime import datetime
from os.path import exists
from os import makedirs
import os

env.hosts = ['34.73.141.155', '35.231.170.192']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa.pub'


@runs_once
def do_pack():
    '''
    Packs files for deployment on server
    '''
    time = datetime.now().strftime("%Y%m%d%H%M%S")

    if not exists('versions'):
        makedirs('versions')

    pack = local("sudo tar -cvzf versions/web_static_{}.tgz web_static/"
                 .format(time))
    if pack.succeeded:
        return "versions/web_static_{}.tgz".format(time)
    else:
        return None


def do_deploy(archive_path):
    '''
    Deploys the packed archive to designated webservers
    '''
    if not exists(archive_path) and not isfile(archive_path):
        return False

    filename = archive_path.split("/")[1][:-4]

    try:
        put(archive_path, "/tmp/")
        sudo("mkdir -p /data/web_static/releases/{}/".format(filename))
        sudo("tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/"
             .format(filename, filename))
        sudo("rm -rf /tmp/{}.tgz".format(filename))
        sudo("mv /data/web_static/releases/{}/web_static/*\
             /data/web_static/releases/{}/".format(filename, filename))
        sudo("rm -rf /data/web_static/releases/{}/web_static".format(filename))
        sudo("rm -rf /data/web_static/current")
        sudo("ln -sf /data/web_static/releases/{}/ /data/web_static/current"
             .format(filename))
        print("New version deployed!")
        return True
    except:
        print("Deployment fail")
        return False
