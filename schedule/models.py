from django.db import models
from schedule.choices import *
from datetime import datetime
from contacts.models import Contact
from django.contrib.auth.models import User
# Create your models here.


class Job(models.Model):
	job_number = models.CharField(max_length=20, primary_key=True)
	cab_designation = models.CharField(max_length=50, blank=True, null=True)
	date_opened = models.DateField(null=True, blank=True)
	date_required = models.DateField(null=True, blank=True)
	status = models.CharField(max_length=50, choices=STATUS_CHOICE, default=0)
	job_name = models.CharField(max_length=150, null=True, blank=True)
	address_1 = models.TextField(max_length=500, blank=True, null=True)
	customer = models.CharField(max_length=100, null=True, blank=True)
	customer_contact_name = models.CharField(max_length=100, null=True, blank=True)
	customer_contact_phone_number = models.CharField(max_length=100, null=True, blank=True)
	contact_email = models.CharField(max_length=500, null=True, blank=True)
	number_of_cabs = models.IntegerField(null=True, blank=True)
	description = models.TextField(max_length=200, null=True, blank=True)
	po_number = models.CharField(max_length=40, null=True, blank=True)
	status_notes = models.TextField(max_length=500, null=True, blank=True)
	drawing_req_date = models.DateField(null=True, blank=True)
	drawing_sent_to_customer_date = models.DateField(null=True, blank=True)
	drawing_approved_date = models.DateField(null=True, blank=True)
	eng_comment = models.TextField(max_length=200, blank=True, null=True)
	search_string = models.TextField(max_length=1000, blank=True, null=True)

	def __unicode__(self):
		return unicode(self.job_number)

	class Meta:
		verbose_name = "Job"
		verbose_name_plural = "Jobs"

		permissions = (
    		('view_job', 'Can View Job'),
    		('view_customer_job', 'Can View Customer Job'),
    	)

class Comment(models.Model):
	job_number = models.CharField(max_length=20, blank=True, null=True)
	job_comment = models.TextField(max_length=500, blank=True, null=True)
	comment_by = models.CharField(max_length=100, blank=True, null=True)
	datetime = models.DateTimeField(default=datetime.now, blank=True, null=True)

	def __unicode__(self):
		return "comments for %s" % self.job_number

	class Meta:
		verbose_name = "Comment"
		verbose_name_plural = "Comments"

		permissions = (
    		('view_comment', 'Can View Comment'),
    	)



