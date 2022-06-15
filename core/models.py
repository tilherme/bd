import email
from email.headerregistry import Address
import secrets
from unicodedata import name
from django.db import models
from django.forms import IntegerField

# Create your models here.
class Adress(models.Model):
    code = models.CharField(max_length=255, null=True, blank=True)
    street = models.CharField(max_length=255, null=True, blank=True)
    number = models.IntegerField(null=True, blank=True)
    complement = models.CharField(max_length=255, null=True, blank=True)
    reference = models.CharField(max_length=255, null=True, blank=True)
    neighborhood = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    latitude = models.CharField(max_length=255, null=True, blank=True)
    longitude = models.CharField(max_length=255, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.neighborhood

class Discipline(models.Model):
    name = models.CharField(max_length=255, null=True)
    class_school = models.ForeignKey("Class_school", null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Class_school(models.Model):
    code_class = models.IntegerField(null=True)
    institution = models.ForeignKey('Institution', null=True, on_delete=models.CASCADE ) 

class User(models.Model):
    TYPE_USER = (('ESTUDANTE', 'ESTUDANTE'),('SECRETARIA', 'SECRETARIA'), ('PROFESSOR', 'PROFESSOR'))
    name = models.CharField(max_length=255, null=True)
    user = models.CharField(max_length=255, choices=TYPE_USER, default='ESTUDANTE')
    sex = models.CharField(max_length=255, null=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(unique=True, null=True)
    cpf = models.CharField(max_length=255, null=True)
    registration = models.CharField(max_length=255, null=True)
    birth_date = models.DateField(null=True)
    specialization = models.CharField(max_length=255, null=True)
    class_school = models.ForeignKey(Class_school, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Institution(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    cnpj = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(unique=True, null=True)
    Address = models.ForeignKey(Adress, on_delete=models.CASCADE, null=True, blank=True)
    user = models.ForeignKey('user', null=True,  on_delete=models.CASCADE)

    def __str__(self):
        return self.name


