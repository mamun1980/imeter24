from schedule.models import Job
from selectable.base import ModelLookup
from selectable.registry import registry

class JobLookup(ModelLookup):
	model = Job
	search_fields = ('job_number__icontains', "cab_designation__icontains", "customer__icontains", 'address1__icontains', )

	def get_item_value(self, item):
		# Display for currently selected item
		return item.id

	def get_item_label(self, item):
		# Display for choice listings
		return u"job-number=%s status=%s (%s) " % (item.job_number, item.status, item.cab_designation)


registry.register(JobLookup)