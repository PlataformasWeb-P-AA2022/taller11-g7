from django.urls import path
# se importa las vistas de la aplicación
from . import views


urlpatterns = [
    # Visualizar
    path('', views.index, name='index'),
    

]