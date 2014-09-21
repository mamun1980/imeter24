from contacts.models import *
from selectable.base import LookupBase
from django.contrib.auth.models import User
from selectable.base import ModelLookup
from selectable.registry import registry
from selectable.decorators import login_required


class PhoneLookup(ModelLookup):
	model = ContactPhone
	search_fields = ('contact_profile__contact_name__icontains', 'phone__icontains', )

	def get_item_label(self, item):
		return u"%s (%s)" % (item.contact_profile.contact.username, item.phone)

class ContactsLookup(ModelLookup):
	model = Contact
	search_fields = ('contact_name__icontains', 'attention_to__icontains', 'city__icontains', )

	def get_item_label(self, item):
		return u"%s (%s)" % (item.contact_name, item.city)

registry.register(ContactsLookup)
registry.register(PhoneLookup)
