# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'PurchaseOrder.po_created_by'
        db.add_column(u'purchase_purchaseorder', 'po_created_by',
                      self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='po_created_by', null=True, to=orm['auth.User']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'PurchaseOrder.po_created_by'
        db.delete_column(u'purchase_purchaseorder', 'po_created_by_id')


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
        u'contacts.currency': {
            'Meta': {'object_name': 'Currency'},
            'currency': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
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
            'last_PO': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'last_PO_date_expected': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'last_PO_date_ordered': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'last_PO_ordered_by': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'last_PO_supplier': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'last_PO_supplier'", 'null': 'True', 'to': u"orm['contacts.Contact']"}),
            'last_cost_paid': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'lead_time': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'lowest_price_last_buy_PO': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'lowest_price_last_buy_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'lowest_price_paid': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'lowest_price_supplier': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'economic_supplier'", 'null': 'True', 'to': u"orm['contacts.Contact']"}),
            'max_order_qty': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'max_single_order_qty': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'minimum_qty': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'minimum_qty_on_hand': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'preference_criteria': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'primary_supplier': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'item_supplier'", 'null': 'True', 'to': u"orm['contacts.Contact']"}),
            'producer_of_item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contacts.Contact']", 'null': 'True', 'blank': 'True'}),
            'production_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inventory.ProductionType']", 'null': 'True', 'blank': 'True'}),
            'qty_on_request': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'quantity_on_hand': ('django.db.models.fields.DecimalField', [], {'default': '0', 'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'quantity_on_order': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'retail_price': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'search_string': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'shipping_weight': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'item-site'", 'null': 'True', 'to': u"orm['contacts.Contact']"}),
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
        u'purchase.pocontact': {
            'Meta': {'object_name': 'POContact'},
            'contact': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'contact_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'purchase_order': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'})
        },
        u'purchase.postatus': {
            'Meta': {'object_name': 'POStatus'},
            'datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 6, 19, 0, 0)', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'po': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['purchase.PurchaseOrder']", 'null': 'True', 'db_column': "'po_number'", 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'Canceled'", 'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'status_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'po_status_by'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'status_comment': ('django.db.models.fields.TextField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'})
        },
        u'purchase.purchaseitem': {
            'Meta': {'object_name': 'PurchaseItem'},
            'cost': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inventory.Item']", 'null': 'True', 'blank': 'True'}),
            'item_recv': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'job_number': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['schedule.Job']", 'null': 'True', 'blank': 'True'}),
            'purchase_status': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'qty': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'search_string': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'sub_total': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'})
        },
        u'purchase.purchaseorder': {
            'Meta': {'object_name': 'PurchaseOrder'},
            'blanket_po': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'date_confirmed': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_expected': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_issued': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2014, 6, 19, 0, 0)', 'null': 'True', 'blank': 'True'}),
            'deliver_internal': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'fob': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'items': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['purchase.PurchaseItem']", 'null': 'True', 'blank': 'True'}),
            'items_total': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'next_number': ('django.db.models.fields.CharField', [], {'max_length': '20', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'po_created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'po_created_by'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'po_number': ('django.db.models.fields.CharField', [], {'max_length': '20', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'po_overwridden_by': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'po_que': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'pst_taxable': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'purchasing_agent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'purchasing_agent'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'returned_type': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'search_string': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'ship_to': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'po_ship_to'", 'null': 'True', 'to': u"orm['contacts.Contact']"}),
            'ship_via': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'shipping_inst': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'New'", 'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'supplier': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'po_item_supplier'", 'null': 'True', 'to': u"orm['contacts.Contact']"}),
            'terms': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'})
        },
        u'purchase.purchaserequest': {
            'Meta': {'object_name': 'PurchaseRequest'},
            'approved_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'approved_qty': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inventory.Item']", 'null': 'True', 'blank': 'True'}),
            'item_require_before': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'order_qty': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'requeste_created_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'user_requested': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'po_requested_user'", 'to': u"orm['auth.User']"})
        },
        u'purchase.purchaserequestcomment': {
            'Meta': {'object_name': 'PurchaseRequestComment'},
            'comment': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'commnet_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'purchase_request': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['purchase.PurchaseRequest']"}),
            'user_commented': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'prc_user'", 'to': u"orm['auth.User']"})
        },
        u'purchase.receiveditemhistory': {
            'Meta': {'object_name': 'ReceivedItemHistory'},
            'comment': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item_po': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['purchase.PurchaseOrder']", 'null': 'True', 'blank': 'True'}),
            'item_received_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'purchase_item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['purchase.PurchaseItem']", 'null': 'True', 'blank': 'True'}),
            'qty_received': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'reveived_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'item_recv_by'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'search_string': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'sub_total': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'})
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
            'job_number': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'number_of_cabs': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'po_number': ('django.db.models.fields.CharField', [], {'max_length': '40', 'null': 'True', 'blank': 'True'}),
            'search_string': ('django.db.models.fields.TextField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': '0', 'max_length': '50'}),
            'status_notes': ('django.db.models.fields.TextField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'})
        },
        u'scomuser.department': {
            'Meta': {'object_name': 'Department'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['purchase']