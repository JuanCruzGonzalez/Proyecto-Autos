from django.shortcuts import render

# Create your views here.
def Inicio(request):
    return render(request, 'PaginaAutos/index.html')

def Autos(request):
    return render(request, 'PaginaAutos/autos.html')

def Marcas(request):
    return render(request, 'PaginaAutos/marcas.html')

def Motores(request):
    return render(request, 'PaginaAutos/motores.html')

def Nosotros(request):
    return render(request, 'PaginaAutos/nosotros.html')

def Contacto(request):
    return render(request, 'PaginaAutos/contacto.html')


