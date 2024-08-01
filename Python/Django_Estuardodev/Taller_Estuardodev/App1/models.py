from django.db import models

# Create your models here.

class Profesion(models.Model):
    nombre = models.CharField(verbose_name="Nombre", max_length=75)
    
    def __str__(self): 
        return self.nombre

class AutorDB(models.Model):
    nombre = models.CharField(max_length=75, verbose_name="Nombre", null = False)
    fecha_nacimiento = models.DateField(verbose_name="Fecha Nacimiento",null = False, blank = False)
    fecha_fallecimiento = models.DateField(verbose_name="Fecha Fallecimiento",null = True, blank= True)
    profesion = models.ManyToManyField(Profesion, verbose_name="Profesion")
    nacionalidad = models.CharField(verbose_name="Nacionalidad", max_length = 50)
    
    class Meta: 
        db_table = "Autores"# Aqui indicamos el nombre que va a tener la tabla en la base de datos
        verbose_name = "Autores"
        verbose_name_plural= "Autores"
        
        
    def __str__(self) -> str: # Esto es para poner un poco mas presentable nuestros registros en las peticiones
        return self.nombre # Aqui se indica que si mandamos a llamar a un registro, nos devuelve el nombre del autor, se puede cambiar para cualquier información que tengamos del autor, por ejemplo podriamos poner self.nacionalidad para que salga "Hondureño " 
    
class FraseDB(models.Model):
    cita = models.TextField(verbose_name="Cita",max_length=400)
    autor_fk = models.ForeignKey(AutorDB, on_delete = models.CASCADE)  # Esta relacionado con el ID
    
    class Meta: 
        db_table = "Frases"
        verbose_name = "Frase"
        verbose_name_plural= "Frases"
        
class MelonDB(models.Model):
    cantidad = models.FloatField(verbose_name="Cantidad")
    chicle_de_melon = models.CharField(max_length=10, verbose_name="¿Es un chicle de melón?")
    maduro = models.CharField(max_length=50, verbose_name="¿Está maduro el melón?" )
    
    class Meta:
        db_table = "Melones"
        verbose_name = "Melon"
        verbose_name_plural= "Melones"
    