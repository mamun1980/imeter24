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
            ('network_que_location', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('printer_type', self.gf('django.db.models.fields.CharField')(max_length=25, null=True, blank=True)),
            ('printer_status', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
        ))
        db.send_create_signal(u'report', ['Printer'])

        # Adding model 'Report'
        db.create_table(u'report_report', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('report_type', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('destination_type', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('comments', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('python_script', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('search_string', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
        ))
        db.send_create_signal(u'report', ['Report'])

        # Adding model 'RecuringReport'
        db.create_table(u'report_recuringreport', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('report', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['report.Report'], null=True, blank=True)),
            ('report_description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('script_name', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('que_type', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
            ('printer', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['report.Printer'], null=True, blank=True)),
            ('fax', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('current_job_status', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('date_submitted', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('time_submitted', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('date_finished', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('time_finished', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('unix_que', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('comment', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('schedule_type', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('week_day', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('randomdays', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('daytime', self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True)),
            ('search_string', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
        ))
        db.send_create_signal(u'report', ['RecuringReport'])

        # Adding model 'SingleReport'
        db.create_table(u'report_singlereport', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('report', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['report.Report'], null=True, blank=True)),
            ('report_description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('script_name', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('que_type', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
            ('printer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['report.Printer'], null=True, blank=True)),
            ('fax', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('current_job_status', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('date_submitted', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('time_submitted', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('date_finished', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('time_finished', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('search_start_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('search_end_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('search_string', self.gf('django.db.models.fields.CharField')(max_length=250, null=True, blank=True)),
            ('search_status_type', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
        ))
        db.send_create_signal(u'report', ['SingleReport'])


    def backwards(self, orm):
        # Deleting model 'Printer'
        db.delete_table(u'report_printer')

        # Deleting model 'Report'
        db.delete_table(u'report_report')

        # Deleting model 'RecuringReport'
        db.delete_table(u'report_recuringreport')

        # Deleting model 'SingleReport'
        db.delete_table(u'report_singlereport')


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
            'comment': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'current_job_status': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'date_finished': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_submitted': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'daytime': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'printer': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'to': u"orm['report.Printer']", 'null': 'True', 'blank': 'True'}),
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
        },
        u'report.singlereport': {
            'Meta': {'object_name': 'SingleReport'},
            'current_job_status': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'date_finished': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_submitted': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'fax': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'printer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['report.Printer']", 'null': 'True', 'blank': 'True'}),
            'que_type': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'report': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['report.Report']", 'null': 'True', 'blank': 'True'}),
            'report_description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'script_name': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'search_end_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'search_start_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'search_status_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'search_string': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'time_finished': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'time_submitted': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['report']