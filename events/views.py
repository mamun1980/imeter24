from django.shortcuts import render
from events.models import *
from events.forms import *
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required

import json
from haystack.forms import ModelSearchForm, SearchForm
from haystack.query import SearchQuerySet, EmptySearchQuerySet
from haystack.views import SearchView
from haystack.inputs import Raw, Clean, AutoQuery
import re

from django.core.paginator import Paginator, EmptyPage, InvalidPage

@login_required
@permission_required("events.add_events")
@csrf_exempt
def add_event(request):
	if request.method == "POST":
		event_form = EventsForm(request.POST)
		if event_form.is_valid():
			event_form.save()
			return HttpResponseRedirect("/events/")
		else:
			return render(request, "events/add-event.html", {'event_form': event_form,  'page_title': 'Add Event'})
	else:
		event_form = EventsForm()
		return render(request, "events/add-event.html", {'event_form': event_form})

@login_required
@permission_required("events.view_events")
def list_event(request):
	events = Events.objects.all().order_by("-eventdate")[:200]
	return render(request, "events/list-event.html", {'events': events,  'page_title': 'list event'})

@csrf_exempt
def search_events(request):
    query = request.GET.get('q',"")
    if request.GET.get('q'):
        events = SearchQuerySet().using('events').filter(content=AutoQuery(query)).load_all()[:30]
    else:
        events = SearchQuerySet().using('events').all().load_all()[:30]

    event_list = []
    if events:
        for event in events:
            if event != None:
                event_dict = {}
                event_dict['eventid'] = event.eventid
                event_dict['name'] = event.name
                event_dict['doorname'] = event.doorname
                event_dict['cardnumber'] = event.cardnumber
                event_dict['zonename'] = event.zonename

                event_list.append(event_dict)
    try:
        page = int(request.GET.get('page','1'))
    except ValueError:
        page = 1
    paginator = Paginator(event_list, 20)
    try:
        pages = paginator.page(page)
    except (EmptyPage, InvalidPage):
        pages = paginator.page(paginator.num_pages)

    results = pages.object_list

    data = json.dumps(results)
    return HttpResponse(data)




@login_required
@permission_required("events.view_events")
def list_event_api(request):
	user = request.user
	import json
	from django.core.serializers.json import DjangoJSONEncoder
	events = Events.objects.all().order_by("-eventdate").values('eventid','eventdate', 'eventtime', 'name', 'category', 'doorname', 'cardnumber', 'event', 'action', 'zonename', 'search_string')[:200]
	events_dict_list = []
	for event in events:
		event['permission'] = {}
		event['permission']['can_add_event'] = user.has_perm("events.add_event")
		event['permission']['can_view_event'] = user.has_perm("events.view_event")
		event['permission']['can_change_event'] = user.has_perm("events.change_event")
		event['permission']['can_delete_event'] = user.has_perm("events.delete_event")
		events_dict_list.append(event)
	json_posts = json.dumps(events_dict_list, cls=DjangoJSONEncoder)
	return HttpResponse(json_posts, mimetype='application/json')


@login_required
@permission_required("events.change_events")
@csrf_exempt
def edit_event(request, id):
	event = Events.objects.get(eventid=id)
	if request.method == "POST":
		event_form = EventsEditForm(request.POST, instance=event)
		if event_form.is_valid():
			event_form.save()
			return HttpResponseRedirect("/events/#/events/list")
		else:
			return render(request, "events/edit-event.html", {'event_form': event_form, 'id': id,  'page_title': 'Update Event'})
	else:
		event_form = EventsEditForm(instance=event)
		return render(request, "events/edit-event.html", {'event_form': event_form, 'id': id, 'page_title': 'Update Event'})

@csrf_exempt
@login_required
@permission_required("events.delete_events")
def delete_event(request):
	if request.method == "POST":
		id = request.POST.get('id')
		event = Events.objects.get(eventid=id)
		event.delete()
		return HttpResponse(id)


@login_required
@permission_required("events.view_events")
@csrf_exempt
def events_details(request, id):
	event = Events.objects.get(eventid=id)
	return render(request, "events/event-details.html", {'event': event,  'page_title': 'Event Details'})

@login_required
@permission_required("events.add_controllers")
@csrf_exempt
def add_controller(request):
	if request.method == "POST":
		controller_form = ControllersForm(request.POST)
		if controller_form.is_valid():
			controller_form.save()
			return HttpResponseRedirect("/events/controllers/#/events/controller-list")
		else:
			return render(request, "events/add-controller.html", {'controller_form': controller_form, 'page_title': 'Add Controller'})
	else:
		controller_form = ControllersForm()
		return render(request, "events/add-controller.html", {'controller_form': controller_form, 'page_title': 'Add Controller'})

