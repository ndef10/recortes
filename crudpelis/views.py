
from django.shortcuts import redirect, render
from crudpelis.models import Categoria

# Create your views here.
def v_categorias(request):
    context = {
        "items": Categoria.objects.all()
    }
    return render(request, "crudpelis/index.html", context)

def v_categoria_crear(request):
    context = {}
    if request.method == "POST":
        # procesar data
        data = request.POST.copy()
        categoria = Categoria()
        categoria.titulo = data["titulo"]
        categoria.descripcion = data["descripcion"]
        categoria.save()
        return redirect("/")
    else:
        return render(request, "crudpelis/categoria_crear.html", context)
    
def v_categoria_editar(request):
    categoria_id = request.GET.get("categoria_id", 0)
    if categoria_id == 0:
        return redirect("/")
    
    categoria_edicion = Categoria.objects.get(id = categoria_id)

    if request.method == "POST":
        data = request.POST.copy()
        categoria_edicion.titulo = data.get("titulo", "")
        categoria_edicion.descripcion = data.get("descripcion", "")
        categoria_edicion.save()
        return redirect("/")
    else:
        context = {
            "categoria_obj": categoria_edicion
        }
        return render(request, "crudpelis/categoria_editar.html", context)
 
def v_categoria_eliminar(request):
    categoria_id = request.GET.get("categoria_id", 0)
    if categoria_id == 0:
        return redirect("/")
    
    categoria_edicion = Categoria.objects.get(id = categoria_id)
    categoria_edicion.delete()
    return redirect("/")