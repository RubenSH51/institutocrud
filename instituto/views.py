from django.shortcuts import render, get_object_or_404,redirect
from .models import Instituto
from .forms import InstitutoForm


def instituto_list(request):
    institutos = Instituto.objects.all()
    return render(request, 'instituto/instituto_list.html', {'institutos': institutos})

def instituto_create(request):
    if request.method == 'POST':
        form = InstitutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('instituto_list')
    else:
        form = InstitutoForm()
    return render(request, 'instituto/instituto_form.html', {'form': form})

def instituto_update(request, id):
    instituto = get_object_or_404(Instituto, id=id)

    if request.method == 'POST':
        form = InstitutoForm(request.POST, instance=instituto)
        if form.is_valid():
            form.save()
            return redirect('instituto_list')
    else:
        form = InstitutoForm(instance=instituto)
    
    return render(request, 'instituto/instituto_edit.html', {'form': form, "instituto": instituto})



def instituto_delete(request, id):
    instituto = get_object_or_404(Instituto, id=id)
    instituto.delete()
    return redirect('instituto_list')
