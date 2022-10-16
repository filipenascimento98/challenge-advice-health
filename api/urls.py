from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import routers

from api.services.car_owner import CarOwnerService
from api.services.car import CarService
from api.services.user import UserService


app_name = "api"

router = routers.DefaultRouter()
router.register(r'user', UserService)

urlpatterns = [
    path("car-owner/", CarOwnerService.as_view()),
    path("car/", CarService.as_view()),
    path("login/", obtain_auth_token),
    path('', include(router.urls))
]