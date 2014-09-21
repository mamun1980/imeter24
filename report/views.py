from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from report.models import *
from report.forms import *

# Create your views here.
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required

# @csrf_exempt
# def add_printer(request):
#     if request.method == "POST":
#         printer_name = request.POST.get("printer_name")
#         try:
#             printer = Printer.objects.create(printer_name=printer_name, is_active=True)
#             return render(request, "report/printer/add-printer-partial.html",
#                 {'printer': printer})
#         except:
#             return HttpResponse("error")
#     else:

#         printers = Printer.objects.all()
#         printer_form = PrinterForm()

#         return render(request, "report/printer/add-list-printer.html",
#             {'printers': printers, 'printer_form': printer_form})

@login_required
@permission_required("report.change_printer")
@csrf_exempt
def edit_printer(request, printer_id):
    if request.method == "POST":
        printer_id = request.POST.get("printer_id")
        printer = Printer.objects.get(printer_id=printer_id)
        printer_form = PrinterEditForm(request.POST, instance=printer)
        if printer_form.is_valid():
            printer = printer_form.save()
            return HttpResponse(printer_id)
    elif request.method == "GET":
        printer = Printer.objects.get(printer_id=printer_id)
        printer_form = PrinterEditForm(instance=printer)

        return render(request, "report/printer/edit-printer-tmpl.html",
            {'printer_form': printer_form, 'printer_id': printer_id})

@login_required
@permission_required("report.view_printerv2")
def view_printer(request, printer_id):
    printer = PrinterV2.objects.get(printer_id=printer_id)
    return render(request, "report/printerv2/printer-details.html", 
        {'printer': printer, 'page_title': 'Printer Details'})



@login_required
@csrf_exempt
def delete_printer(request):
    if request.method == "POST":
        printer_id = request.POST.get("printer_id")
        printer = Printer.objects.get(printer_id=printer_id)
        printer.delete()
        return HttpResponse(printer_id)
    else:
        return HttpResponse("Hello World!")



def list_printer(request):
    printers = Printer.objects.all()
    return render(request, "report/printer/list-printer.html", {'printers': printers, 'page_title': 'List Printer'})



def list_printer_api(request):
    import json
    printers = Printer.objects.all().values("printer_id", "printer_type")
    printer_dict_list = []
    for printer in printers:
        printer_dict_list.append(printer)
    json_printers = json.dumps(printer_dict_list)
    return HttpResponse(json_printers, mimetype='application/json')

# @csrf_exempt
# @login_required
# @permission_required("report.add_reporttype")
# def add_report_type(request):
#     if request.method == "POST":
#         report_type = request.POST.get("report_type")
#         try:
#             report_type = ReportType.objects.create(report_type=report_type, is_active=True)
#             return render(request, "report/report-type/add-report-type-partial.html",
#                 {'report_type': report_type})
#         except:
#             return HttpResponse("error")
#     else:
#         report_types = ReportType.objects.all()
#         report_type_form = ReportTypeForm()

#         return render(request, "report/report-type/add-list-report-tyep.html",
#             {'report_types': report_types, 'report_type_form': report_type_form, 'page_title': 'Add Report Type'})


@login_required
@permission_required("report.change_reporttype")
@csrf_exempt
def edit_report_type(request, report_type_id):
    if request.method == "POST":
        report_type_id = request.POST.get("report_type_id")
        report_type = ReportType.objects.get(id=report_type_id)
        reprot_type_form = ReportTypeForm(request.POST, instance=report_type)
        if reprot_type_form.is_valid():
            report_type = reprot_type_form.save()
            return render(request, "report/report-type/add-report-type-partial.html",
            {'report_type': report_type})
    elif request.method == "GET":
        report_type = ReportType.objects.get(id=report_type_id)
        reprot_type_form = ReportTypeForm(instance=report_type)

        return render(request, "report/report-type/edit-report-type-tmpl.html",
            {'reprot_type_form': reprot_type_form, 'report_type_id': report_type_id})


def list_report_type(request):
    reports = Report.objects.all()
    return render(request, "report/list-report.html", {'reports': reports, 'page_title': 'List Report'})

@csrf_exempt
@login_required
@permission_required("report.delete_report")
def delete_report_type(request):
    if request.method == "POST":
        report_type_id = request.POST.get("report_type_id")
        report_type = ReportType.objects.get(id=report_type_id)
        report_type.delete()
        return HttpResponse(report_type_id)
    else:
        return HttpResponse("Hello World!")


