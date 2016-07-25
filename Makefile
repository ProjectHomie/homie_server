migrate:
	- python homie_server/manage.py makemigrations users posts bitly homie_server
	- python homie_server/manage.py migrate
