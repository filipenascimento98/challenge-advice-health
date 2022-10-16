from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import routers

from api.services.car_owner import CarOwnerService
from api.services.car import CarService
from api.services.user import UserService


app_name = "api"

router = routers.DefaultRouter()
router.register(r'user', UserService)
router.register(r'car-owner', CarOwnerService, basename='CarOwnerModel')
router.register(r'car', CarService, basename='CarModel')

urlpatterns = [
    path("login/", obtain_auth_token),
    path('', include(router.urls))
]