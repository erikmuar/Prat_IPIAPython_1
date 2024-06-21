### Tutorial: Iniciar un Proyecto Django y Mostrar un Index

Este tutorial te guiará a través de los pasos necesarios para iniciar un proyecto Django, crear un índice en la carpeta `templates`, y ver la salida en un puerto.

#### Paso 1: Crear Entorno Virtual
1. Ve a tu carpeta de trabajo.
2. Crea un entorno virtual:
   ```bash
   python3 -m venv venv
   ls # debe salir la carpeta venv
   ```
3. Activa el entorno virtual:
   ```bash
   source venv/bin/activate
   ```

#### Paso 2: Instalar Django
4. Verifica que el entorno virtual esté activo y lista los paquetes instalados (debería estar vacío):
   ```bash
   pip list
   ```
5. Instala Django:
   ```bash
   pip install django
   ```
6. Verifica que Django esté instalado:
   ```bash
   pip list # debe salir Django
   ```

#### Paso 3: Iniciar Proyecto Django
7. Inicia un nuevo proyecto Django:
   ```bash
   django-admin startproject MiDjango .
   ```
8. Verifica la estructura de carpetas y archivos:
   ```bash
   tree MiDjango/
   ```

#### Paso 4: Configurar Proyecto Django
9. Entra en la carpeta del proyecto:
   ```bash
   cd MiDjango
   tree
   ```

10. Abre el archivo `settings.py` y permite que todos los hosts puedan acceder al proyecto:
    ```python
    # En settings.py, busca la línea ALLOWED_HOSTS y modifícala:
    ALLOWED_HOSTS = ['*']
    ```

11. Crea las carpetas `static` y `templates` en la raíz del proyecto:
    ```bash
    mkdir static templates
    ```

12. Configura Django para que use la carpeta `templates`:
    ```python
    # En settings.py, busca TEMPLATES y modifícalo así:
    'DIRS': [BASE_DIR / "templates"],
    ```

#### Paso 5: Crear una Página de Inicio
13. Crea un archivo `index.html` en la carpeta `templates` con el siguiente contenido:
    ```html
    <!DOCTYPE html>
    <html>
    <head>
        <title>Mi Página de Inicio</title>
    </head>
    <body>
        <h1>¡Hola, mundo!</h1>
    </body>
    </html>
    ```

14. Crea una vista en `views.py` para renderizar `index.html`:
    ```python
    # En MiDjango/views.py, añade:
    from django.shortcuts import render

    def index(request):
        return render(request, "index.html")
    ```

#### Paso 6: Configurar URLs
15. Configura las URLs en `urls.py` para incluir la nueva vista:
    ```python
    # En MiDjango/urls.py, modifica el archivo para que se vea así:
    from django.contrib import admin
    from django.urls import path

    from .views import index

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', index, name="index"),
    ]
    ```

#### Paso 7: Ejecutar el Servidor
16. Guarda todos los archivos y ejecuta el servidor:
    ```bash
    python manage.py runserver
    ```

17. Abre tu navegador y ve a `http://localhost:8000` (o el puerto que se indique) para ver la página de inicio.

### Resumen de la Estructura de Directorios

Después de seguir estos pasos, tu estructura de directorios debería verse así:
```
MiDjango/
├── manage.py
├── MiDjango/
│   ├── __init__.py
│   ├── __pycache__/
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   └── wsgi.py
├── static/
└── templates/
    └── index.html
```

### Ejemplo de `urls.py` Completo
```python
from django.contrib import admin
from django.urls import path
from .views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
]
```

### Ejemplo de `views.py` Completo
```python
from django.shortcuts import render

def index(request):
    return render(request, "index.html")
```

¡Felicidades! Ahora tienes un proyecto Django básico corriendo con una página de inicio.