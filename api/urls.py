from django.urls import path

from api.services.car_owner import CarOwnerService
from api.services.car import CarService


app_name = "api"


urlpatterns = [
    path("car-owner/", CarOwnerService.as_view()),
    path("car/", CarService.as_view())
]