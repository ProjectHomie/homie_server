migrate:
	- python homie_server/manage.py makemigrations users
	- python homie_server/manage.py migrate
