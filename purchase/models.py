from django.db import models
from purchase.choices import *
from datetime import datetime
from inventory.models import *
from schedule.models import *

# Create your models here.

class DeliverInternal(models.Model):
	department = models.CharField(max_length=50, blank=True, null=True, help_text="BIN # in warehouse")
	description = models.TextField(blank=True, null=True)

	def __unicode__(self):
		return self.department

	class Meta:
		verbose_name = "Deliver Internal"
		verbose_name_plural = "Deliver Internals"

		permissions = (
    		('view_deliverinternal', 'Can View Deliver Internal'),
    	)



class PurchaseRequest(models.Model):
	"""docstring for PurchaseRequest"""
	user_requested = models.ForeignKey(User, blank=True, null=True, related_name='po_requested_user')
	item = models.ForeignKey(Item, blank=True, null=True)
	description = models.TextField(blank=True, null=True)
	order_qty = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True,default=0.0)
	item_require_before = models.DateField(blank=True, null=True)
	requeste_created_at = models.DateTimeField(blank=True, null=True)
	approved_qty = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True, default=0.0)
	approved_date = models.DateField(blank=True, null=True)
	status = models.CharField(max_length=15, blank=True, null=True)

	def __unicode__(self):
		return str(self.id)

	def status_verbose(self):
		return dict(PR_STATUS)[int(self.status)]

	class Meta:
		verbose_name = u"Purchase Request"
		verbose_name_plural = u"Purchase Requests"

		permissions = (
			('view_purchase_request', 'Can View Purchase Request'),
			('approve_purchase_request', 'Can Approve Purchase Request'),
		)



class PurchaseRequestComment(models.Model):
	purchase_request = models.ForeignKey(PurchaseRequest)
	comment = models.TextField(blank=True, null=True)
	commnet_date = models.DateTimeField(blank=True, null=True)
	user_commented = models.ForeignKey(User, related_name='prc_user')

	def __unicode__(self):
		return str(self.id)

	class Meta:
		verbose_name = u"Purchase Request Comment"
		verbose_name_plural = u"Purchase Request Comments"

		permissions = (
			('view_purchase_request_comment', 'Can View Purchase Request Comment'),
		)




class PurchaseOrder(models.Model):
	'''
	PurchaseOrder will be added for one or more PR.

	'''
	po_number = models.CharField(verbose_name='PO Number', max_length=20, primary_key=True)
	next_number = models.CharField(verbose_name='Next Number', max_length=20, blank=True, null= True)
	date_issued = models.DateField(blank=True, null=True)
	po_status = models.CharField(max_length=20, blank=True, null=True, default='New')
	date_expected = models.DateField(blank=True, null=True)
	supplier = models.ForeignKey(Contact, blank=True, null=True, related_name='po_item_supplier')
	ship_to = models.ForeignKey(Contact, blank=True, null=True, related_name='po_ship_to')
	ship_via = models.ForeignKey(DeliveryChoice, blank=True, null=True, 
		related_name='po_shipping_method')
	terms = models.ForeignKey(PaymentTerm, blank=True, null=True, related_name='po_payment_terms')
	fob = models.CharField(max_length=200, blank=True, null=True)
	shipping_inst = models.TextField(blank=True, null=True)
	deliver_internal = models.ForeignKey(DeliverInternal, blank=True, null=True)
	date_confirmed = models.DateField(blank=True, null=True)
	blanket_po = models.CharField(max_length=2, blank=True, null=True)
	purchasing_agent = models.ForeignKey(User, blank=True, null=True, 
		related_name='purchasing_agent')
	returned_type = models.CharField(max_length=100, blank=True, null=True)
	# items = models.ManyToManyField(PurchaseItem, blank=True, null=True)
	items_total = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True, default=0.0)
	po_total_before_tax = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True, default=0.0)
	hst_taxable = models.CharField(max_length=2, blank=True, null=True)
	hst_taxable_amount = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True, default=0.0)
	total_hst_tax = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True, default=0.0)
	
	pst_taxable = models.CharField(max_length=2, blank=True, null=True)
	pst_taxable_amount = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True, default=0.0)
	total_pst_tax = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True, default=0.0)
	
	total_tax = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True, default=0.0)
	
	po_currency = models.ForeignKey(Currency, max_length=20, blank=True, null=True)
	total_po_amount = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True, default=0.0)
	po_overwridden_by = models.ForeignKey(User, blank=True, null=True, 
		related_name='po_overwridden_by')
	datetime = models.DateTimeField(default=datetime.now(), blank=True, null=True)
	po_que = models.CharField(max_length=30, blank=True, null=True)
	po_created_by = models.ForeignKey(User, blank=True, null=True, related_name='po_created_by')
	save_final_draft = models.NullBooleanField(blank=True, null=True)
	search_string = models.TextField(null=True, blank=True, verbose_name='Search String')

	def __unicode__(self):
		return self.po_number

	# @property
	# def status_verbose(self):
	# 	if self.po_status:
	# 		return dict(PO_STATUS)[int(self.po_status)]
	# 	else:
	# 		return "Unknown"

	def que_verbose(self):
		if self.po_que == '':
			self.po_que = '0'
		return dict(PO_QUE)[int(self.po_que)]

	def get_return_type(self):
		return dict(RETURN_TYPE)[int(self.returned_type)]

	def get_agent_fullname(self):
		if self.purchasing_agent:
			return "%s %s" % (self.purchasing_agent.first_name, self.purchasing_agent.last_name)

	class Meta:
		verbose_name = u"Purchase Order"
		verbose_name_plural = u"Purchase Orders"

		permissions = (
			('view_purchase_order', 'Can View PO'),
		)


