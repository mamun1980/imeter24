# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'SystemVariable.default_printer_for_po'
        db.add_column(u'premierelevator_systemvariable', 'default_printer_for_po',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='default_printer_for_po', null=True, to=orm['report.Printer']),
                      keep_default=False)

        # Adding field 'SystemVariable.default_printer_for_sl'
        db.add_column(u'premierelevator_systemvariable', 'default_printer_for_sl',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='default_printer_for_sl', null=True, to=orm['report.Printer']),
                      keep_default=False)

        # Adding field 'SystemVariable.default_printer_for_pl'
        db.add_column(u'premierelevator_systemvariable', 'default_printer_for_pl',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='default_printer_for_pl', null=True, to=orm['report.Printer']),
                      keep_default=False)

        # Adding field 'SystemVariable.default_printer_for_invoice'
        db.add_column(u'premierelevator_systemvariable', 'default_printer_for_invoice',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='default_printer_for_invoice', null=True, to=orm['report.Printer']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'SystemVariable.default_printer_for_po'
        db.delete_column(u'premierelevator_systemvariable', 'default_printer_for_po_id')

        # Deleting field 'SystemVariable.default_printer_for_sl'
        db.delete_column(u'premierelevator_systemvariable', 'default_printer_for_sl_id')

        # Deleting field 'SystemVariable.default_printer_for_pl'
        db.delete_column(u'premierelevator_systemvariable', 'default_printer_for_pl_id')

        # Deleting field 'SystemVariable.default_printer_for_invoice'
        db.delete_column(u'premierelevator_systemvariable', 'default_printer_for_invoice_id')


    models = {
        u'premierelevator.systemvariable': {
            'Meta': {'object_name': 'SystemVariable'},
            'default_printer_for_invoice': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'default_printer_for_invoice'", 'null': 'True', 'to': u"orm['report.Printer']"}),
            'default_printer_for_pl': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'default_printer_for_pl'", 'null': 'True', 'to': u"orm['report.Printer']"}),
            'default_printer_for_po': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'default_printer_for_po'", 'null': 'True', 'to': u"orm['report.Printer']"}),
            'default_printer_for_sl': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'default_printer_for_sl'", 'null': 'True', 'to': u"orm['report.Printer']"}),
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
        },
        u'report.printer': {
            'Meta': {'object_name': 'Printer'},
            'network_que_location': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'printer_id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'printer_status': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'printer_type': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['premierelevator']