@login_required
@permission_required("events.view_controllers")
def list_controller(request):
	controllers = Controllers.objects.all()
	return render(request, "events/list-controller.html", {'controllers': controllers, 'page_title': 'List Controller'})
	
@login_required
@csrf_exempt
@permission_required("events.change_controllers")
def edit_controller(request, controller_name):
	controller = Controllers.objects.get(controller_name=controller_name)
	if request.method == "POST":
		controller_form = ControllersEditForm(request.POST, instance=controller)
		if controller_form.is_valid():
			controller_form.save()
			return HttpResponseRedirect("/events/controllers/#/events/controller-list")
		else:
			return render(request, "events/edit-controller.html", 
				{'controller_form': controller_form, 'controller_name': controller_name,  'page_title': 'Update Controller'})
	else:
		controller_form = ControllersEditForm(instance=controller)
		return render(request, "events/edit-controller.html", 
			{'controller_form': controller_form, 'controller_name': controller_name, 'page_title': 'Update Controller'})


@login_required
@permission_required("events.view_controllers")
def controller_details(request, controller_name):	
	controller = Controllers.objects.get(controller_name=controller_name)
	return render(request, "events/controller-details.html", {'controller': controller,  'page_title': 'Controller Details'})

@login_required
@permission_required("events.view_controllers")
def controller_list(request):
	user = request.user
	import json
	from django.core.serializers.json import DjangoJSONEncoder
	controllers = Controllers.objects.all() #.values('controller_name','controllerid', 'name', 'doorcurrentstatus', 'controller_alarm_laststate', 'controller_alarm_lastdate', 'controller_alarm_lasttime', 'search_string').order_by("controller_name")
	controllers_dict_list = []
	for controller in controllers:
		controllers_dict = {}

		controllers_dict['permission'] = {}
		controllers_dict['permission']['can_add_controller'] = user.has_perm("events.add_controllers")
		controllers_dict['permission']['can_view_controller'] = user.has_perm("events.view_controllers")
		controllers_dict['permission']['can_change_controller'] = user.has_perm("events.change_controllers")
		controllers_dict['permission']['can_delete_controller'] = user.has_perm("events.delete_controllers")

		controllers_dict['search_string'] = controller.search_string
		controllers_dict['controller_name'] = controller.controller_name
		controllers_dict['doorcurrentstatus'] = controller.doorcurrentstatus

		if controller.card_1_name:
			controllers_dict['card_1'] = True
			controllers_dict['card_1_name'] = controller.card_1_name
			controllers_dict['card_1_type'] = controller.card_1_type
			controllers_dict['card_1_lastdate'] = controller.card_1_lastdate
			controllers_dict['card_1_lastuser'] = controller.card_1_lastuser
		else:
			controllers_dict['card_1'] = False

		

		if controller.input_3_name:
			controllers_dict['input_3'] = True
			controllers_dict['input_3_name'] = controller.input_3_name
			controllers_dict['input_3_type'] = controller.input_3_type
			controllers_dict['input_3_status'] = controller.input_3_status
			controllers_dict['input_3_lastdate'] = controller.input_3_lastdate
		else:
			controllers_dict['input_3'] = False

		if controller.input_4_name:
			controllers_dict['input_4'] = True
			controllers_dict['input_4_name'] = controller.input_4_name
			controllers_dict['input_4_type'] = controller.input_4_type
			controllers_dict['input_4_status'] = controller.input_4_status
			controllers_dict['input_4_lastdate'] = controller.input_4_lastdate
		else:
			controllers_dict['input_4'] = False


		# controllers_dict['controller_name'] = controller.controller_name
		# controllers_dict['controller_name'] = controller.controller_name
		# controllers_dict['controller_name'] = controller.controller_name
		# controllers_dict['controller_name'] = controller.controller_name






		controllers_dict_list.append(controllers_dict)

	json_posts = json.dumps(controllers_dict_list, cls=DjangoJSONEncoder)
	return HttpResponse(json_posts, mimetype='application/json')


@login_required
@permission_required("events.delete_controllers")
@csrf_exempt
def delete_controller(request):
	if request.method == "POST":
		controller_name = request.POST.get('name')
		controller = Controllers.objects.get(controller_name=controller_name)
		controller.delete()
		return HttpResponse(controller_name)




