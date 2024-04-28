from django.contrib import admin
from django.urls import path,include
from api.views import ComapanyViewSet, EmployeeViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'companies', ComapanyViewSet)
router.register(r'employees', EmployeeViewSet)

urlpatterns = [
    path('',include(router.urls))
]