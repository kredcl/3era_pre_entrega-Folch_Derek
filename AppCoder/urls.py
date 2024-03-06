
from django.urls import path
#from AppCoder.templates import *
from .views import *

urlpatterns = [
    path("about/", about, name= "About"),
    path("login/", login, name= "login"),
    path("dueno/", crear_dueño, name= "crear_dueño"),
    path("resto/", crear_resto, name= "crear_resto"),
    path("buscar_resto/", buscar_resto, name= "buscar_resto"),
    path("resultados/", resul_resto, name= "resultados"),
    #path("restoranes", resto, name= "restoranes"), 
    path('usuario/', crear_usuario, name='crear_usuario'),
    path('exito_dueno', exito_dueno, name= 'exito_dueno'),
    path('exito_resto', exito_resto, name= 'exito_resto'),
    path('exito', exito, name='exito'),
    path('', inicio, name='Home'),
]
