from django.contrib import admin

# Rsgistra los modelos aqui. 

# Admin nos sirve para mostrar nuestros modelos (models.py) en la pagina de administracion de django(hacer peticiones, registros, etc)

#Importamos las clases models 

from .models import AutorDB, FraseDB
#Ponemos un "." en models porque estamos en la misma carpeta 

class AutorAdmin(admin.ModelAdmin): 
    fields = ["nombre","fecha_nacimiento","fecha_fallecimiento","profesion","nacionalidad"]