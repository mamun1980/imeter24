# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Job'
        db.create_table(u'schedule_job', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('job_number', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('cab_designation', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('date_opened', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('date_required', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('status', self.gf('django.db.models.fields.CharField')(default=0, max_length=50)),
            ('address1', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('street', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('customer', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('contact_email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('number_of_cabs', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=200, null=True, blank=True)),
            ('po_number', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('status_notes', self.gf('django.db.models.fields.TextField')(max_length=200, null=True, blank=True)),
            ('drawing_req_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('drawing_sent_to_customer_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('drawing_approved_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'schedule', ['Job'])

        # Adding model 'JobStatus'
        db.create_table(u'schedule_jobstatus', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('job', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['schedule.Job'], unique=True)),
            ('fixtures_req_by', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('fixtures_is_done', self.gf('django.db.models.fields.CharField')(default='none', max_length=20, null=True, blank=True)),
            ('wood_shop_req_by', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('wood_shop_is_done', self.gf('django.db.models.fields.CharField')(default='none', max_length=20, null=True, blank=True)),
            ('machine_shop_req_by', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('machine_shop_is_done', self.gf('django.db.models.fields.CharField')(default='none', max_length=20, null=True, blank=True)),
            ('welding', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('welding_is_done', self.gf('django.db.models.fields.CharField')(default='none', max_length=20, null=True, blank=True)),
            ('lacquer', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('lacquer_is_done', self.gf('django.db.models.fields.CharField')(default='none', max_length=20, null=True, blank=True)),
            ('trim_shop_req_by', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('trim_shop_is_done', self.gf('django.db.models.fields.CharField')(default='none', max_length=20, null=True, blank=True)),
            ('cab_assemply_req_by', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('cab_assemply_is_done', self.gf('django.db.models.fields.CharField')(default='none', max_length=20, null=True, blank=True)),
            ('install_date', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('install_is_done', self.gf('django.db.models.fields.CharField')(default='none', max_length=20, null=True, blank=True)),
            ('premier_glass', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('premier_glass_is_done', self.gf('django.db.models.fields.CharField')(default='none', max_length=20, null=True, blank=True)),
            ('tile_installer', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('tile_installer_is_done', self.gf('django.db.models.fields.CharField')(default='none', max_length=20, null=True, blank=True)),
            ('misc_del', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('misc_del_is_done', self.gf('django.db.models.fields.CharField')(default='none', max_length=20, null=True, blank=True)),
            ('bill', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('bill_is_done', self.gf('django.db.models.fields.CharField')(default='none', max_length=20, null=True, blank=True)),
            ('hayward', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('hayward_is_done', self.gf('django.db.models.fields.CharField')(default='none', max_length=20, null=True, blank=True)),
            ('glenn', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('glenn_is_done', self.gf('django.db.models.fields.CharField')(default='none', max_length=20, null=True, blank=True)),
            ('suren', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('suren_is_done', self.gf('django.db.models.fields.CharField')(default='none', max_length=20, null=True, blank=True)),
            ('roger', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('roger_is_done', self.gf('django.db.models.fields.CharField')(default='none', max_length=20, null=True, blank=True)),
            ('matt', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('matt_is_done', self.gf('django.db.models.fields.CharField')(default='none', max_length=20, null=True, blank=True)),
            ('third_party_install', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('third_party_install_is_done', self.gf('django.db.models.fields.CharField')(default='none', max_length=20, null=True, blank=True)),
        ))
        db.send_create_signal(u'schedule', ['JobStatus'])


    def backwards(self, orm):
        # Deleting model 'Job'
        db.delete_table(u'schedule_job')

        # Deleting model 'JobStatus'
        db.delete_table(u'schedule_jobstatus')


    models = {
        u'schedule.job': {
            'Meta': {'object_name': 'Job'},
            'address1': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'cab_designation': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'contact_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'customer': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'date_opened': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_required': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'drawing_approved_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'drawing_req_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'drawing_sent_to_customer_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job_number': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'number_of_cabs': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'po_number': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': '0', 'max_length': '50'}),
            'status_notes': ('django.db.models.fields.TextField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'street': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'schedule.jobstatus': {
            'Meta': {'object_name': 'JobStatus'},
            'bill': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'bill_is_done': ('django.db.models.fields.CharField', [], {'default': "'none'", 'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'cab_assemply_is_done': ('django.db.models.fields.CharField', [], {'default': "'none'", 'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'cab_assemply_req_by': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'fixtures_is_done': ('django.db.models.fields.CharField', [], {'default': "'none'", 'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'fixtures_req_by': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'glenn': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'glenn_is_done': ('django.db.models.fields.CharField', [], {'default': "'none'", 'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'hayward': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'hayward_is_done': ('django.db.models.fields.CharField', [], {'default': "'none'", 'max_length': '20', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'install_date': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'install_is_done': ('django.db.models.fields.CharField', [], {'default': "'none'", 'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'job': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['schedule.Job']", 'unique': 'True'}),
            'lacquer': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'lacquer_is_done': ('django.db.models.fields.CharField', [], {'default': "'none'", 'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'machine_shop_is_done': ('django.db.models.fields.CharField', [], {'default': "'none'", 'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'machine_shop_req_by': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'matt': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'matt_is_done': ('django.db.models.fields.CharField', [], {'default': "'none'", 'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'misc_del': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'misc_del_is_done': ('django.db.models.fields.CharField', [], {'default': "'none'", 'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'premier_glass': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'premier_glass_is_done': ('django.db.models.fields.CharField', [], {'default': "'none'", 'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'roger': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'roger_is_done': ('django.db.models.fields.CharField', [], {'default': "'none'", 'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'suren': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'suren_is_done': ('django.db.models.fields.CharField', [], {'default': "'none'", 'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'third_party_install': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'third_party_install_is_done': ('django.db.models.fields.CharField', [], {'default': "'none'", 'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'tile_installer': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'tile_installer_is_done': ('django.db.models.fields.CharField', [], {'default': "'none'", 'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'trim_shop_is_done': ('django.db.models.fields.CharField', [], {'default': "'none'", 'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'trim_shop_req_by': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'welding': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'welding_is_done': ('django.db.models.fields.CharField', [], {'default': "'none'", 'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'wood_shop_is_done': ('django.db.models.fields.CharField', [], {'default': "'none'", 'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'wood_shop_req_by': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['schedule']