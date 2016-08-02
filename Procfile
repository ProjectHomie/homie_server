web: python homie_server/manage.py runserver 8000
worker: celery --workdir=homie_server/ --app=homie_server.celery:app --concurrency=3 worker
flower: celery --workdir=homie_server/ --app=homie_server.celery:app flower
