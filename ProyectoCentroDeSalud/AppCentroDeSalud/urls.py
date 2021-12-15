from django.urls import path
from AppCentroDeSalud import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('cuerpoMedicoFormulario/', views.cuerpoMedicoFormulario, name="CuerpoMedicoFormulario"),
]