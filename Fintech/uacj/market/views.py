from django.shortcuts import render, redirect

# Create your views here.

from django.http import HttpResponse

from django.template import Template, Context

from django.shortcuts import render


def market(request):
    return render(request, "index.html")



def carrito(request):
    if request.method == "POST":
        # Si el formulario se envía, redirige al usuario a la página de destino
        return redirect('carrito')  # 'pagina_destino' es el nombre de la URL de destino

    return render(request, 'carrito.html')
    
    