@csrf_exempt
def add_printer(request):
    if request.method == "POST":
        printer_form = PrinterForm(request.POST)
        if printer_form.is_valid():
            printer_form.save()
            return HttpResponseRedirect("/report/printer/list/")
        else:
            return render(request, "report/printer/add-printer.html", {'printer_form': printer_form})
    else:
        printer_form = PrinterForm()
        return render(request, "report/printer/add-printer.html", {'printer_form': printer_form})

def printer(request):
    printers = Printer.objects.all()
    return render(request, "report/printer/list-printer.html", {'printers': printers, 'page_title': 'Add Printer'})


@login_required
@permission_required("report.add_report")
@csrf_exempt
def add_report(request):
    if request.method == 'POST':
        report_form = ReportForm(request.POST)
        if report_form.is_valid():
            report_form.save()
            return HttpResponseRedirect("/report/list/")
        else:
            return render(request, "report/add-report.html", {'report_form': report_form, 'page_title': 'Add Report'})
    else:
        report_form = ReportForm(request.POST)
        return render(request, "report/add-report.html", {'report_form': report_form, 'page_title': 'Add Report'})


def list_report(request):
    reports = Report.objects.all()
    return render(request, "report/list-report.html", {'reports': reports, 'page_title': 'Add Report'})

def list_report_api(request):
    import json
    reports = Report.objects.all().values("id", "report_type")
    report_dict_list = []
    for report in reports:
        report_dict_list.append(report)
    json_reports = json.dumps(report_dict_list)
    return HttpResponse(json_reports, mimetype='application/json')

@login_required
@permission_required("report.delete_report")
@csrf_exempt
def delete_report(request):
    if request.method == 'POST':
        rid = request.POST.get('report_id')
        report = Report.objects.get(id=rid)
        try:
            report.delete()
            return HttpResponse(rid)
        except Exception, e:
            raise
    else:
        return HttpResponse("no delete")

@csrf_exempt
@login_required
@permission_required('report.change_report')
def edit_report(request, id):
    if request.method == 'POST':
        report = Report.objects.get(id=id)
        report_form = ReportForm(request.POST, instance=report)
        if report_form.is_valid():
            report_form.save()
            return HttpResponseRedirect("/report/list/")
        else:

            return render(request, "report/edit-report.html", {'report_form': report_form, 'page_title': 'Edit Report'})
    else:
        report = Report.objects.get(id=id)
        report_form = ReportForm(instance=report)
        return render(request, "report/edit-report.html", {'report_form': report_form, 'report_id': id, 'page_title': 'Edit Report'})


def report_details(request, id):
    report = Report.objects.get(id=id)
    return render(request, "report/report-details.html", {'report': report, 'report_id': id, 'page_title': 'Report Details'})

def report_details_api(request, id):
    import json
    from django.core.serializers.json import DjangoJSONEncoder
    job = Report.objects.get(id=id)
    job_dict = {}
    job_dict['id'] = job.id
    job_dict['report_type'] = job.report_type
    # if job.printer:
    #     job_dict['printer'] = job.printer.printer_id
    # else:
    #     job_dict['printer'] = ""

    # job_dict['destination_type'] = job.destination_type
    
    job_dict['comments'] = job.comments
    job_dict['python_script'] = job.python_script
    

    data = json.dumps(job_dict, cls=DjangoJSONEncoder)
    return HttpResponse(data, mimetype='application/json')



def report_view(request):
    if request.method == "POST":
        report_id = request.POST.get("autocomplete")
        return HttpResponseRedirect("/report/view/%s/" % report_id )

@login_required
@csrf_exempt
@permission_required("report.add_recuringreport")
def add_recuring_report(request):
    if request.method == "POST":
        rrform = RecuringReportForm(request.POST)
        if rrform.is_valid():
            rreport = rrform.save()
            # rreport.schedule_type = request.POST.get('schedule_type',"")
            # rreport.week_day = request.POST.get('week_day',"")
            # rreport.randomdays = request.POST.get('randomdays',"")
            # rreport.daytime = request.POST.get('daytime',"")
            rreport.save()

            return HttpResponseRedirect("/report/lists/#/report/recuring-job-list")
    else:
        rrform = RecuringReportForm()

    return render(request, "report/add-recuring-report2.html", {'rrform': rrform})



