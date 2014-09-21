from selectable.base import LookupBase
from django.contrib.auth.models import User
from selectable.base import ModelLookup
from selectable.registry import registry

class UserLookup(ModelLookup):
    model = User
    search_fields = ('username__icontains', 'first_name__icontains', 'email__icontains', )

    def get_item_label(self, item):
		return u"%s" % (item.get_full_name())

registry.register(UserLookup)