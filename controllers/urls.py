from django.conf.urls import patterns, include, url
from haystack.views import SearchView, search_view_factory
from controllers.views import *

urlpatterns = patterns('',
    # Examples:
    url(r'^add/$', ControllerFormAction.as_view()),
    url(r'^list-json/$', ControllerList.as_view()),
    url(r'^delete/(?P<id>[\w]+)/$', "controllers.views.controller_delete"),
    url(r'^contact/delete/$', "controllers.views.contact_delete"),
)