@login_required
@csrf_exempt
@permission_required("report.add_singlereport")
def add_single_report(request):
    if request.method == "POST":
        # import pdb; pdb.set_trace();
        rrform = SingleReportForm(request.POST)
        if rrform.is_valid():
            rreport = rrform.save()
            # rreport.schedule_type = request.POST.get('schedule_type',"")
            # rreport.week_day = request.POST.get('week_day',"")
            # rreport.randomdays = request.POST.get('randomdays',"")
            # rreport.daytime = request.POST.get('daytime',"")
            rreport.save()

            return HttpResponseRedirect("/report/lists/#/report/single-job-list")
    else:
        rrform = SingleReportForm()

    return render(request, "report/add-single-report.html", {'rrform': rrform})


@login_required
@permission_required("report.view_singlereport")
def view_single_report(request, id):
    job = SingleReport.objects.get(id=id)
    return render(request, "report/single-job-details.html", {'job': job})


@csrf_exempt
@login_required
@permission_required("report.change_singlereport")
def edit_single_report(request, id):
    job = SingleReport.objects.get(id=id)
    if request.method == "POST":
        # import pdb; pdb.set_trace();
        job_form = SingleReportForm(request.POST, instance=job)
        if job_form.is_valid():
            job = job_form.save()
            job.que_type = request.POST.get("que_type", "")

            if job.que_type == 'email':
                job.email = request.POST.get("email","")
                job.printer = None
                job.fax = None
            elif job.que_type == 'printer':
                job.email = None
                printer_id = request.POST.get("printer","")
                printer = Printer.objects.get(printer_id=printer_id)
                job.printer = printer
                job.fax = None
            elif job.que_type == 'fax':
                job.email = None
                job.printer = None
                job.fax = request.POST.get("fax","")

            # job.search_start_date = request.POST.get("search_start_date", "")
            # job.search_end_date = request.POST.get("search_end_date", "")
            job.search_string = request.POST.get("search_string", "")
            # # job.search_status_type = request.POST.get("search_status_type", "")


            job.save()


            
            return HttpResponseRedirect("/report/lists/#/report/single-job-list")
    else:
        job_form = SingleReportForm(instance=job)

    return render(request, "report/single-job-edit.html", {'job_form': job_form, 'job_id': id})


def single_report_api(request, jobid):
    # import pdb; pdb.set_trace();
    import json
    from django.core.serializers.json import DjangoJSONEncoder
    job = SingleReport.objects.get(id=jobid)
    job_dict = {}
    job_dict['id'] = job.id
    
    job_dict['report'] = {}
    job_dict['report']['id'] = job.report.id
    job_dict['report']['report_type'] = job.report.report_type
    job_dict['report']['destination_type'] = job.report.destination_type
    job_dict['report']['comments'] = job.report.comments
    job_dict['report']['python_script'] = job.report.python_script
    

    job_dict['report_description'] = job.report_description
    job_dict['script_name'] = job.script_name
    job_dict['que_type'] = job.que_type
    if job.que_type == 'email':
        job_dict['email'] = job.email
        job_dict['printer'] = None
        job_dict['fax'] = None
    elif job.que_type == 'printer':
        job_dict['email'] = None
        job_dict['printer'] = job.printer.printer_id
        job_dict['fax'] = None
    elif job.que_type == 'fax':
        job_dict['email'] = None
        job_dict['printer'] = None
        job_dict['fax'] = job.fax

    job_dict['current_job_status'] = job.current_job_status
    job_dict['date_submitted'] = job.date_submitted
    job_dict['time_submitted'] = job.time_submitted
    job_dict['date_finished'] = job.date_finished
    job_dict['time_finished'] = job.time_finished

    job_dict['search_start_date'] = job.search_start_date
    job_dict['search_end_date'] = job.search_end_date
    job_dict['search_string'] = job.search_string
    job_dict['search_status_type'] = job.search_status_type



    data = json.dumps(job_dict, cls=DjangoJSONEncoder)
    return HttpResponse(data, mimetype='application/json')


@csrf_exempt
@login_required
@permission_required("report.delete_singlereport")
def delete_single_report(request):
    if request.method == "POST":
        id = request.POST.get('id')
        job = SingleReport.objects.get(id=id)
        job.delete()
        return HttpResponse(id)

def recuring_report_list(request):
    return render(request, "report/list-recuring-report.html", {})

@login_required
@permission_required("report.view_recuringreport")
def view_recuring_report(request, id):
    job = RecuringReport.objects.get(id=id)
    return render(request, "report/recuring-job-details.html", {'job': job})

