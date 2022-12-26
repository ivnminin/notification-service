from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend, FilterSet
from rest_framework import filters
from rest_framework import viewsets


from . import serializers
from . import models


class ClientFilter(FilterSet):

    class Meta:
        model = models.Client
        fields = ['number', 'code', 'tag', 'gmt']


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = models.Client.objects.all().order_by('code')
    serializer_class = serializers.ClientSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_class = ClientFilter
    ordering_fields = '__all__'


class MessageViewSet(viewsets.ModelViewSet):
    queryset = models.Message.objects.all()
    serializer_class = serializers.MessageSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = '__all__'


class DeliveryViewSet(viewsets.ModelViewSet):
    queryset = models.Delivery.objects.all()
    serializer_class = serializers.DeliverySerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = '__all__'


class MembershipViewSet(viewsets.ModelViewSet):
    queryset = models.Membership.objects.all()
    serializer_class = serializers.MembershipSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = '__all__'
