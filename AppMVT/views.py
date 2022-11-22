from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Familia

# Create your views here.

def integrante(request):
    integrante1=Familia(nombre='Juan', apellido= 'Granata', edad = 49 , email= 'juan.granata@email.com')
    integrante2=Familia(nombre='Fer', apellido='Pardo', edad = 48 , email='fer.pardo@email.com')
    integrante3=Familia(nombre='Joaco', apellido='Granata', edad = 15 , email='joaco.granata@email.com')
    integrante4=Familia(nombre='Guille', apellido='Granata', edad = 11 , email='guille.granata@email.com')
    integrante1.save()
    integrante2.save()
    integrante3.save()
    integrante4.save()
    familia = f'Se guardaron los siguientes integrates: <br> ------------------------ <br> Nombre: {integrante1.nombre} <br> Apellido: {integrante1.apellido} <br> Edad: {integrante1.edad} <br> Email: {integrante1.email} <br> ------------------------ <br> Nombre: {integrante2.nombre} <br> Apellido: {integrante2.apellido} <br> Edad: {integrante2.edad} <br> Email: {integrante2.email} <br> ------------------------ <br> Nombre: {integrante3.nombre} <br> Apellido: {integrante3.apellido} <br> Edad: {integrante3.edad} <br> Email: {integrante3.email} <br> ------------------------ <br> Nombre: {integrante4.nombre} <br> Apellido: {integrante4.apellido} <br> Edad: {integrante4.edad} <br> Email: {integrante4.email}'
    
    return HttpResponse (familia)

def inicio(self):
    fam="Granata"
    dicionario={'family':fam}
    plantilla=loader.get_template('index.html')
    doc=plantilla.render(dicionario)
    return HttpResponse(doc)
    
