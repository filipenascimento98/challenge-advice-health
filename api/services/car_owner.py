from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from api.serializers.car_owner import (
    CarOwnerSerializer,
    CarOwnerOutputSerializer,
)
from api.domain.car_owner import CarOwnerDomain


class CarOwnerService(viewsets.ViewSet):

    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    domain = CarOwnerDomain()

    def create(self, request):
        serializer = CarOwnerSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            ret = self.domain.create(serializer.data)
        
        return Response({"message": ret["message"]}, status=ret["status"])
    
    def list(self, request):
        ret = self.domain.list()

        serializer = CarOwnerOutputSerializer(ret["message"], many=True)

        return Response({"car_owners": serializer.data})

    def retrieve(self, request, pk=None):
        ret = self.domain.get({"cd_car_owner": pk})

        serializer = CarOwnerOutputSerializer(ret["message"])

        return Response({"car_owner": serializer.data})