from django import forms
from .models import Instituto

class InstitutoForm(forms.ModelForm):
    class Meta:
        model = Instituto
        fields = ['nombre', 'direccion', 'telefono']
