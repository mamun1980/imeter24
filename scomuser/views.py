from django.shortcuts import render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.template import RequestContext
from django.contrib import auth
from django.contrib.auth.models import User, Group
from django.contrib import messages
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView

from premierelevator.helper_functions import *

from scomuser.forms import *
from scomuser.models import *


@login_required
def sc_home(request):
    if request.method == "POST":
        name = request.POST.get("autocomplete")
        user_list = User.objects.filter(username__icontains=name)
    else:
        user_list = User.objects.all()

    userlookupform = UserLookupForm()
    return render_to_response('scomuser/scomuser.html', {'user_list': user_list, 'ulform': userlookupform, 'page_title': 'Home'}, 
        context_instance=RequestContext(request))


@login_required
@csrf_exempt
def change_password2(request):
    # import pdb; pdb.set_trace()
    if request.method == "POST":
        user = request.user
        password_change_form = ChangePasswordForm(request.POST)
        if password_change_form.is_valid():
            current_pass = request.POST.get("current_password")
            user_valid = auth.authenticate(username=user.username, password=current_pass)
            if user_valid:
                password = request.POST.get("new_password")
                user.set_password(password)
                user.save()
                messages.success(request, "Your password has been changed.")
                return HttpResponse("success")
            else:
                return HttpResponse("error")
        else:
            return HttpResponse("error")
    else:
        password_change_form = ChangePasswordForm()
        return render_to_response("scomuser/change-password.html", {'password_change_form': password_change_form, 'page_title': 'Change Password'}, 
            context_instance=RequestContext(request))


@login_required
@csrf_protect
@permission_required("auth.add_user")
def scomuser_add(request):
    groups = Group.objects.all()
    if request.method == 'POST':
        UserAddForm = ScomUserAddForm(request.POST)
        
        if UserAddForm.is_valid():
            user = UserAddForm.save()

            scprofile = ScomUserProfile(user=user)
            SPForm = ScomUserProfileForm(request.POST, request.FILES, instance=scprofile)
            if SPForm.is_valid():
                SPForm.save()

            selected_groups = request.POST.getlist("selected-groups")
            for group in selected_groups:
                gp = Group.objects.get(name=group)
                user.groups.add(gp)

            return HttpResponseRedirect("/scomuser/list/#/userlist")
        else:
            UserAddForm = ScomUserAddForm(request.POST)
            SPForm = ScomUserProfileForm(request.POST)
            return render_to_response("scomuser/add_user.html", 
                {'useraddform':UserAddForm, 'supform': SPForm, 'page_title': 'Add user', 'groups': groups }, 
            context_instance=RequestContext(request))
    else:
        
        UserAddForm = ScomUserAddForm()
        SPForm = ScomUserProfileForm()
        return render_to_response("scomuser/add_user.html", 
            {'useraddform':UserAddForm, 'supform': SPForm, 'page_title': 'Add user', 'groups': groups }, 
            context_instance=RequestContext(request))

@login_required
@csrf_exempt
@permission_required("auth.change_user")
def UserEdit(request, pk):
    user = User.objects.get(pk=pk)
    all_permissions = get_permissions()
    permissions = Permission.objects.filter(user=user)
    groups = Group.objects.all()
    user_groups = user.groups.all()
    try:
        payroll = Payroll.objects.get(user=user)
    except Payroll.DoesNotExist:
        payroll = Payroll.objects.create(user=user)

    try:
        scprofile = ScomUserProfile.objects.get(user=user)
    except ScomUserProfile.DoesNotExist:
        scprofile = ScomUserProfile.objects.create(user=user)

    if request.method == "POST":
        payroll_form = PayrollForm(request.POST, instance=payroll)
        UserEditForm = ScomUserEditForm(request.POST, instance=user)
        UserProfileForm = ScomUserProfileForm(request.POST, request.FILES, instance=scprofile)
        if UserEditForm.is_valid() and UserProfileForm.is_valid() and payroll_form.is_valid():

            user = UserEditForm.save()
            UserProfileForm.save()

            payroll = payroll_form.save()

            return HttpResponseRedirect("/scomuser/list/#/userlist")
        else:
            return render_to_response("scomuser/edit_user.html", 
                {'usereditform': UserEditForm, 'user_obj': user, 'page_title': 'Edit User', 'groups': groups, 'user_groups': user_groups,
        'supform': UserProfileForm, 'all_permissions': all_permissions, 'permissions': permissions}, 
        context_instance=RequestContext(request))

    else:
        payroll_form = PayrollForm(instance=payroll)
        UserEditForm = ScomUserEditForm(instance=user)
        UserProfileForm = ScomUserProfileForm(instance=scprofile)
        

    return render_to_response("scomuser/edit_user.html", 
        {'usereditform': UserEditForm, 'user_obj': user, 'payroll': payroll, 'page_title': 'Edit User', 'groups': groups, 'user_groups': user_groups,
        'supform': UserProfileForm, 'all_permissions': all_permissions, 'permissions': permissions, 'payroll_form': payroll_form,
        }, context_instance=RequestContext(request))

