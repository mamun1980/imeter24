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
            ('job_number', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('cab_designation', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('date_opened', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('date_required', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('status', self.gf('django.db.models.fields.CharField')(default=0, max_length=50)),
            ('job_name', self.gf('django.db.models.fields.CharField')(max_length=150, null=True, blank=True)),
            ('address_1', self.gf('django.db.models.fields.TextField')(max_length=500, null=True, blank=True)),
            ('customer', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('customer_contact_name', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('customer_contact_phone_number', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('contact_email', self.gf('django.db.models.fields.CharField')(max_length=500, null=True, blank=True)),
            ('number_of_cabs', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=200, null=True, blank=True)),
            ('po_number', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('status_notes', self.gf('django.db.models.fields.TextField')(max_length=500, null=True, blank=True)),
            ('drawing_req_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('drawing_sent_to_customer_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('drawing_approved_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('eng_comment', self.gf('django.db.models.fields.TextField')(max_length=200, null=True, blank=True)),
            ('search_string', self.gf('django.db.models.fields.TextField')(max_length=1000, null=True, blank=True)),
        ))
        db.send_create_signal(u'schedule', ['Job'])

        # Adding model 'Comment'
        db.create_table(u'schedule_comment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('job_number', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('job_comment', self.gf('django.db.models.fields.TextField')(max_length=500, null=True, blank=True)),
            ('comment_by', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('datetime', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now, null=True, blank=True)),
        ))
        db.send_create_signal(u'schedule', ['Comment'])

        # Adding model 'JobStatus'
        db.create_table(u'schedule_jobstatus', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('job', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['schedule.Job'], unique=True)),
            ('fixtures_req_by', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('fixtures_is_done', self.gf('django.db.models.fields.CharField')(default='none', max_length=20, null=True, blank=True)),
            ('fixtures_comment', self.gf('django.db.models.fields.TextField')(max_length=200, null=True, blank=True)),
            ('wood_shop_req_by', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('wood_shop_is_done', self.gf('django.db.models.fields.CharField')(default='none', max_length=20, null=True, blank=True)),
            ('wood_shop_req_by_comment', self.gf('django.db.models.fields.TextField')(max_length=200, null=True, blank=True)),
            ('machine_shop_req_by', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('machine_shop_is_done', self.gf('django.db.models.fields.CharField')(default='none', max_length=20, null=True, blank=True)),
            ('machine_shop_req_by_comment', self.gf('django.db.models.fields.TextField')(max_length=200, null=True, blank=True)),
            ('welding', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('welding_is_done', self.gf('django.db.models.fields.CharField')(default='none', max_length=20, null=True, blank=True)),
            ('welding_comment', self.gf('django.db.models.fields.TextField')(max_length=200, null=True, blank=True)),
            ('lacquer', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('lacquer_is_done', self.gf('django.db.models.fields.CharField')(default='none', max_length=20, null=True, blank=True)),
            ('lacquer_comment', self.gf('django.db.models.fields.TextField')(max_length=200, null=True, blank=True)),
            ('trim_shop_req_by', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('trim_shop_is_done', self.gf('django.db.models.fields.CharField')(default='none', max_length=20, null=True, blank=True)),
            ('trim_shop_req_by_comment', self.gf('django.db.models.fields.TextField')(max_length=200, null=True, blank=True)),
            ('cab_assemply_req_by', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('cab_assemply_is_done', self.gf('django.db.models.fields.CharField')(default='none', max_length=20, null=True, blank=True)),
            ('cab_assemply_req_by_comment', self.gf('django.db.models.fields.TextField')(max_length=200, null=True, blank=True)),
            ('install_date', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('install_is_done', self.gf('django.db.models.fields.CharField')(default='none', max_length=20, null=True, blank=True)),
            ('install_date_comment', self.gf('django.db.models.fields.TextField')(max_length=200, null=True, blank=True)),
            ('premier_glass', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('premier_glass_is_done', self.gf('django.db.models.fields.CharField')(default='none', max_length=20, null=True, blank=True)),
            ('premier_glass_comment', self.gf('django.db.models.fields.TextField')(max_length=200, null=True, blank=True)),
            ('tile_installer', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('tile_installer_is_done', self.gf('django.db.models.fields.CharField')(default='none', max_length=20, null=True, blank=True)),
            ('tile_installer_comment', self.gf('django.db.models.fields.TextField')(max_length=200, null=True, blank=True)),
            ('misc_del', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('misc_del_is_done', self.gf('django.db.models.fields.CharField')(default='none', max_length=20, null=True, blank=True)),
            ('misc_del_comment', self.gf('django.db.models.fields.TextField')(max_length=200, null=True, blank=True)),
            ('bill', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('bill_is_done', self.gf('django.db.models.fields.CharField')(default='none', max_length=20, null=True, blank=True)),
            ('bill_comment', self.gf('django.db.models.fields.TextField')(max_length=200, null=True, blank=True)),
            ('hayward', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('hayward_is_done', self.gf('django.db.models.fields.CharField')(default='none', max_length=20, null=True, blank=True)),
            ('hayward_comment', self.gf('django.db.models.fields.TextField')(max_length=200, null=True, blank=True)),
            ('glenn', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('glenn_is_done', self.gf('django.db.models.fields.CharField')(default='none', max_length=20, null=True, blank=True)),
            ('glenn_comment', self.gf('django.db.models.fields.TextField')(max_length=200, null=True, blank=True)),
            ('suren', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('suren_is_done', self.gf('django.db.models.fields.CharField')(default='none', max_length=20, null=True, blank=True)),
            ('suren_comment', self.gf('django.db.models.fields.TextField')(max_length=200, null=True, blank=True)),
            ('roger', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('roger_is_done', self.gf('django.db.models.fields.CharField')(default='none', max_length=20, null=True, blank=True)),
            ('roger_comment', self.gf('django.db.models.fields.TextField')(max_length=200, null=True, blank=True)),
            ('matt', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('matt_is_done', self.gf('django.db.models.fields.CharField')(default='none', max_length=20, null=True, blank=True)),
            ('matt_comment', self.gf('django.db.models.fields.TextField')(max_length=200, null=True, blank=True)),
            ('third_party_install', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('third_party_install_is_done', self.gf('django.db.models.fields.CharField')(default='none', max_length=20, null=True, blank=True)),
            ('third_party_install_comment', self.gf('django.db.models.fields.TextField')(max_length=200, null=True, blank=True)),
            ('tssa_submitted_date', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('tssa_submitted_date_is_done', self.gf('django.db.models.fields.CharField')(default='none', max_length=20, null=True, blank=True)),
            ('tssa_submitted_date_comment', self.gf('django.db.models.fields.TextField')(max_length=200, null=True, blank=True)),
            ('safety_test_schedule_date', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('who_will_test', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('test_comment', self.gf('django.db.models.fields.TextField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal(u'schedule', ['JobStatus'])

        # Adding model 'ElevetorType'
        db.create_table(u'schedule_elevetortype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('elevetor_type', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal(u'schedule', ['ElevetorType'])

        # Adding model 'JobControl'
        db.create_table(u'schedule_jobcontrol', (
            ('job_number', self.gf('django.db.models.fields.CharField')(max_length=20, primary_key=True)),
            ('job_name', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('number_of_cabs', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('sold_to', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='job-control-sold_to', null=True, to=orm['contacts.Contact'])),
            ('ship_to', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='job-control-ship_to', null=True, to=orm['contacts.Contact'])),
            ('elevetor_type', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='job-con-elevetor-type', null=True, to=orm['schedule.ElevetorType'])),
            ('number_of_floors', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('front', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('rear', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('rgw', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('capacity', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('customer_po_number', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('delivery_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('start_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('installed_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contacts.Contact'], null=True, blank=True)),
            ('estimated_price_for_job', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=4, blank=True)),
            ('search_string', self.gf('django.db.models.fields.TextField')(max_length=1000, null=True, blank=True)),
        ))
        db.send_create_signal(u'schedule', ['JobControl'])


    def backwards(self, orm):
        # Deleting model 'Job'
        db.delete_table(u'schedule_job')

        # Deleting model 'Comment'
        db.delete_table(u'schedule_comment')

        # Deleting model 'JobStatus'
        db.delete_table(u'schedule_jobstatus')

        # Deleting model 'ElevetorType'
        db.delete_table(u'schedule_elevetortype')

        # Deleting model 'JobControl'
        db.delete_table(u'schedule_jobcontrol')


    models = {
        u'contacts.contact': {
            'Meta': {'object_name': 'Contact'},
            'address_1': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'address_2': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'attention_to': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'contact_name': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'default': "'Canada'", 'max_length': '40', 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'postal_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'province': ('django.db.models.fields.CharField', [], {'default': "'Ontario'", 'max_length': '64', 'blank': 'True'}),
            'search_string': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'webpage': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'schedule.comment': {
            'Meta': {'object_name': 'Comment'},
            'comment_by': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job_comment': ('django.db.models.fields.TextField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'job_number': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'})
        },
        u'schedule.elevetortype': {
            'Meta': {'object_name': 'ElevetorType'},
            'description': ('django.db.models.fields.TextField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'elevetor_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'schedule.job': {
            'Meta': {'object_name': 'Job'},
            'address_1': ('django.db.models.fields.TextField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'cab_designation': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'contact_email': ('django.db.models.fields.CharField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'customer': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'customer_contact_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'customer_contact_phone_number': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'date_opened': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_required': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'drawing_approved_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'drawing_req_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'drawing_sent_to_customer_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'eng_comment': ('django.db.models.fields.TextField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'job_name': ('django.db.models.fields.CharField', [], {'max_length': '150', 'null': 'True', 'blank': 'True'}),
            'job_number': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'number_of_cabs': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'po_number': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'search_string': ('django.db.models.fields.TextField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': '0', 'max_length': '50'}),
            'status_notes': ('django.db.models.fields.TextField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'})
        },
        u'schedule.jobcontrol': {
            'Meta': {'object_name': 'JobControl'},
            'capacity': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'customer_po_number': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'delivery_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'elevetor_type': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'job-con-elevetor-type'", 'null': 'True', 'to': u"orm['schedule.ElevetorType']"}),
            'estimated_price_for_job': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '4', 'blank': 'True'}),
            'front': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'installed_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contacts.Contact']", 'null': 'True', 'blank': 'True'}),
            'job_name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'job_number': ('django.db.models.fields.CharField', [], {'max_length': '20', 'primary_key': 'True'}),
            'number_of_cabs': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'number_of_floors': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rear': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'rgw': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'search_string': ('django.db.models.fields.TextField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'ship_to': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'job-control-ship_to'", 'null': 'True', 'to': u"orm['contacts.Contact']"}),
            'sold_to': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'job-control-sold_to'", 'null': 'True', 'to': u"orm['contacts.Contact']"}),
            'start_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
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
            'safety_test_schedule_date': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'suren': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'suren_comment': ('django.db.models.fields.TextField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'suren_is_done': ('django.db.models.fields.CharField', [], {'default': "'none'", 'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'test_comment': ('django.db.models.fields.TextField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'third_party_install': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'third_party_install_comment': ('django.db.models.fields.TextField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'third_party_install_is_done': ('django.db.models.fields.CharField', [], {'default': "'none'", 'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'tile_installer': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'tile_installer_comment': ('django.db.models.fields.TextField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'tile_installer_is_done': ('django.db.models.fields.CharField', [], {'default': "'none'", 'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'trim_shop_is_done': ('django.db.models.fields.CharField', [], {'default': "'none'", 'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'trim_shop_req_by': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'trim_shop_req_by_comment': ('django.db.models.fields.TextField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'tssa_submitted_date': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'tssa_submitted_date_comment': ('django.db.models.fields.TextField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'tssa_submitted_date_is_done': ('django.db.models.fields.CharField', [], {'default': "'none'", 'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'welding': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'welding_comment': ('django.db.models.fields.TextField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'welding_is_done': ('django.db.models.fields.CharField', [], {'default': "'none'", 'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'who_will_test': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'wood_shop_is_done': ('django.db.models.fields.CharField', [], {'default': "'none'", 'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'wood_shop_req_by': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'wood_shop_req_by_comment': ('django.db.models.fields.TextField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['schedule']