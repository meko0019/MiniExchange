from app.celery import celery

@celery.task
def process_payment(pending_id):
    # Create locked celery job (using redis) to send payment
    pass


@celery.task
def handle_message(message):
    # callback for websocket server
    pass

@celery.task
def pending_payments():
    pass