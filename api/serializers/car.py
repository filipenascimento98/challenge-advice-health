from rest_framework import serializers
from api.serializers.car_owner import CarOwnerOutputSerializer

class CarSerializer(serializers.Serializer):
    owner = serializers.UUIDField()
    color = serializers.ChoiceField(choices=['Yellow', 'Blue', 'Gray'])
    model = serializers.ChoiceField(choices=['Hatch', 'Sedan', 'Convertible'])

class CarOutputSerializer(serializers.Serializer):
    cd_car = serializers.UUIDField()
    owner = CarOwnerOutputSerializer()
    color = serializers.CharField()
    model = serializers.CharField()