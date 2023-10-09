#!/usr/bin/python3
from fabric.api import *

env.hosts = ["52.201.69.229", "54.152.232.249"]

def do_clean(number=0):
    """deletes out-of-date archives"""

    number = int(number)

    if number == 0:
        number = 2
    else:
        number += 1

    local("cd versions ; ls -t | tail -n +{} | xargs rm -rf".format(number))
    path = "/data/web_static/releases"
    run("cd {} ; ls -t | tail -n +{} | xargs rm -rf".format(path, number))
