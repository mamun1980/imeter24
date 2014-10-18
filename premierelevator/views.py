from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import Group
from scomuser.forms import *
from .forms import *
# Import all widgets from all apps
from scomuser.widgets import *
from contacts.widgets import *
from inventory.widgets import *
from events.widgets import *
from schedule.widgets import *
from report.models import Printer, Report

from premierelevator.helper_functions import *

def home(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect("/dashboard/")
    else:
        LoginForm = ScomUserLoginForm()
        return render_to_response("home.html", {'lform': LoginForm, 'page_title': 'Home' }, context_instance=RequestContext(request))

@login_required
@csrf_exempt
def sys_variable(request):
    printers = Printer.objects.all()
    reports = Report.objects.all()
    try:
        sv = SystemVariable.objects.get(id=1)
    except:
        sv = None

    if request.method == 'POST':
        # import pdb; pdb.set_trace()
        sv_form = SystemVariableForm(request.POST, instance=sv)
        if sv_form.is_valid():
            sv_form.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "base/sys-variable.html", 
                {'form': sv_form,'sv': sv, 'printers': printers, 'reports': reports})
    else:
        sv_form = SystemVariableForm(instance=sv)
        return render_to_response("base/sys-variable.html", 
            {'form': sv_form, 'sv': sv, 'printers': printers, 'reports': reports}, 
            context_instance=RequestContext(request))


def send_mass_mail(request):

    if request.method == 'POST':
        from django.core.validators import validate_email
        import re
        # import pdb; pdb.set_trace();
        mass_mail_form = MassMailForm(request.POST)
        to_all_users = request.POST.get('to_all',"")
        if mass_mail_form.is_valid():
            email_id = mass_mail_form.cleaned_data['email_id']
            subject = mass_mail_form.cleaned_data['subject']
            body = mass_mail_form.cleaned_data['body']
            # mail_status = request.POST.get('mail_status','')
            

            if to_all_users == '0':
                recievers = request.POST.get('reciever','')
                reciever_list = re.split("[, ]+", recievers)
                for rec in reciever_list:
                    reciever = rec.strip()
                    try:
                        validate_email(reciever)
                        massmail = MassMail(email_id=email_id, subject=subject, body=body, reciever=reciever)
                        massmail.mail_status = 'pending'
                        massmail.sender = request.user.email
                        # massmail.mail_status = mail_status
                        massmail.search_string = massmail.email_id + " " + massmail.sender + " " + massmail.mail_status + " " + massmail.reciever
                        massmail.save()
                    except:
                        pass
            else:
                recievers = User.objects.all().values("email")
                for reciever in recievers:
                    rec_email = reciever['email']
                    if rec_email != '':
                        try:
                            validate_email(rec_email)
                            massmail = MassMail(email_id=email_id, subject=subject, body=body, reciever=rec_email)
                            massmail.mail_status = 'pending'
                            massmail.sender = request.user.email
                            massmail.search_string = massmail.email_id + " " + massmail.sender + " " + massmail.mail_status + " " + massmail.reciever
                            massmail.save()
                        except:
                            pass

            return HttpResponseRedirect("/mass-mail-status/#/get-mass-mails")
    else:
        mass_mail_form = MassMailForm()
    
    return render(request, "utility/send-mass-mail.html", {'mass_mail_form': mass_mail_form})



def mass_mail_status(request):
    massmails = MassMail.objects.all()
    return render(request, "utility/mass-mail-status.html", {'massmails': massmails})



def get_mass_mails(request):
    user = request.user
    import json, datetime
    from django.core.serializers.json import DjangoJSONEncoder
    
    massmails = MassMail.objects.all()
    massmails_list = []

    for massmail in massmails:
        massmail_dict = {}

        massmail_dict['email_id'] = massmail.email_id
        massmail_dict['subject'] = massmail.subject
        massmail_dict['body'] = massmail.body
        massmail_dict['sender'] = massmail.sender
        massmail_dict['reciever'] = massmail.reciever
        massmail_dict['mail_status'] = massmail.mail_status
        massmail_dict['request_datetime'] = massmail.request_datetime
        if massmail.delivered_datetime:
            massmail_dict['delivered_datetime'] = massmail.delivered_datetime
        else:
            massmail_dict['delivered_datetime'] = 'Not delivered yet!'

        massmail_dict['search_string'] = massmail.search_string


        massmail_dict['permission'] = {}
        massmail_dict['permission']['can_view_massmail'] = user.has_perm("scomuser.view_massmail")
        massmail_dict['permission']['can_send_massmail'] = user.has_perm("scomuser.send_massmail")

        massmails_list.append(massmail_dict)


    json_job = json.dumps(massmails_list, cls=DjangoJSONEncoder)
    return HttpResponse(json_job, mimetype='application/json')




        
