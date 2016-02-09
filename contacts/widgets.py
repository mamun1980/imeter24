from contacts.models import *



class ContactWidget(object):
	"""docstring for Scomuser"""
	def __init__(self):
		
		super(ContactWidget, self).__init__()
		self.name = 'Contacts'
		self.template = "widget/contact-widget.html"

	def get_total_object(self):
		total_user = ContactProfile.objects.count()
		return total_user

	def get_title(self):
		return self.name

	def get_template(self):
		return self.template

	def get_total_customer(self):
		total_customer = ContactProfile.objects.filter(is_customer=True).count()
		return total_customer

	def get_total_supplier(self):
		total_supplier = ContactProfile.objects.filter(is_supplier=True).count()
		return total_supplier

	def get_url(self):
		return "/contacts/"

	def __unicode__(self):
		return self.name

class PhoneWidget(object):
	"""docstring for Scomuser"""
	def __init__(self):
		
		super(PhoneWidget, self).__init__()
		self.name = 'Contacts Phone'
		self.template = "widget/contact-phone-widget.html"

	def get_total_object(self):
		total_user = ContactProfile.objects.count()
		return total_user

	def get_title(self):
		return self.name

	def get_template(self):
		return self.template

	def get_total_customer(self):
		total_customer = ContactProfile.objects.filter(is_customer=True).count()
		return total_customer

	def get_total_supplier(self):
		total_supplier = ContactProfile.objects.filter(is_supplier=True).count()
		return total_supplier

	def get_url(self):
		return "/contacts/"

	def __unicode__(self):
		return self.name
