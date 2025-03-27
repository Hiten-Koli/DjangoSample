from rest_framework.views import APIView
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema

class SampleView(APIView):
    @extend_schema(summary="Retrieve a sample message", description="Returns a simple greeting message",responses={200: {"example": {"message": "This is secure data"}}},
)
    def get(self, request):
        return Response({"message": "Hello, Swagger with drf-spectacular!"})
