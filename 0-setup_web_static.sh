#!/usr/bin/env bash
# Configures web server for deployment of a static page

# Installs Nginx if not already installed
sudo apt-get update
sudo apt-get -y upgrade
sudo apt-get -y install nginx

# Create data folder and supporting folders for web_static if they dont already exist
sudo mkdir -p /data/web_static/shared/ /data/web_static/releases/test/

# Create a test file to verify Nginx config in .../index.html
SETUP_TEST="<html>
<head>
</head>
<body>
 HBNB Deployment Configuration
</body>
<html>"
echo "$SETUP_TEST" | sudo tee /data/web_static/releases/test/index.html

# Creates symbolic link between data/web_static/current and .../web_static/releases/test/
sudo ln -sf /data/web_static/releases/test /data/web_static/current

# Gives ownership of /data/ folder to ubuntu and group
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx config to serve content of /data/webstatic/current/ to hbnb_static
D_Config=https://raw.githubusercontent.com/jsjimenez51/AirBnB_clone_v2/master/default
D_File=/etc/nginx/sites-available/default
sudo wget $D_Config -O $D_File

sudo service nginx reload
sudo service nginx restart
