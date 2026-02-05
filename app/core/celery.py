from celery import Celery
from app.core.config import celery_settings



celery = Celery(
    "currency_service",
    broker=celery_settings.broker_url,
    include=['app.tasks.prices']
)


celery.conf.update(
    worker_pool="prefork", 
    worker_concurrency=4, 
    task_create_missing_queues=True,
    task_serializer="json",
    result_serializer="json",
    accept_content=["json"],
    timezone="UTC",
    enable_utc=True,
    task_acks_late=True, 
)


celery.conf.beat_schedule = {
    "fetch-btc-price-every-60-seconds": {
        "task": "app.tasks.prices.fetch_price_task",
        "schedule": celery_settings.beat_interval,
        "args": ("BTC-PERPETUAL",),
    },
    "fetch-eth-price-every-60-seconds": {
        "task": "app.tasks.prices.fetch_price_task",
        "schedule": celery_settings.beat_interval,
        "args": ("ETH-PERPETUAL",),
    },
}

# celery -A app.core.celery:celery flower --port=5555

# celery -A app.core.celery:celery worker --loglevel=info -B