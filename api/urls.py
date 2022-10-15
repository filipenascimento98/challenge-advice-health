from django.urls import path

from api.services.car_owner import CarOwnerService


app_name = "api"


urlpatterns = [
    path("car-owner/", CarOwnerService.as_view()),
]