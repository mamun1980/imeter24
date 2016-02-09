# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SystemVariable'
        db.create_table(u'premierelevator_systemvariable', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('next_job_number', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('next_job_control_number', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('next_item_number', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('next_po_number', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('next_sl_number', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('next_pl_number', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('next_invoice_number', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('email_server_host_name', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('email_server_ip_address', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('email_auth_username', self.gf('django.db.models.fields.CharField')(max_length=20, null=True)),
            ('email_auth_password', self.gf('django.db.models.fields.CharField')(max_length=20, null=True)),
        ))
        db.send_create_signal(u'premierelevator', ['SystemVariable'])


    def backwards(self, orm):
        # Deleting model 'SystemVariable'
        db.delete_table(u'premierelevator_systemvariable')


    models = {
        u'premierelevator.systemvariable': {
            'Meta': {'object_name': 'SystemVariable'},
            'email_auth_password': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'email_auth_username': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'email_server_host_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'email_server_ip_address': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'next_invoice_number': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'next_item_number': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'next_job_control_number': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'next_job_number': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'next_pl_number': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'next_po_number': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'next_sl_number': ('django.db.models.fields.IntegerField', [], {'null': 'True'})
        }
    }

    complete_apps = ['premierelevator']