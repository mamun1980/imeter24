from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'imeter24.views.home', name='home'),

    url(r'^generate-pdf/$', 'imeter24.views.generate_pdf', name='generate-pdf'),

    url(r'^system-variable/$', 'imeter24.views.sys_variable', name='sys-variable'),
    
    url(r'^dashboard/$', 'imeter24.views.dashboard', name='user-dashboard'),

    url(r'^send-mass-mail/$', 'imeter24.views.send_mass_mail', name='send-mass-mail'),
    url(r'^mass-mail-status/$', 'imeter24.views.mass_mail_status', name='mass-mail-status'),
    url(r'^get-mass-mails/$', 'imeter24.views.get_mass_mails', name='get-mass-mail'),
    
    url(r'^group/add/$', 'imeter24.views.add_group', name='add-group'),
    url(r'^group/list/$', 'imeter24.views.list_group', name='list-group'),
    url(r'^group/delete/$', 'imeter24.views.delete_group', name='delete-group'),

    #======= Angular route ===========
    url(r'^userlist/$', 'scomuser.views.UserListApi', name='userlistapi'),

    url(r'^group/edit/(?P<group_id>\d+)/$', 'imeter24.views.edit_group', name='edit-group'),
    url(r'^group/view/(?P<group_id>\d+)/$', 'imeter24.views.group_details', name='view-group'),

    url(r'^group/update/$', 'imeter24.views.update_group', name='update-group'),
    url(r'^scomuser/', include('scomuser.urls')),
    url(r'^contacts/', include('contacts.urls')),
    url(r'^inventory/', include('inventory.urls')),
    url(r'^report/', include('report.urls')),
    url(r'^events/', include('events.urls')),
    url(r'^purchase/', include('purchase.urls')),

    url(r'^controllers/', include('controllers.urls')),


    url(r'^schedule/', include('schedule.urls')),

    url(r'^statics/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.STATIC_ROOT}),

    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$',
            'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT, }),
    )