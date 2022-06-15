from django.conf.urls import url, include
from django.urls import path
from .views import *
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'address', AddressViewSet)
router.register(r'discipline', DisciplineViewSet)
router.register(r'class', Class_schoolViewSet)
router.register(r'institution', InstitutionViewSet)
# router.register(r'tasktype', TaskTypesViewSet)


urlpatterns = [
    url(r'^auth/?$', views.obtain_auth_token),
    path('', include(router.urls)),

]
