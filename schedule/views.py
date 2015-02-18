from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from schedule.forms import *
from schedule.models import *
import json, datetime

from haystack.forms import ModelSearchForm, SearchForm
from haystack.query import SearchQuerySet, EmptySearchQuerySet
from haystack.views import SearchView
from haystack.inputs import Raw, Clean, AutoQuery

from django.core.paginator import Paginator, EmptyPage, InvalidPage
# from premierelevator.models import SystemVariable
# Create your views here.
def home(request):
    '''
    list all scheduled job
    '''
    jobs = Job.objects.all()

    job_lookup_form = JobLookupForm()
    return render(request, 'schedule/job-list.html', {'jobs': jobs, 'job_lookup_form': job_lookup_form, 'page_title': 'List Job'})

def get_job(request, job_id):
    job = Job.objects.get(id=job_id)
    job_dict = {}
    job_dict['id'] = job.id
    job_dict['job_number'] = job.job_number
    job_dict['cab_designation'] = job.cab_designation
    if job.date_opened:
        job_dict['date_opened'] = job.date_opened.strftime('%m/%d/%Y')
    else:
        job_dict['date_opened'] = None
    if job.date_required:
        job_dict['date_required'] = job.date_required.strftime('%m/%d/%Y')
    else:
        job_dict['date_required'] = None

    job_dict['status'] = job.status
    job_dict['job_name'] = job.job_name
    job_dict['address_1'] = job.address_1
    job_dict['customer'] = job.customer
    job_dict['customer_contact_name'] = job.customer_contact_name
    job_dict['customer_contact_phone_number'] = job.customer_contact_phone_number
    job_dict['contact_email'] = job.contact_email
    job_dict['number_of_cabs'] = job.number_of_cabs
    job_dict['description'] = job.description
    job_dict['po_number'] = job.po_number
    job_dict['status_notes'] = job.status_notes
    if job.drawing_req_date:
        job_dict['drawing_req_date'] = job.drawing_req_date.strftime('%m/%d/%Y')
    else:
        job_dict['drawing_req_date'] = None
    if job.drawing_sent_to_customer_date:
        job_dict['drawing_sent_to_customer_date'] = job.drawing_sent_to_customer_date.strftime('%m/%d/%Y')
    else:
         job_dict['drawing_sent_to_customer_date'] = None   
    if job.drawing_approved_date:
        job_dict['drawing_approved_date'] = job.drawing_approved_date.strftime('%m/%d/%Y')
    else:
        job_dict['drawing_approved_date'] = None
    job_dict['eng_comment'] = job.eng_comment
    job_dict['search_string'] = job.search_string

    json_jobs = json.dumps(job_dict)

    return HttpResponse(json_jobs, mimetype='application/json')


def job_filter_view(request):
    if request.method == "POST":
        job_id = request.POST.get("autocomplete")
        return HttpResponseRedirect("/schedule/job/view/%s/" % job_id)

