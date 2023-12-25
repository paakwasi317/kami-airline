from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import AirplaneBulkInputSerializer, AirplaneOutputSerializer
from .utils import Airplane


class AirplaneListView(APIView):

    def post(self, request, format=None):
        serializer = AirplaneBulkInputSerializer(data=request.data)
        if serializer.is_valid():
            airplane = Airplane()
            airplane_output = airplane.calculator(serializer.data)
            result_serializer = AirplaneOutputSerializer(airplane_output, many=True)
            return Response(result_serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)