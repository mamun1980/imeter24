from django.db import models
from contacts.models import Contact

# Create your models here.

class Controller(models.Model):
	controller_id = models.CharField(max_length=20, primary_key=True)
	sold_to = models.ForeignKey(Contact, blank=True, null=True, related_name='controller_sold_to')
	location = models.CharField(max_length=200, blank=True, null=True)
	controller_type = models.CharField(max_length=100, blank=True, null=True)
	
	class Meta:
		verbose_name = u"Controller"
		verbose_name_plural = u"Controllers"

	def __unicode__(self):
		return self.controller_id


class ControllerContact(models.Model):
	controller = models.ForeignKey(Controller, null=True)
	contact_id = models.PositiveIntegerField(default=0)
	description = models.TextField(null=True, blank=True, verbose_name='Description')
	status = models.CharField(max_length=10, blank=True, null=True)

	def __unicode__(self):
		return self.contact_id
