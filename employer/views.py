from django.shortcuts import render
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import EmployerSerializer
from .models import Employer
from django.http import Http404

# Create your views here.
class EmployerView(APIView):
    def get(self, request):        
        employers = Employer.objects.filter(user=request.user)
        serializer = EmployerSerializer(employers, many=True)
        return Response(serializer.data)
    
    def post(self, request):   
        serializer = EmployerSerializer(data=request.data)     
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user

class EmployerDetailView(APIView):    
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def get_object(self, pk):
        try:
            return Employer.objects.get(pk=pk, user=self.request.user)
        except Employer.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        employer = self.get_object(pk)
        self.check_object_permissions(request, employer)
        serializer = EmployerSerializer(employer)
        return Response(serializer.data)

    def put(self, request, pk):
        employer = self.get_object(pk)
        serializer = EmployerSerializer(employer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        employer = self.get_object(pk)
        employer.delete()
        return Response({"message": "Entry deleted successfully."}, status=status.HTTP_204_NO_CONTENT)