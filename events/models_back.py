from django.db import models
from contacts.models import Contact
# Create your models here.

class Events(models.Model):
	eventid = models.BigIntegerField(verbose_name='Event ID', max_length=20, primary_key=True)
	eventdate = models.DateField(verbose_name='Event Date', null=True, blank=True)
	eventtime = models.TimeField(verbose_name='Event Time', null=True, blank=True)
	name = models.CharField(verbose_name='Name', max_length=40, null=True, blank=True)
	category = models.CharField(verbose_name='Catagorey', max_length=40, null=True, blank=True)
	doorname = models.CharField(verbose_name='Door Name', max_length=40, null=True, blank=True)
	cardnumber = models.CharField(verbose_name='Card Number', max_length=10, null=True, blank=True)
	event = models.CharField(verbose_name='Event', max_length=40, null=True, blank=True)
	action = models.CharField(verbose_name='Action', max_length=40, null=True, blank=True)
	zonename = models.CharField(verbose_name='Zone Name', max_length=40, null=True, blank=True)
	
	
	class Meta:
		ordering = ['eventid', ]
		db_table = u'alarm_events'
		verbose_name = u"Alarm Events"
		verbose_name_plural = u"Alarm Events"
		permissions = (
    		('view_events', 'View Events'),
    	)

	def __unicode__(self):
		return self.eventid


class Door(models.Model):
	name = models.CharField("Door Title", max_length=25, blank=True, null=True)
	opened_time = models.DateTimeField(verbose_name='Time Last Updated', null=True, blank=True)
	current_status = models.CharField(verbose_name='Door Status', max_length=10, null=True, blank=True)
	closed_time = models.DateTimeField(verbose_name='Time Last Updated', null=True, blank=True)
	last_opened_datetime = models.DateTimeField(verbose_name='Time Last Updated', null=True, blank=True)
	# door_lastopenedtime = models.TimeField(verbose_name='Time Last Updated', null=True, blank=True)
	last_closed_datetime = models.DateTimeField(verbose_name='Time Last Updated', null=True, blank=True)
	# door_lastclosedtime = models.TimeField(verbose_name='Time Last Updated', null=True, blank=True)

	class Meta:
		verbose_name = "Door"
		verbose_name_plural = "Doors"
		permissions = (
			('view_door', 'View Door'),
		)

	def __unicode__(self):
		return self.title

class CardReader(models.Model):
	name = models.CharField(verbose_name='Card One Description', max_length=30, null=True, blank=True)
	card_type = models.CharField(verbose_name='Input Type', max_length=3, choices=alarm_input_choices , default='')
	last_datetime = models.DateTimeField(verbose_name='DateTime Last Updated', null=True, blank=True)
	# last_user = models.CharField(verbose_name='User Last Accessed', max_length=30, null=True, blank=True)
	card_user = models.ForeignKey(Contact, blank=True, null=True, default="Guest")

	class Meta:
		verbose_name = "Card"
		verbose_name_plural = "Cards"

		permissions = (
			('view_card', 'View Card'),
		)

	def __unicode__(self):
		return "%s (%d)" % (self.name, self.id)

class Input(models.Model):
	name = models.CharField(verbose_name='Input One Description', max_length=30, null=True, blank=True)
	input_type = models.CharField(verbose_name='Input Type', max_length=3, choices=alarm_input_choices , default='')
	status = models.CharField(verbose_name='Input One Current Status', max_length=30, null=True, blank=True)
	lastdate = models.DateField(verbose_name='Input 1 Last Accessed', null=True, blank=True)
	laststate = models.CharField(verbose_name='Last State', max_length=30, null=True, blank=True)

	class Meta:
		verbose_name = "Input"
		verbose_name_plural = "Inputs"

		permissions = (
			('view_input', 'View Input'),
		)

	def __unicode__(self):
		return "%s (%d)" % (self.name, self.id)



class Controller(models.Model):
	# controllerid = models.CharField(verbose_name='Controller Id', max_length=20, null=True)
	name = models.CharField(verbose_name='Controller Name', max_length=40,primary_key=True)
	ipaddress = models.CharField(verbose_name='IP Address', max_length=15, null=True, blank=True)
	serial_number = models.CharField(verbose_name='Serial Number', max_length=20, null=True, blank=True)
	door = models.OneToOneField(Door)
		
	controller_alarm_laststate = models.CharField(verbose_name='Controller Alarm Last State', max_length=30, null=True, blank=True)
	controller_alarm_lastdate = models.DateTimeField(verbose_name='Date Last Tripped', null=True, blank=True)
	# controller_alarm_lasttime = models.TimeField(verbose_name='Time Last Tripped', null=True, blank=True)
				
	class Meta:
		verbose_name = u"Controller"
		verbose_name_plural = u"Controllers"

	def __unicode__(self):
		return "%s (%d)" % (self.name, self.id)




