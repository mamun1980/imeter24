from scomuser.models import ScomUserProfile
from selectable.base import ModelLookup
from selectable.registry import registry

class UserLookup(ModelLookup):
	model = ScomUserProfile
	search_fields = ('user__username__icontains', 'cell_phone__icontains', 'address_1__icontains', 'city__icontains', 'home_phone__icontains')

	def get_item_value(self, item):
		# Display for currently selected item
		return item.pk

	def get_item_label(self, item):
		# Display for choice listings
		return u"%s - ( %s - %s )" % (item.user.username, item.address_1, item.city)


registry.register(UserLookup)