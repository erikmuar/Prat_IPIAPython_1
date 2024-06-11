from django.shortcuts import render


def inicio(request):
    print("request",request)
    print("Has llamado a inicio")
    return render(request, "inicio.html")