from rest_framework import serializers


class CarSerializer(serializers.Serializer):
    cd_car_owner = serializers.UUIDField()
    color = serializers.ChoiceField(choices=['Yellow', 'Blue', 'Gray'])
    model = serializers.ChoiceField(choices=['Hatch', 'Sedan', 'Convertible'])