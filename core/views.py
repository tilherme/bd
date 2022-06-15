from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import viewsets



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class Class_schoolViewSet(viewsets.ModelViewSet):
    queryset = Class_school.objects.all()
    serializer_class = Class_schoolSerializer

class InstitutionViewSet(viewsets.ModelViewSet):
    queryset = Institution.objects.all()
    serializer_class = InstitutionSerializer

class DisciplineViewSet(viewsets.ModelViewSet):
    queryset = Discipline.objects.all()
    serializer_class = DiscplineSerializer