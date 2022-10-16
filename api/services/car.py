from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from api.domain.car import CarDomain
from api.serializers.car import CarSerializer, CarOutputSerializer


class CarService(viewsets.ViewSet):

    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    domain = CarDomain()

    def create(self, request):
        serializer = CarSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            ret = self.domain.create(serializer.data)
        
        return Response({"message": ret["message"]}, status=ret["status"])
    
    def list(self, request):
        ret = self.domain.list()

        serializer = CarOutputSerializer(ret["message"], many=True)

        return Response({"cars": serializer.data})
    
    def retrieve(self, request, pk=None):
        ret = self.domain.get({"cd_car": pk})

        serializer = CarOutputSerializer(ret["message"])

        return Response({"car": serializer.data})


