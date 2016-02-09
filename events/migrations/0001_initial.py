# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Events'
        db.create_table(u'events_events', (
            ('eventid', self.gf('django.db.models.fields.CharField')(max_length=20, primary_key=True)),
            ('eventdate', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('eventtime', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('category', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('doorname', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('cardnumber', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('event', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('action', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('zonename', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('search_string', self.gf('django.db.models.fields.TextField')(max_length=1000, null=True, blank=True)),
        ))
        db.send_create_signal(u'events', ['Events'])

        # Adding model 'Controllers'
        db.create_table(u'alarm_controllers', (
            ('controller_name', self.gf('django.db.models.fields.CharField')(max_length=40, primary_key=True)),
            ('controllerid', self.gf('django.db.models.fields.CharField')(max_length=20, null=True)),
            ('ipaddress', self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True)),
            ('serial_number', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('doorcurrentstatus', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('doorlastopeneddate', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('doorlastopenedtime', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('doorlastcloseddate', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('doorlastclosedtime', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('card_1_name', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('card_1_type', self.gf('django.db.models.fields.CharField')(default='', max_length=3)),
            ('card_1_lastdate', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('card_1_lasttime', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('card_1_lastuser', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('card_1_lastcard', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('card_2_name', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('card_2_type', self.gf('django.db.models.fields.CharField')(default='', max_length=3)),
            ('card_2_lastdate', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('card_2_lasttime', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('card_2_lastuser', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('card_2_lastcard', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('input_1_name', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('input_1_type', self.gf('django.db.models.fields.CharField')(default='', max_length=3)),
            ('input_1_status', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('input_1_lastdate', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('input_1_lasttime', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('input_1_laststate', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('input_2_name', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('input_2_type', self.gf('django.db.models.fields.CharField')(default='', max_length=3)),
            ('input_2_status', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('input_2_lastdate', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('input_2_lasttime', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('input_2_laststate', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('input_3_name', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('input_3_type', self.gf('django.db.models.fields.CharField')(default='', max_length=3)),
            ('input_3_status', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('input_3_lastdate', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('input_3_lasttime', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('input_3_laststate', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('input_4_name', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('input_4_type', self.gf('django.db.models.fields.CharField')(default='', max_length=3)),
            ('input_4_status', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('input_4_lastdate', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('input_4_lasttime', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('input_4_laststate', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('controller_alarm_laststate', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('controller_alarm_lastdate', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('controller_alarm_lasttime', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('search_string', self.gf('django.db.models.fields.TextField')(max_length=1000, null=True, blank=True)),
        ))
        db.send_create_signal(u'events', ['Controllers'])

        # Adding model 'EventEntry'
        db.create_table(u'events_evententry', (
            ('entryid', self.gf('django.db.models.fields.CharField')(max_length=50, primary_key=True)),
            ('date_of_transaction', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('time_of_transaction', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('transaction_username', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('transaction_processed', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
            ('search_string', self.gf('django.db.models.fields.TextField')(max_length=1000, null=True, blank=True)),
        ))
        db.send_create_signal(u'events', ['EventEntry'])

        # Adding model 'EventPayroll'
        db.create_table(u'events_eventpayroll', (
            ('serial_id', self.gf('django.db.models.fields.CharField')(max_length=50, primary_key=True)),
            ('event_username', self.gf('django.db.models.fields.CharField')(max_length=40, null=True, blank=True)),
            ('premier_user', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='event-user-for', null=True, to=orm['scomuser.ScomUserProfile'])),
        ))
        db.send_create_signal(u'events', ['EventPayroll'])


    def backwards(self, orm):
        # Deleting model 'Events'
        db.delete_table(u'events_events')

        # Deleting model 'Controllers'
        db.delete_table(u'alarm_controllers')

        # Deleting model 'EventEntry'
        db.delete_table(u'events_evententry')

        # Deleting model 'EventPayroll'
        db.delete_table(u'events_eventpayroll')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'events.controllers': {
            'Meta': {'ordering': "['controllerid']", 'object_name': 'Controllers', 'db_table': "u'alarm_controllers'"},
            'card_1_lastcard': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'card_1_lastdate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'card_1_lasttime': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'card_1_lastuser': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'card_1_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'card_1_type': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '3'}),
            'card_2_lastcard': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'card_2_lastdate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'card_2_lasttime': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'card_2_lastuser': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'card_2_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'card_2_type': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '3'}),
            'controller_alarm_lastdate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'controller_alarm_laststate': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'controller_alarm_lasttime': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'controller_name': ('django.db.models.fields.CharField', [], {'max_length': '40', 'primary_key': 'True'}),
            'controllerid': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'doorcurrentstatus': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'doorlastcloseddate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'doorlastclosedtime': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'doorlastopeneddate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'doorlastopenedtime': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'input_1_lastdate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'input_1_laststate': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'input_1_lasttime': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'input_1_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'input_1_status': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'input_1_type': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '3'}),
            'input_2_lastdate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'input_2_laststate': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'input_2_lasttime': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'input_2_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'input_2_status': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'input_2_type': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '3'}),
            'input_3_lastdate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'input_3_laststate': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'input_3_lasttime': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'input_3_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'input_3_status': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'input_3_type': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '3'}),
            'input_4_lastdate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'input_4_laststate': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'input_4_lasttime': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'input_4_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'input_4_status': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'input_4_type': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '3'}),
            'ipaddress': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'search_string': ('django.db.models.fields.TextField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'serial_number': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'})
        },
        u'events.evententry': {
            'Meta': {'ordering': "['entryid']", 'object_name': 'EventEntry'},
            'date_of_transaction': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'entryid': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'search_string': ('django.db.models.fields.TextField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'time_of_transaction': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'transaction_processed': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'transaction_username': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'})
        },
        u'events.eventpayroll': {
            'Meta': {'object_name': 'EventPayroll'},
            'event_username': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'premier_user': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'event-user-for'", 'null': 'True', 'to': u"orm['scomuser.ScomUserProfile']"}),
            'serial_id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'})
        },
        u'events.events': {
            'Meta': {'ordering': "['eventid']", 'object_name': 'Events'},
            'action': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'cardnumber': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'category': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'doorname': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'event': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'eventdate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'eventid': ('django.db.models.fields.CharField', [], {'max_length': '20', 'primary_key': 'True'}),
            'eventtime': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'search_string': ('django.db.models.fields.TextField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'zonename': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'})
        },
        u'scomuser.scomuserprofile': {
            'Meta': {'object_name': 'ScomUserProfile'},
            'address_1': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'address_2': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'address_3': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'avatar': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'cell_phone': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'em_contact_1': ('django.db.models.fields.TextField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'em_contact_2': ('django.db.models.fields.TextField', [], {'max_length': '128', 'null': 'True', 'blank': 'True'}),
            'home_phone': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'internal_extension': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'max_amount_allowed_to_purchase': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'max_purchase_per_po': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'other_phone': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'postal': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'province': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'search_string': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['events']