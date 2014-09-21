# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'JobStatus.fixtures_comment'
        db.add_column(u'schedule_jobstatus', 'fixtures_comment',
                      self.gf('django.db.models.fields.TextField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'JobStatus.wood_shop_req_by_comment'
        db.add_column(u'schedule_jobstatus', 'wood_shop_req_by_comment',
                      self.gf('django.db.models.fields.TextField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'JobStatus.machine_shop_req_by_comment'
        db.add_column(u'schedule_jobstatus', 'machine_shop_req_by_comment',
                      self.gf('django.db.models.fields.TextField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'JobStatus.welding_comment'
        db.add_column(u'schedule_jobstatus', 'welding_comment',
                      self.gf('django.db.models.fields.TextField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'JobStatus.lacquer_comment'
        db.add_column(u'schedule_jobstatus', 'lacquer_comment',
                      self.gf('django.db.models.fields.TextField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'JobStatus.trim_shop_req_by_comment'
        db.add_column(u'schedule_jobstatus', 'trim_shop_req_by_comment',
                      self.gf('django.db.models.fields.TextField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'JobStatus.cab_assemply_req_by_comment'
        db.add_column(u'schedule_jobstatus', 'cab_assemply_req_by_comment',
                      self.gf('django.db.models.fields.TextField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'JobStatus.install_date_comment'
        db.add_column(u'schedule_jobstatus', 'install_date_comment',
                      self.gf('django.db.models.fields.TextField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'JobStatus.premier_glass_comment'
        db.add_column(u'schedule_jobstatus', 'premier_glass_comment',
                      self.gf('django.db.models.fields.TextField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'JobStatus.tile_installer_comment'
        db.add_column(u'schedule_jobstatus', 'tile_installer_comment',
                      self.gf('django.db.models.fields.TextField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'JobStatus.misc_del_comment'
        db.add_column(u'schedule_jobstatus', 'misc_del_comment',
                      self.gf('django.db.models.fields.TextField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'JobStatus.bill_comment'
        db.add_column(u'schedule_jobstatus', 'bill_comment',
                      self.gf('django.db.models.fields.TextField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'JobStatus.hayward_comment'
        db.add_column(u'schedule_jobstatus', 'hayward_comment',
                      self.gf('django.db.models.fields.TextField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'JobStatus.glenn_comment'
        db.add_column(u'schedule_jobstatus', 'glenn_comment',
                      self.gf('django.db.models.fields.TextField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'JobStatus.suren_comment'
        db.add_column(u'schedule_jobstatus', 'suren_comment',
                      self.gf('django.db.models.fields.TextField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'JobStatus.roger_comment'
        db.add_column(u'schedule_jobstatus', 'roger_comment',
                      self.gf('django.db.models.fields.TextField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'JobStatus.matt_comment'
        db.add_column(u'schedule_jobstatus', 'matt_comment',
                      self.gf('django.db.models.fields.TextField')(max_length=200, null=True, blank=True),
                      keep_default=False)

        # Adding field 'JobStatus.third_party_install_comment'
        db.add_column(u'schedule_jobstatus', 'third_party_install_comment',
                      self.gf('django.db.models.fields.TextField')(max_length=200, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'JobStatus.fixtures_comment'
        db.delete_column(u'schedule_jobstatus', 'fixtures_comment')

        # Deleting field 'JobStatus.wood_shop_req_by_comment'
        db.delete_column(u'schedule_jobstatus', 'wood_shop_req_by_comment')

        # Deleting field 'JobStatus.machine_shop_req_by_comment'
        db.delete_column(u'schedule_jobstatus', 'machine_shop_req_by_comment')

        # Deleting field 'JobStatus.welding_comment'
        db.delete_column(u'schedule_jobstatus', 'welding_comment')

        # Deleting field 'JobStatus.lacquer_comment'
        db.delete_column(u'schedule_jobstatus', 'lacquer_comment')

        # Deleting field 'JobStatus.trim_shop_req_by_comment'
        db.delete_column(u'schedule_jobstatus', 'trim_shop_req_by_comment')

        # Deleting field 'JobStatus.cab_assemply_req_by_comment'
        db.delete_column(u'schedule_jobstatus', 'cab_assemply_req_by_comment')

        # Deleting field 'JobStatus.install_date_comment'
        db.delete_column(u'schedule_jobstatus', 'install_date_comment')

        # Deleting field 'JobStatus.premier_glass_comment'
        db.delete_column(u'schedule_jobstatus', 'premier_glass_comment')

        # Deleting field 'JobStatus.tile_installer_comment'
        db.delete_column(u'schedule_jobstatus', 'tile_installer_comment')

        # Deleting field 'JobStatus.misc_del_comment'
        db.delete_column(u'schedule_jobstatus', 'misc_del_comment')

        # Deleting field 'JobStatus.bill_comment'
        db.delete_column(u'schedule_jobstatus', 'bill_comment')

        # Deleting field 'JobStatus.hayward_comment'
        db.delete_column(u'schedule_jobstatus', 'hayward_comment')

        # Deleting field 'JobStatus.glenn_comment'
        db.delete_column(u'schedule_jobstatus', 'glenn_comment')

        # Deleting field 'JobStatus.suren_comment'
        db.delete_column(u'schedule_jobstatus', 'suren_comment')

        # Deleting field 'JobStatus.roger_comment'
        db.delete_column(u'schedule_jobstatus', 'roger_comment')

        # Deleting field 'JobStatus.matt_comment'
        db.delete_column(u'schedule_jobstatus', 'matt_comment')

        # Deleting field 'JobStatus.third_party_install_comment'
        db.delete_column(u'schedule_jobstatus', 'third_party_install_comment')


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