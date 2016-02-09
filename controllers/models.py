from django.db import models

# Create your models here.

class Controller(models.Model):
	oid					= models.AutoField(primary_key=True)
	controllerid 		= models.CharField(verbose_name="Controller ID",max_length=3,null=True, blank=True)
	relayid				= models.IntegerField(verbose_name="Relay ID",max_length=2,null=True, blank=True)
	status				= models.BooleanField(verbose_name="Status",)
	
	class Meta:
		ordering = ['oid']
		verbose_name = u"Controller"
		verbose_name_plural = u"Controllers"

	def __unicode__(self):
		return self.controllerid