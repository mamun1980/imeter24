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
        ))
        db.send_create_signal(u'events', ['Events'])

        # Adding model 'Controllers'
        db.create_table(u'alarm_controllers', (
            ('controller_name', self.gf('django.db.models.fields.CharField')(max_length=40, primary_key=True)),
            ('controllerid', self.gf('django.db.models.fields.CharField')(max_length=20, null=True)),
            ('ipaddress', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
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
        ))
        db.send_create_signal(u'events', ['Controllers'])


    def backwards(self, orm):
        # Deleting model 'Events'
        db.delete_table(u'events_events')

        # Deleting model 'Controllers'
        db.delete_table(u'alarm_controllers')


    models = {
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
            'ipaddress': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'serial_number': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'})
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
            'zonename': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['events']