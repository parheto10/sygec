# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from annoying.functions import get_object_or_None
from django.core.exceptions import ValidationError

# Create your models here.
import datetime


class Distict(models.Model):
    Distict = (
        ('abidjan', 'ABIDJAN'),
        ('yamoussoukro', 'YAMOUSSOUKRO'),
        ('lacs', 'LACS'),
        ('comoe', 'COMOE'),
        ('denguele', 'DENGUELE'),
        ('goh-djiboua', 'GÔH-DJIBOUA'),
        ('lagunes', 'LAGUNES'),
        ('montagnes', 'MONTAGNES'),
        ('marahoué', 'SASSANDRA-MARAHOUE'),
        ('bas-bassandra', 'BAS-SASSANDRA'),
        ('savanes', 'SAVANES'),
        ('vallee du Bandama', 'VALLEE DU BANDAMA'),
        ('woroba', 'WOROBA'),
        ('zanzan', 'ZANZAN'),
    )
    district = models.CharField(max_length=250, verbose_name="DISTRICT", choices=Distict, default="woroba")
    chef_lieu = models.CharField(max_length=250, verbose_name="CHEF LIEU DE DISTRICT")
    president = models.CharField(max_length=500, verbose_name="NOM ET PRENOMS DU CONSEILLER REGIONAL")
    nbr_region = models.IntegerField(default=0, verbose_name="PRECISER LE NOMBRE DE REGION")

    """
    def clean(self):
       tot = District.objects.count()
       if tot != 0:   raise ValidationError("Un seul District ne peut être configuré")
     """

    def save(self, force_insert=False, force_update=False):
        self.district = self.district.upper()
        self.chef_lieu = self.chef_lieu.upper()
        self.president = self.president.upper()
        super(Distict, self).save(force_insert, force_update)

    class Meta:
        verbose_name_plural = "DISTRICTS"
        verbose_name = "district"

    def __unicode__(self):
        return "%s" % self.chef_lieu


def number():
    no = Region.objects.count()
    if no == None:
        return 1
    else:
        return no + 1


class Region(models.Model):
    Region = (
        ('bere', 'BERE'),
        ('bafing', 'BAFING'),
        ('worodougou', 'WORODOUGOU'),
    )
    Region_Chef = (
        ('mankono', 'MANKONO'),
        ('touba', 'TOUBA'),
        ('seguela', 'SEGUELA'),
    )
    district = models.ForeignKey(Distict, verbose_name="DISTRICT")
    code = models.CharField(max_length=5, verbose_name="CODE REGION")
    region = models.CharField(max_length=250, verbose_name="REGION", choices=Region, default="worodougou")
    chef_lieu = models.CharField(max_length=250, verbose_name="CHEF LIEU DE REGION", choices=Region_Chef,
                                 default="seguela")
    habitant = models.IntegerField(default=0, verbose_name="NOMBRE D'HABITANT")

    def save(self, force_insert=False, force_update=False):
        self.chef_lieu = self.libelle.upper()
        self.president = self.president.upper()
        super(Distict, self).save(force_insert, force_update)

    class Meta:
        verbose_name_plural = "COMMUNES"
        verbose_name = "comune"

    def __unicode__(self):
        return "%s" % self.chef_lieu


class Mairie(models.Model):
    # region    = models.ForeignKey(Region)
    libelle = models.CharField(max_length=150, verbose_name="MAIRIE", unique=True)
    maire = models.CharField(max_length=500, verbose_name="Nom et Prenoms du Maire")
    adjoint1 = models.CharField(max_length=500, verbose_name="Nom et Prenoms du 1er Adjoint")
    adjoint2 = models.CharField(max_length=500, verbose_name="Nom et Prenoms du 2ème Adjoint")
    telephone1 = models.CharField(max_length=50, verbose_name="Telephone 1")
    telephone2 = models.CharField(max_length=50, verbose_name="Telephone 2", blank=True, null=True)
    faxe = models.CharField(max_length=50, verbose_name="Faxe", blank=True, null=True)
    adresse = models.CharField(max_length=100, verbose_name="Adresse Postale", blank=True)
    email = models.CharField(max_length=100, verbose_name="Adresse Email", blank=True)
    site = models.CharField(max_length=100, verbose_name="Site Web", blank=True)
    logo = models.ImageField(upload_to='logos', blank=True, null=True)

    def save(self, force_insert=False, force_update=False):
        self.libelle = self.libelle.upper()
        super(Mairie, self).save(force_insert, force_update)

    def clean(self):
        if not self.id:
            tot = Mairie.objects.count()
            if tot != 0:   raise ValidationError("Mairie déjà créee")

    def __unicode__(self):
        return "%s" % self.libelle

    class Meta:
        verbose_name_plural = "MAIRIES"
        verbose_name = "mairie"


def number():
    no = Centre.objects.count()
    if no == None:
        return 1
    else:
        return no + 1


class Centre(models.Model):
    mairie = models.ForeignKey(Mairie, verbose_name="MAIRIE")
    code = models.CharField(max_length=5, verbose_name="CODE ETABLISSEMENT SANITAIRE")
    libelle = models.CharField(max_length=500, verbose_name="NOM ETABLISSEMENT SANITAIRE")
    emplacement = models.CharField(max_length=500, verbose_name="EMPLACEMENT DU CENTRE SANITAIRE")

    def zcode(self):
        return self.code.zfill(5).upper()

    def save(self, force_insert=False, force_update=False):
        if not self.id:
            self.libelle = self.libelle.upper()
            self.emplacement = self.emplacement.upper()
            super(Centre, self).save(force_insert, force_update)

    class Meta:
        verbose_name_plural = "CENTRES DE SANTE"
        verbose_name = "centre de sante"

    def __unicode__(self):
        return "%s" % self.libelle
