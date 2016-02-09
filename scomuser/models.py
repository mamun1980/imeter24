from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from scomuser.choices import *
import decimal
from django.utils import timezone
from report.models import *


class ScomUserProfile(models.Model):
	user 			= models.OneToOneField(User)
	address_1 		= models.CharField(verbose_name='Address Line 1', max_length=40, null=True, blank=True)
	address_2 		= models.CharField(verbose_name='Address Line 2', max_length=40, null=True, blank=True)
	address_3 		= models.CharField(verbose_name='Address Line 3', max_length=40, null=True, blank=True)
	city 			= models.CharField(verbose_name='City', max_length=40, null=True, blank=True)
	province 		= models.CharField(verbose_name='Province', max_length=30, null=True, blank=True)
	postal 			= models.CharField(verbose_name='Postal Code', max_length=10, null=True, blank=True)
	home_phone 		= models.CharField(verbose_name='Home Phone Number', max_length=15, null=True, blank=True)
	cell_phone 		= models.CharField(verbose_name='Cell Phone Number', max_length=15, null=True, blank=True)
	other_phone 	= models.CharField(verbose_name='Other Phone Number', max_length=15, null=True, blank=True)
	internal_extension = models.CharField(verbose_name='Internal Extension', max_length=15, null=True, blank=True)
	em_contact_1 	= models.TextField(verbose_name='Primary Emergency Contact', max_length=128, null=True, blank=True)
	em_contact_2 	= models.TextField(verbose_name='Secondary Emergency Contact', max_length=128, null=True, blank=True)
	max_amount_allowed_to_purchase = models.CharField(max_length=20, null=True, blank=True)
	max_purchase_per_po = models.CharField(max_length=20, null=True, blank=True)
	avatar 			= models.ImageField(upload_to="avatar", blank=True, null=True, verbose_name="Avatar")
	search_string = models.TextField(blank=True, null=True)

	def __unicode__(self):
		return self.user.username


class Department(models.Model):
	name = models.CharField(max_length=20, blank=True, null=True)
	is_active = models.BooleanField(verbose_name='Is Active', blank=False, default=True)
	

	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name = "Department"
		verbose_name_plural = "Departments"

		permissions = (
    		('view_department', 'Can View Department'),
    	)

class UserReport(models.Model):
	user = models.ForeignKey(User, blank=True, null=True)
	report_type = models.CharField(max_length=50, choices=(('email', 'Email'), ('fax', 'Fax'), ('print', 'Print'), ('pdf', 'PDF')))
	report_printer = models.ForeignKey(Printer, blank=True, null=True)
	report_fax = models.CharField(max_length=50, blank=True, null=True)
	report_email = models.CharField(max_length=100, blank=True, null=True)

	def __unicode__(self):
		return self.report_type
	
		




class PayType(models.Model):
	pay_type = models.CharField(max_length=20, blank=True, null=True)
	is_active = models.BooleanField(verbose_name='Is Active', blank=False, default=True)

	def __unicode__(self):
		return self.pay_type

	class Meta:
		verbose_name = "Pay Type"
		verbose_name_plural = "Pay Types"

		permissions = (
    		('view_paytype', 'Can View Pay Type'),
    	)

class Payroll(models.Model):
	user 			= models.OneToOneField(User, blank=True, null=True)
	sin   			= models.CharField(verbose_name='Employee Sin', max_length=10, null=True, blank=True)
	inital 			= models.CharField(verbose_name='Initals', max_length=3, null=True, blank=True)
	department 		= models.ForeignKey(Department, blank=True, null=True)
	rate_of_pay 	= models.DecimalField(verbose_name='Rate of Pay', max_digits=10, decimal_places=2, default=decimal.Decimal('0.00'))
	rate_of_pay_type= models.ForeignKey(PayType, null=True, blank=True)

	def __unicode__(self):
		return self.sin

	class Meta:
		verbose_name = "Payroll"
		verbose_name_plural = "Payrolls"

		permissions = (
    		('view_payroll', 'Can View payroll'),
    	)

mail_status = (
	('pending', 'Pending'),
	('delivered', 'Delivered'),
	('failed', 'Failed'),
)

class MassMail(models.Model):
	email_id = models.CharField(max_length=20, null=True, blank=True) 
	subject = models.CharField(max_length=200, null=True, blank=True)
	body = models.TextField(blank=True, null=True)
	sender = models.EmailField(max_length=100, null=True, blank=True)
	to_all_users = models.BooleanField(default=True)
	reciever = models.EmailField(max_length=100, null=True, blank=True)
	mail_status = models.CharField(verbose_name='Mail Status', max_length=10, choices=mail_status)
	request_datetime = models.DateTimeField(default=timezone.now)
	delivered_datetime = models.DateTimeField(blank=True, null=True)
	search_string = models.TextField(blank=True, null=True)


	def __unicode__(self):
		return self.email_id

	class Meta:
		verbose_name = "MassMail"
		verbose_name_plural = "MassMails"

		permissions = (
    		('view_massmail', 'Can View MassMail'),
    		('send_massmail', 'Can Send MassMail'),
    	)










