# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Jugement, Extrait, Mariage, Deces


class JugementAdmin(admin.ModelAdmin):
    list_display = ['num_jugement', 'nom', 'prenoms', 'sexe', 'date_naiss', 'heure_naiss', 'hopital', 'mere', 'username']
    list_display_links = ['num_jugement', ]
    list_filter = ('hopital',)
    search_fields = ['num_jugement', 'nom', ]
    ordering = ['-ajouter_le', ]
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
    list_display = ['num_extrait', 'nom', 'prenoms','sexe','date_naiss', 'hopital','mere', 'pere', 'EXTRAIT', 'username']
    list_display_links = ['num_extrait',]
    list_filter = ('annee', 'hopital',)
    search_fields = ['num_extrait', 'nom',]
    ordering = ['-ajouter_le',]
    #exclude=("num_extrait ",)
    #readonly_fields=('num_extrait', )
    fieldsets = (
        ('INFORMATIONS GENERALES', {"fields": ('archive',('annee', 'num_extrait'), ('document'),)}),
        ('INFORMATIONS PERSONNELES', {"fields": (('sexe', 'commune', 'hopital') ,('nom', 'prenoms'), ('date_naiss', 'heure_naiss'), ('jugement', 'num_jugement'), )}),
        ('PARENTS', {"fields": (('mere'), ('date_naiss_mere', 'lieu_naiss_mere'), ('nationalite_mere', 'profession_mere'), ('pere'),('date_naiss_pere', 'lieu_naiss_pere'), ('nationalite_pere', 'profession_pere'), )}),
        #('MENTIONS (EVENTUELLEMENT)', {"fields": (('mariage', 'lieu_mariage'), 'conjoint', ('divorce', 'deces'), 'lieu_deces')}),
    )
    def save_model(self, request, obj, form, change):
      if obj.username == "": obj.username = request.user.username
      obj.save()


class MariageAdmin(admin.ModelAdmin):
    list_display = ['num_mariage', 'demandeur', 'demandeur2','regime','date_mariage', 'lieu_mariage', 'username']
    # list_display_links = ['num_extrait',]
    # list_filter = ('hopital',)
    # search_fields = ['num_extrait', 'nom',]
    ordering = ['-ajouter_le', ]

    fieldsets = (
        ('INFORMATIONS GENERALES', {"fields": ('archive', ('annee', 'num_mariage'), ('categorie'),)}),
        ('INFORMATIONS MARIE(E)', {"fields": ('demandeur', ('date_naiss_demandeur', 'lieu_naiss_demandeur'), ('contact_demandeur', 'contact2_demandeur', ), ('profession_demandeur', 'domicile_demandeur'),
                                               ('pere_demandeur', 'mere_demandeur'), 'temoin_demandeur')}),
        ('INFORMATIONS CONJOINT(E)', {"fields": (
        'demandeur2', ('date_naiss_demandeur2', 'lieu_naiss_demandeur2'), ('contact_demandeur2', 'contact2_demandeur2',),
        ('profession_demandeur2', 'domicile_demandeur2'),
        ('pere_demandeur2', 'mere_demandeur2'), 'temoin_demandeur2')}),
        ('DETAILS MARIAGE', {"fields": ('regime', ('date_mariage', 'heure_mariage'), ('lieu_mariage'),)}),
        ('DETAILS DIVORCE', {"fields": (('date_divorce'), ('details_divorce'),)}),
    )
    def save_model(self, request, obj, form, change):
        if obj.username == "": obj.username = request.user.username
        obj.save()

class DecesAdmin(admin.ModelAdmin):
    list_display = ['num_deces', 'nom_et_prenoms', 'date_naiss','lieu_naiss', 'date_deces', 'heure_deces', 'lieu_deces', 'username']
    ordering = ['-ajouter_le', ]
    fieldsets = (
        ('INFORMATIONS GENERALES', {"fields": ('archive', ('annee', 'num_deces'), ('categorie'),)}),
        ('INFORMATIONS PERSONNELES', {"fields": ('sexe', ('nom_et_prenoms'), ('date_naiss', 'lieu_naiss'),('profession', 'domicile'))}),
        ('INFORMATIONS PARENTS', {"fields": (('pere'), ('mere'),)}),
        ('INFORMATIONS DECES', {"fields": (('date_deces', 'heure_deces'), ('lieu_deces'), ('cause_deces'),)}),
    )
    def save_model(self, request, obj, form, change):
        if obj.username == "": obj.username = request.user.username
        obj.save()


admin.site.register(Jugement, JugementAdmin)
admin.site.register(Extrait, ExtraitsAdmin)
admin.site.register(Mariage, MariageAdmin)
admin.site.register(Deces, DecesAdmin)
