from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UsuarioManager
# Create your models here.





class Usuario (AbstractBaseUser,PermissionsMixin):
    SEXO_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Femenino'),
        ('O', 'Otro'),
    )
    
    dni = models.CharField(max_length=8, unique=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    email = models.EmailField(unique=True)
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    objects = UsuarioManager()
    
    USERNAME_FIELD = 'dni'
    REQUIRED_FIELDS = ['nombre', 'apellido', 'fecha_nacimiento', 'sexo', 'email']
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"