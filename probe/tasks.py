import time

from django_celery.celery import app


@app.task
def sum_task(x, y):
    time.sleep(10)
    return x + y

