# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ItemUnitMeasure'
        db.create_table(u'inventory_itemunitmeasure', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('unit_name', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'inventory', ['ItemUnitMeasure'])

        # Adding model 'ProductionType'
        db.create_table(u'inventory_productiontype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('production_type_name', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'inventory', ['ProductionType'])

        # Adding model 'CustomsDesignation'
        db.create_table(u'inventory_customsdesignation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('designation', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal(u'inventory', ['CustomsDesignation'])

        # Adding model 'Location'
        db.create_table(u'inventory_location', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('warehouse_location', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
        ))
        db.send_create_signal(u'inventory', ['Location'])

        # Adding model 'Item'
        db.create_table(u'inventory_item', (
            ('item_number', self.gf('django.db.models.fields.CharField')(max_length=20, primary_key=True)),
            ('description', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('quantity_on_hand', self.gf('django.db.models.fields.DecimalField')(default=0.0, null=True, max_digits=10, decimal_places=4, blank=True)),
            ('department', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['scomuser.Department'], null=True, blank=True)),
            ('quantity_on_order', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=4, blank=True)),
            ('primary_supplier', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='item_supplier', null=True, to=orm['contacts.Contact'])),
            ('qty_received', self.gf('django.db.models.fields.DecimalField')(default=0.0, null=True, max_digits=10, decimal_places=2, blank=True)),
            ('qty_received_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('last_PO', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('last_PO_date_ordered', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('last_PO_date_expected', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('last_cost_paid', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('last_PO_ordered_by', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='last_PO_order_by', null=True, to=orm['auth.User'])),
            ('last_PO_supplier', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='last_PO_supplier', null=True, to=orm['contacts.Contact'])),
            ('comments', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('item_unit_measure', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inventory.ItemUnitMeasure'], null=True, blank=True)),
            ('stock_status_type', self.gf('django.db.models.fields.CharField')(default='normal', max_length=10)),
            ('currency', self.gf('django.db.models.fields.related.ForeignKey')(max_length=20, to=orm['contacts.Currency'], null=True, blank=True)),
            ('warehouse_location', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inventory.Location'], null=True, blank=True)),
            ('lowest_price_supplier', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='economic_supplier', null=True, to=orm['contacts.Contact'])),
            ('lowest_price_paid', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('lowest_price_last_buy_date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('lowest_price_last_buy_PO', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('qty_on_request', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=4, blank=True)),
            ('max_order_qty', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=4, blank=True)),
            ('max_single_order_qty', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=4, blank=True)),
            ('max_order_qty_remains', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=4, blank=True)),
            ('wholesale_cost', self.gf('django.db.models.fields.DecimalField')(default=0.0, null=True, max_digits=10, decimal_places=2, blank=True)),
            ('retail_price', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('estimated_wholesale_cost', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('production_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inventory.ProductionType'], null=True, blank=True)),
            ('catalog_number', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('country_of_origin', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('lead_time', self.gf('django.db.models.fields.CharField')(max_length=20, null=True, blank=True)),
            ('customs_designation', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inventory.CustomsDesignation'], null=True, blank=True)),
            ('customer_tariff_number', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('preference_criteria', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('producer_of_item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contacts.Contact'], null=True, blank=True)),
            ('shipping_weight', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('minimum_qty_on_hand', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=4, blank=True)),
            ('duty_percentage', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=10, decimal_places=2, blank=True)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=250, null=True, blank=True)),
            ('item_image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
            ('date_added', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('terms', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='item_payment_terms', null=True, to=orm['contacts.PaymentTerm'])),
            ('search_string', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('state', self.gf('django_fsm.FSMField')(default='new', max_length=50)),
        ))
        db.send_create_signal(u'inventory', ['Item'])

        # Adding model 'ItemComment'
        db.create_table(u'inventory_itemcomment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('item', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inventory.Item'], null=True, blank=True)),
            ('comment', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('comment_date', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('comment_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True)),
        ))
        db.send_create_signal(u'inventory', ['ItemComment'])


    def backwards(self, orm):
        # Deleting model 'ItemUnitMeasure'
        db.delete_table(u'inventory_itemunitmeasure')

        # Deleting model 'ProductionType'
        db.delete_table(u'inventory_productiontype')

        # Deleting model 'CustomsDesignation'
        db.delete_table(u'inventory_customsdesignation')

        # Deleting model 'Location'
        db.delete_table(u'inventory_location')

        # Deleting model 'Item'
        db.delete_table(u'inventory_item')

        # Deleting model 'ItemComment'
        db.delete_table(u'inventory_itemcomment')


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
            'department': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['scomuser.Department']", 'null': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'duty_percentage': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'estimated_wholesale_cost': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
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
            'qty_on_request': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '4', 'blank': 'True'}),
            'qty_received': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'qty_received_date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'quantity_on_hand': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'null': 'True', 'max_digits': '10', 'decimal_places': '4', 'blank': 'True'}),
            'quantity_on_order': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '4', 'blank': 'True'}),
            'retail_price': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'search_string': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'shipping_weight': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'state': ('django_fsm.FSMField', [], {'default': "'new'", 'max_length': '50'}),
            'stock_status_type': ('django.db.models.fields.CharField', [], {'default': "'normal'", 'max_length': '10'}),
            'terms': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'item_payment_terms'", 'null': 'True', 'to': u"orm['contacts.PaymentTerm']"}),
            'warehouse_location': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inventory.Location']", 'null': 'True', 'blank': 'True'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            'wholesale_cost': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'})
        },
        u'inventory.itemcomment': {
            'Meta': {'object_name': 'ItemComment'},
            'comment': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'comment_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'comment_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inventory.Item']", 'null': 'True', 'blank': 'True'})
        },
        u'inventory.itemunitmeasure': {
            'Meta': {'object_name': 'ItemUnitMeasure'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'unit_name': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'})
        },
        u'inventory.location': {
            'Meta': {'object_name': 'Location'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'warehouse_location': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
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