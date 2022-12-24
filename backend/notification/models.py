from django.db import models
from django.core.exceptions import ValidationError


class Client(models.Model):
    number = models.BigIntegerField()
    code = models.IntegerField()
    tag = models.CharField(max_length=40)
    gmt = models.IntegerField()

    @property
    def phone_number(self):
        return f'+{self.code} ({str(self.number)[:3]}) {str(self.number)[3:5]}-{str(self.number)[6:]}'

    def __str__(self):
        return self.phone_number


class Message(models.Model):

    message = models.CharField(max_length=2048, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.message[:50]


class Delivery(models.Model):
    message = models.OneToOneField(
        Message,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    time_start = models.DateTimeField()
    time_end = models.DateTimeField()

    members = models.ManyToManyField(Client, through='Membership')

    def __str__(self):
        return f'Delivery {self.pk} with message: {self.message.message[:50]}'


class Membership(models.Model):

    class Status(models.TextChoices):
        NEW = 'NEW'
        SENT = 'SENT'
        NOT_SENT = 'NOT_SENT'
        PROCESSING = 'PROCESSING'

    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.NEW,
    )
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE)

    def __str__(self):
        return f'delivery {self.delivery.pk}'
