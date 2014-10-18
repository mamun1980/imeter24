from django.db import models
from report.models import Printer, Report


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
		return self.id

	class Meta:
		verbose_name = "System variable"
		verbose_name_plural = "System variables"

		permissions = (
    		('view_system_variable', 'Can View System Variable'),
    	)
