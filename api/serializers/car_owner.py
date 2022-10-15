from rest_framework import serializers


class CarOwnerInput(serializers.Serializer):
    name = serializers.CharField()