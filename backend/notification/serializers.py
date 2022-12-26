from django.contrib.auth.models import User
from rest_framework import serializers

from . models import Client, Message, Membership, Delivery


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class ClientSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Client
        fields = ['pk', 'number', 'code', 'tag', 'gmt']


class MessageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Message
        fields = ['text', 'created_at', 'updated_at']


class DeliverySerializer(serializers.ModelSerializer):

    class Meta:
        model = Delivery
        fields = ['message', 'time_start', 'time_end']


class MembershipSerializer(serializers.ModelSerializer):

    class Meta:
        model = Membership
        fields = ['status', 'client', 'delivery']
