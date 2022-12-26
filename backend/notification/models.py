from django.db import models


class Client(models.Model):
    number = models.BigIntegerField()
    code = models.IntegerField()
    tag = models.CharField(max_length=40)
    gmt = models.IntegerField()

    @property
    def phone_number(self):
        return f'+{self.code} ({str(self.number)[:3]}) {str(self.number)[3:6]}-{str(self.number)[6:]}'

    @property
    def phone_number_int(self):
        return int(f'{self.code}{self.number}')

    def __str__(self):
        return self.phone_number


class Message(models.Model):
    text = models.CharField(max_length=2048, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text[:50]


class Delivery(models.Model):
    message = models.ForeignKey(
        Message,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    time_start = models.DateTimeField()
    time_end = models.DateTimeField()

    members = models.ManyToManyField(Client, through='Membership')

    def __str__(self):
        return f'Delivery {self.pk}'


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
        return f'delivery {self.delivery.pk}, client {self.client.pk}'
