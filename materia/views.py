from django.shortcuts import render, redirect, get_object_or_404
from .models import Materia
from .forms import MateriaForm

def materia_list(request):
    materias = Materia.objects.all()
    return render(request, 'materia/materia_list.html', {'materias': materias})

def materia_detail(request, id):
    materia = get_object_or_404(Materia, id=id)
    return render(request, 'materia/materia_detail.html', {'materia': materia})

def materia_create(request):
    if request.method == 'POST':
        form = MateriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('materia_list')
    else:
        form = MateriaForm()
    return render(request, 'materia/materia_form.html', {'form': form})

def materia_update(request, id):
    materia = get_object_or_404(Materia, id=id)
    if request.method == 'POST':
        form = MateriaForm(request.POST, instance=materia)
        if form.is_valid():
            form.save()
            return redirect('materia_list')
    else:
        form = MateriaForm(instance=materia)
    return render(request, 'materia/materia_edit.html', {'form': form, "materia": materia})

def materia_delete(request, id):
    materia = get_object_or_404(Materia, id=id)
    materia.delete()
    return redirect('materia_list')