class PurchaseItem(models.Model):
	'''
	Purchase Item will be added when PO is saved.

	Initial status for PurchaseItem is 'Ordered'.
	When item is received it will be changed to 'Partial Received'.
	If all items are received status will be changed to 'Received'
	'''
	po = models.ForeignKey(PurchaseOrder, blank=True, null=True)
	item = models.ForeignKey(Item, blank=True, null=True)
	job_number = models.ForeignKey(Job, blank=True, null=True)
	unit = models.CharField(max_length=20, blank=True, null=True)
	qty = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True, default=0.0)
	cost = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True, default=0.0)
	sub_total = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True, default=0.0)
	purchase_status = models.CharField(max_length=15, blank=True, null=True)
	comment = models.TextField(null=True, blank=True)
	search_string = models.TextField(null=True, blank=True, verbose_name='Search String')
	item_recv = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True, default=0.0)
	item_recv_date = models.DateField(blank=True, null=True)

	custom_comment = models.TextField(null=True, blank=True)
	custom_detail = models.TextField(null=True, blank=True)


	def __unicode__(self):
		return "%d -(%s)" % (self.id, str(self.po.po_number))

	def status_verbose(self):
		return dict(PT_STATUS)[int(self.purchase_status)]

	class Meta:
		verbose_name = u"Purchase Item"
		verbose_name_plural = u"Purchase Items"

		permissions = (
			('view_purchase_item', 'Can View Purchage Item'),
			('receive_purchase_item', 'Can Receive Purchage Item'),
		)

class RequestItem(models.Model):
	"""
	For each action for purchase request approved one record will be created.
	"""
	pr = models.ForeignKey(PurchaseRequest, blank=True, null=True)
	item = models.ForeignKey(Item, blank=True, null=True)
	approved_qty = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True, default=0.0)
	approved_date = models.DateField(blank=True, null=True)
	po = models.ForeignKey(PurchaseOrder, blank=True, null=True)
	total_po_qty = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True, default=0.0)
	status = models.IntegerField(max_length=2, blank=True, null=True)

	def __unicode__(self):
		return str(self.id)

	class Meta:
		verbose_name = u'Request Item'
		verbose_name_plural = u"Request Items"
		permissions = (
    		('delete_request_item', 'Delete Request Item'),
    	)



class POStatus(models.Model):
	po = models.ForeignKey(PurchaseOrder, blank=True, null=True, db_column='po_number')
	status_by = models.ForeignKey(User, blank=True, null=True, related_name='po_status_by')
	datetime = models.DateTimeField(default=datetime.now(), blank=True, null=True)
	status = models.CharField(max_length=20, blank=True, null=True, default='Canceled')
	status_comment = models.TextField(max_length=1000, blank=True, null=True)

	def __unicode__(self):
		return str(self.pk)

	def status_verbose(self):
		return dict(PO_STATUS)[int(self.status)]

