# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Controller'
        db.create_table(u'controllers_controller', (
            ('controller_id', self.gf('django.db.models.fields.CharField')(max_length=20, primary_key=True)),
            ('sold_to', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='controller_sold_to', null=True, to=orm['contacts.Contact'])),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='controller_location', null=True, to=orm['contacts.Contact'])),
            ('controller_type', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'controllers', ['Controller'])

        # Adding model 'ControllerContact'
        db.create_table(u'controllers_controllercontact', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('controller', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['controllers.Controller'], null=True)),
            ('contact_id', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=10, null=True, blank=True)),
        ))
        db.send_create_signal(u'controllers', ['ControllerContact'])


    def backwards(self, orm):
        # Deleting model 'Controller'
        db.delete_table(u'controllers_controller')

        # Deleting model 'ControllerContact'
        db.delete_table(u'controllers_controllercontact')


    models = {
        u'contacts.contact': {
            'Meta': {'object_name': 'Contact'},
            'address_1': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'address_2': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'ap_contact': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'attention_to': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'bv_ap_account': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'bv_ar_account': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'contact_name': ('django.db.models.fields.CharField', [], {'max_length': '64', 'null': 'True', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'default': "'Canada'", 'max_length': '40', 'null': 'True'}),
            'currency': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contacts.Currency']", 'null': 'True', 'blank': 'True'}),
            'fob': ('django.db.models.fields.CharField', [], {'default': "'Oshawa, Ontario, Canada'", 'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'foreign_account': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'gst_number': ('django.db.models.fields.CharField', [], {'max_length': '17', 'null': 'True', 'blank': 'True'}),
            'gst_tax_exempt': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hst_number': ('django.db.models.fields.CharField', [], {'max_length': '17', 'null': 'True', 'blank': 'True'}),
            'hst_tax_exempt': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_activity': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'mail_list': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'postal_code': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'province': ('django.db.models.fields.CharField', [], {'default': "'Ontario'", 'max_length': '64', 'blank': 'True'}),
            'pst_number': ('django.db.models.fields.CharField', [], {'max_length': '11', 'null': 'True', 'blank': 'True'}),
            'pst_tax_exempt': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'record_created': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'ship_collect': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'shipping_method': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contacts.DeliveryChoice']", 'null': 'True', 'blank': 'True'}),
            'terms': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contacts.PaymentTerm']", 'null': 'True', 'blank': 'True'}),
            'webpage': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'contacts.currency': {
            'Meta': {'object_name': 'Currency'},
            'currency': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'}),
            'currency_icon': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'contacts.deliverychoice': {
            'Meta': {'object_name': 'DeliveryChoice'},
            'delivery_choice': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'contacts.paymentterm': {
            'Meta': {'object_name': 'PaymentTerm'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'term': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'})
        },
        u'controllers.controller': {
            'Meta': {'object_name': 'Controller'},
            'controller_id': ('django.db.models.fields.CharField', [], {'max_length': '20', 'primary_key': 'True'}),
            'controller_type': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'controller_location'", 'null': 'True', 'to': u"orm['contacts.Contact']"}),
            'sold_to': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'controller_sold_to'", 'null': 'True', 'to': u"orm['contacts.Contact']"})
        },
        u'controllers.controllercontact': {
            'Meta': {'object_name': 'ControllerContact'},
            'contact_id': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'controller': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['controllers.Controller']", 'null': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '10', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['controllers']