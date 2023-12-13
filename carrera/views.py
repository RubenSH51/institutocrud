from django.shortcuts import render, redirect, get_object_or_404
from .models import Carrera
from .forms import CarreraForm

def carrera_list(request):
    carreras = Carrera.objects.all()
    return render(request, 'carrera/carrera_list.html', {'carreras': carreras})

def carrera_detail(request, pk):
    carrera = get_object_or_404(Carrera, pk=pk)
    return render(request, 'carrera/carrera_detail.html', {'carrera': carrera})

def carrera_create(request):
    if request.method == 'POST':
        form = CarreraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('carrera_list')
    else:
        form = CarreraForm()
    return render(request, 'carrera/carrera_form.html', {'form': form})

def carrera_update(request, id):
    carrera = get_object_or_404(Carrera, id=id)
    if request.method == 'POST':
        form = CarreraForm(request.POST, instance=carrera)
        if form.is_valid():
            form.save()
            return redirect('carrera_list')
    else:
        form = CarreraForm(instance=carrera)
    return render(request, 'carrera/carrera_edit.html', {'form': form,"carrera":carrera})
    






def carrera_delete(request, id):
    carrera = get_object_or_404(Carrera, id=id)
    carrera.delete()
    return redirect('carrera_list')
