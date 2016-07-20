migrate:
	- python homie_server/manage.py makemigrations users posts
	- python homie_server/manage.py migrate