@login_required
@permission_required("auth.delete_user")
@csrf_exempt
def DeleteUser(request):
    if request.method == 'POST':
        # import pdb; pdb.set_trace();
        uid = request.POST.get("uid")
        try:
            user = User.objects.get(id=uid)
            scomuser= ScomUserProfile.objects.get(user=user)
            scomuser.delete()
            user.delete()
            return HttpResponse(uid)
        except:
            pass



# class UserListView(ListView):
#   context_object_name = 'user_list'
#   queryset = User.objects.filter()
#   template_name = 'scomuser/user_list.html'

#   def get_context_data(self, **kwargs):
#       context = super(UserListView, self).get_context_data(**kwargs)
#         context['userlookupform'] = UserLookupForm()
#         return context


@login_required
@permission_required("auth.view_user")
def UserList(request):
    if request.method == "POST":
        name = request.POST.get("autocomplete")
        user_list = User.objects.filter(username__icontains=name)
    else:
        user_list = User.objects.all().order_by('username')

    userlookupform = UserLookupForm()
    return render_to_response('scomuser/user_list.html', {'user_list': user_list, 'ulform': userlookupform, 'page_title': 'User List',}, 
        context_instance=RequestContext(request))

def scomuser_list(request):
    user = request.user
    return render(request, "scomuser/user_list.html", {'user': user})

@login_required
def UserListApi(request):
    # import pdb; pdb.set_trace()
    req_user = request.user
    import json
    from django.core.serializers.json import DjangoJSONEncoder
    object_id_list = [-1,]
    users = User.objects.all().exclude(id__in=object_id_list).order_by("username")

    # scusers = ScomUserProfile.objects.all()
    user_dict_list = []
    
    for scuser in users:
        user_dict = {}
        user_dict['id'] = scuser.id
        user_dict['username'] = scuser.username
        user_dict['first_name'] = scuser.first_name
        user_dict['last_name'] = scuser.last_name
        user_dict['email'] = scuser.email
        user_dict['is_superuser'] = scuser.is_superuser
        user_dict['last_login'] = scuser.last_login
        if scuser.id == request.user.id:
            user_dict['current_user'] = True
        else:
            user_dict['current_user'] = False

        try:
            user_dict['search_string'] = scuser.scomuserprofile.search_string
            user_dict['profile'] = {}
            user_dict['profile']['city'] = scuser.scomuserprofile.city
            user_dict['profile']['province'] = scuser.scomuserprofile.province
            user_dict['profile']['address_1'] = scuser.scomuserprofile.address_1
            user_dict['profile']['cell_phone'] = scuser.scomuserprofile.cell_phone
        except:
            user_dict['search_string'] = ""
            user_dict['profile'] = {}


        user_dict['permission'] = {}
        user_dict['permission']['can_add_user'] = req_user.has_perm("auth.add_user")
        user_dict['permission']['can_view_user'] = req_user.has_perm("auth.view_user")
        user_dict['permission']['can_change_user'] = req_user.has_perm("auth.change_user")
        user_dict['permission']['can_delete_user'] = req_user.has_perm("auth.delete_user")
        user_dict['permission']['can_change_user_password'] = req_user.has_perm("auth.can_change_password")

        user_dict_list.append(user_dict)
    json_users = json.dumps(user_dict_list, cls=DjangoJSONEncoder)
    return HttpResponse(json_users, mimetype='application/json')