def getJobStatusState(jobstatus):
    # import pdb; pdb.set_trace();
    import datetime
    today = datetime.datetime.today()
    enddate = today + datetime.timedelta(days=7)
    # today = Date()
    state = []
    if jobstatus.fixtures_req_by != '' and jobstatus.fixtures_req_by != None:
        fixtures_req_by_date = datetime.datetime.strptime(jobstatus.fixtures_req_by, "%m/%d/%Y")
        if  fixtures_req_by_date <= today:
            state.append("job-status-red")
        elif fixtures_req_by_date <= enddate:
            state.append("job-status-yellow")

    if jobstatus.wood_shop_req_by != '' and jobstatus.wood_shop_req_by != None:
        wood_shop_req_by_date = datetime.datetime.strptime(jobstatus.wood_shop_req_by, "%m/%d/%Y")
        if wood_shop_req_by_date <= today:
            state.append("job-status-red")
        elif wood_shop_req_by_date <= enddate:
            state.append("job-status-yellow")

    if jobstatus.machine_shop_req_by != '' and jobstatus.machine_shop_req_by != None:
        machine_shop_req_by_date = datetime.datetime.strptime(jobstatus.machine_shop_req_by, "%m/%d/%Y")
        if machine_shop_req_by_date <= today:
            state.append("job-status-red")
        elif machine_shop_req_by_date <= enddate:
            state.append("job-status-yellow")

    if jobstatus.welding != '' and jobstatus.welding != None:
        welding_date = datetime.datetime.strptime(jobstatus.welding, "%m/%d/%Y")
        if welding_date <= today:
            state.append("job-status-red")
        elif welding_date <= enddate:
            state.append("job-status-yellow")

    if jobstatus.lacquer != '' and jobstatus.lacquer != None:
        lacquer_date = datetime.datetime.strptime(jobstatus.lacquer, "%m/%d/%Y")
        if lacquer_date <= today:
            state.append("job-status-red")
        elif lacquer_date <= enddate:
            state.append("job-status-yellow")

    if jobstatus.trim_shop_req_by != '' and jobstatus.trim_shop_req_by != None:
        trim_shop_req_by_date = datetime.datetime.strptime(jobstatus.trim_shop_req_by, "%m/%d/%Y")
        if trim_shop_req_by_date <= today:
            state.append("job-status-red")
        elif trim_shop_req_by_date <= enddate:
            state.append("job-status-yellow")

    if jobstatus.cab_assemply_req_by != '' and jobstatus.cab_assemply_req_by != None:
        cab_assemply_req_by_date = datetime.datetime.strptime(jobstatus.cab_assemply_req_by, "%m/%d/%Y")
        if cab_assemply_req_by_date <= today:
            state.append("job-status-red")
        elif cab_assemply_req_by_date <= enddate:
            state.append("job-status-yellow")

    if jobstatus.install_date != '' and jobstatus.install_date != None:
        install_date_date = datetime.datetime.strptime(jobstatus.install_date, "%m/%d/%Y")
        if install_date_date <= today:
            state.append("job-status-red")
        elif install_date_date <= enddate:
            state.append("job-status-yellow")

    if jobstatus.premier_glass != '' and jobstatus.premier_glass != None:
        premier_glass_date = datetime.datetime.strptime(jobstatus.premier_glass, "%m/%d/%Y")
        if premier_glass_date <= today:
            state.append("job-status-red")
        elif premier_glass_date <= enddate:
            state.append("job-status-yellow")

    if jobstatus.tile_installer != '' and jobstatus.tile_installer != None:
        tile_installer_date = datetime.datetime.strptime(jobstatus.tile_installer, "%m/%d/%Y")
        if tile_installer_date <= today:
            state.append("job-status-red")
        elif tile_installer_date <= enddate:
            state.append("job-status-yellow")

    if jobstatus.misc_del != '' and jobstatus.misc_del != None:
        misc_del_date = datetime.datetime.strptime(jobstatus.misc_del, "%m/%d/%Y")
        if misc_del_date <= today:
            state.append("job-status-red")
        elif misc_del_date <= enddate:
            state.append("job-status-yellow")

    if jobstatus.bill != '' and jobstatus.bill != None:
        bill_date = datetime.datetime.strptime(jobstatus.bill, "%m/%d/%Y")
        if bill_date <= today:
            state.append("job-status-red")
        elif bill_date <= enddate:
            state.append("job-status-yellow")

    if jobstatus.hayward != '' and jobstatus.hayward != None:
        hayward_date = datetime.datetime.strptime(jobstatus.hayward, "%m/%d/%Y")
        if hayward_date <= today:
            state.append("job-status-red")
        elif hayward_date <= enddate:
            state.append("job-status-yellow")

    if jobstatus.glenn != '' and jobstatus.glenn != None:
        glenn_date = datetime.datetime.strptime(jobstatus.glenn, "%m/%d/%Y")
        if glenn_date <= today:
            state.append("job-status-red")
        elif glenn_date <= enddate:
            state.append("job-status-yellow")

    if jobstatus.suren != '' and jobstatus.suren != None:
        suren_date = datetime.datetime.strptime(jobstatus.suren, "%m/%d/%Y")
        if suren_date <= today:
            state.append("job-status-red")
        elif suren_date <= enddate:
            state.append("job-status-yellow")

    if jobstatus.roger != '' and jobstatus.roger != None:
        roger_date = datetime.datetime.strptime(jobstatus.roger, "%m/%d/%Y")
        if roger_date <= today:
            state.append("job-status-red")
        elif roger_date <= enddate:
            state.append("job-status-yellow")

    if jobstatus.matt != '' and jobstatus.matt != None:
        matt_date = datetime.datetime.strptime(jobstatus.matt, "%m/%d/%Y")
        if matt_date <= today:
            state.append("job-status-red")
        elif matt_date <= enddate:
            state.append("job-status-yellow")

    if jobstatus.third_party_install != '' and jobstatus.third_party_install != None:
        third_party_install_date = datetime.datetime.strptime(jobstatus.third_party_install, "%m/%d/%Y")
        if third_party_install_date <= today:
            state.append("job-status-red")
        elif third_party_install_date <= enddate:
            state.append("job-status-yellow")

    if "job-status-red" in state:
        return "job-status-red"
    elif "job-status-yellow" in state:
        return "job-status-yellow"
    else:
        return "job-status-green"