class JobStatus(models.Model):
	job = models.OneToOneField(Job)
	fixtures_req_by = models.CharField(max_length=20, null=True, blank=True)
	fixtures_is_done = models.CharField(max_length=20, choices=DONE_CHOICES, default='none', null=True, blank=True)
	fixtures_comment = models.TextField(max_length=200, blank=True, null=True)

	wood_shop_req_by = models.CharField(max_length=20, null=True, blank=True)
	wood_shop_is_done = models.CharField(max_length=20, choices=DONE_CHOICES, default='none', null=True, blank=True)
	wood_shop_req_by_comment = models.TextField(max_length=200, blank=True, null=True)
	
	machine_shop_req_by = models.CharField(max_length=20, null=True, blank=True)
	machine_shop_is_done = models.CharField(max_length=20, choices=DONE_CHOICES, default='none', null=True, blank=True)
	machine_shop_req_by_comment = models.TextField(max_length=200, blank=True, null=True)

	welding = models.CharField(max_length=20, null=True, blank=True)
	welding_is_done = models.CharField(max_length=20, choices=DONE_CHOICES, default='none', null=True, blank=True)
	welding_comment = models.TextField(max_length=200, blank=True, null=True)
	
	lacquer = models.CharField(max_length=20, null=True, blank=True)
	lacquer_is_done = models.CharField(max_length=20, choices=DONE_CHOICES, default='none', null=True, blank=True)
	lacquer_comment = models.TextField(max_length=200, blank=True, null=True)
	

	trim_shop_req_by = models.CharField(max_length=20, null=True, blank=True)
	trim_shop_is_done = models.CharField(max_length=20, choices=DONE_CHOICES, default='none', null=True, blank=True)
	trim_shop_req_by_comment = models.TextField(max_length=200, blank=True, null=True)
	
	cab_assemply_req_by = models.CharField(max_length=20, null=True, blank=True)
	cab_assemply_is_done = models.CharField(max_length=20, choices=DONE_CHOICES, default='none', null=True, blank=True)
	cab_assemply_req_by_comment = models.TextField(max_length=200, blank=True, null=True)
	
	install_date = models.CharField(max_length=20, null=True, blank=True)
	install_is_done = models.CharField(max_length=20, choices=DONE_CHOICES, default='none', null=True, blank=True)
	install_date_comment = models.TextField(max_length=200, blank=True, null=True)
	
	premier_glass = models.CharField(max_length=20, null=True, blank=True)
	premier_glass_is_done = models.CharField(max_length=20, choices=DONE_CHOICES, default='none', null=True, blank=True)
	premier_glass_comment = models.TextField(max_length=200, blank=True, null=True)
	
	tile_installer = models.CharField(max_length=20, null=True, blank=True)
	tile_installer_is_done = models.CharField(max_length=20, choices=DONE_CHOICES, default='none', null=True, blank=True)
	tile_installer_comment = models.TextField(max_length=200, blank=True, null=True)
	
	misc_del = models.CharField(max_length=20, null=True, blank=True)
	misc_del_is_done = models.CharField(max_length=20, choices=DONE_CHOICES, default='none', null=True, blank=True)
	misc_del_comment = models.TextField(max_length=200, blank=True, null=True)
	
	bill = models.CharField(max_length=20, null=True, blank=True)
	bill_is_done = models.CharField(max_length=20, choices=DONE_CHOICES, default='none', null=True, blank=True)
	bill_comment = models.TextField(max_length=200, blank=True, null=True)
	
	hayward = models.CharField(max_length=20, null=True, blank=True)
	hayward_is_done = models.CharField(max_length=20, choices=DONE_CHOICES, default='none', null=True, blank=True)
	hayward_comment = models.TextField(max_length=200, blank=True, null=True)
	
	glenn = models.CharField(max_length=20, null=True, blank=True)
	glenn_is_done = models.CharField(max_length=20, choices=DONE_CHOICES, default='none', null=True, blank=True)
	glenn_comment = models.TextField(max_length=200, blank=True, null=True)
	
	suren = models.CharField(max_length=20, null=True, blank=True)
	suren_is_done = models.CharField(max_length=20, choices=DONE_CHOICES, default='none', null=True, blank=True)
	suren_comment = models.TextField(max_length=200, blank=True, null=True)
	
	roger = models.CharField(max_length=20, null=True, blank=True)
	roger_is_done = models.CharField(max_length=20, choices=DONE_CHOICES, default='none', null=True, blank=True)
	roger_comment = models.TextField(max_length=200, blank=True, null=True)
	
	matt = models.CharField(max_length=20, null=True, blank=True)
	matt_is_done = models.CharField(max_length=20, choices=DONE_CHOICES, default='none', null=True, blank=True)
	matt_comment = models.TextField(max_length=200, blank=True, null=True)
	

	third_party_install = models.CharField(max_length=20, null=True, blank=True)
	third_party_install_is_done = models.CharField(max_length=20, choices=DONE_CHOICES, default='none', null=True, blank=True)
	third_party_install_comment = models.TextField(max_length=200, blank=True, null=True)

	tssa_submitted_date = models.CharField(max_length=20, null=True, blank=True)
	tssa_submitted_date_is_done = models.CharField(max_length=20, choices=DONE_CHOICES, default='none', null=True, blank=True)
	tssa_submitted_date_comment = models.TextField(max_length=200, blank=True, null=True)

	safety_test_schedule_date = models.CharField(max_length=20, null=True, blank=True)
	who_will_test = models.CharField(max_length=200, null=True, blank=True)
	test_comment = models.TextField(max_length=200, blank=True, null=True)
	
	

	def __unicode__(self):
		return unicode(self.job.id) + ' status'

	class Meta:
		verbose_name = "Job Status"
		verbose_name_plural = "Job Statuses"

		permissions = (
    		('view_jobstatus', 'Can View Job Status'),
    	)

class ElevetorType(models.Model):
	elevetor_type = models.CharField(max_length=50, null=True, blank=True)
	description = models.TextField(max_length=200, blank=True, null=True)

	def __unicode__(self):
		return self.id

	class Meta:
		verbose_name = "Elevetor type"
		verbose_name_plural = "Elevetor types"

		permissions = (
			('view_elevetor_type', 'Can view elevetor type'),
		)



class JobControl(models.Model):
	job_number = models.CharField(max_length=20, primary_key=True)
	# next_job_number = models.CharField(max_length=20, null=True, blank=True)
	sold_to = models.ForeignKey(Contact, null=True, blank=True, related_name='job-control-sold_to')
	ship_to = models.ForeignKey(Contact, null=True, blank=True, related_name='job-control-ship_to')
	elevetor_type = models.ForeignKey(ElevetorType, null=True, blank=True, related_name='job-con-elevetor-type')
	number_of_floors = models.IntegerField(null=True, blank=True)
	front = models.CharField(max_length=20, null=True, blank=True)
	rear = models.CharField(max_length=20, null=True, blank=True)
	rgw = models.CharField(max_length=20, null=True, blank=True)
	capacity = models.IntegerField(null=True, blank=True)
	customer_po_number = models.CharField(max_length=30, null=True, blank=True)
	delivery_date = models.DateField(blank=True, null=True)
	start_date = models.DateField(blank=True, null=True)
	installed_by = models.ForeignKey(Contact, null=True, blank=True)
	job_name = models.CharField(max_length=20, null=True, blank=True)
	estimated_price_for_job = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True)
	search_string = models.TextField(max_length=1000, blank=True, null=True)

	def __unicode__(self):
		return self.id

	class Meta:
		verbose_name = "Job control"
		verbose_name_plural = "Job controls"

		permissions = (
			('view_job_control', 'Can view job control'),
		)