@login_required
@permission_required("auth.view_user")
def UserDetails(request, pk):
    requested_user = request.user
    try:
        user = User.objects.get(pk=pk)
        sc_user_profile = ScomUserProfile.objects.get(user=user)
    except ScomUserProfile.DoesNotExist:
        sc_user_profile = ScomUserProfile.objects.create(user=user)
    except:
        user = None

    # if user != request.user and not request.user.is_superuser:
    if user != request.user and not requested_user.has_perm("auth.view_user"):
        return HttpResponseRedirect("/dashboard/")

    permissions = Permission.objects.filter(user=user)

    user_perms = {}
    for permission in permissions:
        if  permission.content_type.name in user_perms.keys():
            user_perms[permission.content_type.name].append(permission.name)
        else:
            user_perms[permission.content_type.name] = []
            user_perms[permission.content_type.name].append(permission.name)

    try:
        payroll = Payroll.objects.get(user=user)
    except Payroll.DoesNotExist:
        payroll = Payroll.objects.create(user=user)
    
    
    return render_to_response("scomuser/user_details.html", 
        {'userobj': user, 'userprofileobj': sc_user_profile, 'page_title': 'User Details', 'payroll': payroll,
        'permissions': user_perms },
        context_instance=RequestContext(request))

@csrf_protect
@login_required
@permission_required("auth.view_user")
def ProfileDetails(request, user_id):
    try:
        user = User.objects.get(pk=user_id)
        sc_user_profile = ScomUserProfile.objects.get(user=user)
    except ScomUserProfile.DoesNotExist:
        sc_user_profile = ScomUserProfile.objects.create(user=user)

    if request.method == "POST":
        profile_form = ScomUserProfileForm(request.POST, instance=sc_user_profile)
    else:
        profile_form = ScomUserProfileForm(instance=sc_user_profile)

    
    return render_to_response("scomuser/user_profile_details.html", 
        {'userobj': user, 'userprofileobj': sc_user_profile, 'page_title': 'Profile Details'},
        context_instance=RequestContext(request))


def sc_login(request):
    
    if request.method == "POST":
        LoginForm = ScomUserLoginForm(request.POST)
            
        username = request.POST.get('username', "")
        password = request.POST.get('password', "")
        
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            if user.is_active and not user.is_staff:
                auth.login(request, user)
                return HttpResponseRedirect("/dashboard/")

            elif user.is_active and user.is_staff:
                auth.login(request, user)
                return HttpResponseRedirect("/dashboard/")

            else:
                messages.error(request, 'User %s is not activated yet. Please check your mail.' % username)
                return HttpResponseRedirect("/scomuser/login/")

        else:
            messages.error(request, 'Username %s is not available in our system' % username)
            return HttpResponseRedirect("/scomuser/login/")
    else:
        LoginForm = ScomUserLoginForm()
        
        return render_to_response("scomuser/login.html", 
            {'lform': LoginForm, 'page_title': 'User Login'}, 
            context_instance=RequestContext(request))

@login_required
def sc_logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/")

def list_paytype(request):
    pay_types = PayType.objects.all()
    return render_to_response("scomuser/list-pay-type.html",
                {'pay_types': pay_types, 'page_title': 'Paytype List'}, 
                context_instance=RequestContext(request))


@login_required
@csrf_exempt
@permission_required("scomuser.add_paytype")
def add_paytype(request):
    if request.method == "POST":
        pay_type = request.POST.get("pay_type")
        try:
            pay_type = PayType.objects.create(pay_type=pay_type, is_active=True)
            return render_to_response("scomuser/partials/add-pay-type-partial.html",
                {'pay_type': pay_type, 'page_title': 'Add Paytype'}, 
                context_instance=RequestContext(request))
        except:
            return HttpResponse("error")
    else:
        pay_types = PayType.objects.all()
        pay_type_form = PayTypeForm()
        return render_to_response("scomuser/partials/list-pay-type.html",
            {'pay_types': pay_types, 'pay_type_form': pay_type_form, 'page_title': 'Add Paytype'}, 
            context_instance=RequestContext(request))


