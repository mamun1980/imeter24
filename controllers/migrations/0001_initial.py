# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Controller'
        db.create_table(u'controllers_controller', (
            ('oid', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('controllerid', self.gf('django.db.models.fields.CharField')(max_length=3, null=True, blank=True)),
            ('relayid', self.gf('django.db.models.fields.IntegerField')(max_length=2, null=True, blank=True)),
            ('status', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal(u'controllers', ['Controller'])


    def backwards(self, orm):
        # Deleting model 'Controller'
        db.delete_table(u'controllers_controller')


    models = {
        u'controllers.controller': {
            'Meta': {'ordering': "['oid']", 'object_name': 'Controller'},
            'controllerid': ('django.db.models.fields.CharField', [], {'max_length': '3', 'null': 'True', 'blank': 'True'}),
            'oid': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'relayid': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.BooleanField', [], {})
        }
    }

    complete_apps = ['controllers']