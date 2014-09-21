# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Printer'
        db.create_table(u'report_printer', (
            ('printer_id', self.gf('django.db.models.fields.CharField')(max_length=50, primary_key=True)),
            ('printer_location', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('printer_type', self.gf('django.db.models.fields.CharField')(max_length=25, null=True, blank=True)),
            ('printer_status', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('printer_capacity', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
        ))
        db.send_create_signal(u'report', ['Printer'])

        # Adding model 'Report'
        db.create_table(u'report_report', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('report_type', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('printer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['report.Printer'], null=True, blank=True)),
            ('destination_type', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('comments', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('start_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('end_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('rang', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('search_string', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
        ))
        db.send_create_signal(u'report', ['Report'])

        # Adding model 'RecuringReport'
        db.create_table(u'report_recuringreport', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('report', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['report.Report'], null=True, blank=True)),
            ('report_description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('script_name', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('schedule_type', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('week_day', self.gf('django.db.models.fields.CharField')(max_length=25, null=True, blank=True)),
            ('randomdays', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('daytime', self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True)),
            ('search_string', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
        ))
        db.send_create_signal(u'report', ['RecuringReport'])


    def backwards(self, orm):
        # Deleting model 'Printer'
        db.delete_table(u'report_printer')

        # Deleting model 'Report'
        db.delete_table(u'report_report')

        # Deleting model 'RecuringReport'
        db.delete_table(u'report_recuringreport')


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
            'script_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'search_string': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'week_day': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'})
        },
        u'report.report': {
            'Meta': {'object_name': 'Report'},
            'comments': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'destination_type': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'printer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['report.Printer']", 'null': 'True', 'blank': 'True'}),
            'rang': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'report_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'search_string': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['report']