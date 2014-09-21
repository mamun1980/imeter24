from events.models import *



class EventWidget(object):
	"""docstring for Scomuser"""
	def __init__(self):
		
		super(EventWidget, self).__init__()
		self.name = 'Events'
		self.template = "widget/event-widget.html"

	def get_total_object(self):
		pass

	def get_title(self):
		return self.name

	def get_template(self):
		return self.template


	def get_url(self):
		return "/events/"

	def __unicode__(self):
		return self.name
