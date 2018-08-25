# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Centre.code'
        db.alter_column(u'parametres_centre', 'code', self.gf('django.db.models.fields.CharField')(max_length=10))

        # Changing field 'Region.code'
        db.alter_column(u'parametres_region', 'code', self.gf('django.db.models.fields.CharField')(max_length=10))

    def backwards(self, orm):

        # Changing field 'Centre.code'
        db.alter_column(u'parametres_centre', 'code', self.gf('django.db.models.fields.CharField')(max_length=5))

        # Changing field 'Region.code'
        db.alter_column(u'parametres_region', 'code', self.gf('django.db.models.fields.CharField')(max_length=5))

    models = {
        u'parametres.centre': {
            'Meta': {'object_name': 'Centre'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'emplacement': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'libelle': ('django.db.models.fields.CharField', [], {'max_length': '500'}),
            'mairie': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['parametres.Mairie']"})
        },
        u'parametres.distict': {
            'Meta': {'object_name': 'Distict'},
            'chef_lieu': ('django.db.models.fields.CharField', [], {'max_length': '250'}),
            'district': ('django.db.models.fields.CharField', [], {'default': "u'woroba'", 'max_length': '250'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nbr_region': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'president': ('django.db.models.fields.CharField', [], {'max_length': '500'})
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
        },
        u'parametres.region': {
            'Meta': {'object_name': 'Region'},
            'chef_lieu': ('django.db.models.fields.CharField', [], {'default': "u'seguela'", 'max_length': '250'}),
            'code': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'district': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['parametres.Distict']"}),
            'habitant': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'region': ('django.db.models.fields.CharField', [], {'default': "u'worodougou'", 'max_length': '250'})
        }
    }

    complete_apps = ['parametres']