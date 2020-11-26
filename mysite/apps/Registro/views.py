from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Portico, Bicicleta
from .forms import porticoForm, bicicletaForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy

# ------------- importaciones API ---------------------
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PorticoSerializer
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import status
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser


# listar porticos y bicicletas


def listar_porticos(request):
    porticos = Portico.objects.all()
    return render(request, "Registro/listar_porticos.html", {'porticos': porticos})


def listar_bicicletas(request):
    bicicletas = Bicicleta.objects.all()
    return render(request, "Registro/listar_bicicletas.html", {'bicicletas': bicicletas})

 # agregar portico


def agregar_portico(request):
    if request.method == "POST":
        form = porticoForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect("/agregar_portico")
    else:
        form = porticoForm()
        return render(request, "Registro/agregar_portico.html", {'form': form})


# borrar portico

def borrar_portico(request, portico_id):
    # Recuperamos la instancia de la carrera y la borramos
    instancia = Portico.objects.get(id=portico_id)
    instancia.delete()

    # Después redireccionamos de nuevo a la lista
    return redirect('listar_portico')

# editar porticco


def editar_portico(request, portico_id):
    # Recuperamos la instancia de la carrera
    instancia = Portico.objects.get(id=portico_id)

    # Creamos el formulario con los datos de la instancia
    form = porticoForm(instance=instancia)

    # Comprobamos si se ha enviado el formulario
    if request.method == "POST":
        # Actualizamos el formulario con los datos recibidos
        form = porticoForm(request.POST, instance=instancia)
        # Si el formulario es válido...
        if form.is_valid():
            # Guardamos el formulario pero sin confirmarlo,
            # así conseguiremos una instancia para manipular antes de grabar
            instancia = form.save(commit=False)
            # Podemos guardar cuando queramos
            instancia.save()

    # Si llegamos al final renderizamos el formulario
    return render(request, "Registro/editar_portico.html", {'form': form})


# clases crear portico

class PorticoCreate(CreateView):
    model = Portico
    form_class = porticoForm
    template_name = 'Registro/agregar_portico.html'
    success_url = reverse_lazy("list_portico")

# clase listar portico


class PorticoList(ListView):
    model = Portico
    template_name = 'Registro/listar_porticos_filtros.html'

# clase modificar portico


class PorticoUpdate(UpdateView):
    model = Portico
    form_class = porticoForm
    template_name = 'Registro/editar_portico.html'
    success_url = reverse_lazy('list_portico')

# clase borrar portico


class PorticoDelete(DeleteView):
    model = Portico
    template_name = 'Registro/portico_delete.html'
    success_url = reverse_lazy('list_portico')


# agregar bicicleta

def agregar_bicicleta(request):
    if request.method == "POST":
        form = bicicletaForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect("/agregar_bicicleta")
    else:
        form = bicicletaForm()
        return render(request, "Registro/agregar_bicicleta.html", {'form': form})


# borrar bicicleta

def borrar_bicicleta(request, bicicleta_id):
    # Recuperamos la instancia de la carrera y la borramos
    instancia = Bicicleta.objects.get(id=bicicleta_id)
    instancia.delete()

    # Después redireccionamos de nuevo a la lista
    return redirect('listar_bicicletas')

# editar bicicleta


def editar_bicicleta(request, bicicleta_id):
    # Recuperamos la instancia de la carrera
    instancia = Bicicleta.objects.get(id=bicicleta_id)

    # Creamos el formulario con los datos de la instancia
    form = bicicletaForm(instance=instancia)

    # Comprobamos si se ha enviado el formulario
    if request.method == "POST":
        # Actualizamos el formulario con los datos recibidos
        form = bicicletaForm(request.POST, instance=instancia)
        # Si el formulario es válido...
        if form.is_valid():
            # Guardamos el formulario pero sin confirmarlo,
            # así conseguiremos una instancia para manipular antes de grabar
            instancia = form.save(commit=False)
            # Podemos guardar cuando queramos
            instancia.save()

    # Si llegamos al final renderizamos el formulario
    return render(request, "Registro/editar_bicicleta.html", {'form': form})


# clases crear bicicleta

class BicicletaCreate(CreateView):
    model = Bicicleta
    form_class = bicicletaForm
    template_name = 'Registro/agregar_bicicleta.html'
    success_url = reverse_lazy("listar_bicicletas")

# clase listar bicicleta


class BicicletaList(ListView):
    model = Bicicleta
    template_name = 'Registro/listar_bicicletas.html'

# clase modificar bicicleta


class BicicletaUpdate(UpdateView):
    model = Bicicleta
    form_class = bicicletaForm
    template_name = 'Registro/editar_bicicleta.html'
    success_url = reverse_lazy('listar_bicicletas')

# clase borrar bicicleta


class BicicletaDelete(DeleteView):
    model = Bicicleta
    template_name = 'Registro/bicicleta_delete.html'
    success_url = reverse_lazy('listar_bicicletas')

# filtros


def ListPortico(request):
    lista = Portico.objects.all()
    ubicacion = request.GET.get('ubicacion')
    id_portico = request.GET.get('id-portico')

    # if 'btn-buscarIdPorticos' in request.GET:
    #     if cant_semestres:
    #         lista = Portico.objects.filter(semestres__gte=cant_semestres)
    if 'btn-id-portico' in request.GET:
        if id_portico:
            lista = Portico.objects.filter(id_portico__icontains=id_portico)

    elif 'btn-ubicacion' in request.GET:
        if ubicacion:
            lista = Portico.objects.filter(ubicacion__icontains=ubicacion)

    data = {
        'object_list': lista
    }
    return render(request, 'Registro/listar_porticos_filtros.html', data)


@api_view(['GET', 'POST'])
def portico_collection(request):
    if request.method == 'GET':
        porticos = Portico.objects.all()
        serializer = PorticoSerializer(porticos, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PorticoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # Si el proceso de deserialización funciona, devolvemos una respuesta con un código 201 (creado
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # si falla el proceso de deserialización, devolvemos una respuesta 400
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def portico_element(request, pk):
    portico = get_object_or_404(Portico, id_portico=pk)

    if request.method == 'GET':
        serializer = PorticoSerializer(portico)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        portico.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        portico_new = JSONParser().parse(request)
        serializer = PorticoSerializer(portico, data=portico_new)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
