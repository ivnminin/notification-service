import logging
import os
import sys
import time

import django
from django.utils import timezone
import requests

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)8s %(asctime)s %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

API_URI = os.environ['API_URI'] + '/{msg_id}'
JWT_TOKEN = os.environ['TOKEN']
TIME_SLEEP = 5


def send_to_clients(memberships, msg):

    for member in memberships:
        payload = {
            'id': member.pk,
            'phone': member.client.phone_number_int,
            'text': msg
        }

        r = requests.post(
            API_URI.format(msg_id=payload['id']),
            json=payload,
            headers={'Authorization': 'Bearer ' + JWT_TOKEN}
        )

        if r.status_code == 200 and r.json()['message'] == 'OK':
            logging.info(f'      Client {payload["phone"]} notified')
            member.status = models.Membership.Status.SENT
        else:
            logging.info(f'      Client {payload["phone"]} not notified')
            member.status = models.Membership.Status.NOT_SENT
        member.save()


def main():
    deliveries = models.Delivery.objects.filter(
        time_start__lte=timezone.now(),
        time_end__gte=timezone.now()
    ).all()
    logging.info(f'  Number of deliveries: {deliveries.count()}')
    for deliver in deliveries:
        qs = models.Membership.objects.filter(
            delivery_id=deliver.pk,
            status__in=[models.Membership.Status.NEW, models.Membership.Status.NOT_SENT]
        )
        logging.info(f'    Number of clients to send for {deliver}: {qs.count()}')
        if qs:
            send_to_clients(qs, deliver.message.text)


if __name__ == '__main__':

    django.setup()
    from notification import models

    logging.info(f'start worker {sys.argv[0]}')

    while True:
        logging.info(f'sleep... {TIME_SLEEP}')
        time.sleep(TIME_SLEEP)
        main()