@login_required
@permission_required("report.change_recuringreport")
@csrf_exempt
def edit_recuring_report(request, id):
    job = RecuringReport.objects.get(id=id)
    if request.method == "POST":
        # import pdb; pdb.set_trace()
        job_form = RecuringReportForm(request.POST, instance=job)
        if job_form.is_valid():
            job = job_form.save()
            job.que_type = request.POST.get("que_type", "")

            if job.que_type == 'email':
                job.email = request.POST.get("email","")
                job.printer = None
                job.fax = None
            elif job.que_type == 'printer':
                job.email = None
                printer_id = request.POST.get("printer","")
                printer = Printer.objects.get(printer_id=printer_id)
                job.printer = printer
                job.fax = None
            elif job.que_type == 'fax':
                job.email = None
                job.printer = None
                job.fax = request.POST.get("fax","")


            job.schedule_type = request.POST.get("schedule_type","")
            if job.schedule_type == 'weekly':
                job.week_day = request.POST.get("week_day","")
                job.randomdays = ""
            elif job.schedule_type == 'randomdays':
                job.randomdays = request.POST.get("randomdays","")
                job.week_day = ""
            else:
                job.randomdays = ""
                job.week_day = ""


            job.daytime = request.POST.get("daytime","")
            job.save()
            return HttpResponseRedirect("/report/lists/#/report/recuring-job-list")
    else:
        job_form = RecuringReportForm(instance=job)

    return render(request, "report/recuring-job-edit2.html", {'job_form': job_form, 'job_id': id})

@login_required
@permission_required("report.delete_recuringreport")
@csrf_exempt
def delete_recuring_report(request):
    if request.method == "POST":
        id = request.POST.get('id')
        job = RecuringReport.objects.get(id=id)
        job.delete()
        return HttpResponse(id)

def recuring_job_json(request, id):

    import json
    from django.core.serializers.json import DjangoJSONEncoder
    job = RecuringReport.objects.get(id=id)
    job_dict = {}
    job_dict['id'] = job.id
    
    job_dict['report'] = {}
    job_dict['report']['id'] = job.report.id
    job_dict['report']['report_type'] = job.report.report_type
    job_dict['report']['destination_type'] = job.report.destination_type
    job_dict['report']['comments'] = job.report.comments
    job_dict['report']['python_script'] = job.report.python_script
    

    job_dict['report_description'] = job.report_description
    job_dict['script_name'] = job.script_name
    job_dict['que_type'] = job.que_type
    if job.que_type == 'email':
        job_dict['email'] = job.email
        job_dict['printer'] = None
        job_dict['fax'] = None
    elif job.que_type == 'printer':
        job_dict['email'] = None
        job_dict['printer'] = job.printer.printer_id
        job_dict['fax'] = None
    elif job.que_type == 'fax':
        job_dict['email'] = None
        job_dict['printer'] = None
        job_dict['fax'] = job.fax

    job_dict['current_job_status'] = job.current_job_status
    job_dict['date_submitted'] = job.date_submitted
    job_dict['time_submitted'] = job.time_submitted
    job_dict['date_finished'] = job.date_finished
    job_dict['time_finished'] = job.time_finished

    job_dict['unix_que'] = job.unix_que
    job_dict['schedule_type'] = job.schedule_type
    job_dict['week_day'] = job.week_day
    job_dict['randomdays'] = job.randomdays
    job_dict['daytime'] = job.daytime

    data = json.dumps(job_dict, cls=DjangoJSONEncoder)
    return HttpResponse(data, mimetype='application/json')



@login_required
@permission_required("report.view_recuringreport")
def list_recuring_job(request):
    # import pdb; pdb.set_trace();
    user = request.user
    from django.core.serializers.json import DjangoJSONEncoder
    import json
    jobs = RecuringReport.objects.all()
    report_dict_list = []

    for job in jobs:
        job_dict = {}
        job_dict['id'] = job.pk

        job_dict['permission'] = {}
        job_dict['permission']['can_add_recuringreport'] = user.has_perm("report.add_recuringreport")
        job_dict['permission']['can_view_recuringreport'] = user.has_perm("report.view_recuringreport")
        job_dict['permission']['can_change_recuringreport'] = user.has_perm("report.change_recuringreport")
        job_dict['permission']['can_delete_recuringreport'] = user.has_perm("report.delete_recuringreport")

        if job.report:
            job_dict['report'] = {}
            job_dict['report']['report_type'] = job.report.report_type
            job_dict['report']['destination_type'] = job.report.destination_type
            job_dict['report']['comments'] = job.report.comments
            job_dict['report']['python_script'] = job.report.python_script
            job_dict['report']['search_string'] = job.report.search_string

        job_dict['report_description'] = job.report_description
        job_dict['comment'] = job.comment
        job_dict['script_name'] = job.script_name
        job_dict['que_type'] = job.que_type
        if job.que_type == 'email':
            job_dict['email'] = job.email
            job_dict['printer'] = None
            job_dict['fax'] = None
        elif job.que_type == 'printer':
            job_dict['email'] = None
            job_dict['printer'] = job.printer.printer_id
            job_dict['fax'] = None
        elif job.que_type == 'fax':
            job_dict['email'] = None
            job_dict['printer'] = None
            job_dict['fax'] = job.fax
        job_dict['current_job_status'] = job.current_job_status
        job_dict['date_submitted'] = job.date_submitted
        job_dict['time_submitted'] = job.time_submitted
        job_dict['date_finished'] = job.date_finished
        job_dict['time_finished'] = job.time_finished


        job_dict['unix_que'] = job.unix_que
        job_dict['schedule_type'] = job.schedule_type
        job_dict['week_day'] = job.week_day
        job_dict['randomdays'] = job.randomdays
        job_dict['daytime'] = job.daytime
        job_dict['search_string'] = job.search_string
        report_dict_list.append(job_dict)

    data = json.dumps(report_dict_list, cls=DjangoJSONEncoder)
    return HttpResponse(data, mimetype='application/json')

