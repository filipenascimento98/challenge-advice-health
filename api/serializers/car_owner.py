from rest_framework import serializers


class CarOwnerSerializer(serializers.Serializer):
    name = serializers.CharField()

class CarOwnerOutputSerializer(CarOwnerSerializer):
    cd_car_owner = serializers.UUIDField()
    sales_opportunity = serializers.BooleanField()