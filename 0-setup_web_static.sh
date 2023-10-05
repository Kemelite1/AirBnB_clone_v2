#!/usr/bin/env bash
# sets up my web servers for the deployment of web_static
sudo apt-get -y update
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'
mkdir -p
