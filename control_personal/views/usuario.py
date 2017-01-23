#!/usr/bin/python
# -*- coding: utf8 -*-
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, DjangoModelPermissions
from control_personal.serializers import UsuarioSerializer
from control_personal.models import Usuario


class UsuarioViewSet(viewsets.ModelViewSet):
    """
    ## Usuarios del sistema
    Trabajar con usuarios del sistema, solo tiene acceso el administrador del sistema
    """
    permission_classes = [IsAdminUser]
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    filter_backends = (filters.SearchFilter, filters.OrderingFilter,)
    search_fields = ('username',)
    ordering_fields = '__all__'
