from django.db import models
from report.models import Printer, Report
from purchase.models import *
from inventory.models import *



class SystemVariable(models.Model):
	next_job_number = models.IntegerField(null=True, blank=False)
	next_item_number = models.IntegerField(null=True, blank=False)
	next_po_number = models.IntegerField(null=True, blank=False)
	next_sl_number = models.IntegerField(null=True, blank=False)
	next_pl_number = models.IntegerField(null=True, blank=False)
	next_invoice_number = models.IntegerField(null=True, blank=False)
	email_server_host_name = models.CharField(max_length=20, null=False, blank=False)
	email_server_ip_address = models.IntegerField(null=True, blank=False)
	email_auth_username = models.CharField(max_length=20, null=True, blank=False)
	email_auth_password = models.CharField(max_length=20, null=True, blank=False)
	default_printer_for_po = models.ForeignKey(Printer,null=True, blank=True, related_name="default_printer_for_po")
	default_printer_for_sl = models.ForeignKey(Printer,null=True, blank=True, related_name="default_printer_for_sl")
	default_printer_for_pl = models.ForeignKey(Printer,null=True, blank=True, related_name="default_printer_for_pl")
	default_printer_for_invoice = models.ForeignKey(Printer,null=True, blank=True, related_name="default_printer_for_invoice")
	default_printer_for_user = models.ForeignKey(Printer,null=True, blank=True, related_name="default_printer_for_user")

	default_report_for_po = models.ForeignKey(Report,null=True, blank=True, related_name="default_report_for_po")
	default_report_for_sl = models.ForeignKey(Report,null=True, blank=True, related_name="default_report_for_sl")
	default_report_for_pl = models.ForeignKey(Report,null=True, blank=True, related_name="default_report_for_pl")
	default_report_for_invoice = models.ForeignKey(Report,null=True, blank=True, related_name="default_report_for_invoice")

	def __unicode__(self):
		return str(self.id)

	@property
	def get_next_invoice_number(self):
		got_value = False
		if self.next_invoice_number:
			while not got_value:
				try:
					next_invoice_number = 'INV'+str(self.next_invoice_number)
					po = Invoice.objects.get(invoice_number=next_invoice_number)
				except Invoice.DoesNotExist:
					got_value = True
					next_invoice_number = 'INV' + str(self.next_invoice_number)

				self.next_invoice_number = self.next_invoice_number + 1
				self.save()
			return next_invoice_number
		else:
			return self.next_invoice_number

	@property
	def get_next_po_number(self):
		got_value = False
		if self.next_po_number:
			while not got_value:
				try:
					next_po_number = 'PO'+str(self.next_po_number)
					po = PurchaseOrder.objects.get(po_number=next_po_number)
				except PurchaseOrder.DoesNotExist:
					got_value = True
					next_po_number = 'PO' + str(self.next_po_number)

				self.next_po_number = self.next_po_number + 1
				self.save()
			return next_po_number
		else:
			return self.next_po_number

	@property
	def get_next_item_number(self):
		got_value = False
		while not got_value:
			try:
				next_item_number = 'MAT'+str(self.next_item_number)
				po = Item.objects.get(item_number=next_item_number)
			except Item.DoesNotExist:
				got_value = True
				next_item_number = 'MAT' + str(self.next_item_number)

			self.next_item_number = self.next_item_number + 1
			self.save()

		
		return next_item_number

	@property
	def get_next_sl_number(self):
		got_value = False
		while not got_value:
			try:
				next_sl_number = 'SL'+str(self.next_sl_number)
				sl = ShippingList.objects.get(sl_number=next_sl_number)
			except ShippingList.DoesNotExist:
				got_value = True
				next_sl_number = 'SL' + str(self.next_sl_number)

			self.next_sl_number = self.next_sl_number + 1
			self.save()

		
		return next_sl_number
			

	class Meta:
		verbose_name = "System variable"
		verbose_name_plural = "System variables"

		permissions = (
    		('view_system_variable', 'Can View System Variable'),
    	)