def job_list(request):
    # import pdb; pdb.set_trace();
    user = request.user
    from django.core.serializers.json import DjangoJSONEncoder
    today = datetime.date.today()
    enddate = today + datetime.timedelta(days=7)

    jobs = Job.objects.all() #.values('id','jobstatus', 'job_number','cab_designation', 'customer', 'date_opened', 'date_required', 'status', 'job_name', 'number_of_cabs', 'description', 'search_string')
    job_dict_list = []

    for job in jobs:
        job_dict = {}
        job_dict['id'] = job.id
        job_dict['job_number'] = job.job_number
        job_dict['cab_designation'] = job.cab_designation
        job_dict['date_opened'] = job.date_opened
        job_dict['date_required'] = job.date_required
        job_dict['status'] = job.status
        job_dict['customer'] = job.customer
        job_dict['job_name'] = job.job_name
        job_dict['number_of_cabs'] = job.number_of_cabs
        job_dict['description'] = job.description
        job_dict['drawing_req_date'] = job.drawing_req_date
        job_dict['drawing_sent_to_customer_date'] = job.drawing_sent_to_customer_date
        job_dict['search_string'] = job.search_string

        job_dict['permission'] = {}
        job_dict['permission']['can_add_job'] = user.has_perm("schedule.add_job")
        job_dict['permission']['can_view_job'] = user.has_perm("schedule.view_job")
        job_dict['permission']['can_change_job'] = user.has_perm("schedule.change_job")
        job_dict['permission']['can_delete_job'] = user.has_perm("schedule.delete_job")
        # job_status = JobStatus.objects.get(job=)
        job_dict['job_current_state'] = {}
        
        # import pdb; pdb.set_trace();
        if not job.date_opened and not job.date_required:
            job_dict['job_current_state'] = "job-status-white"
        elif job.date_opened and not job.date_required:
            job_dict['job_current_state'] = "job-status-yellow"
        elif job.date_opened and job.date_required:
            state = ''
            if job.date_required <= today:
                job_dict['job_current_state'] = "job-status-red"
            elif job.date_required <= enddate:
                job_dict['job_current_state'] = "job-status-yellow"
            else:
                # job_dict['job_current_state'] = "job-status-green"
                state = getJobStatusState(job.jobstatus)

                if state == 'job-status-red':
                    job_dict['job_current_state'] = "job-status-red"
                elif state == 'job-status-yellow':
                    job_dict['job_current_state'] = "job-status-yellow"
                elif state == 'job-status-green':
                    job_dict['job_current_state'] = "job-status-green"

        # job_dict['job_status']['job_status_id'] = job.jobstatus.pk
        # job_dict['job_status']['fixtures_req_by'] = job.jobstatus.fixtures_req_by
        # job_dict['job_status']['wood_shop_req_by'] = job.jobstatus.wood_shop_req_by
        # job_dict['job_status']['machine_shop_req_by'] = job.jobstatus.machine_shop_req_by
        # job_dict['job_status']['welding'] = job.jobstatus.welding
        # job_dict['job_status']['lacquer'] = job.jobstatus.lacquer
        # job_dict['job_status']['trim_shop_req_by'] = job.jobstatus.trim_shop_req_by
        # job_dict['job_status']['cab_assemply_req_by'] = job.jobstatus.cab_assemply_req_by

        # job_dict['job_status']['install_date'] = job.jobstatus.install_date
        # job_dict['job_status']['premier_glass'] = job.jobstatus.premier_glass
        # job_dict['job_status']['tile_installer'] = job.jobstatus.tile_installer
        # job_dict['job_status']['misc_del'] = job.jobstatus.misc_del
        # job_dict['job_status']['bill'] = job.jobstatus.bill
        # job_dict['job_status']['hayward'] = job.jobstatus.hayward
        # job_dict['job_status']['glenn'] = job.jobstatus.glenn
        # job_dict['job_status']['suren'] = job.jobstatus.suren
        # job_dict['job_status']['roger'] = job.jobstatus.roger
        # job_dict['job_status']['matt'] = job.jobstatus.matt
        # job_dict['job_status']['third_party_install'] = job.jobstatus.third_party_install

        
        job_dict_list.append(job_dict)
    json_posts = json.dumps(job_dict_list, cls=DjangoJSONEncoder)
    return HttpResponse(json_posts, mimetype='application/json')

