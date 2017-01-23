#!/usr/bin/python
# -*- coding: utf8 -*-
from rest_framework import serializers
from control_personal.models import Usuario


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
	fields = '__all__'
        model = Usuario
