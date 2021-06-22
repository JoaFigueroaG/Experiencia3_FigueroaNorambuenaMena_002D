from django import forms
from .models import Client



class RegistroForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = [
            'rut_client',
            'first_name',
            'email',
            'password',
        ]
   