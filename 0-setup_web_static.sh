#!/usr/bin/env bash
# sets up my web servers for the deployment of web_static
sudo apt-get -y update
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'

sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html
echo "<!DOCTYPE html>
<html lang='en'>
    <head>
        <title>testing Nginx server</title>
    </head>
    <body>
        <p>We are live!</p>
    </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

# symbolic link,if already exists, it should be deleted and recreated every time the script is ran
sudo ln -s -f /data/web_static/releases/test/ /data/web_static/current

# recursively give ownership of the /data/ folder to the ubuntu user AND group.
sudo chown -R ubuntu:ubuntu /data/

# Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default

# restart nginx
sudo service nginx restart
