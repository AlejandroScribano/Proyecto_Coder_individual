from django.urls import path
from AppCentroDeSalud import views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('cuerpoMedicoFormulario/', views.cuerpoMedicoFormulario, name="CuerpoMedicoFormulario"),
    path('pacientesFormulario/', views.pacientesFormulario, name="PacientesFormulario"),
    path('consultaFormulario/', views.consultaFormulario, name="ConsultaFormulario"),

    #Path para buscar medico
    path('busquedaMedico', views.busquedaMedico, name='BusquedaMedico'),
    path('buscarMedico/', views.buscarMedico, name='BuscarMedico'),
]