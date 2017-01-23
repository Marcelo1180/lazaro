from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.
class UsuarioManager(BaseUserManager):
    def nombreCompleto(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

class Usuario(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    objects = UsuarioManager()

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    # def __str__(self):
    #     return self.objects.nombreCompleto()

    # def __unicode__(self):
    #     return self.objects.nombreCompleto()