class POContact(models.Model):
	purchase_order = models.ForeignKey(PurchaseOrder, blank=True, null=True)
	contact_type = models.CharField(max_length=50, blank=True, null=True)
	contact = models.CharField(max_length=100, blank=True, null=True)
	contact_name = models.CharField(max_length=100, blank=True, null=True)

	def __unicode__(self):
		return str(self.contact_name)

	class Meta:
		permissions = (
			('view_po_contact', 'Can View PO Contacts'),	
		)

class POShipToContact(models.Model):
	purchase_order = models.ForeignKey(PurchaseOrder, blank=True, null=True)
	contact_type = models.CharField(max_length=50, blank=True, null=True)
	contact = models.CharField(max_length=100, blank=True, null=True)
	contact_name = models.CharField(max_length=100, blank=True, null=True)

	def __unicode__(self):
		return str(self.contact_name)



class ReceivedItemHistory(models.Model):
	purchase_item = models.ForeignKey(PurchaseItem, blank=True, null=True)
	item_po = models.ForeignKey(PurchaseOrder, blank=True, null=True)
	qty_received = models.DecimalField(max_digits=10,decimal_places=4, blank=True, null=True, default=0.0)
	sub_total = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True, default=0.0)
	item_received_date = models.DateTimeField(blank=True, null=True)
	reveived_by = models.ForeignKey(User, blank=True, null=True, related_name='item_recv_by')
	comment = models.TextField(null=True, blank=True, verbose_name='Comment')
	search_string = models.TextField(null=True, blank=True, verbose_name='Search String')
	

	def __unicode__(self):
		return str(self.id)

	class Meta:
		verbose_name = u"Received Item History"
		verbose_name_plural = u"Received Items History"

		permissions = (
			('view_receive_item_history', 'Can View Received Item History'),
		)


class ShippingList(models.Model):
	sl_number = models.CharField(max_length=20, primary_key=True)
	sold_to = models.ForeignKey(Contact, blank=True, null=True, related_name='sl_sold_to')
	ship_to = models.ForeignKey(Contact, blank=True, null=True, related_name='sl_ship_to')
	ordered_date = models.DateField(blank=True, null=True)
	date_required = models.DateField(blank=True, null=True)
	job_number = models.ForeignKey(Job, blank=True, null=True)
	customer_po_number = models.CharField(max_length=20, blank=True, null=True)
	customer_job_number = models.CharField(max_length=20, blank=True, null=True)
	ship_via = models.ForeignKey(DeliveryChoice, blank=True, null=True, related_name='sl_ship_via')
	# items = models.ManyToManyField(PackingItem, blank=True, null=True)
	sl_status = models.CharField(max_length=2, blank=True, null=True)
	search_string = models.TextField(null=True, blank=True, verbose_name='Search String')


	def status_verbose(self):
		return dict(SL_STATUS)[int(self.sl_status)]

	class Meta:
		verbose_name = u"Shipping List"
		verbose_name_plural = u"Shipping Lists"

		permissions = (
			('view_shipping_list', 'Can View shipping list'),
		)

class ShippingItem(models.Model):
	item = models.ForeignKey(Item, related_name='shipping-item')
	description = models.TextField(null=True, blank=True)
	ordered = models.DecimalField(max_digits=10,decimal_places=4, blank=True, null=True, default=0.0)
	# shipped = models.DecimalField(max_digits=10,decimal_places=4, blank=True, null=True, default=0.0, verbose_name='Shipped today')
	shipped_total_to_date = models.DecimalField(max_digits=10,decimal_places=4, blank=True, null=True, default=0.0)
	# shipped_by = models.ForeignKey(User, blank=True, null=True, related_name='item_shipped_by')
	# last_shipped = models.DateField(blank=True, null=True)
	backordered = models.DecimalField(max_digits=10,decimal_places=4, blank=True, null=True, default=0.0)
	# filled = models.DecimalField(max_digits=10,decimal_places=4, blank=True, null=True, default=0.0)
	# price = models.DecimalField(max_digits=10,decimal_places=4, blank=True, null=True, default=0.0)
	shipping_list = models.ForeignKey(ShippingList, related_name='sl-item')
	# item_ship_status = models.CharField(max_length=10, blank=True, null=True)
	search_string = models.TextField(null=True, blank=True, verbose_name='Search String')

	def __unicode__(self):
		return str(self.id)

	# def item_ship_status_verbose(self):
	# 	return dict(SL_ITEM_STATUS)[int(self.item_ship_status)]

	class Meta:
		verbose_name = u"Shipping Item"
		verbose_name_plural = u"Shipping Items"

		permissions = (
			('view_shipping_item', 'Can View shipping item'),
		)


