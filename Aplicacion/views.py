from django.shortcuts import render, redirect
from django.http import HttpResponse

nombres = []

# Create your views here.
def main(request):
    tipo = None
    mensaje = None

    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        
        if nombre in nombres:
            tipo = 'Incorrecto'
            mensaje = 'No se pudo registrar al usuario'
            
        else:
            nombres.append(nombre)
            tipo = 'Correcto'
            mensaje = 'El usuario fue registrado exitosamente.'
    
    return render(request, 'main.html', {
        'mensaje' : mensaje,
        'nombres' : nombres,
        'tipo' : tipo
    })
    
def usuario(request, nombre):
    
    if nombre in nombres:
        return render(request, 'nombre.html', {
            'nombre' : nombre
        })
    
    return render(request, 'error404.html')

def busqueda(request):
    subcadenas = []
    mensaje = None
    
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        
        if nombre in nombres:
            return redirect('user', nombre=nombre)
        
        else:
            # Vamos a recorrer todos los nombres en la lista de usuarios
            for nombre_lista in nombres:

                if nombre.lower() in nombre_lista.lower():
                    subcadenas.append(nombre_lista)
                
                
            if len(subcadenas) > 0:
                mensaje = 'Se encontraron coincidencias.'
                
            else:
                mensaje = 'No se encontraron resultados similares.'
                
            return render(request, 'search.html', {
                'subcadenas' : subcadenas,
                'mensaje' : mensaje
            })
    
    return render(request, 'search.html')