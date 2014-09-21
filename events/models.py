#Premier Alarm Events Model
from django.db import models
from events.choices import *
# from django.contrib.auth.models import User
from scomuser.models import ScomUserProfile

class Events(models.Model):
	eventid = models.CharField(verbose_name='Event ID', max_length=20, primary_key=True)
	eventdate = models.DateField(verbose_name='Event Date', null=True, blank=True)
	eventtime = models.TimeField(verbose_name='Event Time', null=True, blank=True)
	name = models.CharField(verbose_name='Name', max_length=40, null=True, blank=True)
	category = models.CharField(verbose_name='Catagorey', max_length=40, null=True, blank=True)
	doorname = models.CharField(verbose_name='Door Name', max_length=40, null=True, blank=True)
	cardnumber = models.CharField(verbose_name='Card Number', max_length=10, null=True, blank=True)
	event = models.CharField(verbose_name='Event', max_length=40, null=True, blank=True)
	action = models.CharField(verbose_name='Action', max_length=40, null=True, blank=True)
	zonename = models.CharField(verbose_name='Zone Name', max_length=40, null=True, blank=True)
	search_string = models.TextField(max_length=1000, blank=True, null=True)
	
	
	class Meta:
		ordering = ['eventid', ]
		verbose_name = u"Alarm Events"
		verbose_name_plural = u"Alarm Events"

		permissions = (
			('view_events', 'Can View Event'),
		)

	def __unicode__(self):
		return self.eventid
		
class Controllers(models.Model):
	controller_name = models.CharField(max_length=40, verbose_name='Controller Name' ,primary_key=True)
	controllerid = models.CharField(verbose_name='Controller Id', max_length=20, null=True)
	ipaddress = models.CharField(verbose_name='IP Address', max_length=15, null=True, blank=True)
	serial_number = models.CharField(verbose_name='Serial Number', max_length=10, null=True, blank=True)
	name = models.CharField(verbose_name='Name', max_length=30, null=True, blank=True)
	doorcurrentstatus = models.CharField(verbose_name='Door Status', max_length=10, null=True, blank=True)
	doorlastopeneddate = models.DateField(verbose_name='Date Last Updated', null=True, blank=True)
	doorlastopenedtime = models.TimeField(verbose_name='Time Last Updated', null=True, blank=True)
	doorlastcloseddate = models.DateField(verbose_name='Date Last Updated', null=True, blank=True)
	doorlastclosedtime = models.TimeField(verbose_name='Time Last Updated', null=True, blank=True)	
	
	card_1_name = models.CharField(verbose_name='Card One Description', max_length=30, null=True, blank=True)
	card_1_type = models.CharField(verbose_name='Input Type', max_length=3, choices=alarm_input_choices , default='')
	card_1_lastdate = models.DateField(verbose_name='Date Last Updated', null=True, blank=True)
	card_1_lasttime = models.TimeField(verbose_name='Time Last Updated', null=True, blank=True)
	card_1_lastuser = models.CharField(verbose_name='User Last Accessed', max_length=30, null=True, blank=True)
	card_1_lastcard = models.CharField(verbose_name='Card Id Last Accessed', max_length=10, null=True, blank=True)
	
	card_2_name = models.CharField(verbose_name='Card Two Description', max_length=30, null=True, blank=True)
	card_2_type = models.CharField(verbose_name='Input Type', max_length=3, choices=alarm_input_choices , default='')
	card_2_lastdate = models.DateField(verbose_name='Date Last Updated', null=True, blank=True)
	card_2_lasttime = models.TimeField(verbose_name='Time Last Updated', null=True, blank=True)
	card_2_lastuser = models.CharField(verbose_name='User Last Accessed', max_length=30, null=True, blank=True)
	card_2_lastcard = models.CharField(verbose_name='Card Id Last Accessed', max_length=10, null=True, blank=True)
	
	input_1_name = models.CharField(verbose_name='Input One Description', max_length=30, null=True, blank=True)
	input_1_type = models.CharField(verbose_name='Input Type', max_length=3, choices=alarm_input_choices , default='')
	input_1_status = models.CharField(verbose_name='Input One Current Status', max_length=30, null=True, blank=True)
	input_1_lastdate = models.DateField(verbose_name='Input 1 Last Accessed', null=True, blank=True)
	input_1_lasttime = models.TimeField(verbose_name='Time', null=True, blank=True)
	input_1_laststate = models.CharField(verbose_name='Last State', max_length=30, null=True, blank=True)
	
	
	input_2_name = models.CharField(verbose_name='Input Two Description', max_length=30, null=True, blank=True)
	input_2_type = models.CharField(verbose_name='Input Type', max_length=3, choices=alarm_input_choices , default='')
	input_2_status = models.CharField(verbose_name='Current Status', max_length=30, null=True, blank=True)
	input_2_lastdate = models.DateField(verbose_name='Input 2 Last Accessed', null=True, blank=True)
	input_2_lasttime = models.TimeField(verbose_name='Time', null=True, blank=True)
	input_2_laststate = models.CharField(verbose_name='Last State', max_length=30, null=True, blank=True)
	
	
	input_3_name = models.CharField(verbose_name='Input Three Description', max_length=30, null=True, blank=True)
	input_3_type = models.CharField(verbose_name='Input Type', max_length=3, choices=alarm_input_choices , default='')
	input_3_status = models.CharField(verbose_name='Current Status', max_length=30, null=True, blank=True)
	input_3_lastdate = models.DateField(verbose_name='Input 3 Last Accessed', null=True, blank=True)
	input_3_lasttime = models.TimeField(verbose_name='Time', null=True, blank=True)		
	input_3_laststate = models.CharField(verbose_name='Last State', max_length=30, null=True, blank=True)
	
	input_4_name = models.CharField(verbose_name='Input Four Description', max_length=30, null=True, blank=True)
	input_4_type = models.CharField(verbose_name='Input Type', max_length=3, choices=alarm_input_choices , default='')
	input_4_status = models.CharField(verbose_name='Current Status', max_length=30, null=True, blank=True)
	input_4_lastdate = models.DateField(verbose_name='Input 4 Last Accessed', null=True, blank=True)
	input_4_lasttime = models.TimeField(verbose_name='Time', null=True, blank=True)		
	input_4_laststate = models.CharField(verbose_name='Last State', max_length=30, null=True, blank=True)
	
	controller_alarm_laststate = models.CharField(verbose_name='Controller Alarm Last State', max_length=30, null=True, blank=True)
	controller_alarm_lastdate = models.DateField(verbose_name='Date Last Tripped', null=True, blank=True)
	controller_alarm_lasttime = models.TimeField(verbose_name='Time Last Tripped', null=True, blank=True)
	search_string = models.TextField(max_length=1000, blank=True, null=True)


	class Meta:
		ordering = ['controllerid', ]
		db_table = u'alarm_controllers'
		verbose_name = u"Controller"
		verbose_name_plural = u"Controllers"

		permissions = (
			('view_controllers', 'Can View Controllers'),
		)

	def __unicode__(self):
		return self.controller_name



