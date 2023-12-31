from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializers
from rest_framework.viewsets import ModelViewSet
# Create your views here.
class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    