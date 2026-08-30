from django.urls import path
from . import views

urlpatterns = [
    path('', views.empleado, name='empleado'),
    path('insertar_empleado/', views.insertar_empleado, name='insertar_empleado')
]