def list_single_job(request):
    user = request.user
    from django.core.serializers.json import DjangoJSONEncoder
    import json
    jobs = SingleReport.objects.all()
    report_dict_list = []

    for job in jobs:
        job_dict = {}
        job_dict['id'] = job.pk

        job_dict['permission'] = {}
        job_dict['permission']['can_add_singlereport'] = user.has_perm("report.add_sinlgereport")
        job_dict['permission']['can_view_singlereport'] = user.has_perm("report.view_singlereport")
        job_dict['permission']['can_change_singlereport'] = user.has_perm("report.change_singlereport")
        job_dict['permission']['can_delete_singlereport'] = user.has_perm("report.delete_singlereport")

        if job.report:
            job_dict['report'] = {}
            job_dict['report']['report_type'] = job.report.report_type
            job_dict['report']['destination_type'] = job.report.destination_type
            job_dict['report']['comments'] = job.report.comments
            job_dict['report']['python_script'] = job.report.python_script
            job_dict['report']['search_string'] = job.report.search_string

        job_dict['report_description'] = job.report_description
        job_dict['script_name'] = job.script_name
        job_dict['que_type'] = job.que_type
        if job.que_type == 'email':
            job_dict['email'] = job.email
            job_dict['printer'] = None
            job_dict['fax'] = None
        elif job.que_type == 'printer':
            job_dict['email'] = None
            job_dict['printer'] = job.printer.printer_id
            job_dict['fax'] = None
        elif job.que_type == 'fax':
            job_dict['email'] = None
            job_dict['printer'] = None
            job_dict['fax'] = job.fax
        job_dict['current_job_status'] = job.current_job_status
        job_dict['date_submitted'] = job.date_submitted
        job_dict['time_submitted'] = job.time_submitted
        job_dict['date_finished'] = job.date_finished
        job_dict['time_finished'] = job.time_finished


        job_dict['search_start_date'] = job.search_start_date
        job_dict['search_end_date'] = job.search_end_date
        job_dict['search_string'] = job.search_string
        job_dict['search_status_type'] = job.search_status_type

        report_dict_list.append(job_dict)

    data = json.dumps(report_dict_list, cls=DjangoJSONEncoder)
    return HttpResponse(data, mimetype='application/json')


def list_report_job(request):
    user = request.user
    from django.core.serializers.json import DjangoJSONEncoder
    import json
    reports = Report.objects.all()
    report_dict_list = []
    for report in reports:
        report_dict = {}
        report_dict['id'] = report.pk
        if report.report_type:
            report_dict['report_type'] = report.report_type.report_type
        # if report.printer:
        #     report_dict['printer'] = report.printer.printer_id
        # report_dict['destination_type'] = report.destination_type
        
        report_dict['comments'] = report.comments
        report_dict['python_script'] = report.python_script
        
        report_dict['search_string'] = report.search_string

        report_dict['permission'] = {}
        report_dict['permission']['can_add_report'] = user.has_perm("report.add_report")
        report_dict['permission']['can_view_report'] = user.has_perm("report.view_report")
        report_dict['permission']['can_change_report'] = user.has_perm("report.change_report")
        report_dict['permission']['can_delete_report'] = user.has_perm("report.delete_report")
        report_dict_list.append(report_dict)

    data = json.dumps(report_dict_list, cls=DjangoJSONEncoder)
    return HttpResponse(data, mimetype='application/json')








