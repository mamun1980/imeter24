from django.db import models
from report.choices import *

# Create your models here.


# class ReportType(models.Model):
# 	report_type = models.CharField(max_length=20, null=True, blank=True)
# 	is_active = models.BooleanField(verbose_name="Is Active", blank=False, default=True)

# 	def __unicode__(self):
# 		return self.report_type

# 	# def natural_key(self):
# 	# 	return self.report_type

# 	class Meta:
# 		verbose_name = "Report Type"
# 		verbose_name_plural = "Report Types"

# 		permissions = (
#     		('view_reporttype', 'Can View Report Type'),
#     	)


# class Printer(models.Model):
# 	printer_name = models.CharField(max_length=20, null=True, blank=True)
# 	is_active = models.BooleanField(verbose_name="Is Active", blank=False, default=True)

# 	def __unicode__(self):
# 		return self.printer_name

# 	# def natural_key(self):
# 	# 	return self.printer_name

# 	class Meta:
# 		verbose_name = "Printer Name"
# 		verbose_name_plural = "Printer Names"

# 		permissions = (
#     		('view_printer', 'Can View Printer'),
#     	)

class Printer(models.Model):
	printer_id = models.CharField(max_length=50, primary_key=True)
	# printer_name = models.CharField(max_length=20, null=True, blank=True)
	network_que_location = models.CharField(max_length=200, null=True, blank=True)
	printer_type = models.CharField(max_length=25, choices=PRINTER_TYPE, null=True, blank=True)
	printer_status = models.CharField(max_length=20, choices=PRINTER_STATUS, null=True, blank=True)
	

	def __unicode__(self):
		return self.printer_id

	# def natural_key(self):
	# 	nk = { 'printer_name': self.printer_id}
	# 	return (nk)

	class Meta:
		verbose_name = "Printer"
		verbose_name_plural = "Printers"

		permissions = (
    		('view_printer', 'Can View Printer'),
    	)


class Report(models.Model):
	report_type = models.CharField(max_length=50, blank=True, null=True)
	# printer = models.ForeignKey(Printer, blank=True, null=True)
	destination_type = models.CharField(max_length=20, choices=QUE_TYPE, null=True, blank=True)
	# status = models.CharField(max_length=20, choices=STATUS, null=True, blank=True)
	comments = models.TextField(blank=True, null=True)
	# start_date = models.DateField(blank=True, null=True)
	# end_date = models.DateField(blank=True, null=True)
	# rang = models.CharField(max_length=50, blank=True, null=True)
	python_script = models.CharField(max_length=200, blank=True, null=True)
	search_string = models.CharField(max_length=250, blank=True, null=True)

	def __unicode__(self):
		return self.report_type

	class Meta:
		verbose_name = "report"
		verbose_name_plural = "reports"

		permissions = (
    		('view_report', 'Can View report'),
    	)

class RecuringReport(models.Model):
	report = models.ForeignKey(Report, blank=True, null=True)
	report_description = models.TextField(blank=True, null=True)
	script_name = models.CharField(max_length=200, blank=True, null=True)

	que_type = models.CharField(max_length=20, choices=QUE_TYPE, null=True, blank=True)
	email = models.CharField(max_length=500, blank=True, null=True)
	printer = models.ForeignKey(Printer, blank=True, null=True, default=None)
	fax = models.CharField(max_length=20, blank=True, null=True)
	current_job_status = models.CharField(max_length=50, choices=JOB_STATUS, null=True, blank=True)
	date_submitted = models.DateField(blank=True, null=True)
	time_submitted = models.TimeField(blank=True, null=True)
	date_finished = models.DateField(blank=True, null=True)
	time_finished = models.TimeField(blank=True, null=True)
	# script_name = models.CharField(max_length=50, blank=True, null=True)
	unix_que = models.CharField(max_length=100, blank=True, null=True)
	comment = models.TextField(blank=True, null=True)

	schedule_type = models.CharField(max_length=15, choices=(('weekly', 'Weekly'), ('daily', 'Daily'), ('randomdays', 'Random week days')))
	week_day = models.CharField(max_length=200, blank=True, null=True)
	randomdays = models.CharField(max_length=200, blank=True, null=True)
	daytime = models.CharField(max_length=15, blank=True, null=True)
	search_string = models.CharField(max_length=250, blank=True, null=True)

	def __unicode__(self):
		return "%s - %s" % (self.report.report_type, self.que_type)

	class Meta:
		verbose_name = "recuring report"
		verbose_name_plural = "recuring reports"

		permissions = (
    		('view_recuringreport', 'Can View recuring report'),
    	)


class SingleReport(models.Model):
	report = models.ForeignKey(Report, blank=True, null=True)
	report_description = models.TextField(blank=True, null=True)
	script_name = models.CharField(max_length=200, blank=True, null=True)

	que_type = models.CharField(max_length=20, choices=QUE_TYPE, null=True, blank=True)
	email = models.CharField(max_length=500, blank=True, null=True)
	printer = models.ForeignKey(Printer, blank=True, null=True)
	fax = models.CharField(max_length=20, blank=True, null=True)
	current_job_status = models.CharField(max_length=50, choices=JOB_STATUS, null=True, blank=True)
	date_submitted = models.DateField(blank=True, null=True)
	time_submitted = models.TimeField(blank=True, null=True)
	date_finished = models.DateField(blank=True, null=True)
	time_finished = models.TimeField(blank=True, null=True)
	search_start_date = models.DateField(blank=True, null=True)
	search_end_date = models.DateField(blank=True, null=True)
	search_string = models.CharField(max_length=250, blank=True, null=True)
	search_status_type = models.CharField(max_length=50, null=True, blank=True)

	def __unicode__(self):
		return "%s - %s" % (self.report.report_type, self.que_type)

	class Meta:
		verbose_name = "single report"
		verbose_name_plural = "single reports"

		permissions = (
    		('view_singlereport', 'Can View single report'),
    	)











