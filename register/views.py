from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Registration
from .serializers import RegistrationSerializer
# Create your views here.


@api_view(['POST'])
def register_user(request):
    serializer = RegistrationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Registration successful'})
    return Response(serializer.errors, status=400)