class SLShipToContact(models.Model):
	sl = models.ForeignKey(ShippingList, blank=True, null=True)
	contact_type = models.CharField(max_length=50, blank=True, null=True)
	contact = models.CharField(max_length=100, blank=True, null=True)
	contact_name = models.CharField(max_length=100, blank=True, null=True)

	def __unicode__(self):
		return str(self.contact_name)


class SLSoldToContact(models.Model):
	sl = models.ForeignKey(ShippingList, blank=True, null=True)
	contact_type = models.CharField(max_length=50, blank=True, null=True)
	contact = models.CharField(max_length=100, blank=True, null=True)
	contact_name = models.CharField(max_length=100, blank=True, null=True)

	def __unicode__(self):
		return str(self.contact_name)


class PackingList(models.Model):
	pl_number = models.CharField(max_length=20, primary_key=True)
	sl = models.ForeignKey(ShippingList, blank=True, null=True)
	sold_to = models.ForeignKey(Contact, blank=True, null=True, related_name='sold_to')
	ship_to = models.ForeignKey(Contact, blank=True, null=True, related_name='ship_to')
	date_issued = models.DateField(blank=True, null=True)
	date_shipped = models.DateField(blank=True, null=True)
	shipped_by = models.ForeignKey(User, blank=True, null=True, related_name='shipped_by')
	nel_packing_slip = models.BooleanField(default=False)
	job_number = models.ForeignKey(Job, blank=True, null=True)
	generated_by = models.ForeignKey(User, blank=True, null=True, related_name='generated_by')
	order_type = models.CharField(max_length=50, blank=True, null=True)
	ship_via = models.ForeignKey(DeliveryChoice, blank=True, null=True, related_name='ship_via')
	hold_at_dept_for_pickup = models.BooleanField(default=False)
	customer_broker = models.ForeignKey(Contact, blank=True, null=True, related_name='pl_customer_broker')
	customer_po_number = models.CharField(max_length=50, blank=True, null=True)
	freight_charges = models.DecimalField(max_digits=10,decimal_places=4, blank=True, null=True, default=0.0)
	status = models.CharField(max_length=20, blank=True, null=True)
	invoiced_on = models.DateField(blank=True, null=True)
	# items = models.ManyToManyField(PackingItem, blank=True, null=True)
	search_string = models.TextField(null=True, blank=True, verbose_name='Search String')

	def __unicode__(self):
		return self.pl_number

	def status_verbose(self):
		return dict(PL_STATUS)[int(self.status)]

	def order_type_verbose(self):
		return dict(PL_TYPE)[int(self.order_type)]

	class Meta:
		verbose_name = u"Packing List"
		verbose_name_plural = u"Packing Lists"

		permissions = (
			('view_packing_list', 'Can View packing list'),
		)

class PackingItem(models.Model):
	sl_item = models.ForeignKey(ShippingItem, blank=True, null=True)
	# item = models.ForeignKey(Item, blank=True, null=True)
	description = models.TextField(blank=True, null=True)
	unit = models.CharField(max_length=20, blank=True, null=True)
	qty_ordered = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True, default=0.0)
	qty_bo = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True, default=0.0)
	qty_shipped = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True, default=0.0)	
	# price = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True, default=0.0)
	status = models.BooleanField(default=0)
	pl = models.ForeignKey(PackingList, blank=True, null=True, related_name='pl_items')
	search_string = models.TextField(null=True, blank=True, verbose_name='Search String')

	def __unicode__(self):
		return str(self.id)
	

	class Meta:
		verbose_name = u"Packing Item"
		verbose_name_plural = u"Packing Items"

		permissions = (
			('view_packing_item', 'Can View Packing Item'),
		)

