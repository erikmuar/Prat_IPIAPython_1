from django.db import models

# Create your models here.
class AutorDB(models.Model):
    nombre = models.CharField(max_length=75, verbose_name="Nombre", null = False)
    fecha_nacimiento = models.DateField(verbose_name="Fecha Nacimiento",null = False, blank = False)
    fecha_fallecimiento = models.DateField(verbose_name="Fecha Fallecimiento",null = True, blank= True)
    profesion = models.CharField(verbose_name="Profesión", max_length=50)
    nacionalidad = models.CharField(verbose_name="Nacionalidad", max_length = 50)
    
    class Meta: 
        db_table = "Autores"# Aqui indicamos el nombre que va a tener la tabla en la base de datos
        verbose_name = "Autores"
        verbose_name_plural= "Autores"
        
        
    def __str__(self) -> str: # Esto es para poner un poco mas presentable nuestros registros en las peticiones
        return self.nombre # Aqui se indica que si mandamos a llamar a un registro, nos devuelve el nombre del autor para que asi sepamos a que nos referimos 
    
class FraseDB(models.Model):
    cita = models.TextField(verbose_name="Cita",max_length=400)
    autor_fk = models.ForeignKey(AutorDB, on_delete = models.CASCADE)  # Esta relacionado con el ID
    
    class Meta: 
        db_table = "Frase"