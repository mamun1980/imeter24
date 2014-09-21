from report.models import Report
from selectable.base import ModelLookup
from selectable.registry import registry

class ReportLookup(ModelLookup):
	model = Report
	search_fields = ("search_string__icontains",)

	def get_item_value(self, item):
		# Display for currently selected item
		return item.pk

	def get_item_label(self, item):
		# Display for choice listings
		return u"%s (%s) " % (item.search_string, item.pk)


registry.register(ReportLookup)