@login_required
@csrf_exempt
@permission_required("scomuser.change_paytype")
def edit_paytype(request, pay_type_id):
    if request.method == "POST":
        pay_type_id = request.POST.get("pay_type_id")
        pay_type = PayType.objects.get(id=pay_type_id)
        pay_type_form = PayTypeForm(request.POST, instance=pay_type)
        if pay_type_form.is_valid():
            pay_type = pay_type_form.save()
            return render_to_response("scomuser/partials/add-pay-type-partial.html", {'pay_type': pay_type, 'page_title': 'Edit Paytype'}, 
                context_instance=RequestContext(request))
    elif request.method == "GET":
        pay_type = PayType.objects.get(id=pay_type_id)
        pay_type_form = PayTypeForm(instance=pay_type)

        return render_to_response("scomuser/partials/edit-pay-type-tmpl.html",
            {'pay_type_form': pay_type_form, 'pay_type_id': pay_type_id, 'page_title': 'Edit Paytype'}, 
            context_instance=RequestContext(request))

@login_required
@permission_required("scomuser.delete_paytype")
@csrf_exempt
def delete_paytype(request):
    if request.method == "POST":
        paytypeid = request.POST.get("paytypeid")
        pay_type = PayType.objects.get(id=paytypeid)
        pay_type.delete()
        return HttpResponse(paytypeid)
    else:
        return HttpResponse("Hello World!")


@login_required
@permission_required("scomuser.add_department")
@csrf_exempt
def add_department(request):
    if request.method == "POST":
        department = request.POST.get("name")
        try:
            department = Department.objects.create(name=department, is_active=True)
            return render_to_response("scomuser/partials/add-department-partial.html",
                {'department': department, 'page_title': 'Add Department'}, 
                context_instance=RequestContext(request))
        except:
            return HttpResponse("error")
    else:
        departments = Department.objects.all()
        department_form = DepartmentForm()
        return render_to_response("scomuser/partials/list-department.html",
            {'departments': departments, 'department_form': department_form, 'page_title': 'Add Department'}, 
            context_instance=RequestContext(request))

@login_required
@permission_required("scomuser.change_department")
@csrf_exempt
def edit_department(request, department_id):
    if request.method == "POST":
        department_id = request.POST.get("department_id")
        department = Department.objects.get(id=department_id)
        department_form = DepartmentForm(request.POST, instance=department)
        if department_form.is_valid():
            department = department_form.save()
            return render_to_response("scomuser/partials/add-department-partial.html",
            {'department': department, 'page_title': 'Edit Department'}, context_instance=RequestContext(request))
    
    else:
        department = Department.objects.get(id=department_id)
        department_form = DepartmentForm(instance=department)

        return render_to_response("scomuser/partials/edit-department-tmpl.html",
            {'department_form': department_form, 'department_id': department_id, 'page_title': 'Edit Department'}, context_instance=RequestContext(request))


@login_required
@permission_required("scomuser.view_department")
def list_department(request):
    departments = Department.objects.all()
    return render_to_response("scomuser/list-department.html", {'departments': departments, 'page_title': 'List Department'}, context_instance=RequestContext(request))

@login_required
@permission_required("scomuser.delete_department")
@csrf_exempt
def delete_department(request):
    if request.method == "POST":
        department_id = request.POST.get("department_id")
        department = Department.objects.get(id=department_id)
        department.delete()
        return HttpResponse(department_id)
    else:
        return HttpResponse("Hello World!")



