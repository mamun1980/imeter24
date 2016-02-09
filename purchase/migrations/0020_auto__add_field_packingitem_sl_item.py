# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'PackingItem.sl_item'
        db.add_column(u'purchase_packingitem', 'sl_item',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['purchase.ShippingItem'], null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'PackingItem.sl_item'
        db.delete_column(u'purchase_packingitem', 'sl_item_id')


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
        u'inventory.deliverinternal': {
            'Meta': {'object_name': 'DeliverInternal'},
            'department': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'inventory.item': {
            'Meta': {'object_name': 'Item'},
            'catalog_number': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'comments': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'country_of_origin': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'currency': ('django.db.models.fields.related.ForeignKey', [], {'max_length': '20', 'to': u"orm['contacts.Currency']", 'null': 'True', 'blank': 'True'}),
            'customer_tariff_number': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'customs_designation': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inventory.CustomsDesignation']", 'null': 'True', 'blank': 'True'}),
            'date_added': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'deliver_internal': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inventory.DeliverInternal']", 'null': 'True', 'blank': 'True'}),
            'department': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['scomuser.Department']", 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'duty_percentage': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'estimated_wholesale_cost': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'hst_taxable': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'item_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'item_number': ('django.db.models.fields.CharField', [], {'max_length': '20', 'primary_key': 'True'}),
            'item_unit_measure': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inventory.ItemUnitMeasure']", 'null': 'True', 'blank': 'True'}),
            'last_PO': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'last_PO_date_expected': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'last_PO_date_ordered': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'last_PO_ordered_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'last_PO_order_by'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'last_PO_supplier': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'last_PO_supplier'", 'null': 'True', 'to': u"orm['contacts.Contact']"}),
            'last_cost_paid': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'lead_time': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'lowest_price_last_buy_PO': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'lowest_price_last_buy_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'lowest_price_paid': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'lowest_price_supplier': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'economic_supplier'", 'null': 'True', 'to': u"orm['contacts.Contact']"}),
            'max_order_qty': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '4', 'blank': 'True'}),
            'max_order_qty_remains': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '4', 'blank': 'True'}),
            'max_single_order_qty': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '4', 'blank': 'True'}),
            'minimum_qty_on_hand': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '4', 'blank': 'True'}),
            'preference_criteria': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'primary_supplier': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'item_supplier'", 'null': 'True', 'to': u"orm['contacts.Contact']"}),
            'producer_of_item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contacts.Contact']", 'null': 'True', 'blank': 'True'}),
            'production_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inventory.ProductionType']", 'null': 'True', 'blank': 'True'}),
            'pst_taxable': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'qty_on_request': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '4', 'blank': 'True'}),
            'qty_received': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'qty_received_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'quantity_on_hand': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'null': 'True', 'max_digits': '10', 'decimal_places': '4', 'blank': 'True'}),
            'quantity_on_order': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '4', 'blank': 'True'}),
            'retail_price': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'search_string': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'shipping_unit': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'shipping_weight': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'state': ('django_fsm.FSMField', [], {'default': "'new'", 'max_length': '50'}),
            'stock_status_type': ('django.db.models.fields.CharField', [], {'default': "'normal'", 'max_length': '10'}),
            'terms': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'item_payment_terms'", 'null': 'True', 'to': u"orm['contacts.PaymentTerm']"}),
            'warehouse_location': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'wholesale_cost': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'})
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
        u'purchase.deliverinternal': {
            'Meta': {'object_name': 'DeliverInternal'},
            'department': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'purchase.invoice': {
            'Meta': {'object_name': 'Invoice'},
            'broker': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'invoice_broker'", 'null': 'True', 'to': u"orm['contacts.Contact']"}),
            'comment': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'discount': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'null': 'True', 'max_digits': '10', 'decimal_places': '4', 'blank': 'True'}),
            'discount_type': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'discounted_sub_total': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'null': 'True', 'max_digits': '10', 'decimal_places': '4', 'blank': 'True'}),
            'fob': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'hst_taxable': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'hst_taxable_amount': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'null': 'True', 'max_digits': '10', 'decimal_places': '4', 'blank': 'True'}),
            'invoice_currency': ('django.db.models.fields.related.ForeignKey', [], {'max_length': '20', 'to': u"orm['contacts.Currency']", 'null': 'True', 'blank': 'True'}),
            'invoice_number': ('django.db.models.fields.CharField', [], {'max_length': '20', 'primary_key': 'True'}),
            'invoice_qty': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'null': 'True', 'max_digits': '10', 'decimal_places': '4', 'blank': 'True'}),
            'invoiced_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'invoiced_by'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'job': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['schedule.Job']", 'null': 'True', 'blank': 'True'}),
            'pl': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'packing-list'", 'null': 'True', 'to': u"orm['purchase.PackingList']"}),
            'po': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'pst_taxable': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'pst_taxable_amount': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'null': 'True', 'max_digits': '10', 'decimal_places': '4', 'blank': 'True'}),
            'ship_to': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'invoice-ship-to'", 'null': 'True', 'to': u"orm['contacts.Contact']"}),
            'ship_via': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'invoice_shipping_method'", 'null': 'True', 'to': u"orm['contacts.DeliveryChoice']"}),
            'sold_to': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'invoice-sold-to'", 'null': 'True', 'to': u"orm['contacts.Contact']"}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '5', 'null': 'True', 'blank': 'True'}),
            'sub_total': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'null': 'True', 'max_digits': '10', 'decimal_places': '4', 'blank': 'True'}),
            'terms': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'invoice_payment_terms'", 'null': 'True', 'to': u"orm['contacts.PaymentTerm']"}),
            'total_amount': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'null': 'True', 'max_digits': '10', 'decimal_places': '4', 'blank': 'True'})
        },
        u'purchase.invoiceditem': {
            'Meta': {'object_name': 'InvoicedItem'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'invoice': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['purchase.Invoice']", 'null': 'True', 'blank': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['purchase.PackingItem']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'price': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'null': 'True', 'max_digits': '10', 'decimal_places': '4', 'blank': 'True'}),
            'qty': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'null': 'True', 'max_digits': '10', 'decimal_places': '4', 'blank': 'True'}),
            'sub_total': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'null': 'True', 'max_digits': '10', 'decimal_places': '4', 'blank': 'True'}),
            'unit': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'})
        },
        u'purchase.packingitem': {
            'Meta': {'object_name': 'PackingItem'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inventory.Item']", 'null': 'True', 'blank': 'True'}),
            'line_comments': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'pl': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'pl_items'", 'null': 'True', 'to': u"orm['purchase.PackingList']"}),
            'qty_ordered': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'null': 'True', 'max_digits': '10', 'decimal_places': '4', 'blank': 'True'}),
            'qty_shipped': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'null': 'True', 'max_digits': '10', 'decimal_places': '4', 'blank': 'True'}),
            'sl_item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['purchase.ShippingItem']", 'null': 'True', 'blank': 'True'}),
            'unit': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'})
        },
        u'purchase.packinglist': {
            'Meta': {'object_name': 'PackingList'},
            'customer_broker': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'pl_customer_broker'", 'null': 'True', 'to': u"orm['contacts.Contact']"}),
            'customer_po_number': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'date_issued': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_shipped': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'freight_charges': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'null': 'True', 'max_digits': '10', 'decimal_places': '4', 'blank': 'True'}),
            'generated_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'generated_by'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'hold_at_dept_for_pickup': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'invoiced_on': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'invoiced_on_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'job_number': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['schedule.Job']", 'null': 'True', 'blank': 'True'}),
            'order_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'pl_number': ('django.db.models.fields.CharField', [], {'max_length': '20', 'primary_key': 'True'}),
            'ship_to': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'ship_to'", 'null': 'True', 'to': u"orm['contacts.Contact']"}),
            'ship_via': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'ship_via'", 'null': 'True', 'to': u"orm['contacts.DeliveryChoice']"}),
            'shipped_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'shipped_by'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'shipping_bl_number': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'shipping_comment': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'sl': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['purchase.ShippingList']", 'null': 'True', 'blank': 'True'}),
            'sold_to': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'sold_to'", 'null': 'True', 'to': u"orm['contacts.Contact']"}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'})
        },
        u'purchase.plcbcontact': {
            'Meta': {'object_name': 'PLCBContact'},
            'contact': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'contact_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'contact_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pl': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['purchase.PackingList']", 'null': 'True', 'blank': 'True'})
        },
        u'purchase.plshiptocontact': {
            'Meta': {'object_name': 'PLShipToContact'},
            'contact': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'contact_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'contact_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pl': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['purchase.PackingList']", 'null': 'True', 'blank': 'True'})
        },
        u'purchase.plsoldtocontact': {
            'Meta': {'object_name': 'PLSoldToContact'},
            'contact': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'contact_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'contact_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'pl': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['purchase.PackingList']", 'null': 'True', 'blank': 'True'})
        },
        u'purchase.pocontact': {
            'Meta': {'object_name': 'POContact'},
            'contact': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'contact_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'contact_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'purchase_order': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['purchase.PurchaseOrder']", 'null': 'True', 'blank': 'True'})
        },
        u'purchase.poshiptocontact': {
            'Meta': {'object_name': 'POShipToContact'},
            'contact': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'contact_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'contact_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'purchase_order': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['purchase.PurchaseOrder']", 'null': 'True', 'blank': 'True'})
        },
        u'purchase.postatus': {
            'Meta': {'object_name': 'POStatus'},
            'datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2016, 1, 15, 0, 0)', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'po': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['purchase.PurchaseOrder']", 'null': 'True', 'db_column': "'po_number'", 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'Canceled'", 'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'status_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'po_status_by'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'status_comment': ('django.db.models.fields.TextField', [], {'max_length': '1000', 'null': 'True', 'blank': 'True'})
        },
        u'purchase.purchaseitem': {
            'Meta': {'object_name': 'PurchaseItem'},
            'comment': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'cost': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'null': 'True', 'max_digits': '10', 'decimal_places': '4', 'blank': 'True'}),
            'custom_comment': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'custom_detail': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inventory.Item']", 'null': 'True', 'blank': 'True'}),
            'item_recv': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'null': 'True', 'max_digits': '10', 'decimal_places': '4', 'blank': 'True'}),
            'item_recv_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'job_number': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['schedule.Job']", 'null': 'True', 'blank': 'True'}),
            'po': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['purchase.PurchaseOrder']", 'null': 'True', 'blank': 'True'}),
            'purchase_status': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'qty': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'null': 'True', 'max_digits': '10', 'decimal_places': '4', 'blank': 'True'}),
            'search_string': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'sub_total': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'null': 'True', 'max_digits': '10', 'decimal_places': '4', 'blank': 'True'}),
            'unit': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'})
        },
        u'purchase.purchaseorder': {
            'Meta': {'object_name': 'PurchaseOrder'},
            'blanket_po': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'date_confirmed': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_expected': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'date_issued': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'datetime': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2016, 1, 15, 0, 0)', 'null': 'True', 'blank': 'True'}),
            'deliver_internal': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['purchase.DeliverInternal']", 'null': 'True', 'blank': 'True'}),
            'fob': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'hst_taxable': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'hst_taxable_amount': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'null': 'True', 'max_digits': '10', 'decimal_places': '4', 'blank': 'True'}),
            'items_total': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'null': 'True', 'max_digits': '10', 'decimal_places': '4', 'blank': 'True'}),
            'next_number': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'po_created_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'po_created_by'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'po_currency': ('django.db.models.fields.related.ForeignKey', [], {'max_length': '20', 'to': u"orm['contacts.Currency']", 'null': 'True', 'blank': 'True'}),
            'po_number': ('django.db.models.fields.CharField', [], {'max_length': '20', 'primary_key': 'True'}),
            'po_overwridden_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'po_overwridden_by'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'po_que': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'po_status': ('django.db.models.fields.CharField', [], {'default': "'New'", 'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'po_total_before_tax': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'null': 'True', 'max_digits': '10', 'decimal_places': '4', 'blank': 'True'}),
            'pst_taxable': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'pst_taxable_amount': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'null': 'True', 'max_digits': '10', 'decimal_places': '4', 'blank': 'True'}),
            'purchasing_agent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'purchasing_agent'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'returned_type': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'save_final_draft': ('django.db.models.fields.NullBooleanField', [], {'null': 'True', 'blank': 'True'}),
            'search_string': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'ship_to': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'po_ship_to'", 'null': 'True', 'to': u"orm['contacts.Contact']"}),
            'ship_via': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'po_shipping_method'", 'null': 'True', 'to': u"orm['contacts.DeliveryChoice']"}),
            'shipping_inst': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'supplier': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'po_item_supplier'", 'null': 'True', 'to': u"orm['contacts.Contact']"}),
            'terms': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'po_payment_terms'", 'null': 'True', 'to': u"orm['contacts.PaymentTerm']"}),
            'total_hst_tax': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'null': 'True', 'max_digits': '10', 'decimal_places': '4', 'blank': 'True'}),
            'total_po_amount': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'null': 'True', 'max_digits': '10', 'decimal_places': '4', 'blank': 'True'}),
            'total_pst_tax': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'null': 'True', 'max_digits': '10', 'decimal_places': '4', 'blank': 'True'}),
            'total_tax': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'null': 'True', 'max_digits': '10', 'decimal_places': '4', 'blank': 'True'})
        },
        u'purchase.purchaserequest': {
            'Meta': {'object_name': 'PurchaseRequest'},
            'approved_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'approved_qty': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'null': 'True', 'max_digits': '10', 'decimal_places': '4', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inventory.Item']", 'null': 'True', 'blank': 'True'}),
            'item_require_before': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'order_qty': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'null': 'True', 'max_digits': '10', 'decimal_places': '4', 'blank': 'True'}),
            'requeste_created_at': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'user_requested': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'po_requested_user'", 'null': 'True', 'to': u"orm['auth.User']"})
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
            'qty_received': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'null': 'True', 'max_digits': '10', 'decimal_places': '4', 'blank': 'True'}),
            'reveived_by': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'item_recv_by'", 'null': 'True', 'to': u"orm['auth.User']"}),
            'search_string': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'sub_total': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'null': 'True', 'max_digits': '10', 'decimal_places': '4', 'blank': 'True'})
        },
        u'purchase.requestitem': {
            'Meta': {'object_name': 'RequestItem'},
            'approved_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'approved_qty': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'null': 'True', 'max_digits': '10', 'decimal_places': '4', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inventory.Item']", 'null': 'True', 'blank': 'True'}),
            'po': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['purchase.PurchaseOrder']", 'null': 'True', 'blank': 'True'}),
            'pr': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['purchase.PurchaseRequest']", 'null': 'True', 'blank': 'True'}),
            'status': ('django.db.models.fields.IntegerField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'total_po_qty': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'null': 'True', 'max_digits': '10', 'decimal_places': '4', 'blank': 'True'})
        },
        u'purchase.shippingitem': {
            'Meta': {'object_name': 'ShippingItem'},
            'backordered': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'null': 'True', 'max_digits': '10', 'decimal_places': '4', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'shipping-item'", 'to': u"orm['inventory.Item']"}),
            'ordered': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'null': 'True', 'max_digits': '10', 'decimal_places': '4', 'blank': 'True'}),
            'search_string': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'shipped_total_to_date': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'null': 'True', 'max_digits': '10', 'decimal_places': '4', 'blank': 'True'}),
            'shipping_list': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'sl-item'", 'to': u"orm['purchase.ShippingList']"}),
            'unit_measure': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'})
        },
        u'purchase.shippinglist': {
            'Meta': {'object_name': 'ShippingList'},
            'customer_job_number': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'customer_po_number': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'date_required': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'job_number': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['schedule.Job']", 'null': 'True', 'blank': 'True'}),
            'ordered_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'search_string': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'ship_to': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'sl_ship_to'", 'null': 'True', 'to': u"orm['contacts.Contact']"}),
            'ship_via': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'sl_ship_via'", 'null': 'True', 'to': u"orm['contacts.DeliveryChoice']"}),
            'sl_number': ('django.db.models.fields.CharField', [], {'max_length': '20', 'primary_key': 'True'}),
            'sl_status': ('django.db.models.fields.CharField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'sold_to': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'sl_sold_to'", 'null': 'True', 'to': u"orm['contacts.Contact']"})
        },
        u'purchase.slshiptocontact': {
            'Meta': {'object_name': 'SLShipToContact'},
            'contact': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'contact_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'contact_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sl': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['purchase.ShippingList']", 'null': 'True', 'blank': 'True'})
        },
        u'purchase.slsoldtocontact': {
            'Meta': {'object_name': 'SLSoldToContact'},
            'contact': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'contact_name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'contact_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sl': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['purchase.ShippingList']", 'null': 'True', 'blank': 'True'})
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
        u'scomuser.department': {
            'Meta': {'object_name': 'Department'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['purchase']