@login_required
@csrf_exempt
@permission_required("auth.add_group")
def add_group(request):

    
    all_permissions = get_permissions()
    if request.method == "POST":
        group_name = request.POST.get("group_name","")
        if group_name != "":
            group, created = Group.objects.get_or_create(name=group_name)

            group_perms = request.POST.getlist("selected_permissions[]")            
            group.permissions.clear()
            
            for perm in group_perms:
                content_type_id = perm.split("-")[0]
                codename = perm.split("-")[1]
                model_name = perm.split("_")[-1]
                ct = ContentType.objects.get(id=content_type_id)
                permission = Permission.objects.get(codename=codename, content_type=ct)
                group.permissions.add(permission)

            return HttpResponse('success')
        else:
            group_form = GroupForm(request.POST)

    else:
        group_form = GroupForm()

    return render(request, "base/add-group.html", {'group_form': group_form, 'all_permissions': all_permissions})

@login_required
@permission_required("auth.view_group")
def list_group(request):
    groups = Group.objects.all()
    return render(request, "base/list-group.html", {'groups': groups,})


@login_required
@permission_required("auth.delete_group")
@csrf_exempt
def delete_group(request):
    if request.method == "POST":
        group_id = request.POST.get("group_id")
        group = Group.objects.get(id=group_id)
        group.delete()
        return HttpResponse(group_id)


def group_details(request, group_id):
    group = Group.objects.get(id=group_id)
    return render(request, "base/group-details.html", {'group': group})


@login_required
@permission_required("auth.change_group")
@csrf_exempt
def edit_group(request, group_id):
    group = Group.objects.get(id=group_id)
    all_permissions = get_permissions()
    permissions = group.permissions.all()

    if request.method == "POST":
        
        group_name = request.POST.get("group_name","")
        if group_name != "":
            group.name = group_name
            group.save()

            group_perms = request.POST.getlist("selected_permissions[]")            
            group.permissions.clear()
            
            for perm in group_perms:
                content_type_id = perm.split("-")[0]
                codename = perm.split("-")[1]
                model_name = perm.split("_")[-1]
                ct = ContentType.objects.get(id=content_type_id)
                permission = Permission.objects.get(codename=codename, content_type=ct)
                group.permissions.add(permission)

            return HttpResponse('success')
        else:
            group_form = GroupForm(initial={'name': group.name})

    else:
        
        group_form = GroupForm(initial={'name': group.name})

    return render(request, "base/edit-group.html", {'group_form': group_form, 'group':group, 'permissions': permissions, 'all_permissions': all_permissions})


@login_required
@permission_required("auth.change_group")
@csrf_exempt
def update_group(request):
    if request.method == "POST":
        user_id = request.POST['user_id']
        group_list = request.POST.getlist("selected_groups[]")
        myuser = User.objects.get(id=user_id)
        myuser.groups.clear()
        for group in group_list:
            group_name = group.split("-")[1]
            gp = Group.objects.get(name=group_name)
            myuser.groups.add(gp)
              
        return HttpResponse("success")


@login_required
def dashboard(request):
    
    user = request.user
    UWidget = UserWidget()
    ConWidget = ContactWidget()
    InvWidget = InventoryWidget()
    EvWidget = EventWidget()
    JobWidget = ScheduleJobWidget(user)
    # all_perms = user.user_permissions.all()

    return render_to_response("base/dashboard.html", 
        {'userwidget': UWidget, 'contactwidget': ConWidget, 'inventorywidget': InvWidget, 'eventwidget': EvWidget, 
        'ScheduleJobWidget': JobWidget, 'page_title': 'Dashboard' },

        context_instance=RequestContext(request)
    )