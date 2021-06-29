#!/bin/sh

cd /var/lib/jenkins/Prussian-Django-Deploy-Test
git pull
cp ./django_test/settings_dev.py ./django_test/settings.py 
pip3 install -r requirements.txt
python3 ./manage.py migrate
python3 ./manage.py runserver 0.0.0.0:8000