from django import forms
from .models import Usuario
from django.contrib.auth.forms import AuthenticationForm


class BootstrapFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "form-control"

class RegistroForm(forms.ModelForm):
    # password = forms.CharField(widget=forms.PasswordInput)
    # confirmar_password = forms.CharField(widget=forms.PasswordInput)


    password = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Ingresa tu contraseña"
        })
    )
    confirmar_password = forms.CharField(
        label="Confirmar Contraseña",
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Repite tu contraseña"
        })
    )

    class Meta:
        model = Usuario
        fields = ['dni', 'nombre', 'apellido', 'fecha_nacimiento', 'sexo', 'email']
        widgets = {
            'dni': forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Ingresa tu DNI"
            }),
            'nombre': forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Ingresa tu nombre"
            }),
            'apellido': forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Ingresa tu apellido"
            }),
            'fecha_nacimiento': forms.DateInput(attrs={
                "class": "form-control",
                "type": "date"
            }),
            'sexo': forms.Select(attrs={
                "class": "form-control"
            }),
            'email': forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "ejemplo@mail.com"
            }),
        }
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirmar_password = cleaned_data.get('confirmar_password')
        if password != confirmar_password:
            raise forms.ValidationError("Las contraseñas no coinciden")
        return cleaned_data

class LoginForm(AuthenticationForm):
    username = forms.CharField(
        label="DNI",
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Ingresa tu DNI"
        })
    )
    password = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Ingresa tu contraseña"
        })
    )