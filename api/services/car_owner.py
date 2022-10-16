from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

from api.serializers.car_owner import (
    CarOwnerSerializer,
    CarOwnerOutputSerializer,
)
from api.domain.car_owner import CarOwnerDomain


class CarOwnerService(APIView):

    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

    domain = CarOwnerDomain()

    def post(self, request):
        serializer = CarOwnerSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            ret = self.domain.create(serializer.data)
        
        return Response({"message": ret["message"]}, status=ret["status"])
    
    def get(self, request):
        ret = self.domain.list()

        serializer = CarOwnerOutputSerializer(ret["message"], many=True)

        return Response({"car_owners": serializer.data})