def job_list_filter(request):
    if request.method == "GET":
        terms = request.GET.get('term','')
        if terms:
            items = Job.objects.filter(job_number__contains=terms) #. 'production_type', 'search_string')
        else:
            items = Job.objects.all()
        inventory_dict_list = []
        for item in items:
            item_dict = {}
            item_dict['id'] = item.id
            item_dict['label'] = item.job_number
            item_dict['value'] = item.job_number
            inventory_dict_list.append(item_dict)

        json_posts = json.dumps(inventory_dict_list)
        return HttpResponse(json_posts, mimetype='application/json')

def my_jobs(request):
    user = request.user
    import json
    from django.core.serializers.json import DjangoJSONEncoder
    jobs = Job.objects.filter(contact_email=request.user.email).values('id','job_number','cab_designation', 'customer', 'date_opened', 'date_required', 'status', 'job_name', 'number_of_cabs', 'description', 'search_string')
    job_dict_list = []
    for job in jobs:
        job['permission'] = {}
        job['permission']['can_add_job'] = user.has_perm("schedule.add_job")
        job['permission']['can_view_job'] = user.has_perm("schedule.view_job")
        job['permission']['can_change_job'] = user.has_perm("schedule.change_job")
        job['permission']['can_delete_job'] = user.has_perm("schedule.delete_job")
        job_dict_list.append(job)
    json_posts = json.dumps(job_dict_list, cls=DjangoJSONEncoder)
    return HttpResponse(json_posts, mimetype='application/json')


@login_required
@permission_required("schedule.add_job")
@csrf_exempt
def add_job(request):
    '''
    Creates a new job model instance.
    '''
    if request.method == "POST":
        # import pdb; pdb.set_trace()
        job_id = request.POST.get("job_id","")
        if job_id != "":
            job = Job.objects.get(id=job_id)
            job_form = JobForm(request.POST, instance=job)
        else:
            job_form = JobForm(request.POST)
        
        if job_form.is_valid():
            job_status = job_form.save()
            # job_status_form = JobStatusForm(request.POST, instance=job_status)
            # job_status_form.save()
            return HttpResponseRedirect("/schedule/job-status/add/%s/" % job_status.id)
        else:
            return render(request, 'schedule/add-job.html', {'jobform': job_form, 'page_title': 'Add Job'})
    else:
        job_form = JobForm()
        # job_status_form = JobStatusForm(request.POST)
        return render(request, 'schedule/add-job.html', {'jobform': job_form, 'page_title': 'Add Job'})

@login_required
@permission_required("schedule.view_job")
def view_job(request, jobid):
    job = Job.objects.get(id=jobid)
    job_status = JobStatus.objects.get(job=job)
    comments = Comment.objects.filter(job_number=job.job_number).order_by("-datetime")
    return render(request, "schedule/view-job.html", 
        {'job': job, 'job_status': job_status, 'comments':comments, 'page_title': 'Job Details', 'job_number': job.job_number})


def view_job_api(request, jobstatusid):
    # user = request.user
    import json
    from django.core.serializers.json import DjangoJSONEncoder
    job_status = JobStatus.objects.get(id=jobstatusid)
    jobid = job_status.job.id

    job = Job.objects.get(id=jobid)
    job_dict = {}
    job_dict['job_id'] = job.id
    job_dict['date_opened'] = job.date_opened
    job_dict['date_required'] = job.date_required
    job_dict['status'] = job.status
    job_dict['customer'] = job.customer
    job_dict['po_number'] = job.po_number
    job_dict['drawing_req_date'] = job.drawing_req_date
    json_job = json.dumps(job_dict, cls=DjangoJSONEncoder)
    return HttpResponse(json_job, mimetype='application/json')


def view_job_api2(request, jobid):
    import json
    from django.core.serializers.json import DjangoJSONEncoder

    job = Job.objects.get(id=jobid)
    job_dict = {}
    job_dict['job_number'] = job.job_number
    job_dict['date_opened'] = job.date_opened
    job_dict['date_required'] = job.date_required
    job_dict['status_id'] = job.jobstatus.id
    # job_dict['customer'] = job.customer
    # job_dict['po_number'] = job.po_number
    job_dict['drawing_req_date'] = job.drawing_req_date
    job_dict['drawing_sent_to_customer_date'] = job.drawing_sent_to_customer_date
    job_dict['drawing_approved_date'] = job.drawing_approved_date
    
    json_job = json.dumps(job_dict, cls=DjangoJSONEncoder)
    return HttpResponse(json_job, mimetype='application/json')

