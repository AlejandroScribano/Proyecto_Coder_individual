from django.db.models.enums import IntegerChoices
from django.shortcuts import render
from AppCentroDeSalud.models import CuerpoMedico
from AppCentroDeSalud.forms import CuerpoMedicoFormulario

# Create your views here.
def inicio(request):
    return render(request, "AppCentroDeSalud/inicio.html")

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

