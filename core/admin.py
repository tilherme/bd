from django.contrib import admin

from core.models import Adress, Class_school, Discipline, Institution

# Register your models here.

admin.site.register(Adress)
admin.site.register(Institution)
admin.site.register(Discipline)
admin.site.register(Class_school)