@login_required
@csrf_exempt
@permission_required("schedule.change_job")
def edit_job(request, jobid):
    '''
    Updates a job with job id (jobid)
    '''
    if request.method == "POST":
        # import pdb; pdb.set_trace();
        jobid = request.POST.get("jobid")
        job = Job.objects.get(id=jobid)
        

        job_form = JobEditForm(request.POST, instance=job)
        
        
        if job_form.is_valid():
            job_form.save()
            
    else:
        job = Job.objects.get(id=jobid)
        job_form = JobEditForm(instance=job)
    
    job_status = JobStatus.objects.get(job=job)
    job_status_form = JobStatusForm(instance=job_status)

    comments = Comment.objects.filter(job_number=job.job_number).order_by("-datetime")
    comment_form = CommentForm()
    
    return render(request, 'schedule/edit-job.html', 
            {'jobform': job_form, 'job_status_form': job_status_form, 'jobid': jobid, 'jsid': job_status.id, 'page_title': 'Edit Job',
            'comments': comments, 'comment_form': comment_form, 'job_number': job.job_number})


@csrf_exempt
def copy_job(request, jobid):
    if request.method == "POST":
        job_form = JobForm(request.POST)
        
        if job_form.is_valid():
            job_status = job_form.save()
            job_status_form = JobStatusForm(request.POST, instance=job_status)
            job_status_form.save()
            return HttpResponseRedirect("/schedule/job-status/add/%s/" % job_status.id)
        
            
    else:
        job = Job.objects.get(id=jobid)
        job_form = JobEditForm(instance=job)
        return render(request, 'schedule/copy-job.html', 
            {'jobform': job_form, 'jobid': jobid, 'page_title': 'Copy Job'})



@csrf_exempt
# @permission_required('schedule.delete_job')
def delete_job(request):
    '''
    Delete job of id = jobid. jobid is recieved from ajax call through request object.
    '''
    if request.method == "POST":
        
        jobid = request.POST.get("jobid")
        job = Job.objects.get(id=jobid)
        job_status = JobStatus.objects.get(job=job)
        try:
            job_status.delete()
            job.delete()
            return HttpResponse(jobid)
        except:
            return HttpResponse(jobid)
        

# def view_job(request, jobid):
#     job = Job.objects.get(id=jobid)
#     job_status = JobStatus.objects.get(job=job)

#     return render(request, "schedule/view-job.html", {'job': job, 'job_status': job_status})


def add_job_status(request, jsid):
    job_status = JobStatus.objects.get(id=jsid)

    if request.method == 'POST':
        job_status_form = JobStatusForm(request.POST, instance=job_status)
        if job_status_form.is_valid():
            job_status_form.save()
            return HttpResponseRedirect("/schedule/jobs/#/schedule/all-jobs")
        else:
            return render(request, "schedule/add-job-status.html", {'job_status_form': job_status_form})
    else:
        job_status_form = JobStatusForm(request.POST, instance=job_status)
        return render(request, "schedule/add-job-status.html", {'job_status_form': job_status_form, 'job': job_status.job, 'jsid': jsid})

@csrf_exempt
@login_required
def edit_job_status(request, jsid):
    job_status = JobStatus.objects.get(id=jsid)

    if request.method == 'POST':
        # import pdb; pdb.set_trace();
        
        job_status_form = JobStatusForm(request.POST, instance=job_status)
        if job_status_form.is_valid():
            job_status_form.save()
            # return HttpResponse("hello")
            return render(request, "schedule/edit-job-status.html", {'job_status_form': job_status_form, 'job': job_status.job, 'jsid': jsid})
        else:
            return render(request, "schedule/edit-job-status.html", {'job_status_form': job_status_form})
    else:
        job_status_form = JobStatusForm(instance=job_status)
        return render(request, "schedule/edit-job-status.html", {'job_status_form': job_status_form, 'job': job_status.job, 'jsid': jsid})


