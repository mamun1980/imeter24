# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Item'
        db.create_table(u'inventory_item', (
            ('item_number', self.gf('django.db.models.fields.CharField')(max_length=20, primary_key=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('quantity_on_hand', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('department', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['scomuser.Department'], null=True, blank=True)),
            ('quantity_on_order', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('comments', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('item_unit_measure', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inventory.ItemUnitMeasure'], null=True, blank=True)),
            ('stock_status_type', self.gf('django.db.models.fields.CharField')(default='normal', max_length=25)),
            ('currency', self.gf('django.db.models.fields.related.ForeignKey')(max_length=20, to=orm['contacts.Currency'], null=True, blank=True)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('qty_on_request', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('minimum_qty', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('max_order_qty', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('max_single_order_qty', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('retail_price', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('wholesale_cost', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('estimated_wholesale_cost', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('production_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inventory.ProductionType'], null=True, blank=True)),
            ('PO_status', self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True)),
            ('catalog_number', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('country_of_origin', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('lead_time', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('customs_designation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inventory.CustomsDesignation'], null=True, blank=True)),
            ('customer_tariff_number', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('preference_criteria', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('producer_of_item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contacts.Contact'], null=True, blank=True)),
            ('shipping_weight', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('minimum_qty_on_hand', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('duty_percentage', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'inventory', ['Item'])


    def backwards(self, orm):
        # Deleting model 'Item'
        db.delete_table(u'inventory_item')


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
            'webpage': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        },
        u'contacts.currency': {
            'Meta': {'object_name': 'Currency'},
            'currency': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'inventory.customsdesignation': {
            'Meta': {'object_name': 'CustomsDesignation'},
            'designation': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'})
        },
        u'inventory.item': {
            'Meta': {'object_name': 'Item'},
            'PO_status': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'catalog_number': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'comments': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'country_of_origin': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'currency': ('django.db.models.fields.related.ForeignKey', [], {'max_length': '20', 'to': u"orm['contacts.Currency']", 'null': 'True', 'blank': 'True'}),
            'customer_tariff_number': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'customs_designation': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inventory.CustomsDesignation']", 'null': 'True', 'blank': 'True'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'department': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['scomuser.Department']", 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'duty_percentage': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'estimated_wholesale_cost': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'item_number': ('django.db.models.fields.CharField', [], {'max_length': '20', 'primary_key': 'True'}),
            'item_unit_measure': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inventory.ItemUnitMeasure']", 'null': 'True', 'blank': 'True'}),
            'lead_time': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'max_order_qty': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'max_single_order_qty': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'minimum_qty': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'minimum_qty_on_hand': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'preference_criteria': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'producer_of_item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contacts.Contact']", 'null': 'True', 'blank': 'True'}),
            'production_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inventory.ProductionType']", 'null': 'True', 'blank': 'True'}),
            'qty_on_request': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'quantity_on_hand': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'quantity_on_order': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'retail_price': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'shipping_weight': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'stock_status_type': ('django.db.models.fields.CharField', [], {'default': "'normal'", 'max_length': '25'}),
            'wholesale_cost': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'})
        },
        u'inventory.itemunitmeasure': {
            'Meta': {'object_name': 'ItemUnitMeasure'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'unit_name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'})
        },
        u'inventory.productiontype': {
            'Meta': {'object_name': 'ProductionType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'production_type_name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'})
        },
        u'scomuser.department': {
            'Meta': {'object_name': 'Department'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['inventory']