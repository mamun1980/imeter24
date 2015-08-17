from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'events.views.list_event', name='event-list'),
    url(r'^search/$', 'events.views.search_events', name='events-list'),
    url(r'^list/$', 'events.views.list_event_api', name='event-list-api'),
    url(r'^add/$', 'events.views.add_event', name='add-event'),
    url(r'^edit/(?P<id>\w+)/$', 'events.views.edit_event', name='edit-events'),
    url(r'^delete/$', 'events.views.delete_event', name='delete-events'),
    url(r'^view/(?P<id>\w+)/$', 'events.views.events_details', name='events-details'),
    # url(r'event/filter/$', 'events.views.item_details_filtered', name='events-details-filtered'),
   
    url(r'^controllers/$', 'events.views.list_controller', name='controller-list'),
    url(r'^controller-list/$', 'events.views.controller_list', name='list-controller'),
    url(r'^controllers/add/$', 'events.views.add_controller', name='add-controller'),
    url(r'^controllers/edit/(?P<controller_name>[\w ,\']+)/$', 'events.views.edit_controller', name='edit-controller'),
    url(r'^controllers/delete/$', 'events.views.delete_controller', name='delete-controller'),
    url(r'^controllers/view/(?P<controller_name>[\w ,\']+)/$', 'events.views.controller_details', name='controller-details'),
    # url(r'event/filter/$', 'events.views.item_details_filtered', name='events-details-filtered'),


    url(r'^evententry/add/$', 'events.views.add_evententry', name='add-event-entry'),
    url(r'^evententry/delete/$', 'events.views.delete_evententry', name='delete-event-entry'),
    url(r'^evententry/edit/(?P<entryid>[\w ,\']+)/$', 'events.views.edit_evententry', name='edit-event-entry'),
    url(r'^evententry/view/(?P<entryid>[\w ,\']+)/$', 'events.views.view_evententry', name='view-event-entry'),
    url(r'^entry/list/$', 'events.views.list_evententry', name='list-event-entry'),
    
    url(r'^event-entry-list/$', 'events.views.list_evententry_api', name='list-event-entry-api'),


    url(r'^eventpayroll/add/$', 'events.views.add_eventpayroll', name='add-event-payroll'),
    url(r'^payroll/delete/$', 'events.views.delete_eventpayroll', name='delete-event-payroll'),
    url(r'^payroll/edit/(?P<serial_id>[\w ,\']+)/$', 'events.views.edit_eventpayroll', name='edit-event-payroll'),
    url(r'^payroll/view/(?P<serial_id>[\w ,\']+)/$', 'events.views.view_eventpayroll', name='view-event-payroll'),
    url(r'^payroll/list/$', 'events.views.list_eventpayroll', name='list-event-payroll'),
   
)