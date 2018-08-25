# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Jugement.lieu_naiss_pere'
        db.alter_column(u'documents_jugement', 'lieu_naiss_pere', self.gf('django.db.models.fields.CharField')(max_length=250))

        # Changing field 'Jugement.lieu_naiss_mere'
        db.alter_column(u'documents_jugement', 'lieu_naiss_mere', self.gf('django.db.models.fields.CharField')(max_length=250))

    def backwards(self, orm):

        # Changing field 'Jugement.lieu_naiss_pere'
        db.alter_column(u'documents_jugement', 'lieu_naiss_pere', self.gf('django.db.models.fields.DateField')())

        # Changing field 'Jugement.lieu_naiss_mere'
        db.alter_column(u'documents_jugement', 'lieu_naiss_mere', self.gf('django.db.models.fields.DateField')())

    models = {
        u'documents.deces': {
            'Meta': {'object_name': 'Deces'},
            'ajouter_le': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'annee': ('django.db.models.fields.IntegerField', [], {'default': '2018'}),
            'archive': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'categorie': ('django.db.models.fields.CharField', [], {'default': "u'deces'", 'max_length': '50'}),
            'cause_deces': ('django.db.models.fields.TextField', [], {'max_length': '250', 'blank': 'True'}),
            'date_deces': ('django.db.models.fields.DateField', [], {'max_length': '250'}),
            'date_naiss': ('django.db.models.fields.DateField', [], {'max_length': '250', 'blank': 'True'}),
            'domicile': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'heure_deces': ('django.db.models.fields.TimeField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lieu_deces': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'lieu_naiss': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'mere': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'modifier_le': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'nom_et_prenoms': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'num_deces': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'pere': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'profession': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'sexe': ('django.db.models.fields.CharField', [], {'default': "u'M'", 'max_length': '150'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        },
        u'documents.extrait': {
            'Meta': {'object_name': 'Extrait'},
            'ajouter_le': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'annee': ('django.db.models.fields.IntegerField', [], {'default': '2018'}),
            'archive': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'commune': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['parametres.Mairie']"}),
            'date_naiss': ('django.db.models.fields.DateField', [], {}),
            'date_naiss_mere': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_naiss_pere': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'document': ('django.db.models.fields.CharField', [], {'default': "u'normal'", 'max_length': '150'}),
            'heure_naiss': ('django.db.models.fields.TimeField', [], {'blank': 'True'}),
            'hopital': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['parametres.Centre']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'jugement': ('django.db.models.fields.CharField', [], {'default': "u'non'", 'max_length': '5'}),
            'lieu_naiss_mere': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'lieu_naiss_pere': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'mere': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'modifier_le': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'nationalite_mere': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'nationalite_pere': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'num_extrait': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'num_jugement': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'pere': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'prenoms': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'profession_mere': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'profession_pere': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'sexe': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        },
        u'documents.jugement': {
            'Meta': {'object_name': 'Jugement'},
            'ajouter_le': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'annee': ('django.db.models.fields.IntegerField', [], {'default': '2018'}),
            'archive': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'commune': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['parametres.Mairie']"}),
            'date_naiss': ('django.db.models.fields.DateField', [], {}),
            'date_naiss_mere': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_naiss_pere': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'document': ('django.db.models.fields.CharField', [], {'default': "u'copie'", 'max_length': '150'}),
            'domicile_mere': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'domicile_pere': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'heure_naiss': ('django.db.models.fields.TimeField', [], {}),
            'hopital': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['parametres.Centre']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lieu_naiss_mere': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'lieu_naiss_pere': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'mere': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'modifier_le': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'nationalite_mere': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'nationalite_pere': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'nom': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'num_jugement': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'officie': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'pere': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'prenoms': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'profession_mere': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'profession_pere': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'sexe': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        },
        u'documents.mariage': {
            'Meta': {'object_name': 'Mariage'},
            'ajouter_le': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'annee': ('django.db.models.fields.IntegerField', [], {'default': '2018'}),
            'archive': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'categorie': ('django.db.models.fields.CharField', [], {'default': "u'mariage'", 'max_length': '50'}),
            'contact2_demandeur': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'contact2_demandeur2': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'contact_demandeur': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'contact_demandeur2': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'date_divorce': ('django.db.models.fields.DateField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'date_mariage': ('django.db.models.fields.DateField', [], {}),
            'date_naiss_demandeur': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'date_naiss_demandeur2': ('django.db.models.fields.DateField', [], {'blank': 'True'}),
            'demandeur': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'demandeur2': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'details_divorce': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'domicile_demandeur': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'domicile_demandeur2': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'heure_mariage': ('django.db.models.fields.TimeField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'lieu_mariage': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'lieu_naiss_demandeur': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'lieu_naiss_demandeur2': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'mere_demandeur': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'mere_demandeur2': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'modifier_le': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'num_mariage': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'pere_demandeur': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'pere_demandeur2': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'profession_demandeur': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'profession_demandeur2': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'regime': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'temoin_demandeur': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'temoin_demandeur2': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        },
        u'parametres.centre': {
            'Meta': {'object_name': 'Centre'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'emplacement': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'libelle': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'mairie': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['parametres.Mairie']"})
        },
        u'parametres.mairie': {
            'Meta': {'object_name': 'Mairie'},
            'adjoint1': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'adjoint2': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'adresse': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'faxe': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'libelle': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '150'}),
            'logo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'maire': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'site': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'telephone1': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'telephone2': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['documents']