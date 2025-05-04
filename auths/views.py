from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserSerializer, CustomTokenObtainPairSerializer
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
# Create your views here.

class SignUpView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class LoginView(TokenObtainPairView):
    serializer_class =CustomTokenObtainPairSerializer
    

class ProfileView(APIView):
    def get(sefl, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)