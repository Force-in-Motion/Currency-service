from celery import Celery
from  app.tasks import *

celery = Celery(
    'app',
    broker='redis://:0502@localhost:3030/0',
    backend='redis://:0502@localhost:3030/1',
)