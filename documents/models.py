# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.exceptions import ValidationError
from django.db import models
import datetime
from parametres.models import Distict, Region, Mairie, Centre

TYPE_DOC = (
    ('ACTE DE NAISSANCES', (
        ("normal", "NORMAL"),
        ("copie", "COPIE INTEGRALE / JUGEMENT SUPPLETIF"),
    )
     ),
)

TYPE_MENTION = (
    ('PRECISER LA MENTIONS', (
        ("mariage", "ACTE DE MARIAGE"),
        ("deces", "ACTE DE DECES"),
    )
     ),
)


def number():
    no = Extrait.objects.count()
    if no == None:
        return 1
    else:
        return no + 1


class Jugement(models.Model):
    YEAR_CHOICES = []
    for r in range(1960, (datetime.datetime.now().year + 1)):
        YEAR_CHOICES.append((r, r))

    Sexe = (
        ('M', 'Masculin'),
        ('F', 'Feminin'),
    )
    # Infos Gles
    username = models.CharField(max_length=25, verbose_name="TRAITE PAR", editable=False)
    archive = models.BooleanField(default=False, verbose_name="ARCHIVE")
    annee = models.IntegerField(verbose_name='ANNEE DU REGISTRE', choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    num_jugement = models.CharField(max_length=150, blank=True, verbose_name='NUMERO JUGEMENT', help_text="UNIQUEMENT POUR LES ARCCHIVES")
    document = models.CharField(max_length=150, verbose_name='NATURE DU DOCUMENT', choices=TYPE_DOC, default="copie")

    # informations recipiendaire
    sexe = models.CharField(max_length=150, verbose_name='PRECISER LE SEXE', choices=Sexe)
    nom = models.CharField(max_length=250, verbose_name='NOM')
    prenoms = models.CharField(max_length=250, verbose_name='PRENOMS')
    date_naiss = models.DateField(verbose_name='DATE DE NAISSANCE')
    heure_naiss = models.TimeField(verbose_name='LIEU DE NAISSANCE')
    hopital = models.ForeignKey(Centre)
    commune = models.ForeignKey(Mairie)
    officie = models.CharField(max_length=500, verbose_name="NOM ET PRENOMS OFFICIER")

    # parents
    pere = models.CharField(max_length=250, verbose_name='NOM ET PRENOMS DU PERE', blank=True)
    nationalite_pere = models.CharField(max_length=250, verbose_name='NATIONALITE DU PERE', blank=True)
    date_naiss_pere = models.DateField(verbose_name='DATE DE NAISSANCE DU PERE', blank=True)
    lieu_naiss_pere = models.DateField(verbose_name='LIEU DE NAISSANCE DU PERE', blank=True)
    profession_pere = models.CharField(max_length=250, verbose_name='PROFESSION DU PERE', blank=True)
    domicile_pere = models.CharField(max_length=250, verbose_name='LIEU DE RESIDENCE DU PERE', blank=True)

    mere = models.CharField(max_length=250, verbose_name='NOM ET PRENOMS DE LA MERE')
    nationalite_mere = models.CharField(max_length=250, verbose_name='NATIONALITE DE LA MERE', blank=True)
    date_naiss_mere = models.DateField(verbose_name='DATE DE NAISSANCE DE LA MERE', blank=True)
    lieu_naiss_mere = models.DateField(verbose_name='LIEU DE NAISSANCE DE LA MERE', blank=True)
    profession_mere = models.CharField(max_length=250, verbose_name='PROFESSION DE LA MERE', blank=True)
    domicile_mere = models.CharField(max_length=250, verbose_name='LIEU DE RESIDENCE DE LA MERE', blank=True)
    ajouter_le = models.DateTimeField(auto_now_add=True, auto_now=False)
    modifier_le = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return 'Jugement Supplétif de + %s + %s' % (self.nom, self.prenoms)

    def clean(self):
        if self.archive == False and self.num_jugement != "":  raise ValidationError(
            "Pour les nouveaux Jugements, pas besoin de saisir le numero. Il est géré automatiquement par le système")

    class Meta:
        verbose_name_plural = "JUGEMENTS SUPPLETIFS"
        verbose_name = "Jugement Suppletif"

    def save(self, force_insert=False, force_update=False):
        self.nom = self.nom.upper()
        self.prenoms = self.prenoms.upper()
        self.hopital = self.hopital.upper()
        self.officie = self.officie.upper()

        self.pere = self.pere.upper()
        self.lieu_naiss_pere = self.lieu_naiss_pere.upper()
        self.domicile_pere = self.domicile_pere.upper()

        self.mere = self.mere.upper()
        self.lieu_naiss_mere = self.lieu_naiss_mere.upper()
        self.domicile_mere = self.domicile_mere.upper()

        # numerotation automatique
        if self.archive == False:
            last_number = 500
            tot = Jugement.objects.count()
            numero = last_number + 1
            madate = datetime.date.today()
            self.num_jugement = "%s du %s" % (numero, datetime.date.strftime(madate, '%d/%m/%Y'))

        super(Jugement, self).save(force_insert, force_update)


class Extrait(models.Model):
    YEAR_CHOICES = []
    for r in range(1960, (datetime.datetime.now().year + 1)):
        YEAR_CHOICES.append((r, r))

    Sexe = (
        ('M', 'Masculin'),
        ('F', 'Feminin'),
    )

    Jugement_Choice = (
        ('oui', 'OUI'),
        ('non', 'NON')
    )

    # Infos Gles
    username = models.CharField(max_length=25, verbose_name="TRAITE PAR", editable=False)
    archive = models.BooleanField(default=False, verbose_name="ARCHIVE")
    annee = models.IntegerField(verbose_name='ANNEE DU REGISTRE', choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    num_extrait = models.CharField(max_length=150, blank=True, verbose_name='NUMERO EXTRAIT', help_text="UNIQUEMENT POUR LES ARCCHIVES")
    document = models.CharField(max_length=150, verbose_name='NATURE DU DOCUMENT', choices=TYPE_DOC, default="normal")

    # informations recipiendaire
    sexe = models.CharField(max_length=150, verbose_name='SEXE', choices=Sexe)
    nom = models.CharField(max_length=250, verbose_name='NOM')
    prenoms = models.CharField(max_length=250, verbose_name='PRENOMS')
    date_naiss = models.DateField(verbose_name='DATE DE NAISSANCE')
    heure_naiss = models.TimeField(verbose_name='HEURE DE NAISSANCE', blank=True)
    hopital = models.ForeignKey(Centre)
    commune = models.ForeignKey(Mairie)
    jugement = models.CharField(max_length=5, verbose_name="TRANSCRIPTION DE JUGEMENT SUPPLETIF ?", choices=Jugement_Choice, default="non")
    num_jugement = models.CharField(max_length=255, verbose_name="PRECISER LE NUMERO DU JUGEMENT SUPPLETIF", blank=True)

    # parents
    pere = models.CharField(max_length=250, verbose_name='NOM ET PRENOMS DU PERE', blank=True)
    date_naiss_pere = models.DateField(verbose_name='DATE NAISSANCE PERE', blank=True)
    lieu_naiss_pere = models.CharField(max_length=250, verbose_name='LIEU NAISSANCE PERE', blank=True)
    nationalite_pere = models.CharField(max_length=250, verbose_name='NATIONALITE DU PERE', blank=True)
    profession_pere = models.CharField(max_length=250, verbose_name='PROFESSION DU PERE', blank=True)

    # parents
    mere = models.CharField(max_length=250, verbose_name='NOM  ET PRENOMS DE LA MERE')
    date_naiss_mere = models.DateField(verbose_name='DATE NAISSANCE MERE', blank=True)
    lieu_naiss_mere = models.CharField(max_length=250, verbose_name='LIEU NAISSANCE MERE', blank=True)
    nationalite_mere = models.CharField(max_length=250, verbose_name='NATIONALITE DE LA MERE', blank=True)
    profession_mere = models.CharField(max_length=250, verbose_name='PROFESSION DE LA MERE', blank=True)

    ajouter_le = models.DateTimeField(auto_now_add=True, auto_now=False)
    modifier_le = models.DateTimeField(auto_now_add=False, auto_now=True)

    def clean(self):
        if self.archive == False and self.num_extrait != "":  raise ValidationError(
            "Pour les nouveaux extraits, pas besoin de saisir le numero. Il est géré automatiquement par le système")
        if self.jugement == "non" and self.num_jugement != "":
            raise ValidationError(
                "VEUILLEZ PRECISER LE NUMERO DU JUGEMENT SUPPLETIF SVP !")
        else:
            if self.jugement == "oui" and self.num_jugement == "": raise ValidationError(
                "VEUILLEZ PRECISER LE NUMERO DU JUGEMENT SUPPLETIF SVP !"
            )

    def EXTRAIT(self):
        return "<a href='/pdf/extrait/?numero=%s' target='_blank'>Consulter</a>" % (self.num_extrait)

    EXTRAIT.allow_tags = True
    EXTRAIT.short_description = "EXTRAIT PDF"

    class Meta:
        verbose_name_plural = "ACTES DE NAISSANCE"
        verbose_name = "Acte de naissance"

    def save(self, force_insert=False, force_update=False):
        self.nom = self.nom.upper()
        self.prenoms = self.prenoms.upper()
        self.pere = self.pere.upper()
        self.mere = self.mere.upper()

        # numerotation automatique
        if self.archive == False:
            last_number = 500
            tot = Extrait.objects.count()
            numero = last_number + 1
            madate = datetime.date.today()
            self.num_extrait = "%s du %s" % (numero, datetime.date.strftime(madate, '%d/%m/%Y'))

        super(Extrait, self).save(force_insert, force_update)


    def __unicode__(self):
        return 'Extrait de Naissance de + %s + %s' % (self.nom, self.prenoms)


class Mariage(models.Model):
    YEAR_CHOICES = []
    for r in range(2000, (datetime.datetime.now().year + 1)):
        YEAR_CHOICES.append((r, r))

    Regime = (
        ('simple', 'SIMPLE'),
        ('communaute', 'COMUAUTE DE BIEN'),
        ('separation', 'SEPARATION DE BIEN'),
    )
    username = models.CharField(max_length=25, verbose_name="TRAITE PAR", editable=False)
    archive = models.BooleanField(default=False, verbose_name="ARCHIVE")
    annee = models.IntegerField(verbose_name='ANNEE DU REGISTRE', choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    num_mariage = models.CharField(max_length=150, blank=True, verbose_name='NUMERO MARIAGE', help_text="UNIQUEMENT POUR LES ARCCHIVES")
    categorie = models.CharField(verbose_name='TYPE DE DOCUMENT', max_length=50, choices=TYPE_MENTION, default="mariage")

    #emandeur
    demandeur = models.CharField(max_length=250, verbose_name="NOM ET PRENOMS DU DEMANDEUR")
    date_naiss_demandeur = models.DateField(verbose_name="DATE DATE DE NAISSANCE DU DEMANDEUR", blank=True)
    lieu_naiss_demandeur = models.CharField(max_length=500, verbose_name="LIEU DE NASSANCE DU DEMANDEUR", blank=True)
    contact_demandeur = models.CharField(max_length=250, verbose_name='CONTACT1 DEMANDEUR')
    contact2_demandeur = models.CharField(max_length=250, verbose_name='CONTACT2 DEMANDEUR', blank=True)
    profession_demandeur = models.CharField(max_length=500, verbose_name="PROFESSION DEMANDEUR", blank=True)
    domicile_demandeur = models.CharField(max_length=500, verbose_name="DOMICILE DEMANDEUR", blank=True)
    pere_demandeur = models.CharField(max_length=250, verbose_name='NOM ET PRENOMS DU PERE DU DEMANDEUR', blank=True)
    mere_demandeur = models.CharField(max_length=250, verbose_name='NOM ET PRENOMS DE LA MERE DU DEMANDEUR', blank=True)
    temoin_demandeur = models.CharField(max_length=250, verbose_name='NOM ET PRENOMS DU TEMOINS DU DEMANDEUR', blank=True)

    # Avec(Conjoint/conjointe)
    demandeur2 = models.CharField(max_length=250, verbose_name="NOM ET PRENOMS DU CONJOINT(E)")
    date_naiss_demandeur2 = models.DateField(verbose_name="DATE DATE DE NAISSANCE DU CONJOINT(E)", blank=True)
    lieu_naiss_demandeur2 = models.CharField(max_length=500, verbose_name="LIEU DE NASSANCE DU CONJOINT(E)", blank=True)
    contact_demandeur2 = models.CharField(max_length=250, verbose_name='CONTACT1 CONJOINT(E)')
    contact2_demandeur2 = models.CharField(max_length=250, verbose_name='CONTACT2 CONJOINT(E)', blank=True)
    profession_demandeur2 = models.CharField(max_length=500, verbose_name="PROFESSION CONJOINT(E)", blank=True)
    domicile_demandeur2 = models.CharField(max_length=500, verbose_name="DOMICILE CONJOINT(E)", blank=True)
    pere_demandeur2 = models.CharField(max_length=250, verbose_name='NOM ET PRENOMS DU PERE DU CONJOINT(E)', blank=True)
    mere_demandeur2 = models.CharField(max_length=250, verbose_name='NOM ET PRENOMS DE LA MERE DU CONJOINT(E)', blank=True)
    temoin_demandeur2 = models.CharField(max_length=250, verbose_name='NOM ET PRENOMS DU TEMOINS DU CONJOINT(E)', blank=True)

    #details
    date_mariage = models.DateField(verbose_name="DATE MARIAGE")
    heure_mariage = models.DateField(verbose_name="HEURE MARIAGE", blank=True)
    regime = models.CharField(max_length=150, verbose_name="TYPE DE REGIME", choices=Regime)
    lieu_mariage = models.CharField(max_length=500, verbose_name="LIEU DU MARIAGE", blank=True)
    ajouter_le = models.DateTimeField(auto_now_add=True, auto_now=False)
    modifier_le = models.DateTimeField(auto_now_add=False, auto_now=True)

    # divorce
    date_divorce = models.DateField(max_length=250, verbose_name="DATE DIVORCE", blank=True)
    details_divorce = models.TextField(verbose_name="DETAILS DIVORCE", blank=True)

    class Meta:
        verbose_name_plural = "ACTES DE MARIAGE"
        verbose_name = "Acte de Mariage"

    def save(self, force_insert=False, force_update=False):
        self.demandeur = self.demandeur.upper()
        self.demandeur2 = self.demandeur2.upper()
        #self.pere = self.pere.upper()
        #self.mere = self.mere.upper()

        # numerotation automatique
        if self.archive == False:
            last_number = 500
            tot = Mariage.objects.count()
            numero = last_number + 1
            madate = datetime.date.today()
            self.num_mariage = "%s du %s" % (numero, datetime.date.strftime(madate, '%d/%m/%Y'))

        super(Mariage, self).save(force_insert, force_update)

    def __unicode__(self):
        return 'MARIAGE ENTRE + %s + %s' % (self.demandeur, self.demandeur2)


class Deces(models.Model):
    YEAR_CHOICES = []
    for r in range(2000, (datetime.datetime.now().year + 1)):
        YEAR_CHOICES.append((r, r))

    #infos Generales
    username = models.CharField(max_length=25, verbose_name="TRAITE PAR", editable=False)
    archive = models.BooleanField(default=False, verbose_name="ARCHIVE")
    annee = models.IntegerField(verbose_name='ANNEE DU REGISTRE', choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    num_deces = models.CharField(max_length=150, blank=True, verbose_name='NUMERO DECES', help_text="UNIQUEMENT POUR LES ARCCHIVES")
    categorie = models.CharField(verbose_name='TYPE DE DOCUMENT', max_length=50, choices=TYPE_MENTION, default="deces")

    #informarions Personne decede
    nom_et_prenoms = models.CharField(max_length=50, verbose_name="NOM ET PRENOMS")
    date_naiss = models.DateField(max_length=250, verbose_name="NE(E) LE", blank=True)
    lieu_naiss = models.CharField(max_length=250, verbose_name="LIEU DE NAISSANCE", blank=True)
    profession = models.CharField(max_length=250, verbose_name="PROFESSION", blank=True)
    domicile = models.CharField(max_length=250, verbose_name="DOMICILE A", blank=True)

    #parents
    pere = models.CharField(max_length=250, verbose_name="NOM ET PRENOMS DU PERE", blank=True)
    mere = models.CharField(max_length=250, verbose_name="NOM ET PRENOMS DE LA MERE", blank=True)

    #details deces
    date_deces = models.DateField(max_length=250, verbose_name="DATE DU DECES", blank=True)
    heure_deces = models.TimeField(max_length=250, verbose_name="HEURE DU DECES", blank=True)
    lieu_deces = models.CharField(max_length=250, verbose_name="LIEU DU DECES", blank=True)
    cause_deces = models.CharField(max_length=250, verbose_name="CAUSES DU DECES", blank=True)
    ajouter_le = models.DateTimeField(auto_now_add=True, auto_now=False)
    modifier_le = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name_plural = "ACTES DE DECES"
        verbose_name = "Acte de deces"

    def save(self, force_insert=False, force_update=False):
        self.nom_et_prenoms = self.demandeur.upper()

        # numerotation automatique
        if self.archive == False:
            last_number = 500
            tot = Deces.objects.count()
            numero = last_number + 1
            madate = datetime.date.today()
            self.num_deces = "%s du %s" % (numero, datetime.date.strftime(madate, '%d/%m/%Y'))

        super(Deces, self).save(force_insert, force_update)

    def __unicode__(self):
        return 'DECES DE + %s + le %s à %s' % (self.nom_et_prenoms, self.date_naiss, self.heure_deces)

# Create your models here.
