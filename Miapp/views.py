from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from random import randint

def cursos(request):
    return render(request, "Miapp/cursos.html")

def cursos_enriquecido(request):

    return render(
        request, 
        "Miapp/cursos_enriquecido.html",
        {"nombre": "elefante", "numero_aleatorio": randint(0, 100)}
    )

def cursos_formulario(request):
    print("*" * 90)
    print(request.method)
    print("*" * 90)
    
    
    if request.method == "POST":
        print(request.POST)
        return render(request, "Miapp/cursos.html")
    else:
        return render(request, "Miapp/curso_formulario.html")
    print("*" * 90)

    #return HttpResponse("Llego el formulario!")
    