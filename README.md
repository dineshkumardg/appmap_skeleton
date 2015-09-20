# appmap_skeleton
A skeleton for appmap

Assumptions:
1. that there is a mysql installation with username as root and password as root
2. that there us a database named DolphinD.
3. 	mkdir /home/test/appmap_project
4.	virtualenv --no-site-packages appmap_project
5.	cd appmap_project
6.	source bin/activate
7.	pip install Django==1.7
8.	pip install django-tastypie
9.	checkout this repo
10.	cd appmap
11.	python manage.py runserver 0.0.0.0:8000
12.	 Goto this URL:
13.	http://192.168.56.101:8000/api/whatever/?format=json
14.	This is for test
You should see the table data in json format
----------------
