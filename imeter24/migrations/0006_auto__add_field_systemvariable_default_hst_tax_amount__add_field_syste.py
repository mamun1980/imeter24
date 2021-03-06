# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'SystemVariable.default_hst_tax_amount'
        db.add_column(u'premierelevator_systemvariable', 'default_hst_tax_amount',
                      self.gf('django.db.models.fields.CharField')(max_length=20, null=True),
                      keep_default=False)

        # Adding field 'SystemVariable.default_pst_tax_amount'
        db.add_column(u'premierelevator_systemvariable', 'default_pst_tax_amount',
                      self.gf('django.db.models.fields.CharField')(max_length=20, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'SystemVariable.default_hst_tax_amount'
        db.delete_column(u'premierelevator_systemvariable', 'default_hst_tax_amount')

        # Deleting field 'SystemVariable.default_pst_tax_amount'
        db.delete_column(u'premierelevator_systemvariable', 'default_pst_tax_amount')


    models = {
        u'premierelevator.systemvariable': {
            'Meta': {'object_name': 'SystemVariable'},
            'default_hst_tax_amount': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'default_printer_for_invoice': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'default_printer_for_invoice'", 'null': 'True', 'to': u"orm['report.Printer']"}),
            'default_printer_for_pl': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'default_printer_for_pl'", 'null': 'True', 'to': u"orm['report.Printer']"}),
            'default_printer_for_po': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'default_printer_for_po'", 'null': 'True', 'to': u"orm['report.Printer']"}),
            'default_printer_for_sl': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'default_printer_for_sl'", 'null': 'True', 'to': u"orm['report.Printer']"}),
            'default_printer_for_user': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'default_printer_for_user'", 'null': 'True', 'to': u"orm['report.Printer']"}),
            'default_pst_tax_amount': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'default_report_for_invoice': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'default_report_for_invoice'", 'null': 'True', 'to': u"orm['report.Report']"}),
            'default_report_for_pl': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'default_report_for_pl'", 'null': 'True', 'to': u"orm['report.Report']"}),
            'default_report_for_po': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'default_report_for_po'", 'null': 'True', 'to': u"orm['report.Report']"}),
            'default_report_for_sl': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'default_report_for_sl'", 'null': 'True', 'to': u"orm['report.Report']"}),
            'email_auth_password': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'email_auth_username': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'email_server_host_name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'email_server_ip_address': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'next_invoice_number': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'next_item_number': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
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
        },
        u'report.report': {
            'Meta': {'object_name': 'Report'},
            'comments': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'destination_type': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'python_script': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'report_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'search_string': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['premierelevator']