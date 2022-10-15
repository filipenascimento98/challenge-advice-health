from rest_framework import serializers


class CarOwnerSerializer(serializers.Serializer):
    name = serializers.CharField()