from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from api.domain.car import CarDomain
from api.serializers.car import CarSerializer, CarOutputSerializer


class CarService(APIView):

    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    domain = CarDomain()

    def post(self, request):
        serializer = CarSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            ret = self.domain.create(serializer.data)
        
        return Response({"message": ret["message"]}, status=ret["status"])
    
    def get(self, request):
        ret = self.domain.list()

        serializer = CarOutputSerializer(ret["message"], many=True)

        return Response({"cars": serializer.data})


