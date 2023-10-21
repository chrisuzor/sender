from celery import shared_task

from api import handle_xml


@shared_task(bind=True,autoretry_for=(Exception,), retry_backoff=True, retry_kwargs={"max_retries": 5},
             name='sender_mews:generate_xml')
def generate_xml(self, data: str):
    print('inside generate_xml')
    handle_xml.mews(data)
    return 'success'
