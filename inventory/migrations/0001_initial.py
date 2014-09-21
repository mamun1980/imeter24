# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ItemUnitMeasure'
        db.create_table(u'inventory_itemunitmeasure', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('unit_name', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'inventory', ['ItemUnitMeasure'])

        # Adding model 'ProductionType'
        db.create_table(u'inventory_productiontype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('production_type_name', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'inventory', ['ProductionType'])

        # Adding model 'CustomsDesignation'
        db.create_table(u'inventory_customsdesignation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('designation', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'inventory', ['CustomsDesignation'])


    def backwards(self, orm):
        # Deleting model 'ItemUnitMeasure'
        db.delete_table(u'inventory_itemunitmeasure')

        # Deleting model 'ProductionType'
        db.delete_table(u'inventory_productiontype')

        # Deleting model 'CustomsDesignation'
        db.delete_table(u'inventory_customsdesignation')


    models = {
        u'inventory.customsdesignation': {
            'Meta': {'object_name': 'CustomsDesignation'},
            'designation': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'inventory.itemunitmeasure': {
            'Meta': {'object_name': 'ItemUnitMeasure'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'unit_name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'})
        },
        u'inventory.productiontype': {
            'Meta': {'object_name': 'ProductionType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'production_type_name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['inventory']