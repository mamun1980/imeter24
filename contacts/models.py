from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from datetime import datetime
from contacts.choices import *

# Create your models here.

class DistributionMethod(models.Model):
	distribution_method = models.CharField(max_length=100, verbose_name='Distribution Method', null=True, blank=True)
	is_active = models.BooleanField(verbose_name="Is Active", blank=False, default=True)

	def __unicode__(self):
		return self.distribution_method

	class Meta:
		verbose_name = "Delivery Choice"
		verbose_name_plural = "Delivery Choice"

		permissions = (
    		('view_distributionmethod', 'Can View Distribution Method'),
    	)

class DeliveryChoice(models.Model):
	delivery_choice = models.CharField(max_length=100, verbose_name='Shipping Method', help_text='', null=True, blank=True)
	is_active = models.BooleanField(verbose_name="Is Active", blank=False, default=True)

	def __unicode__(self):
		return self.delivery_choice

	class Meta:
		verbose_name = "Delivery Choice"
		verbose_name_plural = "Delivery Choice"

		permissions = (
    		('view_deliverychoice', 'Can View Delivery Choice'),
    	)


class PaymentTerm(models.Model):
	term = models.CharField(max_length=25, verbose_name='Payment Terms', null=True, blank=True)
	is_active = models.BooleanField(verbose_name="Is Active", blank=False, default=True)

	def __unicode__(self):
		return self.term

	class Meta:
		verbose_name = "Payment Term"
		verbose_name_plural = "Payment Term"

		permissions = (
    		('view_paymentterm', 'Can View Payment Term'),
    	)

		
class Currency(models.Model):
	currency = models.CharField(max_length=10, verbose_name="Currency", null=True, blank=True)
	currency_icon = models.CharField(max_length=2, null=True, blank=True)

	def __unicode__(self):
		return self.currency

	def get_currency_icon(self):
		if self.currency_icon:
			return dict(currency_choices)[int(self.currency_icon)]
		else:
			return dict(currency_choices)[0]


	class Meta:
		verbose_name = "Currency"
		verbose_name_plural = "Currency"

		permissions = (
    		('view_currency', 'Can View Currency'),
    	)

class Contact(models.Model):	
	contact_name 	  = models.CharField(max_length=64, verbose_name='Contact Name', null=True, blank=True)
	attention_to      = models.CharField(max_length=64, verbose_name='Attention To', null=True, blank=True)
	
	address_1         = models.CharField(max_length=64, verbose_name='Address Line 1', null=True, blank=True)
	address_2         = models.CharField(max_length=64, verbose_name='Address Line 2', null=True, blank=True)
	city              = models.CharField(max_length=64, verbose_name='city', null=True, blank=True)
	province          = models.CharField(max_length=64, verbose_name='Province or State', null=False, blank=True, default="Ontario")
	country           = models.CharField(max_length=40, verbose_name='Country', null=True, blank=False, default="Canada")
	postal_code       = models.CharField(max_length=15, verbose_name='Postal Code or ZIP', null=True, blank=True)
	webpage           = models.URLField(max_length=200, null=True, blank=True)
	search_string 	  = models.TextField(null=True, blank=True, verbose_name='Search String')

	class Meta:
		verbose_name = "Contact"
		verbose_name_plural = "Contacts"

		permissions = (
    		('view_contact', 'Can View Contact'),
    	)

	def __unicode__(self):
		return self.contact_name

def create_contact_profile(sender, instance, created, **kwargs):
	if created:
		ContactProfile.objects.create(contact=instance)

post_save.connect(create_contact_profile, sender=Contact)

class ContactProfile(models.Model):	
	contact           = models.OneToOneField(Contact,  null=False, on_delete=models.CASCADE)
	gst_number        = models.CharField(max_length=17, verbose_name='GST number', null=True, blank=True)
	gst_tax_exempt    = models.BooleanField(verbose_name='GST Tax Exempt?', blank=False, default=False)
	hst_number        = models.CharField(max_length=17, verbose_name='HST number', null=True, blank=True)
	hst_tax_exempt    = models.BooleanField(verbose_name='HST Tax Exempt?', blank=False, default=False)
	pst_number        = models.CharField(max_length=11, verbose_name='PST number', null=True, blank=True)
	pst_tax_exempt    = models.BooleanField(verbose_name='PST Tax Exempt?', blank=False, default=False)
	foreign_account   = models.CharField(max_length=30, verbose_name='Our Account # With Them', null=True, blank=True)
	mail_list         = models.CharField(max_length=15, verbose_name='Mailing List Type', null=True, blank=True)
	
	terms             = models.ForeignKey(PaymentTerm, null=True, blank=True)
	
	shipping_method   = models.ForeignKey(DeliveryChoice, null=True, blank=True)
	
	ship_collect      = models.BooleanField(verbose_name="Ship Collect?", blank=False, default=False)
	currency          = models.ForeignKey(Currency, null=True, blank=True)
	fob               = models.CharField(max_length=50, verbose_name='FOB', default='Oshawa, Ontario, Canada', null=True, blank=True)
	ap_contact        = models.TextField(null=True, blank=True, verbose_name='AP contact info', help_text='Enter Accounts Payable contact name, number and e-mail.')
	bv_ap_account 	  = models.CharField(max_length=50, verbose_name='BV A/P Account ', null=True, blank=True)
	bv_ar_account 	  = models.CharField(max_length=50, verbose_name='BV A/R Account ', null=True, blank=True)
	record_created    = models.DateTimeField(null=True, blank=True)
	last_activity     = models.DateTimeField(auto_now=True, blank=True)

	class Meta:
		verbose_name = "ContactProfile"
		verbose_name_plural = "ContactProfiles"

		permissions = (
    		('view_contactprofile', 'Can View Contact Profile'),
    	)

	def __unicode__(self):
		return self.contact.contact_name + "'s profile"

