# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Job.status_notes'
        db.alter_column(u'schedule_job', 'status_notes', self.gf('django.db.models.fields.TextField')(max_length=500, null=True))

        # Changing field 'Job.search_string'
        db.alter_column(u'schedule_job', 'search_string', self.gf('django.db.models.fields.TextField')(max_length=1000, null=True))

    def backwards(self, orm):

        # Changing field 'Job.status_notes'
        db.alter_column(u'schedule_job', 'status_notes', self.gf('django.db.models.fields.TextField')(max_length=200, null=True))

        # Changing field 'Job.search_string'
        db.alter_column(u'schedule_job', 'search_string', self.gf('django.db.models.fields.TextField')(max_length=800, null=True))

    models = {
        u'schedule.job': {
            'Meta': {'object_name': 'Job'},
            'cab_designation': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'contact_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'customer': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'date_opened': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_required': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'drawing_approved_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'drawing_req_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'drawing_sent_to_customer_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'eng_comment': ('django.db.models.fields.TextField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job_name': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'job_number': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'number_of_cabs': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'po_number': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'search_string': ('django.db.models.fields.TextField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': '0', 'max_length': '50'}),
            'status_notes': ('django.db.models.fields.TextField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'})
        },
        u'schedule.jobstatus': {
            'Meta': {'object_name': 'JobStatus'},
            'bill': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'bill_comment': ('django.db.models.fields.TextField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'bill_is_done': ('django.db.models.fields.CharField', [], {'default': "'none'", 'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'cab_assemply_is_done': ('django.db.models.fields.CharField', [], {'default': "'none'", 'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'cab_assemply_req_by': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'cab_assemply_req_by_comment': ('django.db.models.fields.TextField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'fixtures_comment': ('django.db.models.fields.TextField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'fixtures_is_done': ('django.db.models.fields.CharField', [], {'default': "'none'", 'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'fixtures_req_by': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'glenn': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'glenn_comment': ('django.db.models.fields.TextField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'glenn_is_done': ('django.db.models.fields.CharField', [], {'default': "'none'", 'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'hayward': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'hayward_comment': ('django.db.models.fields.TextField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'hayward_is_done': ('django.db.models.fields.CharField', [], {'default': "'none'", 'max_length': '20', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'install_date': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'install_date_comment': ('django.db.models.fields.TextField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'install_is_done': ('django.db.models.fields.CharField', [], {'default': "'none'", 'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'job': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['schedule.Job']", 'unique': 'True'}),
            'lacquer': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'lacquer_comment': ('django.db.models.fields.TextField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'lacquer_is_done': ('django.db.models.fields.CharField', [], {'default': "'none'", 'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'machine_shop_is_done': ('django.db.models.fields.CharField', [], {'default': "'none'", 'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'machine_shop_req_by': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'machine_shop_req_by_comment': ('django.db.models.fields.TextField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'matt': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'matt_comment': ('django.db.models.fields.TextField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'matt_is_done': ('django.db.models.fields.CharField', [], {'default': "'none'", 'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'misc_del': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'misc_del_comment': ('django.db.models.fields.TextField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'misc_del_is_done': ('django.db.models.fields.CharField', [], {'default': "'none'", 'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'premier_glass': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'premier_glass_comment': ('django.db.models.fields.TextField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'premier_glass_is_done': ('django.db.models.fields.CharField', [], {'default': "'none'", 'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'roger': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'roger_comment': ('django.db.models.fields.TextField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'roger_is_done': ('django.db.models.fields.CharField', [], {'default': "'none'", 'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'suren': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'suren_comment': ('django.db.models.fields.TextField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'suren_is_done': ('django.db.models.fields.CharField', [], {'default': "'none'", 'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'third_party_install': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'third_party_install_comment': ('django.db.models.fields.TextField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'third_party_install_is_done': ('django.db.models.fields.CharField', [], {'default': "'none'", 'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'tile_installer': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'tile_installer_comment': ('django.db.models.fields.TextField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'tile_installer_is_done': ('django.db.models.fields.CharField', [], {'default': "'none'", 'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'trim_shop_is_done': ('django.db.models.fields.CharField', [], {'default': "'none'", 'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'trim_shop_req_by': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'trim_shop_req_by_comment': ('django.db.models.fields.TextField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'welding': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'welding_comment': ('django.db.models.fields.TextField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'welding_is_done': ('django.db.models.fields.CharField', [], {'default': "'none'", 'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'wood_shop_is_done': ('django.db.models.fields.CharField', [], {'default': "'none'", 'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'wood_shop_req_by': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'wood_shop_req_by_comment': ('django.db.models.fields.TextField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['schedule']