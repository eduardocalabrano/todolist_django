from django import forms
from .models import Usuario

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control form-control-sm campos_new_user', 'placeholder': 'email', 'id': 'nuevo_email'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control form-control-sm campos_new_user', 'placeholder': 'Nombre', 'id': 'nuevo_nombre'}),
            'color': forms.TextInput(attrs={'class': 'form-control form-control-sm campos_new_user', 'placeholder': 'color', 'id': 'nuevo_color'}),
        }
        fields = ('nombre', 'email','color',)
