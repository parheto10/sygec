# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Region, Centre, Mairie, Distict

class MairieAdmin(admin.ModelAdmin):
    list_display = ['libelle', 'maire', 'telephone1',  'thumb']
    list_display_links = ['libelle', ]
    fieldsets = (
        ('INFORMATIONS MAIRIE', {"fields": (('libelle', 'maire'), ('adjoint1', 'adjoint2'), ('telephone1', 'telephone2'), ('faxe','adresse'), ('email', 'site'), 'logo')}),
    )

class CentreAdmin(admin.ModelAdmin):
    list_display = ['code', 'libelle', 'emplacement', 'mairie']
    list_display_links = ['libelle', ]
    ordering = ['libelle', ]


admin.site.register(Mairie, MairieAdmin)
admin.site.register(Centre, CentreAdmin)