def view_job_status_api(request, jobid):
    import json
    from django.core.serializers.json import DjangoJSONEncoder
    job = Job.objects.get(id=jobid)
    job_status = JobStatus.objects.get(job=job)
    
    job_status_dict = {}
    job_status_dict['job_status_id'] = job_status.id

    job_status_dict['fixtures_req_by'] = job_status.fixtures_req_by
    job_status_dict['fixtures_comment'] = job_status.fixtures_comment

    job_status_dict['wood_shop_req_by'] = job_status.wood_shop_req_by
    job_status_dict['wood_shop_req_by_comment'] = job_status.wood_shop_req_by_comment

    job_status_dict['machine_shop_req_by'] = job_status.machine_shop_req_by
    job_status_dict['machine_shop_req_by_comment'] = job_status.machine_shop_req_by_comment

    job_status_dict['welding'] = job_status.welding
    job_status_dict['welding_comment'] = job_status.welding_comment

    job_status_dict['lacquer'] = job_status.lacquer
    job_status_dict['lacquer_comment'] = job_status.lacquer_comment

    job_status_dict['trim_shop_req_by'] = job_status.trim_shop_req_by
    job_status_dict['trim_shop_req_by_comment'] = job_status.trim_shop_req_by_comment

    job_status_dict['cab_assemply_req_by'] = job_status.cab_assemply_req_by
    job_status_dict['cab_assemply_req_by_comment'] = job_status.cab_assemply_req_by_comment

    job_status_dict['install_date'] = job_status.install_date
    job_status_dict['install_date_comment'] = job_status.install_date_comment

    job_status_dict['premier_glass'] = job_status.premier_glass
    job_status_dict['premier_glass_comment'] = job_status.premier_glass_comment

    job_status_dict['tile_installer'] = job_status.tile_installer
    job_status_dict['tile_installer_comment'] = job_status.tile_installer_comment

    job_status_dict['misc_del'] = job_status.misc_del
    job_status_dict['misc_del_comment'] = job_status.misc_del_comment

    job_status_dict['bill'] = job_status.bill
    job_status_dict['bill_comment'] = job_status.bill_comment

    job_status_dict['hayward'] = job_status.hayward
    job_status_dict['hayward_comment'] = job_status.hayward_comment

    job_status_dict['suren'] = job_status.suren
    job_status_dict['suren_comment'] = job_status.suren_comment
    
    job_status_dict['glenn'] = job_status.glenn
    job_status_dict['glenn_comment'] = job_status.glenn_comment

    job_status_dict['roger'] = job_status.roger
    job_status_dict['roger_comment'] = job_status.roger_comment

    job_status_dict['matt'] = job_status.matt
    job_status_dict['matt_comment'] = job_status.matt_comment

    job_status_dict['third_party_install'] = job_status.third_party_install
    job_status_dict['third_party_install_comment'] = job_status.third_party_install_comment

    job_status_dict['tssa_submitted_date'] = job_status.tssa_submitted_date
    job_status_dict['tssa_submitted_date_comment'] = job_status.tssa_submitted_date_comment

    job_status_dict['safety_test_schedule_date'] = job_status.safety_test_schedule_date
    job_status_dict['who_will_test'] = job_status.who_will_test
    job_status_dict['test_comment'] = job_status.test_comment
    
    json_job_status = json.dumps(job_status_dict, cls=DjangoJSONEncoder)
    return HttpResponse(json_job_status, mimetype='application/json')

