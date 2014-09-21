from django import forms
from events.models import *
from events.choices import *
# from django.contrib.auth.models import User
from scomuser.models import ScomUserProfile
from events.lookups import UserLookup
import selectable

class EventsForm(forms.ModelForm):
    eventid = forms.CharField( max_length=15,
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': "Event id"}))
    eventdate = forms.DateField(required=False, widget=forms.DateInput(
        attrs={"class": "form-control datepicker", 'placeholder':"event date"}))
    eventtime = forms.TimeField(required=False,
        widget=forms.TextInput( attrs={"class": "form-control timepicker", 'placeholder':"event date"}))
    username = forms.CharField( max_length=25, required=False,
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder':"User Name"}))
    category = forms.CharField( max_length=25, required=False,
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder':"Category"}))
    doorname = forms.CharField( max_length=25, required=False,
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder':"Door Name"}))
    cardnumber = forms.CharField( max_length=25, required=False,
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder':"Card Number"}))
    event = forms.CharField( max_length=25, required=False,
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder':"Event"}))
    action = forms.CharField( max_length=25, required=False,
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder':"Action"}))
    zonename = forms.CharField( max_length=25, required=False,
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder':"Action"}))

    class Meta:
        model = Events
        exclude = ['search_string']

    def save(self, commit=True):
        event = super(EventsForm, self).save(commit=False)
        event.search_string = event.eventid + " " + event.username + " " + event.category + " " + event.doorname
        event.save()
        return event



class EventsEditForm(EventsForm):
    eventid = forms.CharField( max_length=15,
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': "Event id", 'readonly': True}))


class ControllersForm(forms.ModelForm):
    controller_name = forms.CharField( max_length=25,
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': "Controller Name"}))
    controllerid = forms.CharField( max_length=15,
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': "Controller ID"}))
    ipaddress = forms.CharField( max_length=15, required=False,
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': "IP Address"}))
    serial_number = forms.CharField( max_length=15, required=False,
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': "Serial Number"}))
    name = forms.CharField( max_length=15, required=False,
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': "Name"}))
    doorcurrentstatus = forms.CharField( max_length=15, required=False,
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': "Door Current Status"}))
    doorlastopeneddate = forms.DateField(required=False, widget=forms.DateInput(
        attrs={"class": "form-control datepicker", 'placeholder':"Door last oppened date"}))
    doorlastopenedtime = forms.TimeField(required=False, widget=forms.TextInput(
        attrs={"class": "form-control timepicker", 'placeholder':"Door last oppened time"}))
    doorlastcloseddate = forms.DateField(required=False, widget=forms.DateInput(
        attrs={"class": "form-control datepicker", 'placeholder':"Door last closed date"}))
    doorlastclosedtime = forms.TimeField(required=False, widget=forms.TextInput(
        attrs={"class": "form-control timepicker", 'placeholder':"Door last closed time"}))

    card_1_name = forms.CharField( max_length=25, required=False,
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder':"Card 1 name"}))
    card_1_type = forms.ChoiceField(choices = alarm_input_choices,
        widget=forms.Select(attrs={"class": "form-control"}))
    card_1_lastdate = forms.DateField(required=False, widget=forms.DateInput(
        attrs={"class": "form-control datepicker", 'placeholder':"Card 1 last date"}))
    card_1_lasttime = forms.TimeField(required=False, widget=forms.TextInput(
        attrs={"class": "form-control timepicker", 'placeholder':"Card 1 last time"}))
    card_1_lastuser = forms.CharField( max_length=30, required=False,
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': "Card 1 last user"}))
    card_1_lastcard = forms.CharField( max_length=15, required=False,
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': "Card 1 last card"}))

    card_2_name = forms.CharField( max_length=25, required=False,
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder':"Card 2 name"}))
    card_2_type = forms.ChoiceField( choices = alarm_input_choices,
        widget=forms.Select(attrs={"class": "form-control"}))
    card_2_lastdate = forms.DateField(required=False, widget=forms.DateInput(
        attrs={"class": "form-control datepicker", 'placeholder':"Card 2 last date"}))
    card_2_lasttime = forms.TimeField(required=False, widget=forms.TextInput(
        attrs={"class": "form-control timepicker", 'placeholder':"Card 2 last time"}))
    card_2_lastuser = forms.CharField( max_length=30, required=False,
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': "Card 2 last user"}))
    card_2_lastcard = forms.CharField( max_length=15, required=False,
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': "Card 2 last card"}))

    input_1_name = forms.CharField( max_length=25, required=False,
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder':"Input 1 name"}))
    input_1_type = forms.ChoiceField( choices = alarm_input_choices,
        widget=forms.Select(attrs={"class": "form-control"}))
    input_1_status = forms.CharField( max_length=25, required=False,
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder':"Input 1 status"}))
    input_1_lastdate = forms.DateField(required=False, widget=forms.DateInput(
        attrs={"class": "form-control datepicker", 'placeholder':"Input 1 last date"}))
    input_1_lasttime = forms.TimeField(required=False, widget=forms.TextInput(
        attrs={"class": "form-control timepicker", 'placeholder':"Input 1 last time"}))
    input_1_laststate = forms.CharField( max_length=25, required=False,
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder':"Input 1 laststate"}))

    input_2_name = forms.CharField( max_length=25, required=False,
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder':"Input 2 name"}))
    input_2_type = forms.ChoiceField( choices = alarm_input_choices,
        widget=forms.Select(attrs={"class": "form-control"}))
    input_2_status = forms.CharField( max_length=25, required=False,
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder':"Input 2 status"}))
    input_2_lastdate = forms.DateField(required=False, widget=forms.DateInput(
        attrs={"class": "form-control datepicker", 'placeholder':"Input 2 last date"}))
    input_2_lasttime = forms.TimeField(required=False, widget=forms.TextInput(
        attrs={"class": "form-control timepicker", 'placeholder':"Input 2 last time"}))
    input_2_laststate = forms.CharField( max_length=25, required=False,
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder':"Input 2 laststate"}))

    input_3_name = forms.CharField( max_length=25, required=False,
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder':"Input 3 name"}))
    input_3_type = forms.ChoiceField( choices = alarm_input_choices,
        widget=forms.Select(attrs={"class": "form-control"}))
    input_3_status = forms.CharField( max_length=25, required=False,
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder':"Input 3 status"}))
    input_3_lastdate = forms.DateField(required=False, widget=forms.DateInput(
        attrs={"class": "form-control datepicker", 'placeholder':"Input 3 last date"}))
    input_3_lasttime = forms.TimeField(required=False, widget=forms.TextInput(
        attrs={"class": "form-control timepicker", 'placeholder':"Input 3 last time"}))
    input_3_laststate = forms.CharField( max_length=25, required=False,
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder':"Input 3 laststate"}))

    input_4_name = forms.CharField( max_length=25, required=False,
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder':"Input 4 name"}))
    input_4_type = forms.ChoiceField( choices = alarm_input_choices,
        widget=forms.Select(attrs={"class": "form-control"}))
    input_4_status = forms.CharField( max_length=25, required=False,
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder':"Input 4 status"}))
    input_4_lastdate = forms.DateField(required=False, widget=forms.DateInput(
        attrs={"class": "form-control datepicker", 'placeholder':"Input 4 last date"}))
    input_4_lasttime = forms.TimeField(required=False, widget=forms.TextInput(
        attrs={"class": "form-control timepicker", 'placeholder':"Input 4 last time"}))
    input_4_laststate = forms.CharField( max_length=25, required=False,
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder':"Input 4 laststate"}))


    controller_alarm_laststate = forms.CharField( max_length=25, required=False,
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Controller Alarm Last State'}))
    controller_alarm_lastdate = forms.DateField(required=False, widget=forms.DateInput(
        attrs={"class": "form-control datepicker", 'placeholder':"Date Last Tripped"}))
    controller_alarm_lasttime = forms.TimeField(required=False, widget=forms.TextInput(
        attrs={"class": "form-control timepicker", 'placeholder':"Time Last Tripped"}))

    class Meta:
        model = Controllers
        exclude = ['search_string']

    def save(self, commit=True):
        controller = super(ControllersForm, self).save(commit=False)
        controller.search_string = controller.controller_name + " " + controller.card_1_name + " " + controller.card_1_type + " " + controller.card_2_name+ " " + controller.card_2_type+ " " + controller.input_1_name+ " " + controller.input_1_type+ " " + controller.input_2_name+ " " + controller.input_2_type+ " " + controller.input_3_name+ " " + controller.input_3_type+ " " + controller.input_3_name+ " " + controller.input_4_type+ " " + controller.input_4_name
        controller.save()
        return controller


class ControllersEditForm(ControllersForm):
    controller_name = forms.CharField( max_length=25,
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': "Controller Name", 'readonly': True}))




class EventEntryForm(forms.ModelForm):
    entryid = forms.CharField( max_length=15,
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': "Event id"}))
    date_of_transaction = forms.DateField(required=False, widget=forms.DateInput(
        attrs={"class": "form-control datepicker", 'placeholder':"event date"}))
    time_of_transaction = forms.TimeField(required=False,
        widget=forms.TextInput( attrs={"class": "form-control timepicker", 'placeholder':"00:00:00"}))
    transaction_username = forms.CharField( max_length=40, required=False,
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder':"User Name"}))
    transaction_processed = forms.ChoiceField(required=False, choices=TRANSACTION_STATUS,
        widget=forms.Select(attrs={"class": "form-control"}))

    class Meta:
        model = EventEntry
        exclude = ['search_string']


    def save(self, commit=True):
        event = super(EventEntryForm, self).save(commit=False)
        event.search_string = event.entryid + " " + event.transaction_username
        event.save()
        return event


class EventPayrollForm(forms.ModelForm):
    serial_id = forms.CharField( max_length=15,
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': "Serial id"}))
    event_username = forms.CharField( max_length=40, required=False,
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder':"User Name From Events"}))
    premier_user = forms.ModelChoiceField(queryset=ScomUserProfile.objects.all(),
          label='Premier User',
          widget=selectable.forms.AutoCompleteWidget(UserLookup, 
          attrs={"class": "form-control primary_supplier", 'placeholder': "search for supplier", 'name': 'search-user'}),
          required=False,
    )
    class Meta:
        model = EventPayroll











