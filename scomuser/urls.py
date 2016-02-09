from django.conf.urls import patterns, include, url
# from scomuser.views import UserListView

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'scomuser.views.sc_home', name='scomuser-home'),
    url(r'^search/$', 'scomuser.views.search_user', name='search-user'),
    url(r'^profile/(?P<pk>\d+)/$', 'scomuser.views.UserDetails', name='scuser-profile'),
    # url(r'^edit/(?P<user_id>\d+)/$', 'scomuser.views.edit_user', name='edit-user'),
    # url(r'^profile/edit/(?P<profile_id>\d+)/$', 'scomuser.views.edit_profile', name='edit-profile'),

    url(r'^login/$', 'scomuser.views.sc_login', name='user-login'),
    url(r'^logout/$', 'scomuser.views.sc_logout', name='user-logout'),
    
    url(r'^change-password/$', 'scomuser.views.change_password2', name='change-password'),

    url(r'^adduser/$', 'scomuser.views.scomuser_add', name='adduser'),
    url(r'^userlist/$', 'scomuser.views.UserList', name='userlist'),
    url(r'^userlist/json/$', 'scomuser.views.UserListApi', name='userlist-json'),


    url(r'^list/$', 'scomuser.views.scomuser_list', name='userlistapi'),
    # url(r'^userlist/$', UserListView.as_view(), name='userlist'),
    url(r'^viewuser/(?P<pk>\d+)/$', "scomuser.views.UserDetails", name='userview'),
    url(r'^edituser/(?P<pk>\d+)/$', "scomuser.views.UserEdit", name='edituser'),
    url(r'^deleteuser/$', "scomuser.views.DeleteUser", name='deleteuser'),

    url(r'^user/report/add/$', "scomuser.views.user_report_add", name='user_report_add'),
    url(r'^user/report/delete/$', "scomuser.views.user_report_delete", name='user_report_delete'),


    url(r'^pay-types/$', "scomuser.views.list_paytype", name='list-pay-type'),
    url(r'^pay-type/add/$', "scomuser.views.add_paytype", name='add-pay-type'),
    url(r'^pay-type/edit/(?P<pay_type_id>\d+)/$', "scomuser.views.edit_paytype", name='edit-pay-type'),
    url(r'^pay-type/delete/$', "scomuser.views.delete_paytype", name='delete-pay-type'),

    url(r'^departments/$', "scomuser.views.list_department", name='list-department'),
    url(r'^department/add/$', "scomuser.views.add_department", name='add-department'),
    url(r'^department/edit/(?P<department_id>\d+)/$', "scomuser.views.edit_department", name='edit-department'),
    url(r'^department/delete/$', "scomuser.views.delete_department", name='delete-department'),

    url(r'^payrolls/$', "scomuser.views.list_payroll", name='list-payroll'),
    url(r'^payroll/(?P<payroll_id>\d+)/$', "scomuser.views.view_payroll", name='view-payroll'),
    url(r'^payroll/add/(?P<uid>\w+)/$', "scomuser.views.add_payroll", name='add-payroll'),
    url(r'^payroll/edit/(?P<payroll_id>\d+)/$', "scomuser.views.edit_payroll", name='edit-payroll'),
    url(r'^payroll/delete/$', "scomuser.views.delete_payroll", name='delete-payroll'),

    url(r'^change/password/$', 'scomuser.views.change_password', name='change-password'),    

    url(r'^permission/add/$', 'scomuser.views.scomuser_permission_add', name='scomuser-permission-add'),

    url(r'^get-change-password-form/(?P<uid>\d+)/$', 'scomuser.views.send_change_password_form')

)
