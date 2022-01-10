from django import forms
from django.db.models.enums import IntegerChoices
from django.http.response import HttpResponse
from django.shortcuts import render
from AppCentroDeSalud.models import CuerpoMedico, Pacientes, Consulta
from AppCentroDeSalud.forms import CuerpoMedicoFormulario, PacientesFormulario, ConsultaFormulario


# Create your views here.
def inicio(request):
    return render(request, "AppCentroDeSalud/inicio.html")

#cargar datos en model cuerpoMedico
def cuerpoMedicoFormulario(request):

    if request.method == "POST":

        miFormulario = CuerpoMedicoFormulario(request.POST)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            
            datos = CuerpoMedico(
                nombre = informacion["nombre"],
                apellido = informacion["apellido"],
                especialidad = informacion["especialidad"],
                dia_hora_atencion = informacion["dia_hora_atencion"],
                email = informacion["email"],
                telefono = informacion["telefono"]
            )
            datos.save()
            return render(request, 'AppCentroDeSalud/inicio.html')
            
            
    else:
        miFormulario = CuerpoMedicoFormulario()
        return render(request, 'AppCentroDeSalud/cuerpoMedicoFormulario.html',{"miFormulario":miFormulario})


def pacientesFormulario(request):

    if request.method == "POST":

        miFormulario = PacientesFormulario(request.POST)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
           

            datos = Pacientes(
                nombre = informacion["nombre"],
                apellido = informacion["apellido"],
                documento = informacion["documento"],
                email = informacion["email"],
                telefono = informacion["telefono"]
            )
            datos.save()
            return render(request, 'AppCentroDeSalud/inicio.html')
            
            
    else:
        miFormulario = PacientesFormulario()
        return render(request, 'AppCentroDeSalud/pacientesFormulario.html',{"miFormulario":miFormulario})


def consultaFormulario(request):

    if request.method == "POST":

        miFormulario = ConsultaFormulario(request.POST)

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            

            datos = Consulta(
                nombre = informacion["nombre"],
                apellido = informacion["apellido"],
                email = informacion["email"],
                telefono = informacion["telefono"],
                consulta_paciente = informacion["consulta_paciente"]
            )
            datos.save()
            return render(request, 'AppCentroDeSalud/inicio.html')
            
            
    else:
        miFormulario = ConsultaFormulario()
        return render(request, 'AppCentroDeSalud/consultaFormulario.html',{"miFormulario":miFormulario})

#Buscar datos

def busquedaMedico(request):
    return render(request, 'AppCentroDeSalud/busquedaMedico.html')

def buscarMedico(request):
    if request.method == 'GET':
        especialidad = request.GET['especialidad']
        medicos = CuerpoMedico.objects.filter(especialidad__icontains=especialidad)

        return render(request, "AppCentroDeSalud/resultadosBusqueda.html", {"medicos":medicos, "especialidad":especialidad})
    else:
        return HttpResponse("No enviaste datos")

#CRUD - CUERPO MEDICO

def leerCuerpoMedico(request):
    medicos = CuerpoMedico.objects.all()
    contexto = {"medicos": medicos}
    return render(request, 'AppCentroDeSalud/leerCuerpoMedico.html', contexto)

def eliminarMedico(request, medico_nombre):
    medico = CuerpoMedico.objects.get(nombre = medico_nombre)
    medico.delete()

    medicos = CuerpoMedico.objects.all()
    contexto = {"medicos": medicos}
    return render(request, 'AppCentroDeSalud/leerCuerpoMedico.html', contexto)
     

#FIN CRUD - CUERPO MEDICO


