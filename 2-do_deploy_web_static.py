#!/usr/bin/python3
"""A Fabric script (based on the file 1-pack_web_static.py) that distributes an archive to my web servers,
using the function do_deploy"""

import os

from fabric.api import *


env.hosts = ["52.201.69.229", "54.152.232.249"]


def do_deploy(archive_path):
    """Prototype: def do_deploy(archive_path):
    Returns False if the file at the path archive_path does not exist
    The script should take the following steps:
    Upload the archive to the /tmp/ directory of the web server
    Uncompress the archive to the folder /data/web_static/releases/<archive filename without extension> on the web server
    Delete the archive from the web server"""
    local("mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    archived_f_path = "versions/web_static_{}.tgz".format(date)
    t_gzip_archive = local("tar -cvzf {} web_static".format(archived_f_path))

    if t_gzip_archive.succeeded:
        return archived_f_path
    else:
        return None


def do_deploy(archive_path):
    """
        Distribute archive.
    """
    if os.path.exists(archive_path):
        archived_file = archive_path[9:]
        newest_version = "/data/web_static/releases/" + archived_file[:-4]
        archived_file = "/tmp/" + archived_file
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}".format(newest_version))
        run("sudo tar -xzf {} -C {}/".format(archived_file,
                                             newest_version))
        run("sudo rm {}".format(archived_file))
        run("sudo mv {}/web_static/* {}".format(newest_version,
                                                newest_version))
        run("sudo rm -rf {}/web_static".format(newest_version))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(newest_version))

        print("New version deployed!")
        return True

    return False
