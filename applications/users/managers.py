from django.db import models
from django.contrib.auth.models import BaseUserManager

class UsuarioManager(BaseUserManager):
    def create_user(self, dni, nombre, apellido, fecha_nacimiento, sexo, email, password=None):
        if not dni:
            raise ValueError("El usuario debe tener un DNI")
        if not email:
            raise ValueError("El usuario debe tener un correo electrónico")
        
        email = self.normalize_email(email)
        usuario = self.model(
            dni=dni,
            nombre=nombre,
            apellido=apellido,
            fecha_nacimiento=fecha_nacimiento,
            sexo=sexo,
            email=email
        )
        usuario.set_password(password)
        usuario.save(using=self._db)
        return usuario

    def create_superuser(self, dni, nombre, apellido, fecha_nacimiento, sexo, email, password):
        usuario = self.create_user(dni, nombre, apellido, fecha_nacimiento, sexo, email, password)
        usuario.is_staff = True
        usuario.is_superuser = True
        usuario.save(using=self._db)
        return usuario