@login_required
@permission_required("scomuser.add_payroll")
@csrf_exempt
def add_payroll(request, uid):
    if request.method == 'POST':
        user = User.objects.get(id=uid)
        payroll_form = PayrollForm(request.POST)
        if payroll_form.is_valid():
            payroll = payroll_form.save(commit=False)
            payroll.user = user
            payroll.save()
            return HttpResponse(payroll.id)
        else:
            return render_to_response("scomuser/add-payroll.html", {'payroll_form': payroll_form, 'uid': uid, 'page_title': 'Add Payroll'},
            context_instance=RequestContext(request))

    else:

        payroll_form = PayrollForm()
        return render_to_response("scomuser/add-payroll.html", {'payroll_form': payroll_form, 'uid': uid, 'page_title': 'Add Payroll'},
            context_instance=RequestContext(request))

@login_required
@permission_required("scomuser.view_payroll")
def list_payroll(request):
    payrolls = Payroll.objects.all()
    return render_to_response("scomuser/payroll-list.html", {"payrolls": payrolls, 'page_title': 'List Payroll'}, context_instance=RequestContext(request))


@login_required
@permission_required("scomuser.delete_payroll")
@csrf_exempt
def delete_payroll(request):
    if request.method == "POST":
        payroll_id = request.POST.get("payroll_id")
        payroll = Payroll.objects.get(id=payroll_id)
        payroll.delete()
        return HttpResponse(payroll_id)
    else:
        return HttpResponse("Hello World!")

@login_required
@permission_required("scomuser.change_payroll")
@csrf_exempt
def edit_payroll(request, payroll_id):
    if request.method == "POST":
        payroll = Payroll.objects.get(id=payroll_id)
        payroll_form = PayrollForm(request.POST, instance=payroll)
        if payroll_form.is_valid():
            payroll_form.save()
            return HttpResponseRedirect("/scomuser/payrolls/")
        else:
            return render_to_response("scomuser/payroll/edit-payroll.html", 
                {'payroll_form': payroll_form, 'payroll_id': payroll_id, 'page_title': 'Edit Payroll'},
            context_instance=RequestContext(request))
    else:
        payroll = Payroll.objects.get(id=payroll_id)
        payroll_form = PayrollForm(instance=payroll)
        return render_to_response("scomuser/payroll/edit-payroll.html", 
            {'payroll_form': payroll_form, 'payroll_id': payroll_id, 'page_title': 'Edit Payroll'},
            context_instance=RequestContext(request))


@login_required
@permission_required("scomuser.view_payroll")
def view_payroll(request, payroll_id):
    payroll = Payroll.objects.get(id=payroll_id)
    user = payroll.user
    try:
        userprofile = ScomUserProfile.objects.get(user=user)
    except:
        userprofile = ScomUserProfile.objects.create(user=user)

    page_title = 'Payroll details of ('+ user.username + ')'
    return render_to_response("scomuser/payroll-details.html", 
        {'user': user, 'payroll': payroll, 'userprofile': userprofile, 'page_title': page_title}, 
        context_instance=RequestContext(request))



@login_required
@csrf_exempt
# @permission_required("add_permission")
def scomuser_permission_add(request):

    if request.method == "POST":
        # import pdb; pdb.set_trace();
        user_id = request.POST['user_id']
        perm_list = request.POST.getlist("selected_permissions[]")
        myuser = User.objects.get(id=user_id)
        myuser.user_permissions.clear()
        for perm in perm_list:
            content_type_id = perm.split("-")[0]
            codename = perm.split("-")[1]
            model_name = perm.split("_")[-1]
            ct = ContentType.objects.get(id=content_type_id)
            permission = Permission.objects.get(codename=codename, content_type=ct)
            myuser.user_permissions.add(permission)

        messages.success(request, "Permissions updated successfully.")      
        return HttpResponse("success")
    else:
        return False


def send_change_password_form(request, uid):
    return render(request, "scomuser/partials/change-password-tpl.html", {'uid': uid})


@login_required
@csrf_exempt
@permission_required("auth.can_change_password")
def change_password(request):
    if request.method == 'POST':
        userid = request.POST.get('userid', "")
        new_password = request.POST.get('newpassword', "")
        if new_password != "" and userid != "":
            user = User.objects.get(id=userid)
            user.set_password(new_password)
            user.save()

            return HttpResponse("New password for %s is updated" % user.username)
        else:
            return HttpResponse("Not valid user & password")