class EventEntry(models.Model):
	"""docstring for EntryEvent"""

	entryid = models.CharField(verbose_name='Entry ID', max_length=50, primary_key=True)
	date_of_transaction = models.DateField(verbose_name='Date of Transaction', null=True, blank=True)
	time_of_transaction = models.TimeField(verbose_name='Time of Transaction', null=True, blank=True)
	transaction_username = models.CharField(verbose_name='User Name', max_length=40, null=True, blank=True)
	transaction_processed = models.CharField(max_length=10, null=True, blank=True)
	search_string = models.TextField(max_length=1000, blank=True, null=True)

	class Meta:
		ordering = ['entryid', ]
		
		verbose_name = u"EventEntry"
		verbose_name_plural = u"EventEntry"

		permissions = (
			('view_evententry', 'Can View Event Entry'),
		)

	def __unicode__(self):
		return "%s - %s" % (self.entryid, self.transaction_username)


class EventPayroll(models.Model):
	serial_id = models.CharField(verbose_name='Entry ID', max_length=50, primary_key=True)
	event_username = models.CharField(verbose_name='User Name From Event', max_length=40, null=True, blank=True)
	premier_user = models.ForeignKey(ScomUserProfile, null=True, blank=True, related_name='event-user-for')

	class Meta:
		
		verbose_name = u"EventPayroll"
		verbose_name_plural = u"EventPayroll"

		permissions = (
			('view_eventpayroll', 'Can View Event Payroll'),
		)

	def __unicode__(self):
		return "Payroll ID: %s ( %s )" % (self.serial_id, self.event_username)









		