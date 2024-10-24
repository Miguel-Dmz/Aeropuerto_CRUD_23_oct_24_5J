from django.shortcuts import render
from .models import Aviones
# Create your views here.
def listadoAviones(request):
    Losaviones=Aviones.objects.all()
    return render(request,"GestionarAviones.html",{"misaviones":Losaviones})