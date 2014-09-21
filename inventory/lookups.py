from contacts.models import Contact
from selectable.base import ModelLookup
from selectable.registry import registry

class ContactLookup(ModelLookup):
	model = Contact
	search_fields = ('contact_name__icontains', 'attention_to__icontains', 'address_1__icontains', 'city__icontains')

	def get_item_value(self, item):
		# Display for currently selected item
		return item.pk

	def get_item_label(self, item):
		# Display for choice listings
		return u"%s - %s - %s - %s" % (item.contact_name, item.attention_to, item.address_1, item.city)


registry.register(ContactLookup)