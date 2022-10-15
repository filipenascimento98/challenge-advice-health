from rest_framework.views import APIView
from rest_framework.response import Response
from api.domain.car import CarDomain
from api.serializers.car import CarSerializer

class CarService(APIView):
    domain = CarDomain()

    def post(self, request):
        serializer = CarSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            ret = self.domain.create(serializer.data)
        
        return Response({"message": ret["message"]}, status=ret["status"])
