from django.urls import path
from hola.views import def_articulo, def_articulos,def_articulo_eliminar
from hola.views import def_articulo_editar

urlpatterns = [
    path('nuevo/', def_articulo, name='articulo'),
    path('lista/', def_articulos, name='articulos'),
    path('eliminar/<int:id>', def_articulo_eliminar, name='eliminar'),
    path('editar/<int:id>', def_articulo_editar, name='editar'),
]
