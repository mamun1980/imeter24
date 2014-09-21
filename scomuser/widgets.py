from django.contrib.auth.models import User

class UserWidget(object):
	"""docstring for Scomuser"""
	def __init__(self):
		
		super(UserWidget, self).__init__()
		self.name = 'Scome Staff'
		self.template = "widget/user-widget.html"

	def get_total_object(self):
		total_user = User.objects.count()
		return total_user

	def get_title(self):
		return self.name

	def get_template(self):
		return self.template

	def get_url(self):
		return "/scomuser/"

	def __unicode__(self):
		return self.name
