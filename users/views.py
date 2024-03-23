from django.shortcuts import render
from rest_framework.views import APIView, Response
from . serializers import UserSerializer

# Create your views here.

class Register(APIView):
    def post(self, request):
        seralizer = UserSerializer(data=request.data)
        seralizer.is_valid(raise_exception=True)
        seralizer.save()
        return Response(seralizer.data)
