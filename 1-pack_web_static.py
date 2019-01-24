#!/usr/bin/python3
'''Fabric script that will generate a .tgz archive from a folder'''
from fabric.api import local
from datetime import datetime
from os.path import exists
from os import makedirs
import os


def do_pack():
    '''
    Generates a .tgz archive
    Return:
    path to the archive, else none
    '''
    time = datetime.now().strftime("%Y%m%d%H%M%S")
    print("Packing web_static to versions/web_static_{}.tgz".format(time))

    if not exists('versions'):
        makedirs('versions')

    pack = local("sudo tar -cvzf versions/webstatic_{}.tgz web_static/"
                 .format(time))

    local("sudo chmod 664 versions/webstatic_{}.tgz".format(time))

    size = os.stat("versions/webstatic_{}.tgz".format(time)).st_size

    if pack.succeeded:
        print("web_static packed: versions/web_static_{} -> {}Bytes"
              .format(time, size))
        return "versions/web_static_{}.tgz".format(time)
    else:
        return None
