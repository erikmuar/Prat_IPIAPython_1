from django.shortcuts import render, get_object_or_404
from .models  import AutorDB, FraseDB, MelonDB  #Para hacer consultas a la base de datos hay que importar estas DB
#from django.http import HttpResponse. Asi ya podemos crear el objeto en la funcion de IndexView de abajo.


# Create your views here.
def IndexView(request):
    """Esto es la pagina principal"""
    
    objeto = AutorDB.objects.all().order_by("-id")  # Esto lo hacemos para descargar toda(.all) la informacion(objetos) de la base de datos. Este objeto hay que pasarlo por el render de abajo. 
    
    
    
    return render(request,"index.html", {"objeto":objeto})


def AutorView(request, id): 
    autor = get_object_or_404(AutorDB, id=id)
    return render(request,"autor.html", {"objeto":autor})