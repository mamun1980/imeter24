from schedule.models import *


class ScheduleJobWidget(object):
	"""docstring for Scomuser"""
	def __init__(self, usr):
		
		super(ScheduleJobWidget, self).__init__()
		self.name = 'Schedule'
		self.usr = usr
		self.template = "widget/schedule-widget.html"

	def get_total_object(self):
		email = self.usr.email
		total_job = Job.objects.filter(contact_email=email).count()
		return total_job

	def get_title(self):
		return self.name

	def get_template(self):
		return self.template

	def __unicode__(self):
		return self.name
