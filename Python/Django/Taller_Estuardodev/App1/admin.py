from django.contrib import admin

# Rsgistra los modelos aqui. 

# Admin nos sirve para mostrar nuestros modelos (models.py) en la pagina de administracion de django(hacer peticiones, registros, etc)

#Importamos las clases models 

from .models import AutorDB, FraseDB, MelonDB, Profesion
#Ponemos un "." en models porque estamos en la misma carpeta 


admin.site.site_header = "Encabezado Nuevo" # Esto es para cambiar el Encabezado de la web donde antes ponia "Administrador de Django "
admin.site.index_title = "Titulo de la page"
admin.site.site_title = "Otro lado"



@admin.register(Profesion)
class ProfesionAdmin(admin.ModelAdmin):
    list_display=["nombre"]
    fields = ["nombre"]




class FraseInLine(admin.TabularInline): # *1 Para crear las frases dentro del administrador de autores directamente(en la web)
    model = FraseDB
    extra = 1

class AutorAdmin(admin.ModelAdmin): 
    fields = ["nombre","fecha_nacimiento","fecha_fallecimiento","profesion","nacionalidad"]
    list_display = ["nombre","fecha_nacimiento"] #Esto es lo que nos muestra el apartado de usuario en la web de django, en "Usuarios"
    
    
    inlines = [FraseInLine]   # *1 Lo linkeamos con la clase FraseInLine 
    
    def actualizar_o(self, request, queryset): # Para crear acciones en el desplegable de cada lista (De momento solo está el de eliminar de la lista). Con esta funcion lo que haremos es cambiar las "O" mayuscula a minuscula del nombre de la persona
        for obj in queryset: #queryset es un conjunto de objetos que han sido seleccionados 
            if "O" in obj.nombre: 
                nombre1 = obj.nombre
                obj.nombre = nombre1.replace("O","o")
                obj.save()
        self.message_user(request, "Exitosamente")
        
    actualizar_o.short_description= "Actualizar letras O"
    
    
    actions = ["actualizar_o"]
    
    
    
admin.site.register(AutorDB,AutorAdmin) #Para registrar los cambios tenemos que hacer un admin.site.register


@admin.register(FraseDB) # Forma mas sencilla para registrar que la de arriba, usar esa 
class FraseAdmin(admin.ModelAdmin):
    fields =["cita","autor_fk"]
    list_display = ["cita"] 
    
    
@admin.register(MelonDB)
class MelonAdmin(admin.ModelAdmin):
    fields = ["cantidad","chicle_de_melon","maduro"]
    list_display = ["cantidad","chicle_de_melon","maduro"]

    
