import time


from celery import shared_task


@shared_task()
def send_email_dummy(email=None):
    time.sleep(5)
    print("this is celery tasks")
    return
