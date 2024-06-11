from django.shortcuts import render


def inicio(request):
    context = {
    "nombre": "pepe"
    }
    print("request",request)
    print("Has llamado a inicio")
    return render(request, "inicio.html")