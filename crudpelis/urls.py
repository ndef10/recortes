from django.urls import path
from .views import v_categorias, v_categoria_crear,\
    v_categoria_editar, v_categoria_eliminar

urlpatterns = [
    path('', v_categorias, name="categorias"),
    path('categoria/crear', v_categoria_crear, name="categoria_crear"),
    path('categoria/editar', v_categoria_editar, name="categoria_editar"),
    path('categoria/eliminar', v_categoria_eliminar, name="categoria_editar"),
]