@csrf_exempt
@login_required
@permission_required("events.add_evententry")
def add_evententry(request):
	if request.method == "POST":
		
		event_entry_form = EventEntryForm(request.POST)
		if event_entry_form.is_valid():
			event_entry_form.save()
			return HttpResponseRedirect("/events/entry/list/#/events/event-entry-list")
	else:
		event_entry_form = EventEntryForm()

		return render(request, "events/add-event-entry.html", {"event_entry_form": event_entry_form})

@csrf_exempt
@login_required
@permission_required("events.delete_evententry")
def delete_evententry(request):
	if request.method == 'POST':
		entryid = request.POST.get("entryid", "")
		entry = EventEntry.objects.get(entryid=entryid)
		entry.delete()
		return HttpResponse(entryid)


@csrf_exempt
@login_required
@permission_required("events.change_evententry")
def edit_evententry(request, entryid):
	entry = EventEntry.objects.get(entryid=entryid)
	
	if request.method == 'POST':
		entry_form = EventEntryForm(request.POST, instance=entry)
		if entry_form.is_valid():
			entry_form.save()
			return HttpResponseRedirect("/events/entry/list/#/events/event-entry-list")
	else:
		entry_form = EventEntryForm(instance=entry)
	
	return render(request, "events/edit-event-entry.html", {'event_entry_form': entry_form, 'entryid': entryid})


@csrf_exempt
@login_required
@permission_required("events.view_evententry")
def view_evententry(request, entryid):
	entry = EventEntry.objects.get(entryid=entryid)
	return render(request, 'events/view-event-entry.html', {'entry': entry})


def list_evententry(request):
	entries = EventEntry.objects.all()
	return render(request, "events/list-event-entry.html", {"entries": entries})


def list_evententry_api(request):
	user = request.user
	import json
	from django.core.serializers.json import DjangoJSONEncoder
	entries = EventEntry.objects.all().values('entryid','date_of_transaction', 'time_of_transaction', 'transaction_username', 'transaction_processed', 'search_string').order_by("entryid")
	entries_dict_list = []
	for entry in entries:
		entry['permission'] = {}
		entry['permission']['can_view_evententry'] = user.has_perm("events.view_evententry")
		entry['permission']['can_add_evententry'] = user.has_perm("events.add_evententry")
		entry['permission']['can_change_evententry'] = user.has_perm("events.change_evententry")
		entry['permission']['can_delete_evententry'] = user.has_perm("events.delete_evententry")
		entries_dict_list.append(entry)

	json_entries = json.dumps(entries_dict_list, cls=DjangoJSONEncoder)
	return HttpResponse(json_entries, mimetype='application/json')




@csrf_exempt
@login_required
@permission_required("events.add_eventpayroll")
def add_eventpayroll(request):
	if request.method == "POST":
		
		event_payroll_form = EventPayrollForm(request.POST)
		if event_payroll_form.is_valid():
			event_payroll_form.save()
			return HttpResponseRedirect("/events/payroll/list/")
	else:
		event_payroll_form = EventPayrollForm()

	return render(request, "events/add-event-payroll.html", {"event_payroll_form": event_payroll_form})



@csrf_exempt
@login_required
@permission_required("events.delete_eventpayroll")
def delete_eventpayroll(request,):
	if request.method == 'POST':
		# import pdb; pdb.set_trace();
		serial_id = request.POST.get("serial_id", "")
		payroll = EventPayroll.objects.get(serial_id=serial_id)
		payroll.delete()
		return HttpResponse(serial_id)


@csrf_exempt
@login_required
@permission_required("events.change_evententry")
def edit_eventpayroll(request, serial_id):
	payroll = EventPayroll.objects.get(serial_id=serial_id)
	
	if request.method == 'POST':
		payroll_form = EventPayrollForm(request.POST, instance=payroll)
		if payroll_form.is_valid():
			payroll_form.save()
			return HttpResponseRedirect("/events/payroll/list/")
		else:
			return render(request, "events/edit-event-payroll.html", {'payroll_form': payroll_form, 'serial_id': serial_id})		
	else:
		payroll_form = EventPayrollForm(instance=payroll)
	
	return render(request, "events/edit-event-payroll.html", {'payroll_form': payroll_form, 'serial_id': serial_id})


@csrf_exempt
@login_required
@permission_required("events.view_eventpayroll")
def view_eventpayroll(request, serial_id):
	payroll = EventPayroll.objects.get(serial_id=serial_id)
	return render(request, 'events/view-event-payroll.html', {'payroll': payroll})


def list_eventpayroll(request):
	payrolls = EventPayroll.objects.all()
	return render(request, "events/list-event-payroll.html", {"payrolls": payrolls})




