# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Distict'
        db.create_table(u'parametres_distict', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('district', self.gf('django.db.models.fields.CharField')(default=u'woroba', max_length=250)),
            ('chef_lieu', self.gf('django.db.models.fields.CharField')(max_length=250)),
            ('president', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('nbr_region', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'parametres', ['Distict'])

        # Adding model 'Region'
        db.create_table(u'parametres_region', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('district', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['parametres.Distict'])),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('region', self.gf('django.db.models.fields.CharField')(default=u'worodougou', max_length=250)),
            ('chef_lieu', self.gf('django.db.models.fields.CharField')(default=u'seguela', max_length=250)),
            ('habitant', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal(u'parametres', ['Region'])

        # Adding model 'Mairie'
        db.create_table(u'parametres_mairie', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('libelle', self.gf('django.db.models.fields.CharField')(unique=True, max_length=150)),
            ('maire', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('adjoint1', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('adjoint2', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('telephone1', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('telephone2', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('faxe', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('adresse', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('site', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('logo', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'parametres', ['Mairie'])

        # Adding model 'Centre'
        db.create_table(u'parametres_centre', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('mairie', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['parametres.Mairie'])),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('libelle', self.gf('django.db.models.fields.CharField')(max_length=500)),
            ('emplacement', self.gf('django.db.models.fields.CharField')(max_length=500)),
        ))
        db.send_create_signal(u'parametres', ['Centre'])


    def backwards(self, orm):
        # Deleting model 'Distict'
        db.delete_table(u'parametres_distict')

        # Deleting model 'Region'
        db.delete_table(u'parametres_region')

        # Deleting model 'Mairie'
        db.delete_table(u'parametres_mairie')

        # Deleting model 'Centre'
        db.delete_table(u'parametres_centre')


    models = {
        u'parametres.centre': {
            'Meta': {'object_name': 'Centre'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
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
            'code': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'district': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['parametres.Distict']"}),
            'habitant': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'region': ('django.db.models.fields.CharField', [], {'default': "u'worodougou'", 'max_length': '250'})
        }
    }

    complete_apps = ['parametres']