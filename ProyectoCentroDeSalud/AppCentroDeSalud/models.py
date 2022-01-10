from django.db import models

# Create your models here.
class CuerpoMedico(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    especialidad = models.CharField(max_length=30)
    dia_hora_atencion = models.CharField(max_length=90)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return f"Nombre y apellido: {self.nombre} {self.apellido} - Especialidad: {self.especialidad} - Día y hora de atención: {self.dia_hora_atencion}"
    
class Pacientes(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    documento = models.IntegerField()
    email = models.EmailField()
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return f"Nombre y apellido: {self.nombre} {self.apellido} - Documento: {self.documento} - email: {self.email} - Telefono: {self.telefono}"

class Consulta(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    telefono = models.CharField(max_length=15)
    consulta_paciente = models.CharField(max_length=150)

    def __str__(self):
        return f"Nombre y apellido: {self.nombre} {self.apellido} - email: {self.email} - Telefono: {self.telefono} - Consulta: {self.consulta_paciente}"
