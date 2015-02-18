# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Controllers.card_1_lastcard'
        db.alter_column(u'alarm_controllers', 'card_1_lastcard', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Controllers.input_1_status'
        db.alter_column(u'alarm_controllers', 'input_1_status', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Controllers.input_4_laststate'
        db.alter_column(u'alarm_controllers', 'input_4_laststate', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Controllers.controllerid'
        db.alter_column(u'alarm_controllers', 'controllerid', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Controllers.controller_name'
        db.alter_column(u'alarm_controllers', 'controller_name', self.gf('django.db.models.fields.CharField')(max_length=100, primary_key=True))

        # Changing field 'Controllers.input_3_type'
        db.alter_column(u'alarm_controllers', 'input_3_type', self.gf('django.db.models.fields.CharField')(max_length=10))

        # Changing field 'Controllers.card_2_lastuser'
        db.alter_column(u'alarm_controllers', 'card_2_lastuser', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Controllers.card_1_type'
        db.alter_column(u'alarm_controllers', 'card_1_type', self.gf('django.db.models.fields.CharField')(max_length=10))

        # Changing field 'Controllers.card_2_lastcard'
        db.alter_column(u'alarm_controllers', 'card_2_lastcard', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Controllers.card_2_type'
        db.alter_column(u'alarm_controllers', 'card_2_type', self.gf('django.db.models.fields.CharField')(max_length=10))

        # Changing field 'Controllers.card_2_name'
        db.alter_column(u'alarm_controllers', 'card_2_name', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Controllers.input_4_type'
        db.alter_column(u'alarm_controllers', 'input_4_type', self.gf('django.db.models.fields.CharField')(max_length=10))

        # Changing field 'Controllers.input_1_laststate'
        db.alter_column(u'alarm_controllers', 'input_1_laststate', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Controllers.input_2_laststate'
        db.alter_column(u'alarm_controllers', 'input_2_laststate', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Controllers.serial_number'
        db.alter_column(u'alarm_controllers', 'serial_number', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Controllers.card_1_name'
        db.alter_column(u'alarm_controllers', 'card_1_name', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Controllers.input_2_status'
        db.alter_column(u'alarm_controllers', 'input_2_status', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Controllers.input_3_laststate'
        db.alter_column(u'alarm_controllers', 'input_3_laststate', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Controllers.card_1_lastuser'
        db.alter_column(u'alarm_controllers', 'card_1_lastuser', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Controllers.input_4_status'
        db.alter_column(u'alarm_controllers', 'input_4_status', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Controllers.controller_alarm_laststate'
        db.alter_column(u'alarm_controllers', 'controller_alarm_laststate', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Controllers.input_1_name'
        db.alter_column(u'alarm_controllers', 'input_1_name', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Controllers.input_2_type'
        db.alter_column(u'alarm_controllers', 'input_2_type', self.gf('django.db.models.fields.CharField')(max_length=10))

        # Changing field 'Controllers.input_1_type'
        db.alter_column(u'alarm_controllers', 'input_1_type', self.gf('django.db.models.fields.CharField')(max_length=10))

        # Changing field 'Controllers.input_2_name'
        db.alter_column(u'alarm_controllers', 'input_2_name', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Controllers.doorcurrentstatus'
        db.alter_column(u'alarm_controllers', 'doorcurrentstatus', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Controllers.name'
        db.alter_column(u'alarm_controllers', 'name', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Controllers.input_3_name'
        db.alter_column(u'alarm_controllers', 'input_3_name', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Controllers.input_4_name'
        db.alter_column(u'alarm_controllers', 'input_4_name', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

        # Changing field 'Controllers.input_3_status'
        db.alter_column(u'alarm_controllers', 'input_3_status', self.gf('django.db.models.fields.CharField')(max_length=50, null=True))

    def backwards(self, orm):

        # Changing field 'Controllers.card_1_lastcard'
        db.alter_column(u'alarm_controllers', 'card_1_lastcard', self.gf('django.db.models.fields.CharField')(max_length=10, null=True))

        # Changing field 'Controllers.input_1_status'
        db.alter_column(u'alarm_controllers', 'input_1_status', self.gf('django.db.models.fields.CharField')(max_length=30, null=True))

        # Changing field 'Controllers.input_4_laststate'
        db.alter_column(u'alarm_controllers', 'input_4_laststate', self.gf('django.db.models.fields.CharField')(max_length=30, null=True))

        # Changing field 'Controllers.controllerid'
        db.alter_column(u'alarm_controllers', 'controllerid', self.gf('django.db.models.fields.CharField')(max_length=20, null=True))

        # Changing field 'Controllers.controller_name'
        db.alter_column(u'alarm_controllers', 'controller_name', self.gf('django.db.models.fields.CharField')(max_length=40, primary_key=True))

        # Changing field 'Controllers.input_3_type'
        db.alter_column(u'alarm_controllers', 'input_3_type', self.gf('django.db.models.fields.CharField')(max_length=3))

        # Changing field 'Controllers.card_2_lastuser'
        db.alter_column(u'alarm_controllers', 'card_2_lastuser', self.gf('django.db.models.fields.CharField')(max_length=30, null=True))

        # Changing field 'Controllers.card_1_type'
        db.alter_column(u'alarm_controllers', 'card_1_type', self.gf('django.db.models.fields.CharField')(max_length=3))

        # Changing field 'Controllers.card_2_lastcard'
        db.alter_column(u'alarm_controllers', 'card_2_lastcard', self.gf('django.db.models.fields.CharField')(max_length=10, null=True))

        # Changing field 'Controllers.card_2_type'
        db.alter_column(u'alarm_controllers', 'card_2_type', self.gf('django.db.models.fields.CharField')(max_length=3))

        # Changing field 'Controllers.card_2_name'
        db.alter_column(u'alarm_controllers', 'card_2_name', self.gf('django.db.models.fields.CharField')(max_length=30, null=True))

        # Changing field 'Controllers.input_4_type'
        db.alter_column(u'alarm_controllers', 'input_4_type', self.gf('django.db.models.fields.CharField')(max_length=3))

        # Changing field 'Controllers.input_1_laststate'
        db.alter_column(u'alarm_controllers', 'input_1_laststate', self.gf('django.db.models.fields.CharField')(max_length=30, null=True))

        # Changing field 'Controllers.input_2_laststate'
        db.alter_column(u'alarm_controllers', 'input_2_laststate', self.gf('django.db.models.fields.CharField')(max_length=30, null=True))

        # Changing field 'Controllers.serial_number'
        db.alter_column(u'alarm_controllers', 'serial_number', self.gf('django.db.models.fields.CharField')(max_length=10, null=True))

        # Changing field 'Controllers.card_1_name'
        db.alter_column(u'alarm_controllers', 'card_1_name', self.gf('django.db.models.fields.CharField')(max_length=30, null=True))

        # Changing field 'Controllers.input_2_status'
        db.alter_column(u'alarm_controllers', 'input_2_status', self.gf('django.db.models.fields.CharField')(max_length=30, null=True))

        # Changing field 'Controllers.input_3_laststate'
        db.alter_column(u'alarm_controllers', 'input_3_laststate', self.gf('django.db.models.fields.CharField')(max_length=30, null=True))

        # Changing field 'Controllers.card_1_lastuser'
        db.alter_column(u'alarm_controllers', 'card_1_lastuser', self.gf('django.db.models.fields.CharField')(max_length=30, null=True))

        # Changing field 'Controllers.input_4_status'
        db.alter_column(u'alarm_controllers', 'input_4_status', self.gf('django.db.models.fields.CharField')(max_length=30, null=True))

        # Changing field 'Controllers.controller_alarm_laststate'
        db.alter_column(u'alarm_controllers', 'controller_alarm_laststate', self.gf('django.db.models.fields.CharField')(max_length=30, null=True))

        # Changing field 'Controllers.input_1_name'
        db.alter_column(u'alarm_controllers', 'input_1_name', self.gf('django.db.models.fields.CharField')(max_length=30, null=True))

        # Changing field 'Controllers.input_2_type'
        db.alter_column(u'alarm_controllers', 'input_2_type', self.gf('django.db.models.fields.CharField')(max_length=3))

        # Changing field 'Controllers.input_1_type'
        db.alter_column(u'alarm_controllers', 'input_1_type', self.gf('django.db.models.fields.CharField')(max_length=3))

        # Changing field 'Controllers.input_2_name'
        db.alter_column(u'alarm_controllers', 'input_2_name', self.gf('django.db.models.fields.CharField')(max_length=30, null=True))

        # Changing field 'Controllers.doorcurrentstatus'
        db.alter_column(u'alarm_controllers', 'doorcurrentstatus', self.gf('django.db.models.fields.CharField')(max_length=10, null=True))

        # Changing field 'Controllers.name'
        db.alter_column(u'alarm_controllers', 'name', self.gf('django.db.models.fields.CharField')(max_length=30, null=True))

        # Changing field 'Controllers.input_3_name'
        db.alter_column(u'alarm_controllers', 'input_3_name', self.gf('django.db.models.fields.CharField')(max_length=30, null=True))

        # Changing field 'Controllers.input_4_name'
        db.alter_column(u'alarm_controllers', 'input_4_name', self.gf('django.db.models.fields.CharField')(max_length=30, null=True))

        # Changing field 'Controllers.input_3_status'
        db.alter_column(u'alarm_controllers', 'input_3_status', self.gf('django.db.models.fields.CharField')(max_length=30, null=True))

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
            'card_1_lastcard': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'card_1_lastdate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'card_1_lasttime': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'card_1_lastuser': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'card_1_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'card_1_type': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10'}),
            'card_2_lastcard': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'card_2_lastdate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'card_2_lasttime': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'card_2_lastuser': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'card_2_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'card_2_type': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10'}),
            'controller_alarm_lastdate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'controller_alarm_laststate': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'controller_alarm_lasttime': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'controller_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'primary_key': 'True'}),
            'controllerid': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True'}),
            'doorcurrentstatus': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'doorlastcloseddate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'doorlastclosedtime': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'doorlastopeneddate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'doorlastopenedtime': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'input_1_lastdate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'input_1_laststate': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'input_1_lasttime': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'input_1_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'input_1_status': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'input_1_type': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10'}),
            'input_2_lastdate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'input_2_laststate': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'input_2_lasttime': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'input_2_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'input_2_status': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'input_2_type': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10'}),
            'input_3_lastdate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'input_3_laststate': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'input_3_lasttime': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'input_3_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'input_3_status': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'input_3_type': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10'}),
            'input_4_lastdate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'input_4_laststate': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'input_4_lasttime': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'input_4_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'input_4_status': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'input_4_type': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '10'}),
            'ipaddress': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'search_string': ('django.db.models.fields.TextField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'serial_number': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
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
            'action': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'cardnumber': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'category': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'doorname': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'event': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'eventdate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'eventid': ('django.db.models.fields.CharField', [], {'max_length': '50', 'primary_key': 'True'}),
            'eventtime': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'search_string': ('django.db.models.fields.TextField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'zonename': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
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