# PL Form
class PLSoldToContact(models.Model):
	pl = models.ForeignKey(PackingList, blank=True, null=True)
	contact_type = models.CharField(max_length=50, blank=True, null=True)
	contact = models.CharField(max_length=100, blank=True, null=True)
	contact_name = models.CharField(max_length=100, blank=True, null=True)

	def __unicode__(self):
		return str(self.contact_name)

class PLShipToContact(models.Model):
	pl = models.ForeignKey(PackingList, blank=True, null=True)
	contact_type = models.CharField(max_length=50, blank=True, null=True)
	contact = models.CharField(max_length=100, blank=True, null=True)
	contact_name = models.CharField(max_length=100, blank=True, null=True)

	def __unicode__(self):
		return str(self.contact_name)

class PLCBContact(models.Model):
	pl = models.ForeignKey(PackingList, blank=True, null=True)
	contact_type = models.CharField(max_length=50, blank=True, null=True)
	contact = models.CharField(max_length=100, blank=True, null=True)
	contact_name = models.CharField(max_length=100, blank=True, null=True)

	def __unicode__(self):
		return str(self.contact_name)

class Invoice(models.Model):
	invoice_number = models.CharField(max_length=20, primary_key=True)
	invoiced_by = models.ForeignKey(User, blank=True, null=True, related_name='invoiced_by')
	# shipping_item = models.ForeignKey(ShippingItem, blank=True, null=True)
	sold_to = models.ForeignKey(Contact, blank=True, null=True, related_name='invoice-sold-to')
	ship_to = models.ForeignKey(Contact, blank=True, null=True, related_name='invoice-ship-to')
	broker = models.ForeignKey(Contact, blank=True, null=True, verbose_name='Packing Slip', related_name='invoice_broker')
	pl = models.ForeignKey(PackingList, blank=True, null=True, related_name='packing-list')
	date = models.DateField(blank=True, null=True)
	ship_via = models.ForeignKey(DeliveryChoice, blank=True, null=True, related_name='invoice_shipping_method')
	po = models.CharField(max_length=50, blank=True, null=True)
	job =  models.ForeignKey(Job, blank=True, null=True, verbose_name='Contract/Job')
	terms = models.ForeignKey(PaymentTerm, blank=True, null=True, related_name='invoice_payment_terms')
	fob = models.CharField(max_length=200, blank=True, null=True)
	invoice_qty = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True, default=0.0)
	
	sub_total = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True, default=0.0)
	discount = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True, default=0.0)
	discount_type = models.CharField(max_length=20, blank=True, null=True)
	comment = models.TextField(blank=True, null=True)
	discounted_sub_total = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True, default=0.0)
	hst_taxable = models.CharField(max_length=2, blank=True, null=True)
	hst_taxable_amount = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True, default=0.0)
	pst_taxable = models.CharField(max_length=2, blank=True, null=True)
	pst_taxable_amount = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True, default=0.0)
	invoice_currency = models.ForeignKey(Currency, max_length=20, blank=True, null=True)
	total_amount = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True, default=0.0)
	status = models.CharField(max_length=5, blank=True, null=True)

	def __unicode__(self):
		return str(self.id)

	@property
	def status_verbose(self):
		if self.status:
			return dict(INVOICE_STATUS)[int(self.status)]
		else:
			return "Unknown"

	class Meta:
		verbose_name = u"Invoice"
		verbose_name_plural = u"Invoices"

		permissions = (
			('view_invoice', 'Can View Invoice'),
		)

class InvoicedItem(models.Model):
	invoice = models.ForeignKey(Invoice, blank=True, null=True)
	item = models.ForeignKey(PackingItem, blank=True, null=True, unique=True)
	unit = models.CharField(max_length=20, blank=True, null=True)
	qty = models.DecimalField(max_digits=10, decimal_places=4, blank=True, null=True, default=0.0)
	price = models.DecimalField(max_digits=10,decimal_places=4, blank=True, null=True, default=0.0)
	sub_total = models.DecimalField(max_digits=10,decimal_places=4, blank=True, null=True, default=0.0)

	def __unicode__(self):
		return str(self.id)

	class Meta:
		verbose_name = u"Invoice Item"
		verbose_name_plural = u"Invoice Items"

		permissions = (
			('view_invoice_item', 'Can View Invoice item'),
		)
