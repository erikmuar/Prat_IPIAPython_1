from django.urls import path 
from .views import IndexView, AutorView

urlpatterns = [
    path("", IndexView),
    path("autor/<int:id>", AutorView )
]
