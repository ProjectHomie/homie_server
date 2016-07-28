migrate:
	- python homie_server/manage.py makemigrations users posts
	- python homie_server/manage.py migrate


test:
	- pep8 . -v
	- python homie_server/manage.py test users posts -v2
