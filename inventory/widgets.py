from inventory.models import *



class InventoryWidget(object):
	"""docstring for Scomuser"""
	def __init__(self):
		
		super(InventoryWidget, self).__init__()
		self.name = 'Inventory'
		self.template = "widget/inventory-widget.html"

	def get_total_object(self):
		pass

	def get_title(self):
		return self.name

	def get_template(self):
		return self.template

	def get_total_customer(self):
		pass

	def get_total_supplier(self):
		pass

	def get_url(self):
		return "/inventory/"

	def __unicode__(self):
		return self.name
