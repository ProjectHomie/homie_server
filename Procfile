web: gunicorn --pythonpath homie_server/ --bind :7633 --workers=3 homie_server.wsgi
worker: celery --workdir=homie_server/ --app=homie_server.celery:app --concurrency=3 worker
flower: celery --workdir=homie_server/ --app=homie_server.celery:app flower
