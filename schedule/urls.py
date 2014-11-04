from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    url(r'^jobs/$', 'schedule.views.home', name='schedule-home'),
    url(r'^get-job/(?P<job_id>[\d]+)/$', 'schedule.views.get_job', name='get-job'),
    
    #  API view
    url(r'^all-jobs/$', 'schedule.views.job_list', name='job-list'),
    url(r'^current-jobs/$', 'schedule.views.job_list', name='current-jobs'),
    url(r'^my-jobs/$', 'schedule.views.my_jobs', name='my-jobs'),

    url(r'^list-filter/$', 'schedule.views.job_list_filter', name='job-list-filter'),

    url(r'^jobs/filter/$', 'schedule.views.job_filter_view', name='schedule-job-filter-view'),
    url(r'^job/add/$', 'schedule.views.add_job', name='add-job'),
    url(r'^job/view/(?P<jobid>\w+)/$', 'schedule.views.view_job', name='view-job'),
    url(r'^job/view/api/(?P<jobid>\w+)/$', 'schedule.views.view_job_api2', name='api-view-job'),
    url(r'^job/(?P<jobstatusid>\w+)/$', 'schedule.views.view_job_api', name='view-job-api'),
    url(r'^job/edit/(?P<jobid>\w+)/$', 'schedule.views.edit_job', name='edit-job'),
    url(r'^job/copy/(?P<jobid>\w+)/$', 'schedule.views.copy_job', name='copy-job'),

    url(r'^job-delete/$', 'schedule.views.delete_job', name='delete-job'),

    url(r'^job-status/add/(?P<jsid>\w+)/$', 'schedule.views.add_job_status', name='add-job-status'),
    url(r'^job-status/edit/(?P<jsid>\w+)/$', 'schedule.views.edit_job_status', name='edit-job-status'),
    url(r'^job-status/view/(?P<jsid>\w+)/$', 'schedule.views.view_job_status', name='view-job-status'),
    url(r'^job-status/view/api/(?P<jobid>\w+)/$', 'schedule.views.view_job_status_api', name='view-job-status-api'),
    # url(r'^job/(?P<jobid>\w+)/view/$', 'schedule.views.view_job_status', name='view-job-status'),

    url(r'^customer/job/list/$', 'schedule.views.total_pending_job', name='customer-job-list'),

    url(r'^comment/add/$', 'schedule.views.add_comment', name='add-comment'),
    url(r'^comment/edit/(?P<comid>\w+)/$', 'schedule.views.edit_comment', name='edit-comment'),
    url(r'^comment/delete/$', 'schedule.views.delete_comment', name='delete-comment'),

    url(r'^sjob/reindex/$', 'schedule.views.job_reindex', name='job-reindex'),
    
    url(r'^job-control/add/$', 'schedule.views.job_control_add', name='job-control-add'),
    url(r'^job-control/edit/(?P<jobid>\w+)/$', 'schedule.views.job_control_edit', name='job-control-edit'),
    url(r'^job-control/list/$', 'schedule.views.job_control_list', name='job-control-add'),
    url(r'^job-control/list/json/$', 'schedule.views.job_control_list_json', name='job-control-add-json'),

    url(r'^elevetor-type/add/$', 'schedule.views.elevetor_type_add', name='elevetor-type-add'),
    url(r'^elevetor-type/list/$', 'schedule.views.elevetor_type_list', name='elevetor-type-list'),
    url(r'^elevetor-type/delete/$', 'schedule.views.elevetor_type_delete', name='elevetor-type-delete'),

    
)