class PhoneType(models.Model):
	phone_type = models.CharField(max_length=15, verbose_name='Phone Type', null=True, blank=True)

	def __unicode__(self):
		return self.phone_type

	class Meta:
		verbose_name = "Phone Type"
		verbose_name_plural = "Phone Types"

class ContactPhone(models.Model):
	contact 		= models.ForeignKey(Contact, null=True, blank=True)
	phone_type      = models.ForeignKey(PhoneType, null=True, blank=True)
	phone           = models.CharField(max_length=15, verbose_name='Phone Number', null=True, blank=True)
	phone_ext       = models.CharField(max_length=10, verbose_name='Phone Extension', null=True, blank=True)

	def __unicode__(self):
		return self.phone

	class Meta:
		verbose_name = "Contact phone"
		verbose_name_plural = "Contact phones"

		permissions = (
    		('view_contactphone', 'Can View Contact Phone'),
    	)


class ContactType(models.Model):
	contact_type = models.CharField(max_length=15, verbose_name='Contact Type', null=True, blank=True)
	is_active = models.BooleanField(verbose_name="Is Active", blank=False, default=True)

	def __unicode__(self):
		return self.contact_type

	class Meta:
		verbose_name = "Contact Type"
		verbose_name_plural = "Contact Types"

class ContactContactType(models.Model):
	contact 		= models.ForeignKey(Contact, null=False)
	contact_type      = models.ForeignKey(ContactType, null=True, blank=True)
	description 		= models.TextField(null=True, blank=True)

	def __unicode__(self):
		return self.contact + " / " + self.contact_type

	class Meta:
		verbose_name = "Contact Contact Type"
		verbose_name_plural = "Contact Contact Types"

		permissions = (
    		('view_contactcontacttype', 'Can View Contact Contact Type'),
    	)


class EmailAddressType(models.Model):
	email_type = models.CharField(max_length=15, verbose_name='Email Address Type', null=True, blank=False)
	is_active = models.BooleanField(verbose_name="Is Active", blank=False, default=True)

	def __unicode__(self):
		return self.email_type

	class Meta:
		verbose_name = "Email Address Type"
		verbose_name_plural = "Email Address Types"

		permissions = (
    		('view_emailaddresstype', 'Can View Email Address Type'),
    	)


class ContactEmailAddress(models.Model):
	contact 			= models.ForeignKey(Contact,  null=True, blank=True)
	email_address_type 	= models.ForeignKey(EmailAddressType,  null=False)
	email_address 		= models.EmailField(max_length=100)

	def __unicode__(self):
		return self.email_address

	class Meta:
		verbose_name = "Email Address"
		verbose_name_plural = "Email Addresses"

		permissions = (
    		('view_contactemailaddress', 'Can View Contact Email Address'),
    	)


class ContactDistributionMethod(models.Model):
	distribution_method = models.ForeignKey(DistributionMethod,  null=False)
	contact 			= models.ForeignKey(Contact,  null=False)
	description 		= models.TextField(null=True, blank=True)

	def __unicode__(self):
		return self.contact.contact_name + " " + self.distribution_method.distribution_method

	class Meta:
		verbose_name = "Contact Distribution Method"
		verbose_name_plural = "Contact Distribution Methods"

		permissions = (
    		('view_contactdistributionmethod', 'Can View Contact Distribution Method'),
    	)


class Comment(models.Model):
	contact = models.ForeignKey(Contact,  null=False)
	staff = models.ForeignKey(User, null=True)
	comment = models.TextField(null=True, blank=True, verbose_name='Comments')
	comment_date = models.DateTimeField(auto_now=True)


	def __unicode__(self):
		return self.comment

	class Meta:
		verbose_name = "Comment"
		verbose_name_plural = "Comments"

		permissions = (
    		('view_comment', 'Can View Comments'),
    	)
