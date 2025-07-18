from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Registration
from .serializers import RegistrationSerializer
from django.contrib.auth import authenticate
from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.contrib.auth import logout
# Create your views here.


@api_view(['POST'])
def register_user(request):
    serializer = RegistrationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Registration successful'})
    return Response(serializer.errors, status=400)

@api_view(['POST'])
def admin_login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user and user.is_staff:
        return JsonResponse({'message': 'Login successful', 'admin': True})
    return JsonResponse({'error': 'Invalid credentials'}, status=401)

@api_view(['GET'])
def students_list(request):
    students = Registration.objects.all()
    serializer = RegistrationSerializer(students, many=True)
    return Response(serializer.data)

@api_view(['DELETE'])
def delete_student(request, pk):
    try:
        student = Registration.objects.get(id=pk)
        student.delete()
        return Response({'message': 'Student deleted successfully'})
    except Registration.DoesNotExist:
        return Response({'error': 'Student not found'}, status=404)
    
def admin_logout_view(request):
    if request.method == "POST":
        logout(request)
        return JsonResponse({'message': 'Logged out successfully'})
    return JsonResponse({'error': 'Invalid request'}, status=400)