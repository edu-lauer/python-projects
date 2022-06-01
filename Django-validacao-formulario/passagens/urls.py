from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('revisao_consulta', views.revisao_consulta, name='revisao_consulta')
]
