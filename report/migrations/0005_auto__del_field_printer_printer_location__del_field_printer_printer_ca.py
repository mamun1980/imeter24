# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Printer.printer_location'
        db.delete_column(u'report_printer', 'printer_location')

        # Deleting field 'Printer.printer_capacity'
        db.delete_column(u'report_printer', 'printer_capacity')

        # Adding field 'Printer.network_que_location'
        db.add_column(u'report_printer', 'network_que_location',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Printer.printer_location'
        db.add_column(u'report_printer', 'printer_location',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Printer.printer_capacity'
        db.add_column(u'report_printer', 'printer_capacity',
                      self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Printer.network_que_location'
        db.delete_column(u'report_printer', 'network_que_location')


    models = {
        u'report.printer': {
            'Meta': {'object_name': 'Printer'},
            'network_que_location': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'printer_id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'printer_status': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'printer_type': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'})
        },
        u'report.recuringreport': {
            'Meta': {'object_name': 'RecuringReport'},
            'current_job_status': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'date_finished': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_submitted': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'daytime': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'printer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['report.Printer']", 'null': 'True', 'blank': 'True'}),
            'que_type': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'randomdays': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'report': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['report.Report']", 'null': 'True', 'blank': 'True'}),
            'report_description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'schedule_type': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'script_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'search_string': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'time_finished': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'time_submitted': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'unix_que': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'week_day': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
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

    complete_apps = ['report']