from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    url(r'^list/$', 'report.views.list_report', name='report-list'),
    url(r'^list/api/$', 'report.views.list_report_api', name='report-list-api'),
    
    url(r'^add/$', 'report.views.add_report', name='add-report'),
    url(r'^delete/$', 'report.views.delete_report', name='delete-report'),
    url(r'^edit/(?P<id>[\w -]+)/$', 'report.views.edit_report', name='edit-report'),
    url(r'^view/(?P<id>[\w -]+)/$', 'report.views.report_details', name='report-details'),
    url(r'^view/api/(?P<id>[\w -]+)/$', 'report.views.report_details_api', name='report-details'),
    url(r'^view/$', 'report.views.report_view', name='report-view'),

    url(r'^recuring/add/$', 'report.views.add_recuring_report', name='add-recuring-report'),
    url(r'^recuring/delete/$', 'report.views.delete_recuring_report', name='delete-recuring-report'),
    url(r'^recuring/view/(?P<id>[\w -]+)/$', 'report.views.view_recuring_report', name='view-recuring-report'),
    url(r'^recuring/edit/(?P<id>[\w -]+)/$', 'report.views.edit_recuring_report', name='edit-recuring-report'),

    url(r'^singlejob/add/$', 'report.views.add_single_report', name='add-single-report'),
    url(r'^singlejob/view/(?P<id>[\w -]+)/$', 'report.views.view_single_report', name='view-single-report'),
    url(r'^singlejob/api/(?P<jobid>[\w -]+)/$', 'report.views.single_report_api', name='api-single-report'),
    url(r'^singlejob/edit/(?P<id>[\w -]+)/$', 'report.views.edit_single_report', name='edit-single-report'),
    url(r'^singlejob/delete/$', 'report.views.delete_single_report', name='delete-single-report'),

    url(r'^recuring/job/api/(?P<id>[\w -]+)/$', 'report.views.recuring_job_json', name='recuring-job-api'),

    url(r'^lists/$', 'report.views.recuring_report_list', name='list-recuring-report'),
    url(r'^recuring-job-list/$', 'report.views.list_recuring_job', name='report-recuring-list'),
    url(r'^single-job-list/$', 'report.views.list_single_job', name='report-single-list'),

    url(r'^printer/list/$', 'report.views.list_printer', name='list-printer'),
    url(r'^printer/list/api/$', 'report.views.list_printer_api', name='list-printer-api'),
    url(r'^printer/add/$', 'report.views.add_printer', name='add-printer'),
    url(r'^printer/view/(?P<printer_id>[\w -]+)/$', 'report.views.view_printer', name='view-printer'),
    url(r'^printer/edit/(?P<printer_id>[\w -]+)/$', 'report.views.edit_printer', name='edit-printer'),
    url(r'^printer/delete/$', 'report.views.delete_printer', name='delete-printer'),


)