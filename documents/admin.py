# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Jugement, Extrait, Mariage, Deces


class JugementAdmin(admin.ModelAdmin):
    list_display = ['num_jugement', 'nom', 'prenoms', 'sexe', 'date_naiss', 'heure_naiss', 'hopital', 'mere']
    list_display_links = ['num_jugement', ]
    list_filter = ('hopital',)
    search_fields = ['num_jugement', 'nom', ]
    ordering = ['date_naiss', ]
    fieldsets = (
        ('INFORMATIONS GENERALES', {"fields": ('archive', ('annee', 'num_jugement'), ('document'),)}),
        ('INFORMATIONS PERSONNELES', {"fields": (('sexe', 'hopital'), ('nom', 'prenoms'), ('date_naiss', 'heure_naiss'), ('commune', 'officie'),)}),
        ('PARENTS - PERE', {"fields": (('pere', 'nationalite_pere'), ('date_naiss_pere', 'lieu_naiss_pere'),('profession_pere', 'domicile_pere'))}),
        ('PARENTS - MERE', {"fields": (('mere', 'nationalite_mere'), ('date_naiss_mere', 'lieu_naiss_mere'), ('profession_mere', 'domicile_mere'))}),

    )

    def save_model(self, request, obj, form, change):
      if obj.username == "": obj.username = request.user.username
      obj.save()

class ExtraitsAdmin(admin.ModelAdmin):
    list_display = ['num_extrait', 'nom', 'prenoms','sexe','date_naiss', 'heure_naiss', 'hopital','mere','EXTRAIT']
    list_display_links = ['num_extrait',]
    list_filter = ('hopital',)
    search_fields = ['num_extrait', 'nom',]
    ordering = ['date_naiss',]
    #exclude=("num_extrait ",)
    readonly_fields=('num_extrait', )
    fieldsets = (
        ('INFORMATIONS GENERALES', {"fields": ('archive',('annee', 'num_extrait'), ('document'),)}),
        ('INFORMATIONS PERSONNELES', {"fields": (('sexe', 'commune', 'hopital') ,('nom', 'prenoms'), ('date_naiss', 'heure_naiss'), ('jugement', 'num_jugement'), )}),
        ('PARENTS', {"fields": (('mere'), ('date_naiss_mere', 'lieu_naiss_mere'), ('nationalite_mere', 'profession_mere'), ('pere'),('date_naiss_pere', 'lieu_naiss_pere'), ('nationalite_pere', 'profession_pere'), )}),
        #('MENTIONS (EVENTUELLEMENT)', {"fields": (('mariage', 'lieu_mariage'), 'conjoint', ('divorce', 'deces'), 'lieu_deces')}),
    )

    def save_model(self, request, obj, form, change):
      if obj.username == "": obj.username = request.user.username
      obj.save()


admin.site.register(Jugement, JugementAdmin)
admin.site.register(Extrait, ExtraitsAdmin)
admin.site.register(Mariage)
admin.site.register(Deces)
