from django.db import models
from contacts.models import *
from scomuser.models import *
from inventory.choices import *
# from purchase.models import PurchaseItem
from django_fsm import FSMField, transition
# Create your models here.


class ItemUnitMeasure(models.Model):
	unit_name = models.CharField(max_length=20, null=True, blank=True)
	is_active = models.BooleanField(verbose_name="Is Active", blank=False, default=True)

	def __unicode__(self):
		return self.unit_name

	class Meta:
		verbose_name = "Item Unit Measure"
		verbose_name_plural = "Item Unit Measure"

		permissions = (
    		('view_itemunitmeasure', 'Can View Item Unit Measure'),
    	)

class ProductionType(models.Model):
	production_type_name = models.CharField(max_length=20, null=True, blank=True)
	is_active = models.BooleanField(verbose_name="Is Active", blank=False, default=True)

	def __unicode__(self):
		return self.production_type_name

	class Meta:
		verbose_name = "Production Type Name"
		verbose_name_plural = "Production Type Names"

		permissions = (
    		('view_productiontype', 'Can View Production Type Name'),
    	)

class CustomsDesignation(models.Model):
	designation = models.CharField(max_length=20, null=True, blank=True)
	is_active = models.BooleanField(verbose_name="Is Active", blank=False, default=True)

	def __unicode__(self):
		return self.designation

	class Meta:
		verbose_name = "Designation"
		verbose_name_plural = "Designations"

		permissions = (
    		('view_customsdesignation', 'Can View Custom Designation'),
    	)

class Location(models.Model):
	warehouse_location = models.CharField(max_length=50, blank=True, null=True, help_text="BIN # in warehouse")
	description = models.TextField(blank=True, null=True)

	def __unicode__(self):
		return self.warehouse_location

	class Meta:
		verbose_name = "Location"
		verbose_name_plural = "Locations"

		permissions = (
    		('view_location', 'Can View Location'),
    	)


class Item(models.Model):
	item_number = models.CharField(max_length=20, primary_key=True)
	description  = models.TextField(blank=True, null=True)
	quantity_on_hand = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True, default=0.0)
	department = models.ForeignKey(Department, blank=True, null=True)
	quantity_on_order = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
	primary_supplier = models.ForeignKey(Contact, blank=True, null=True, related_name='item_supplier')
	
	'''
	last_PO, date_ordered, date_expected, last_cost_paid = These field will be auto updated with po or invoice
	'''
	qty_received = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, default=0.0)
	qty_received_date = models.DateField(blank=True, null=True)
	last_PO = models.CharField(max_length=20, blank=True, null=True)
	last_PO_date_ordered = models.DateField(blank=True, null=True)
	last_PO_date_expected = models.DateField(blank=True, null=True)
	last_cost_paid = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
	last_PO_ordered_by = models.ForeignKey(User, blank=True, null=True, related_name='last_PO_order_by')
	last_PO_supplier = models.ForeignKey(Contact, blank=True, null=True, related_name='last_PO_supplier')
	
	comments = models.TextField(blank=True, null=True, help_text="Anything entered here will print on reports")
	item_unit_measure = models.ForeignKey(ItemUnitMeasure, blank=True, null=True)
	
	stock_status_type = models.CharField(max_length=10, choices=STOCK_STATUS_TYPE, default="normal")
	currency = models.ForeignKey(Currency, max_length=20, blank=True, null=True)
	warehouse_location = models.ForeignKey(Location, blank=True, null=True)

	lowest_price_supplier = models.ForeignKey(Contact, blank=True, null=True, related_name="economic_supplier")
	lowest_price_paid = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
	lowest_price_last_buy_date = models.DateField(blank=True, null=True)
	lowest_price_last_buy_PO = models.CharField(max_length=20, blank=True, null=True)

	# last_shop_order = models.CharField(max_length=10, blank=True, null=True)
	# shop_order_date = models.DateField(blank=True, null=True)
	# shop_order_expected = models.DateField(blank=True, null=True)
	# shop_order_status = models.CharField(max_length=10, choices=SHOP_STATUS_CHOICES, default="0", blank=False, null=False)
	
	qty_on_request = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
	max_order_qty = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
	max_single_order_qty = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
	# This field value give remaining qty of item for max_order_qty
	max_order_qty_remains = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
	wholesale_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, default=0.0)
	retail_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
	
	estimated_wholesale_cost = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
	
	production_type =  models.ForeignKey(ProductionType, blank=True, null=True)
	catalog_number = models.CharField(max_length=50, blank=True, null=True, help_text = "Supplier part number to use on our POs")
	country_of_origin = models.CharField(max_length=50, blank=True, null=True)
	lead_time = models.CharField(max_length=20, blank=True, null=True, 
		help_text='Enter lead time in English, such as "14 d" or "14 days" or even "3m 2d"')
	customs_designation = models.ForeignKey(CustomsDesignation, blank=True, null=True, 
		help_text="Enter minimum 4 digit WCO HS code for exporting.")
	customer_tariff_number  = models.CharField(max_length=50, blank=True, null=True)
	preference_criteria = models.CharField(max_length=50, blank=True, null=True)
	producer_of_item = models.ForeignKey(Contact, blank=True, null=True)
	shipping_weight = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
	minimum_qty_on_hand = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True)
	duty_percentage = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
	# notes = GenericRelation(Comment, object_id_field='object_pk', 
	# 	help_text=_("Anything entered here can only be displayed online."))
	# site = models.ForeignKey(Contact, blank=True, null=True, related_name='item-site',
	#  	help_text="Indicate which contact/site this record belongs to")
	hst_taxable = models.BooleanField(verbose_name="HST Taxable", default=True)
	pst_taxable = models.BooleanField(verbose_name="PST Taxable", default=True)
	website = models.URLField(blank=True, null=True, max_length=250)
	item_image = models.ImageField(upload_to='item_image', blank=True, null=True)
	date_added = models.DateTimeField('date added', auto_now_add=True)
	date_modified = models.DateTimeField('date modified', auto_now=True)
	terms = models.ForeignKey(PaymentTerm, blank=True, null=True, related_name='item_payment_terms')
	search_string 	  = models.TextField(null=True, blank=True, verbose_name='Search String')
	state = FSMField(default='new')

	def __unicode__(self):
		return self.item_number

	def get_currency(self):
		if self.currency:
			pass
	
	@property	
	def order_restriction(self):
		if self.max_order_qty_remains and self.max_single_order_qty:
			if self.max_order_qty_remains <= self.max_single_order_qty:
				return self.max_order_qty_remains
			else:
				return self.max_single_order_qty
		else:
			return self.max_single_order_qty

	class Meta:
		verbose_name = "Item"
		verbose_name_plural = "Items"

		permissions = (
    		('view_item', 'Can View Item'),
    	)

class ItemComment(models.Model):
	item = models.ForeignKey(Item, blank=True, null=True)
	comment = models.TextField(null=True, blank=True, verbose_name='Item Comment')
	comment_date = models.DateTimeField('comment date', auto_now=True)
	comment_by = models.ForeignKey(User, blank=True, null=True)

	def __unicode__(self):
		return self.item.item_number

	class Meta:
		verbose_name = "ItemComment"
		verbose_name_plural = "Item Comments"

		permissions = (
    		('view_itemcomment', 'Can View Item comment'),
    	)

