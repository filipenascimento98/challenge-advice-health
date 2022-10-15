from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializers.car_owner import CarOwnerInput
from api.domain.car_owner import CarOwnerDomain


class CarOwnerService(APIView):

    domain = CarOwnerDomain()

    def post(self, request):
        serializer = CarOwnerInput(data=request.data)

        if serializer.is_valid(raise_exception=True):
            ret = self.domain.create(data_car_owner=serializer.data)
        
        return Response({"success": ret["success"]}, status=ret["status"])