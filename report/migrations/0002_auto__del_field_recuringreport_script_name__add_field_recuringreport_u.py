# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'RecuringReport.script_name'
        db.delete_column(u'report_recuringreport', 'script_name')

        # Adding field 'RecuringReport.unix_que'
        db.add_column(u'report_recuringreport', 'unix_que',
                      self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Report.status'
        db.delete_column(u'report_report', 'status')

        # Deleting field 'Report.rang'
        db.delete_column(u'report_report', 'rang')

        # Deleting field 'Report.end_date'
        db.delete_column(u'report_report', 'end_date')

        # Deleting field 'Report.start_date'
        db.delete_column(u'report_report', 'start_date')

        # Adding field 'Report.python_script'
        db.add_column(u'report_report', 'python_script',
                      self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'RecuringReport.script_name'
        db.add_column(u'report_recuringreport', 'script_name',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True),
                      keep_default=False)

        # Deleting field 'RecuringReport.unix_que'
        db.delete_column(u'report_recuringreport', 'unix_que')

        # Adding field 'Report.status'
        db.add_column(u'report_report', 'status',
                      self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Report.rang'
        db.add_column(u'report_report', 'rang',
                      self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Report.end_date'
        db.add_column(u'report_report', 'end_date',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'Report.start_date'
        db.add_column(u'report_report', 'start_date',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Report.python_script'
        db.delete_column(u'report_report', 'python_script')


    models = {
        u'report.printer': {
            'Meta': {'object_name': 'Printer'},
            'printer_capacity': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'printer_id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'printer_location': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'printer_status': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'printer_type': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'})
        },
        u'report.recuringreport': {
            'Meta': {'object_name': 'RecuringReport'},
            'daytime': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'randomdays': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'report': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['report.Report']", 'null': 'True', 'blank': 'True'}),
            'report_description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'schedule_type': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'search_string': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'unix_que': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'week_day': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'})
        },
        u'report.report': {
            'Meta': {'object_name': 'Report'},
            'comments': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'destination_type': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'printer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['report.Printer']", 'null': 'True', 'blank': 'True'}),
            'python_script': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'report_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'search_string': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['report']