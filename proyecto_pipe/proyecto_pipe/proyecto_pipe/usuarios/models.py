from django.db import models
from django.contrib.auth.models import AbstractUser, Permission

class Usuario(AbstractUser):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    contraseña = models.CharField(max_length=128)
    correo = models.EmailField(unique=True)
    usuario = models.CharField(max_length=150, unique=True)
    groups = models.ManyToManyField(
        Permission,
        related_name='usuario_groups',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='usuario_user_permissions',
    )
    
    
    
    
    
    def __str__(self):
        return self.username