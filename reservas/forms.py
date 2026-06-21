from django import forms
from .models import Reserva
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['nombre_cliente', 'cancha', 'fecha', 'horario']
        widgets = {
            'nombre_cliente': forms.TextInput(attrs= {'class':'form-control'}),
            'cancha': forms.Select(attrs= {'class':'form-select'}),
            'fecha': forms.DateInput(attrs= {'class':'form-control','type':'date'}),
            'horario': forms.Select(attrs= {'class':'form-select'})
            }
    
    def clean(self):
        cleaned_data = super().clean()

        cancha = cleaned_data.get('cancha')
        fecha = cleaned_data.get('fecha')
        horario = cleaned_data.get('horario')

        if Reserva.objects.filter(
            cancha=cancha,
            fecha=fecha,
            horario=horario
        ).exclude(pk=self.instance.pk).exists():
            
            raise forms.ValidationError(
                'Ese horario ya está reservado para esa cancha'
            )
        
        return cleaned_data
    
class RegistroUsuarioForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]