def view_job_status(request, jsid):
    # import pdb; pdb.set_trace();
    import json
    from django.core.serializers.json import DjangoJSONEncoder
    job_status = JobStatus.objects.get(id=jsid)
    
    job_status_dict = {}
    job_status_dict['job_status_id'] = job_status.id

    job_status_dict['fixtures_req_by'] = job_status.fixtures_req_by
    job_status_dict['fixtures_comment'] = job_status.fixtures_comment

    job_status_dict['wood_shop_req_by'] = job_status.wood_shop_req_by
    job_status_dict['wood_shop_req_by_comment'] = job_status.wood_shop_req_by_comment

    job_status_dict['machine_shop_req_by'] = job_status.machine_shop_req_by
    job_status_dict['machine_shop_req_by_comment'] = job_status.machine_shop_req_by_comment

    job_status_dict['welding'] = job_status.welding
    job_status_dict['welding_comment'] = job_status.welding_comment

    job_status_dict['lacquer'] = job_status.lacquer
    job_status_dict['lacquer_comment'] = job_status.lacquer_comment

    job_status_dict['trim_shop_req_by'] = job_status.trim_shop_req_by
    job_status_dict['trim_shop_req_by_comment'] = job_status.trim_shop_req_by_comment

    job_status_dict['cab_assemply_req_by'] = job_status.cab_assemply_req_by
    job_status_dict['cab_assemply_req_by_comment'] = job_status.cab_assemply_req_by_comment

    job_status_dict['install_date'] = job_status.install_date
    job_status_dict['install_date_comment'] = job_status.install_date_comment

    job_status_dict['premier_glass'] = job_status.premier_glass
    job_status_dict['premier_glass_comment'] = job_status.premier_glass_comment

    job_status_dict['tile_installer'] = job_status.tile_installer
    job_status_dict['tile_installer_comment'] = job_status.tile_installer_comment

    job_status_dict['misc_del'] = job_status.misc_del
    job_status_dict['misc_del_comment'] = job_status.misc_del_comment

    job_status_dict['bill'] = job_status.bill
    job_status_dict['bill_comment'] = job_status.bill_comment

    job_status_dict['hayward'] = job_status.hayward
    job_status_dict['hayward_comment'] = job_status.hayward_comment

    job_status_dict['suren'] = job_status.suren
    job_status_dict['suren_comment'] = job_status.suren_comment
    
    job_status_dict['glenn'] = job_status.glenn
    job_status_dict['glenn_comment'] = job_status.glenn_comment

    job_status_dict['roger'] = job_status.roger
    job_status_dict['roger_comment'] = job_status.roger_comment

    job_status_dict['matt'] = job_status.matt
    job_status_dict['matt_comment'] = job_status.matt_comment

    job_status_dict['third_party_install'] = job_status.third_party_install
    job_status_dict['third_party_install_comment'] = job_status.third_party_install_comment

    job_status_dict['tssa_submitted_date'] = job_status.tssa_submitted_date
    job_status_dict['tssa_submitted_date_comment'] = job_status.tssa_submitted_date_comment

    job_status_dict['safety_test_schedule_date'] = job_status.safety_test_schedule_date
    job_status_dict['who_will_test'] = job_status.who_will_test
    job_status_dict['test_comment'] = job_status.test_comment
    
    json_job_status = json.dumps(job_status_dict, cls=DjangoJSONEncoder)
    return HttpResponse(json_job_status, mimetype='application/json')



@login_required
@permission_required("schedule.view_job")
def total_pending_job(request):
    email = request.user.email
    jobs = Job.objects.filter(contact_email=email)
    return render(request, "schedule/customer-job-list.html", {'jobs': jobs})


@csrf_exempt
@login_required
@permission_required("schedule.add_comment")
def add_comment(request):
    if request.method == 'POST':
        # import pdb; pdb.set_trace();
        comment_form = CommentForm(request.POST)
        # comment = request.POST.get("commnet", "")
        # job_number = request.POST.get("job_number", "")
        # comment_by = request.POST.get("comment_by", "admin")
        if comment_form.is_valid():
            comment = comment_form.save()
            return render(request, "schedule/add-comment-tpl.html", {'comment': comment})



@csrf_exempt
@login_required
@permission_required("schedule.delete_comment")
def delete_comment(request):
    if request.method == 'POST':
        # import pdb; pdb.set_trace();
        comid = request.POST.get("com_id")
        comment = Comment.objects.get(id=comid)
        comment.delete()
        return HttpResponse(comid)



def edit_comment(request, comid):
    comment = Comment.objects.get(id=comid)
    if request.method == 'POST':        
        comment_form = CommentEditForm(request.POST, instance=comment)
        if comment_form.is_valid():
            comment = comment_form.save()
            comment.datetime = datetime.datetime.now()
            comment.comment_by = request.user.username
            comment.save()
            return HttpResponse(comment.id)
    else:
        comment_form = CommentEditForm(instance=comment)
        job_comment = comment.job_comment
        return render(request, "schedule/edit-comment.html", {'comment_form': comment_form, 'comid': comid, 'job_comment': job_comment})


@csrf_exempt
@login_required
def job_reindex(request):
    # import pdb; pdb.set_trace()
    jobs = Job.objects.all()
    for job in jobs:
        job.search_string = job.job_number + " " + job.cab_designation + " " + job.job_name + " " + job.customer + " " + job.status + " " + job.description+ " " + job.address_1 + " " + job.customer_contact_name + " " + job.customer_contact_phone_number
        job.save()
    return HttpResponseRedirect("/")



def job_control_add(request):
    elevetor_types = ElevetorType.objects.all()
    # contacts = Contact.objects.all()
    if request.method == 'POST':
        job_number = request.POST.get("job_number", '')
        if job_number:
            job = JobControl.objects.get(job_number=job_number)
            jc_form = JobControlForm(request.POST, instance=job, action='update')
        else:
            jc_form = JobControlForm(request.POST, action='new')
        if jc_form.is_valid():
            jc = jc_form.save()
            
            return HttpResponseRedirect("/schedule/job-control/list/")
        else:
            return render(request, "schedule/add-job-control.html", 
                {'form': jc_form,'elevetor_types': elevetor_types,})
    else:
        jc_form = JobControlForm()
        return render(request, "schedule/add-job-control.html", 
            {'form': jc_form,'elevetor_types': elevetor_types,})


