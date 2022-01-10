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

    #Path para leer CuerpoMedico
    path('leerCuerpoMedico', views.leerCuerpoMedico, name='LeerCuerpoMedico'),

    #Path para eliminar Medico
    path('eliminarMedico/<medico_nombre>', views.eliminarMedico, name='EliminarMedico'),
]