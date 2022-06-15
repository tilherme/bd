from dataclasses import fields
from .models import *
from rest_framework import serializers

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'

class UserSerializer(serializers. ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class InstitutionSerializer(serializers. ModelSerializer):
    class Meta:
        model =  Institution
        fields = '__all__'


class InstitutionSerializer(serializers. ModelSerializer):
    class Meta:
        model =  Institution
        fields = '__all__'

class DiscplineSerializer(serializers. ModelSerializer):
    class Meta:
        model =  Discipline
        fields = '__all__'

class Class_schoolSerializer(serializers. ModelSerializer):
    class Meta:
        model =  Class_school
        fields = '__all__'