def job_control_search(request):
    query = request.GET.get('q','')
    if request.GET.get('q'):
        jobs = SearchQuerySet().using('jobcontrol').filter(content=AutoQuery(query)).load_all()[:20]
    else:
        jobs = SearchQuerySet().using('jobcontrol').all().load_all()[:20]

    job_list = []
    if jobs:
        for job in jobs:
            if job != None:
                job_dict = {}
                job_dict['job_number'] = job.job_number
                job_dict['job_name'] = job.job_name
                job_dict['sold_to'] = job.sold_to
                job_dict['ship_to'] = job.ship_to
                job_dict['elevetor_type'] = job.elevetor_type
                job_dict['number_of_cabs'] = job.number_of_cabs
                job_dict['number_of_floors'] = job.number_of_floors
                job_dict['front'] = job.front
                job_dict['rear'] = job.rear
                job_dict['rgw'] = job.rgw

                job_dict['capacity'] = job.capacity
                job_dict['customer_po_number'] = job.customer_po_number
                job_dict['delivery_date'] = job.delivery_date
                job_dict['start_date'] = job.start_date
                job_dict['installed_by'] = job.installed_by
                job_dict['estimated_price_for_job'] = job.estimated_price_for_job
                job_list.append(job_dict)
    try:
        page = int(request.GET.get('page','1'))
    except ValueError:
        page = 1
    paginator = Paginator(job_list, 20)
    try:
        pages = paginator.page(page)
    except (EmptyPage, InvalidPage):
        pages = paginator.page(paginator.num_pages)

    results = pages.object_list

    data = json.dumps(results)
    return HttpResponse(data)


def job_control_list(request):
    return render(request, "schedule/list-job-control.html", {})


def job_control_list_json(request):
    job_controls = JobControl.objects.all()
    jc_list = []
    for jc in job_controls:
        jc_dict = {}
        # jc_dict['id'] = jc.id
        jc_dict['job_number'] = jc.job_number
        if jc.sold_to:
            jc_dict['sold_to'] = jc.sold_to.contact_name
        else:
            jc_dict['sold_to'] = None
        
        if jc.ship_to:
            jc_dict['ship_to'] = jc.ship_to.contact_name
        else:
            jc_dict['ship_to'] = None
        
        if jc.elevetor_type:
            jc_dict['elevetor_type'] = jc.elevetor_type.elevetor_type
        else:
            jc_dict['elevetor_type'] = None

        jc_dict['number_of_floors'] = jc.number_of_floors
        jc_dict['front'] = jc.front
        jc_dict['rear'] = jc.rear
        jc_dict['rgw'] = jc.rgw
        jc_dict['capacity'] = jc.capacity
        jc_dict['customer_po_number'] = jc.customer_po_number
        if jc.delivery_date:
            jc_dict['delivery_date'] = jc.delivery_date.isoformat()

        if jc.start_date:
            jc_dict['start_date'] = jc.start_date.isoformat()

        if jc.installed_by:
            jc_dict['installed_by'] = jc.installed_by.contact_name
        jc_dict['job_name'] = jc.job_name

        if jc.estimated_price_for_job:
            jc_dict['estimated_price_for_job'] = float(jc.estimated_price_for_job)
        jc_dict['search_string'] = jc.search_string

        jc_list.append(jc_dict)

    jc_json = json.dumps(jc_list)

    return HttpResponse(jc_json, mimetype='application/json')


def elevetor_type_add(request):
    if request.method == 'POST':
        # import pdb; pdb.set_trace();
        et_form = ElevetorTypeForm(request.POST)
        if et_form.is_valid():
            et = et_form.save()
            return HttpResponseRedirect("/schedule/elevetor-type/list/")
        else:
            return render(request, "schedule/add-elevetor-type.html", 
                {'form': et_form})
    else:
        et_form = ElevetorTypeForm()
        return render(request, "schedule/add-elevetor-type.html", 
            {'form': et_form})


def elevetor_type_list(request):
    elevetor_types = ElevetorType.objects.all()
    return render(request, "schedule/elevetor-type-list.html", {'elevetor_types': elevetor_types})

@csrf_exempt
def elevetor_type_delete(request):
    et_id = request.POST.get("et_id")
    et = ElevetorType.objects.get(id=et_id)
    et.delete()
    return HttpResponse(et_id)

def job_control_edit(request, jobid):
    pass