from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'deliveries', views.DeliveryViewSet)
router.register(r'messages', views.MessageViewSet)
router.register(r'clients', views.ClientViewSet)
router.register(r'memberships', views.MembershipViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
