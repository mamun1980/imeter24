from django.shortcuts import render, render_to_response
from django.http import HttpRequest, HttpResponseRedirect, HttpResponse
from django.contrib import messages
from purchase.forms import *
from purchase.models import *
from premierelevator.models import SystemVariable
# Create your views here.
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
import json
from decimal import Decimal
import datetime
from django.template.loader import get_template, render_to_string
from django.template import Context
import ho.pisa as pisa
import cStringIO as StringIO
import logging
import sys
import os
# import reportlab
# from reportlab.pdfgen import canvas
# from reportlab.lib.pagesizes import letter, A4
# from premierelevator.generate_report import write_pdf

from haystack.forms import ModelSearchForm, SearchForm
from haystack.query import SearchQuerySet, EmptySearchQuerySet
from haystack.views import SearchView
from haystack.inputs import Raw, Clean, AutoQuery
import re
import time
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from purchase.serializer import *


@csrf_exempt
def call_number(request, number, ext):
    # import pdb; pdb.set_trace();
    output = str(number)+":"+str(ext)
    phone = str(number)
    if ext != '0':
        phone += '-ext-'+str(ext)

    domain = request.get_host()
    if domain == '127.0.0.1:8000':
        filename = '/home/mamun/paul_asterisk/'+str(time.time())+'_'+phone+".call"
    else:
        filename = '/rmt/asterisk/var/spool/asterisk/outgoing/temp_'+phone+".call"
    f = open (filename,'w')
    f.write ('Channel: DAHDI/g0/6478399800\n')
    f.write ('CallerID: "SCOM Temp Alarm" <8009991001>\n')
    f.write ('Application: Playback\n')
    f.write ('Data: custom/temp_warning \n')
    f.write ('MaxRetries: 5\n')
    f.write ('RetryTime: 30\n')
    f.close()
    return HttpResponse(output)


def html_to_pdf_response(html):
    result = StringIO.StringIO()
    pdf = pisa.pisaDocument(
            StringIO.StringIO(html.encode("UTF-8")),
            result
    )

    if not pdf.err:
        return HttpResponse(
                result.getvalue(),
                mimetype='application/pdf'
        )
    else:
        return HttpResponse('We had some errors')
def generate_po(request, po_id):
    
    resource_directory = os.path.dirname(os.path.dirname(__file__))
    po = PurchaseOrder.objects.get(po_number=po_id)
    purchase_items = PurchaseItem.objects.filter(po=po)
    rendered_html = render_to_string("purchase/po-report.html", locals())
    return html_to_pdf_response(rendered_html)
    # po = PurchaseOrder.objects.get(id=po_id)
    # return write_pdf('purchase/po-report.html',{
    #     'pagesize' : 'A4',
    #     'po' : po})
    
def preview_generete_po(request, po_id):
    # import pdb; pdb.set_trace();
    po = PurchaseOrder.objects.get(po_number=po_id)
    purchase_items = PurchaseItem.objects.filter(po=po)
    return render(request, "purchase/po-report.html", 
        {'po': po, 'items': purchase_items})

def generate_sl(request, sl_number):
    # import pdb; pdb.set_trace()
    resource_directory = os.path.dirname(os.path.dirname(__file__))
    sl = ShippingList.objects.get(sl_number=sl_number)
    shipping_items = ShippingItem.objects.filter(shipping_list=sl)
    rendered_html = render_to_string("purchase/sl-report.html", locals())
    return html_to_pdf_response(rendered_html)

def preview_generete_sl(request, sl_number):
    # import pdb; pdb.set_trace()
    sl = ShippingList.objects.get(sl_number=sl_number)
    shipping_items = ShippingItem.objects.filter(shipping_list=sl)
    return render(request, "purchase/sl-report.html", 
        {'sl': sl, 'shipping_items': shipping_items})


def generate_pl(request, pl_number):
    # import pdb; pdb.set_trace()
    resource_directory = os.path.dirname(os.path.dirname(__file__))
    pl = PackingList.objects.get(pl_number=pl_number)
    packing_items = PackingItem.objects.filter(pl=pl)
    rendered_html = render_to_string("purchase/pl-report.html", locals())
    return html_to_pdf_response(rendered_html)

def preview_generete_pl(request, pl_id):
    # import pdb; pdb.set_trace()
    pl = PackingList.objects.get(id=pl_id)
    packing_items = PackingItem.objects.filter(pl=pl)
    return render(request, "purchase/pl-report.html", 
        {'pl': pl, 'packing_items': packing_items})

def generate_invoice_pdf(request, invoice_number):
    resource_directory = os.path.dirname(os.path.dirname(__file__))
    invoice = Invoice.objects.get(invoice_number=invoice_number)
    invoice_items = InvoicedItem.objects.filter(invoice=invoice)
    # return render_to_response("purchase/invoice/invoice-report.html", {"invoice": invoice, 'invoice_items': invoice_items})
    rendered_html = render_to_string("purchase/invoice/invoice-report.html", locals())
    return html_to_pdf_response(rendered_html)

@login_required
@permission_required("purchase.add_purchaserequest")
@csrf_exempt
def add_purchase_request(request):

    if request.method == 'POST':
        pr_add_form = PRAddForm(request.POST)
        
        if pr_add_form.is_valid():
            pr = pr_add_form.save()
            pr.status = 0           
            pr.requeste_created_at = datetime.now()
            pr.approved_qty = 0.0
            pr.save()

            #  Update Inventory Item ========
            item = pr.item
            item.qty_on_request = item.qty_on_request + pr.order_qty
            item.save()
            
            return HttpResponseRedirect("/purchase/list-purchase-requests/")

    else:
 
        users = User.objects.all().exclude(id=-1)
        
        if not request.user.is_superuser:
            lock_requested_user = True
        else:
            lock_requested_user = False

        return render(request, "purchase/add_pr.html", 
            {'users': users, 'lock_requested_user': lock_requested_user})


@login_required
@permission_required("purchase.view_purchase_request")
@csrf_exempt
def list_purchase_request(request):
    pr_list = PurchaseRequest.objects.all().order_by("-requeste_created_at")
    return render(request, "purchase/pr-list.html", {'pr_list': pr_list})

@login_required
def list_approved_pr(request):
    pr_list = RequestItem.objects.all().order_by("-approved_date")
    return render(request, "purchase/pr-approved-list.html", {'pr_list': pr_list})

@login_required
@permission_required("purchase.view_purchase_request")
@csrf_exempt
def view_purchase_request(request, pk):
    pr = PurchaseRequest.objects.get(pk=pk)
    prc_form = PRCAddForm()
    prc = PurchaseRequestComment.objects.filter(purchase_request=pr).order_by("-commnet_date")
    return render(request, "purchase/pr-view.html", {'pr': pr, 'prc_form': prc_form, 'comments': prc})

@login_required
@permission_required("purchase.approve_purchase_request")
@csrf_exempt
def approve_purchase_request(request, pk):
    pr = PurchaseRequest.objects.get(pk=pk)
    if request.method == 'POST':
        # import pdb; pdb.set_trace();
        if pr.approved_qty:
            approved_qty = pr.approved_qty
        else:
            approved_qty = 0
        new_approved_qty = request.POST.get("approved_qty","")
        pr_approve_form = PRApproveForm(request.POST, instance=pr)
        comment = request.POST.get('comment','')
        prc = PurchaseRequestComment(
            purchase_request = pr,
            comment = comment,
            commnet_date = datetime.now(),
            user_commented = request.user
        )
        if pr_approve_form.is_valid():
            pr = pr_approve_form.save()

            if approved_qty:
                total_approved_qty = approved_qty + pr.approved_qty
            else:
                total_approved_qty = pr.approved_qty
            if total_approved_qty >= pr.order_qty:
                pr.approved_qty = pr.order_qty
                pr.status = 1
                new_approved_qty = pr.approved_qty - approved_qty
            elif total_approved_qty < pr.order_qty:
                pr.approved_qty = total_approved_qty
                pr.status = 2
            pr.approved_date = datetime.now()
            
            pr.save()
            prc.save()

            # Add request item
            ri = RequestItem(pr=pr, item=pr.item)
            ri.approved_qty = new_approved_qty
            ri.approved_date = pr.approved_date
            ri.status = 0
            ri.save()
            

            # Create PO 
            # import pdb; pdb.set_trace();
            sv = SystemVariable.objects.get(id=1)
            new_po_number = sv.get_next_po_number
            po = PurchaseOrder.objects.create(po_number=new_po_number)
            po.date_issued = datetime.now()
            po.po_created_by = request.user
            po.fob = 'Oshawa, Ontario, Canada'
            po.po_status = 'New'
            po.save_final_draft = 1
            po.supplier = pr.item.primary_supplier
            po.save()

            # import pdb; pdb.set_trace();
            pi = PurchaseItem.objects.create(po=po)
            pi.item = pr.item
            pi.qty = new_approved_qty
            pi.cost = pr.item.wholesale_cost
            pi.sub_total = pr.item.wholesale_cost * Decimal(new_approved_qty)
            po.total_po_amount = pi.sub_total
            po.save()
            pi.comment = pr.description
            pi.purchase_status = 0
            pi.save()

            # Update Inventory item
            item = pr.item

            if item.qty_on_request:
                item.qty_on_request = item.qty_on_request - Decimal(new_approved_qty)
            else:
                item.qty_on_request = 0.0
            if item.quantity_on_order:
                item.quantity_on_order = item.quantity_on_order + Decimal(new_approved_qty)
            else:
                item.quantity_on_order = Decimal(new_approved_qty)

            item.max_order_qty_remains = item.max_order_qty_remains - Decimal(new_approved_qty)

            item.save()

                  

        return HttpResponse(pk)
    else:
        pr_approve_form = PRApproveForm(instance=pr)
        pr_com_form = PRCAddForm()
        return render(request, "purchase/pr-approve.html", 
            {'pr_approve_form': pr_approve_form, 'pr_com_form': pr_com_form, 'pr': pr})

@csrf_exempt
def declien_purchase_request(request):
    if request.method == 'POST':
        pr_id = request.POST.get('pr_id')
        pr = PurchaseRequest.objects.get(id=pr_id)
        pr.status = 3
        pr.save()
        item = pr.item
        item.qty_on_request = item.qty_on_request - (pr.order_qty - pr.approved_qty)
        item.save()
        return HttpResponse(pr_id)

@csrf_exempt
def onhold_purchase_request(request):
    if request.method == 'POST':
        pr_id = request.POST.get('pr_id')
        pr = PurchaseRequest.objects.get(id=pr_id)
        pr.status = 4
        pr.save()
        return HttpResponse(pr_id)

@csrf_exempt
@login_required
# @permission_required("")
def request_item_delete(request):
    ri_id = request.POST.get("id")
    ri = RequestItem.objects.get(id=ri_id)
    if ri.status not in ['1', '2']:
        pr = ri.pr
        pr.approved_qty = pr.approved_qty - ri.approved_qty
        if pr.approved_qty == 0:
            pr.status = 0
        else:
            pr.status = 2
        pr.save()
        ri.delete()
        return HttpResponse('delete')
    else:
        return HttpResponse("Item added to PO can't be deleted.")



@login_required
def list_ri_json(request):
    user = request.user
    request_items = RequestItem.objects.filter(status__lt=2)
    ri_list = []
    for request_item in request_items:
        item = request_item.item
        item_dict = {}
        item_dict['item_id'] = request_item.id
        item_dict['item_number'] = item.item_number
        item_dict['label'] = item.item_number
        item_dict['approved_qty'] = float(request_item.approved_qty)
        item_dict['approved_date'] = request_item.approved_date.isoformat()
        item_dict['total_po_qty'] = float(request_item.total_po_qty)
        item_dict['description'] = item.description
        if item.wholesale_cost:
            item_dict['wholesale_cost'] = item.wholesale_cost.to_eng_string()
        else:
            item_dict['wholesale_cost'] = 0.0

        if item.currency:
            item_dict['currency'] = item.currency.currency
            item_dict['currency_id'] = item.currency.id
        else:
            item_dict['currency'] = None
        if not item.quantity_on_hand:
            item_dict['quantity_on_hand'] = 0
        else:
            item_dict['quantity_on_hand'] = float(item.quantity_on_hand)

        if not item.quantity_on_order:
            item_dict['quantity_on_order'] = 0
        else:
            item_dict['quantity_on_order'] = float(item.quantity_on_order)

        if item.primary_supplier:
            item_dict['primary_supplier'] = item.primary_supplier.contact_name
        else:
            item_dict['primary_supplier'] = None

        if item.last_PO_date_ordered:
            item_dict['last_ordered'] = item.last_PO_date_ordered.isoformat()
        else:
            item_dict['last_ordered'] = None


        if item.department:
            item_dict['department'] = item.department.name
        else:
            item_dict['department'] = 'Not Configured'

        if item.item_unit_measure:
            item_dict['item_unit_measure'] = item.item_unit_measure.unit_name
        else:
            item_dict['item_unit_measure'] = 'Unit not configured'

        if item.warehouse_location:
            item_dict['warehouse_location'] = item.warehouse_location.warehouse_location
            item_dict['location_description'] = item.warehouse_location.description
        item_dict['production_type'] = item.production_type
        item_dict['search_string'] = item.search_string


        item_dict['permission'] = {}
        item_dict['permission']['can_add_item'] = user.has_perm("inventory.add_item")
        item_dict['permission']['can_view_item'] = user.has_perm("inventory.view_item")
        item_dict['permission']['can_change_item'] = user.has_perm("inventory.change_item")
        item_dict['permission']['can_delete_item'] = user.has_perm("inventory.delete_item")
        ri_list.append(item_dict)
    json_posts = json.dumps(ri_list)
    return HttpResponse(json_posts, mimetype='application/json')

@csrf_exempt
def comment_purchase_request(request):
    if request.method == 'POST':
        # import pdb; pdb.set_trace();
        pr_id = request.POST.get('purchase_request')
        pr = PurchaseRequest.objects.get(pk=pr_id)
        pr_comment = request.POST.get('comment')
        prc = PurchaseRequestComment(
            purchase_request = pr,
            comment = pr_comment,
            commnet_date = datetime.now(),
            user_commented = request.user
            )
        prc.save()
        return render(request, "purchase/add-pr-comment.html", {'comment': prc})

@login_required
@permission_required("purchase.add_purchaseorder")
@csrf_exempt
def add_purchase_order(request):
    if request.method == 'POST':
        # import pdb; pdb.set_trace();
        po_form = POForm(request.POST)
        if po_form.is_valid():
            po = po_form.save()
            po.po_created_by = request.user
            po.datetime = datetime.now()
            po.search_string = po.po_number + " "
            if po.supplier:
                po.search_string += po.supplier.contact_name + " "
        
            items = []
            item_list = request.POST.getlist('item_item')
            if item_list:
                count = 0
                for item in item_list:
                    item_dict = {}
                    item_dict['item_number'] = item
                    item_dict['qty'] = float(request.POST.getlist('item_qty')[count])
                    item_dict['job_number'] = request.POST.getlist('item_job_number')[count]
                    item_dict['job_id'] = request.POST.getlist('item_job_id')[count]
                    item_dict['cost'] = float(request.POST.getlist('item_cost')[count])
                    item_dict['sub_total'] = float(request.POST.getlist('item_sub_total')[count])
                    # item_dict['item_recv'] = request.POST.getlist('item_recv')[count]

                    items.append(item_dict)
                    count = count + 1
            for item in items:
                itemobj = Item.objects.get(item_number=item['item_number'])
                po.search_string += item['item_number'] + " "
                try:
                    job = Job.objects.get(id=item['job_id'])
                    po.search_string += job.job_number + " "

                except Job.DoesNotExist:
                    job = None
                pi = PurchaseItem(po=po, item=itemobj, job_number=job,
                    qty=item['qty'], cost=item['cost'], sub_total=item['sub_total'])
                pi.purchase_status = 0
                pi.save()
                po.save()
            return HttpResponseRedirect("/purchase/list-purchase-orders/")
        else:
            return HttpResponse("Error")        

    else:
        now = datetime.now()
        try:
            po = PurchaseOrder.objects.latest('id')
            po_number = 'P' + po.next_number
            next_number = 'P'+ int(po.next_number) + 1
        except PurchaseOrder.DoesNotExist:
            po_number = 'P' + '1000'
            next_number = '1001'

        user_id = request.user.pk

        form_init = {
            'date_issued': now.strftime('%Y-%m-%d'),
            'datetime': now,
            'po_status': 'New',
            'ship_to': 1,
            'fob': '1400 Phillip Murray Avenue, Oshawa, Ontario - L1J7E8',
            'purchasing_agent': user_id,

        }
        po_form = POForm(initial=form_init)
        po_contact_form = POContactForm()
        po_contacts = POContact.objects.filter(purchase_order=po_number)

        if not request.user.is_superuser:
            po_form.fields['purchasing_agent'].widget.attrs['readonly'] = True
            po_form.fields['po_overwridden_by'].widget.attrs['readonly'] = True
        return render(request, "purchase/add-po2.html", 
            {'poform': po_form, 'po_contact_form': po_contact_form, 
            'po_number': po_number, 'po_contacts': po_contacts, 'next_number': sv.next_po_number})


@csrf_exempt
def add_new_po(request):


    try:
        sv = SystemVariable.objects.get(id=1)
    except Exception, e:
        messages.warning(request, "System varible is not set for PO. Please ask your admin to update System variable.")
        return HttpResponseRedirect("/")

    if request.method == 'POST':

        po_number = request.POST.get("po_number","")
        email_po = request.POST.get("email_po")
        fax_po = request.POST.get("fax_po")
        print_po = request.POST.get("print_po")
        pdf_po = request.POST.get("pdf_po")

        if po_number != "":
            po = PurchaseOrder.objects.get(po_number=po_number)
            po_form = POForm(request.POST, instance=po, request=request, action='update')
        else:
            po_form = POForm(request.POST, request=request, action='new')

        if po_form.is_valid():
            po = po_form.save()
            if po_number == "":
                po.po_created_by = request.user
                # po.datetime = datetime.datetime.now()
                po.save_final_draft = 1
                po.po_status = 'New'
                po.save()

                # check for contacts................
                con_phone_types = request.POST.getlist('po_contact_phone_type')
                if con_phone_types:
                    count = 0
                    for ph_type in con_phone_types:
                        if ph_type == 'Fax':
                            po_contact = POContact(purchase_order=po, contact_type='Fax')
                        else:
                            po_contact = POContact(purchase_order=po, contact_type='Phone')

                        if request.POST.getlist('po_contact_phone_ext')[count]:
                            contact = request.POST.getlist('po_contact_phone_number')[count] + " ext:" + request.POST.getlist('po_contact_phone_ext')[count]
                        else:
                            contact = request.POST.getlist('po_contact_phone_number')[count]
                        con_attention = request.POST.getlist('po_contact_phone_attention')[count]
                        count = count + 1

                        po_contact.contact = contact
                        po_contact.contact_name = con_attention
                        po_contact.save()
                con_email_types = request.POST.getlist('po_contact_email_type')
                
                if con_email_types:
                    count = 0
                    for email_type in con_email_types:
                        po_contact = POContact(purchase_order=po,contact_type='Email')
                        contact = request.POST.getlist('po_contact_email')[count]
                        contact_name = request.POST.getlist('po_contact_email_attention')[count]
                        count = count + 1
                        po_contact.contact = contact
                        po_contact.contact_name = contact_name
                        po_contact.save()


                # ========= shipto contact ==================
                con_shipto_phone_types = request.POST.getlist('po_shipto_contact_phone_type')
                if con_shipto_phone_types:
                    count = 0
                    for ph_type in con_shipto_phone_types:
                        if ph_type == 'Fax':
                            po_contact = POShipToContact(purchase_order=po, contact_type='Fax')
                        else:
                            po_contact = POShipToContact(purchase_order=po, contact_type=ph_type)

                        if request.POST.getlist('po_shipto_contact_phone_ext')[count]:
                            contact = request.POST.getlist('po_shipto_contact_phone_number')[count] + " ext:" + request.POST.getlist('po_contact_phone_ext')[count]
                        else:
                            contact = request.POST.getlist('po_shipto_contact_phone_number')[count]
                        con_attention = request.POST.getlist('po_shipto_contact_phone_attention')[count]
                        count = count + 1

                        po_contact.contact = contact
                        po_contact.contact_name = con_attention
                        po_contact.save()
                
                con_shipto_email_types = request.POST.getlist('po_shipto_contact_email_type')
                # import pdb; pdb.set_trace();
                if con_shipto_email_types:
                    count = 0
                    for email_type in con_shipto_email_types:
                        po_contact = POShipToContact(purchase_order=po,contact_type=email_type)
                        contact = request.POST.getlist('po_shipto_contact_email')[count]
                        contact_name = request.POST.getlist('po_shipto_contact_email_attention')[count]
                        count = count + 1
                        po_contact.contact = contact
                        po_contact.contact_name = contact_name
                        po_contact.save()

                # return HttpResponse("Hello world!")




            # ========== Add / Remove extra contact
            # import pdb; pdb.set_trace();
            extra_contact_ids = request.POST.getlist('po_extra_contacts')
            if extra_contact_ids:
                for extra_contact_id in extra_contact_ids:
                    extra_contact = POContact.objects.get(id=extra_contact_id)
                    extra_contact.purchase_order = po
                    extra_contact.save()


            extra_shipto_contact_ids = request.POST.getlist('po_extra_shipto_contacts')
            if extra_shipto_contact_ids:
                for extra_contact_id in extra_shipto_contact_ids:
                    extra_contact = POShipToContact.objects.get(id=extra_contact_id)
                    extra_contact.purchase_order = po
                    extra_contact.save()

            items = []
            item_list = request.POST.getlist('added_item_number')
            po_items_seq = request.POST.getlist('po_item_seq')
            deleted_items = request.POST.getlist("removed_item")
            if deleted_items:
                for deleted_item in deleted_items:
                    di = PurchaseItem.objects.get(id=deleted_item)
                    di.delete()
            if item_list:
                count = 0
                for item in item_list:
                    item_dict = {}
                    item_seq = request.POST.getlist('po_item_seq')[count]

                    item_dict['item_number'] = item
                    qty = request.POST.getlist('item_qty')[count]

                    item_dict['qty'] = float(qty) if qty != '' else qty
                    item_dict['unit'] = request.POST.getlist('unit')[count]
                    item_dict['comment'] = request.POST.getlist('item_comment')[count]
                    item_dict['job_number'] = request.POST.getlist('item_job_number')[count]
                    item_dict['job_id'] = request.POST.getlist('item_job_id')[count]
                    cost = request.POST.getlist('item_cost')[count]
                    item_dict['cost'] = float(cost) if cost != '' else cost
                    sub_total = request.POST.getlist('item_sub_total')[count]
                    item_dict['sub_total'] = float(sub_total) if sub_total != '' else sub_total
                    
                    item_dict['item_custom_detail'] = request.POST.get('custom_detail_'+item_seq, '')
                    # item_dict['item_custom_comment'] = request.POST.get('custom_comment_'+item_seq, '')

                    items.append(item_dict)
                    count = count + 1
                for item in items:
                    itemobj = Item.objects.get(item_number=item['item_number'])
                    # po.search_string += item['item_number'] + " "
                    try:
                        job = Job.objects.get(id=item['job_id'])
                        # po.search_string += job.job_number + " "

                    except:
                        job = None

                    try:
                        pi, created = PurchaseItem.objects.get_or_create(po=po, item=itemobj)
                        
                        pi.job_number = job
                        if item['qty'] != '':
                            pi.qty = item['qty']
                        if item['unit'] != '':
                            pi.unit = item['unit']
                        if item['cost'] != '':
                            pi.cost = item['cost']
                        if item['sub_total'] != '':
                            pi.sub_total = item['sub_total']
                        pi.comment = item['comment']

                        pi.custom_detail = item['item_custom_detail']
                            # pi.custom_comment = item['item_custom_comment']

                        if created:
                            pi.purchase_status = 0
                        pi.save()
                    except Exception, e:
                        raise e
                    # Update inventory item for Last PO info
                    if created:
                        if itemobj.quantity_on_order and pi.qty:
                            itemobj.quantity_on_order = itemobj.quantity_on_order + Decimal(pi.qty)
                        else:
                            itemobj.quantity_on_order = pi.qty
                        itemobj.last_PO = po.po_number
                        itemobj.last_PO_date_ordered = po.date_issued
                        itemobj.last_PO_date_expected = po.date_expected
                        itemobj.last_cost_paid = pi.cost
                        itemobj.last_PO_ordered_by = po.po_created_by
                        itemobj.last_PO_supplier = po.supplier
                        if pi.qty and itemobj.max_order_qty_remains:
                            itemobj.max_order_qty_remains = itemobj.max_order_qty_remains - Decimal(pi.qty)

                    itemobj.save()
            
            
            import time
            po_extra_contacts = POContact.objects.filter(purchase_order=po.po_number)
            po_items = PurchaseItem.objects.filter(po=po)
            domain = request.get_host()
            url = 'http://'+domain+'/purchase/pdf-po/'+po.po_number+'/'
            # import pdb; pdb.set_trace()
            context = {
                'po': po,
                'purchase_items': po_items
            }
            temp = "purchase/pdf_po.html"

            try:
                report = Report.objects.get(report_type__icontains='PO Email')    
            except Exception, e:
                report = Report.objects.get(id=1)

            if email_po:
                if domain != '127.0.0.1:8000':
                    filepath = '/usr/home/www/'+domain+'/temp/'+po.po_number+"_"+str(time.time())+"_temp_fax.pdf"
                else:
                    filepath = '/home/mamun/report/'+po.po_number+"_"+str(time.time())+"_temp_fax.pdf"

                try:
                    
                    write_pdf(temp, context, filepath)
                    
                    single_report = SingleReport.objects.create(report=report)
                    single_report.que_type = 'email'
                    single_report.filepath = filepath
                    # single_report.search_string = "="+str(po.po_number)
                    single_report.search_status_type = 'PO'
                    single_report.current_job_status = 'new'
                    single_report.script_name = report.python_script
                    single_report.save()

                except Exception, e:
                    raise e
            


            if pdf_po:
                
                if domain != '127.0.0.1:8000':
                    filepath = '/usr/home/www/'+domain+'/temp/'+po.po_number+"_"+str(time.time())+"_temp_fax.pdf"
                else:
                    filepath = '/home/mamun/report/'+po.po_number+"_"+str(time.time())+"_temp.pdf"

                try:

                    write_pdf(temp, context, filepath)

                    single_report = SingleReport.objects.create(report=report)
                    single_report.que_type = 'pdf'
                    single_report.filepath = filepath
                    # single_report.search_string = "="+str(po.po_number)
                    single_report.search_status_type = 'PO'
                    single_report.current_job_status = 'new'
                    single_report.email = 'paul@scom.ca'
                    single_report.script_name = report.python_script
                    single_report.save()
                except Exception, e:
                    raise e
                

            if print_po:
                if domain != '127.0.0.1:8000':
                    filepath = '/usr/home/www/'+domain+'/temp/'+po.po_number+"_"+str(time.time())+"_temp_fax.pdf"
                else:
                    filepath = '/home/mamun/report/'+po.po_number+"_"+str(time.time())+"_temp_print.pdf"

                try:

                    write_pdf(temp, context, filepath)

                    single_report = SingleReport.objects.create(report=report)
                    single_report.que_type = 'print'
                    single_report.filepath = filepath
                    # single_report.search_string = "="+str(po.po_number)
                    single_report.search_status_type = 'PO'
                    single_report.current_job_status = 'new'
                    single_report.script_name = report.python_script
                    single_report.save()

                except Exception, e:
                    raise e

            if fax_po:
                if domain != '127.0.0.1:8000':
                    filepath = '/usr/home/www/'+domain+'/temp/'+po.po_number+"_"+str(time.time())+"_temp_fax.pdf"
                else:
                    filepath = '/home/mamun/report/'+po.po_number+"_"+str(time.time())+"_temp_fax.pdf"

                try:
                    
                    write_pdf(temp, context, filepath)
                    
                    single_report = SingleReport.objects.create(report=report)
                    single_report.que_type = 'fax'
                    single_report.filepath = filepath
                    # single_report.search_string = "="+str(po.po_number)
                    single_report.search_status_type = 'PO'
                    single_report.current_job_status = 'new'
                    single_report.script_name = report.python_script
                    single_report.save()

                except Exception, e:
                    raise e

            po.items_total = request.POST.get("items_total")
            po.save()

            return HttpResponseRedirect("/purchase/list-purchase-orders/")

            # return render(request, "purchase/show_draft_po.html", {'po': po, 'extra_contacts': po_extra_contacts, 'po_items': po_items})
        else:
            
            return HttpResponseRedirect("/purchase/add-po/")
    else:

        currencies = Currency.objects.all()
        delivery_choices = DeliveryChoice.objects.all()
        terms = PaymentTerm.objects.all()
        item_unit_measures = ItemUnitMeasure.objects.filter(is_active=True)
        deliver_internals = DeliverInternal.objects.all()
        users = User.objects.all().exclude(id__in=[-1]).order_by("username")
        adminusers = User.objects.filter(is_superuser=1)

        # POContact.objects.filter(purchase_order=po_number).delete()
        po_contact_form = POContactForm()

        return render(request, "purchase/add-po.html", 
            {"po_number":'NEW' , 'po_contact_form': po_contact_form, 'currencies': currencies,
            'delivery_choices': delivery_choices, 'terms': terms,
            'deliver_internals': deliver_internals, 'users': users, 'item_unit_measures':item_unit_measures,
            'adminusers': adminusers, 'sv': sv})



def write_pdf(template_src, context_dict, filename):
    template = get_template(template_src)
    context = Context(context_dict)
    html  = template.render(context)
    result = open(filename, 'wb') # Changed from file to filename
    pdf = pisa.pisaDocument(StringIO.StringIO(
        html.encode("UTF-8")), result)
    result.close()
    

def pdf_po(request, po_id):
    # import pdb; pdb.set_trace();
    # resource_directory = os.path.dirname(os.path.dirname(__file__))
    # rendered_html = render_to_string("purchase/pdf_po.html", locals())
    po = PurchaseOrder.objects.get(po_number=po_id)
    purchase_items = PurchaseItem.objects.filter(po=po)

    domain = request.get_host()
    url = 'http://'+domain+'/purchase/pdf-po/'+po.po_number+'/'
    if domain != '127.0.0.1:8000':
        filepath = '/usr/home/www/'+domain+'/temp/'+po.po_number+".pdf"
    else:
        filepath = '/home/mamun/report/'+po.po_number+".pdf"

    context = {
        'po': po,
        'purchase_items': purchase_items
    }

    temp = "purchase/pdf_po.html"

    write_pdf(temp, context, filepath)

    return render(request, "purchase/pdf_po.html", {'po': po, 'purchase_items':purchase_items})


@csrf_exempt
def add_new_po_and_email(request):
    if request.method == 'POST':
        # import pdb; pdb.set_trace();
        po_number = request.POST.get("po_number")
        if po_number:
            po = PurchaseOrder.objects.get(po_number=po_number)
        else:
            sv = SystemVariable.objects.get(id=1)
            next_po_number = sv.get_next_po_number
            po = PurchaseOrder.objects.create(po_number=next_po_number)

        date_issued = request.POST.get("date_issued")
        po.date_issued = date_issued

        date_expected = request.POST.get("date_expected")
        po.date_expected = date_expected

        supplier = request.POST.get("supplier")
        try:
            contact = Contact.objects.get(id=supplier)
            po.supplier = contact
        except Exception, e:
            pass       

        ship_to_id = request.POST.get("ship_to")
        try:
            ship_to = Contact.objects.get(id=ship_to_id)
            po.ship_to = ship_to
        except Exception, e:
            pass        

        ship_via_id = request.POST.get("ship_via")
        try:
            ship_via = DeliveryChoice.objects.get(id=ship_via_id)
            po.ship_via = ship_via    
        except Exception, e:
            pass
        

        deliver_internal_id = request.POST.get("deliver_internal")
        try:
            deliver_internal = DeliverInternal.objects.get(id=deliver_internal_id)
            po.deliver_internal = deliver_internal
        except Exception, e:
            pass
        

        shipping_inst = request.POST.get("shipping_inst")
        po.shipping_inst = shipping_inst

        blanket_po = request.POST.get("blanket_po")
        po.blanket_po = blanket_po

        terms_id = request.POST.get("terms")
        try:
            terms = PaymentTerm.objects.get(id=terms_id)
            po.terms = terms
        except Exception, e:
            pass        

        purchasing_agent_id = request.POST.get("purchasing_agent")
        try:
            purchasing_agent = User.objects.get(id=purchasing_agent_id)
            po.purchasing_agent = purchasing_agent
        except Exception, e:
            pass
        

        returned_type = request.POST.get("returned_type")
        po.returned_type = returned_type

        items_total = request.POST.get("items_total")
        po.items_total = items_total

        hst_taxable = request.POST.get("hst_taxable")
        po.hst_taxable = hst_taxable

        hst_taxable_amount = request.POST.get("hst_taxable_amount")
        po.hst_taxable_amount = hst_taxable_amount

        pst_taxable = request.POST.get("pst_taxable")
        po.pst_taxable = pst_taxable

        pst_taxable_amount = request.POST.get("pst_taxable_amount")
        po.pst_taxable_amount = pst_taxable_amount

        po_currency_id = request.POST.get("po_currency")
        try:
            po_currency = Currency.objects.get(id=po_currency_id)
            po.po_currency = po_currency
        except Exception, e:
            pass
        

        total_po_amount = request.POST.get("total_po_amount")
        po.total_amount = total_amount

        po.save_final_draft = 1
        po.po_status = 'New'

        po.save()

        added_item_numbers = request.POST.getlist("added_item_number")
        unit = request.POST.getlist("unit")
        item_cost = request.POST.getlist("item_cost")
        item_qty = request.POST.getlist("item_qty")
        item_sub_total = request.POST.getlist("item_sub_total")
        item_job_number = request.POST.getlist("item_job_number")
        item_job_id = request.POST.getlist("item_job_id")
        item_comment = request.POST.getlist("item_comment")
        

        for i, item_number in enumerate(added_item_numbers):
            try:
                item = Item.objects.get(item_number=item_number)
                po_item, created = PurchaseItem.objects.get_or_create(po=po, item=item)
                po_item.unit = unit[i]
                po_item.cost = item_cost[i]
                po_item.qty = item_qty[i]
                po_item.sub_total = item_sub_total[i]
                po_item.job_number = item_job_id[i]
                po_item.item_comment = item_comment[i]
                po_item.purchase_status = 0

                po_item.save()

                if created:
                    if item.quantity_on_order and po_item.qty:
                        item.quantity_on_order = item.quantity_on_order + Decimal(po_item.qty)
                    else:
                        item.quantity_on_order = po_item.qty
                    item.last_PO = po.po_number
                    item.last_PO_date_ordered = po.date_issued
                    item.last_PO_date_expected = po.date_expected
                    item.last_cost_paid = po_item.cost
                    item.last_PO_ordered_by = po.po_created_by
                    item.last_PO_supplier = po.supplier
                    if po_item.qty:
                        item.max_order_qty_remains = item.max_order_qty_remains - Decimal(po_item.qty)

                item.save()

            except Item.DoesNotExist:
                pass
        

@csrf_exempt
def save_po(request):
    po_number = request.POST.get("po_number","")
    action = request.POST.get("action","")
    po = PurchaseOrder.objects.get(po_number=po_number)
    if action == 'save':
        po.save_final_draft = 1
        po.save()

    else:
        po_extra_contacts = POContact.objects.filter(purchase_order=po.po_number)
        po_items = PurchaseItem.objects.filter(po=po)
        po_extra_contacts.delete()
        po_items.delete()
        po.delete()

    return HttpResponseRedirect("/purchase/list-purchase-orders/")


def search_po(request):
    # import pdb; pdb.set_trace();
    query = request.GET.get('q','')
    if request.GET.get('q'):
        purchase_orders = SearchQuerySet().using('po').filter(content=AutoQuery(query))[:30]
    else:
        purchase_orders = SearchQuerySet().using('po').all().load_all()[:30]

    po_list = []
    for po in purchase_orders:
        if po != None:
            po_dict = {}
            po_dict['po_number'] = po.po_number
            po_dict['po_status'] = po.po_status
            po_dict['supplier'] = po.supplier
            po_dict['terms'] = po.terms
            po_dict['shipping_inst'] = po.shipping_inst
            po_dict['items'] = po.po_items
            po_dict['hst_taxable'] = po.hst_taxable
            po_dict['hst_taxable_amount'] = po.hst_taxable_amount
            po_dict['total_hst_tax'] = po.total_hst_tax
            po_dict['pst_taxable'] = po.pst_taxable
            po_dict['pst_taxable_amount'] = po.pst_taxable_amount
            po_dict['total_pst_tax'] = po.total_pst_tax
            po_dict['total_tax'] = po.total_tax

            po_list.append(po_dict)

    # try:
    #     page = int(request.GET.get('page','1'))
    # except ValueError:
    #     page = 1
    # paginator = Paginator(po_list, 30)
    # try:
    #     pages = paginator.page(page)
    # except (EmptyPage, InvalidPage):
    #     pages = paginator.page(paginator.num_pages)

    # results = pages.object_list

    data = json.dumps(po_list)
    return HttpResponse(data)





@login_required
@permission_required("purchase.view_purchase_order")
@csrf_exempt
def list_purchase_orders(request):
    # import pdb; pdb.set_trace()
    # status = request.GET.get('status', '')
    # if status != '':
    #   purchase_orders = PurchaseOrder.objects.filter(status=status)
    # else:
    #   purchase_orders = PurchaseOrder.objects.all()

    return render(request, "purchase/po-list.html", {})


def po_list(request):
    # import pdb; pdb.set_trace()
    pos = PurchaseOrder.objects.all()
    polist = []
    for po in pos:
        po_dict = {}
        po_dict['po_number'] = po.po_number
        po_dict['po_status'] = po.po_status
        po_dict['po_created_by'] = po.po_created_by.id
        if po.po_created_by.id == request.user.id or request.user.is_superuser == True:
            po_dict['can_edit'] = True
        else:
            po_dict['can_edit'] = False

        if po.date_issued:
            po_dict['date_issued'] = po.date_issued.isoformat()
        if po.supplier:
            po_dict['supplier'] = po.supplier.contact_name
            po_dict['supplier_id'] = po.supplier.id
        else:
            po_dict['supplier'] = None

        polist.append(po_dict)

    json_posts = json.dumps(polist)
    return HttpResponse(json_posts, mimetype='application/json')

def get_po_by_id(request,pk):
    # import pdb; pdb.set_trace()
    po = PurchaseOrder.objects.get(po_number=pk)
    po_items = po.purchaseitem_set.all()
    # po_contact = POContact.objects.filter(purchase_order=po.po_number)

    po_dict = {}
    po_dict['po_number'] = po.po_number
    if po.items_total:
        po_dict['total_qty'] = po.items_total.to_eng_string()
    else:
        po_dict['total_qty'] = '0.00'
    po_dict['next_number'] = po.next_number
    if po.date_issued:
        po_dict['date_issued'] = po.date_issued.isoformat()

    if po.date_expected:
        po_dict['date_expected'] = po.date_expected.isoformat()
    else:
        po_dict['date_expected'] = None

    po_dict['po_status'] = po.po_status

    if po.supplier:
        supplier = {}
        supplier['id'] = str(po.supplier.id)
        supplier['contact_name'] = po.supplier.contact_name
        supplier['attention_to'] = po.supplier.attention_to
        supplier['address_1'] = po.supplier.address_1
        supplier['address_2'] = po.supplier.address_2
        supplier['country'] = po.supplier.country
        supplier['city'] = po.supplier.city
        supplier['postal_code'] = po.supplier.postal_code
        supplier['province'] = po.supplier.province
        supplier['phones'] = []
        phones = ContactPhone.objects.filter(contact=po.supplier)
        # import pdb; pdb.set_trace();
        for phone in phones:
            ph = {}
            ph['type'] = phone.phone_type.phone_type
            ph['number'] = phone.phone
            ph['phone_ext'] = phone.phone_ext
            supplier['phones'].append(ph)

        supplier['emails'] = []
        semails = ContactEmailAddress.objects.filter(contact=po.supplier)
        for email in semails:
            email_dict = {}
            email_dict['email_type'] = email.email_address_type.email_type
            email_dict['email_address'] = email.email_address
            supplier['emails'].append(email_dict)
        po_dict['supplier'] = supplier
    else:
        po_dict['supplier'] = 'None'

    extra_contacts = POContact.objects.filter(purchase_order=po)
    ec_list = []
    if extra_contacts:
        for ec in extra_contacts:
            ex = {}
            ex['id'] = ec.id
            ex['contact_type'] = ec.contact_type
            ex['contact'] = ec.contact
            ex['contact_name'] = ec.contact_name
            ec_list.append(ex)

    po_dict['extra_contacts'] = ec_list

    extra_shipto_contacts = POShipToContact.objects.filter(purchase_order=po)
    ec_list = []
    if extra_shipto_contacts:
        for ec in extra_shipto_contacts:
            ex = {}
            ex['id'] = ec.id
            ex['contact_type'] = ec.contact_type
            ex['contact'] = ec.contact
            ex['contact_name'] = ec.contact_name
            ec_list.append(ex)

    po_dict['extra_shipto_contacts'] = ec_list

    if po.ship_to:
        ship_to = {}
        ship_to['id'] = str(po.ship_to.id)
        ship_to['contact_name'] = po.ship_to.contact_name
        ship_to['attention_to'] = po.ship_to.attention_to
        ship_to['address_1'] = po.ship_to.address_1
        ship_to['address_2'] = po.ship_to.address_2
        ship_to['country'] = po.ship_to.country
        ship_to['city'] = po.ship_to.city
        ship_to['postal_code'] = po.ship_to.postal_code
        ship_to['province'] = po.ship_to.province

        ship_to['phones'] = []
        phones = ContactPhone.objects.filter(contact=po.ship_to)
        # import pdb; pdb.set_trace();
        for phone in phones:
            ph = {}
            ph['type'] = phone.phone_type.phone_type
            ph['number'] = phone.phone
            ph['phone_ext'] = phone.phone_ext
            ship_to['phones'].append(ph)

        ship_to['emails'] = []
        shemails = semails = ContactEmailAddress.objects.filter(contact=po.ship_to)
        for email in shemails:
            email_dict = {}
            email_dict['email_type'] = email.email_address_type.email_type
            email_dict['email_address'] = email.email_address
            ship_to['emails'].append(email_dict)

        po_dict['ship_to'] = ship_to
    else:
        po_dict['ship_to'] = None

    if po.ship_via:
        ship_via = {}
        ship_via['id'] = po.ship_via.id
        ship_via['delivery_choice'] = po.ship_via.delivery_choice
        po_dict['ship_via'] = ship_via
    else:
        po_dict['ship_via'] = None

    if po.terms:
        term = {}
        term['id'] = str(po.terms.id)
        term['terms'] = po.terms.term
        po_dict['terms'] = term
    else:
        po_dict['terms'] = None

    po_dict['fob'] = po.fob

    po_dict['shipping_inst'] = po.shipping_inst

    if po.deliver_internal:
        deliver_internal = {}
        deliver_internal['id'] = po.deliver_internal.id
        deliver_internal['department'] = po.deliver_internal.department
        deliver_internal['description'] = po.deliver_internal.description
        po_dict['deliver_internal'] = deliver_internal
    else:
        po_dict['deliver_internal'] = None

    if po.date_confirmed:
        po_dict['date_confirmed'] = po.date_confirmed.isoformat()
    else:
        po_dict['date_confirmed'] = None

    # if po.blanket_po:
    #   blanket_po = {}
    #   blanket_po['id'] = po.
    po_dict['blanket_po'] = po.blanket_po
    if po.purchasing_agent:
        purchasing_agent = {}
        purchasing_agent['name'] = po.purchasing_agent.first_name + " " + po.purchasing_agent.last_name
        purchasing_agent['id'] = po.purchasing_agent.id
        po_dict['purchasing_agent'] = purchasing_agent
    else:
        po_dict['purchasing_agent'] = None

    if po.returned_type:
        return_type = {}
        return_type['id'] = po.returned_type
        return_type['value'] = po.get_return_type()
        po_dict['return_type'] = return_type
    else:
        po_dict['returned_type'] = None
    if po.items_total:
        po_dict['items_total'] = po.items_total.to_eng_string()
    else:
        po_dict['items_total'] = None

    po_dict['hst_taxable'] = po.hst_taxable
    if po.hst_taxable:
        po_dict['hst_taxable_amount'] = po.hst_taxable_amount.to_eng_string()
        po_dict['total_hst_tax'] = po.total_hst_tax.to_eng_string()
    else:
        po_dict['hst_taxable_amount'] = po.hst_taxable_amount.to_eng_string()
        po_dict['total_hst_tax'] = po.total_hst_tax.to_eng_string()

    po_dict['pst_taxable'] = po.pst_taxable
    if po.pst_taxable:
        po_dict['pst_taxable_amount'] = po.pst_taxable_amount.to_eng_string()
        po_dict['total_pst_tax'] = po.total_pst_tax.to_eng_string()
    else:
        po_dict['pst_taxable_amount'] = po.pst_taxable_amount.to_eng_string()
        po_dict['total_pst_tax'] = po.total_pst_tax.to_eng_string()

    if po.total_tax:
        po_dict['total_tax'] = po.total_tax.to_eng_string()
    else:
        po_dict['total_tax'] = po.total_tax.to_eng_string()

    if po.po_currency:
        currency = {}
        currency['id'] = str(po.po_currency.id)
        currency['currency'] = po.po_currency.currency
        currency['currency_icon'] = po.po_currency.currency_icon
        po_dict['currency'] = currency
    else:
        po_dict['currency'] = None

    po_dict['total_po_amount'] = po.total_po_amount.to_eng_string()
    if po.po_overwridden_by:
        overwridden_by = {}
        overwridden_by['id'] = str(po.po_overwridden_by.id)
        overwridden_by['username'] = po.po_overwridden_by.username
        po_dict['po_overwridden_by'] = overwridden_by
    else:
        po_dict['po_overwridden_by'] = None

    if po.po_que:
        po_que = {}
        po_que['id'] = po.po_que
        po_que['label'] = po.que_verbose()
        po_dict['po_que'] = po_que

    if po.po_created_by:
        po_created_by = {}
        po_created_by['id'] = str(po.po_created_by.id)
        po_created_by['username'] = po.po_created_by.username
        po_dict['po_created_by'] = po_created_by
    else:
        po_dict['po_created_by'] = None

    po_dict['search_string'] = po.search_string

    purchase_items = PurchaseItem.objects.filter(po=po)
    po_items = []
    for po_item in purchase_items:
        item = {}
        item['p_item_id'] = po_item.id
        item['unit'] = po_item.unit
        if po_item.item:
            item['item_number'] = po_item.item.item_number
            item['description'] = po_item.item.description
            
        if po_item.item.currency:
            item['currency'] = po_item.item.currency.currency
            item['currency_id'] = po_item.item.currency.id
            item['currency_icon'] = po_item.item.currency.get_currency_icon()

        if po_item.job_number:
            item['job_number'] = po_item.job_number.job_number
        
        item['qty'] = po_item.qty.to_eng_string()
        item['cost'] = po_item.cost.to_eng_string()
        
        item['sub_total'] = po_item.sub_total.to_eng_string()
        if po_item.purchase_status:
            item['purchase_status'] = po_item.status_verbose()

        item['comment'] = po_item.comment
        if po_item.item_recv:
            item['item_received'] = po_item.item_recv.to_eng_string()
        else:
            item['item_received'] = None

        if po_item.item_recv_date:
            item['item_recv_date'] = po_item.item_recv_date.isoformat()
        else:
            item['item_recv_date'] = None
        if po_item.job_number:
            item['job_number'] = po_item.job_number.job_number
            item['job_number_id'] = po_item.job_number.id
        else:
            item['job_number'] = None
            item['job_number_id'] = None

        if po_item.custom_comment != '':
            item['custom_comment'] = po_item.custom_comment
        else:
            item['custom_comment'] = ''

        if po_item.custom_detail != '':
            item['custom_detail'] = po_item.custom_detail
        else:
            item['custom_detail'] = ''


        po_items.append(item)

    po_dict['items'] = po_items
    po_dict['po_total_before_tax'] = po.po_total_before_tax.to_eng_string()

    json_posts = json.dumps(po_dict)
    return HttpResponse(json_posts, mimetype='application/json')


def get_purchase_orders(request):
    
    purchase_orders = PurchaseOrder.objects.all()
    po_list = []
    for po in purchase_orders:
        po_dict = {}
        po_dict['po_number'] = po.po_number
        if po.total_po_amount:
            po_dict['total_po_amount'] = po.total_po_amount.to_eng_string()
        if po.po_created_by:
            po_dict['po_created_by'] = po.po_created_by.id
            if po.po_created_by.id == request.user.id or request.user.is_superuser:
                po_dict['can_edit'] = True
            else:
                po_dict['can_edit'] = False
        elif request.user.is_superuser:
            po_dict['can_edit'] = True
        else:
            po_dict['can_edit'] = False

        po_dict['search_string'] = po.search_string
        if po.date_issued:
            po_dict['date_issued'] = po.date_issued.isoformat()
        else:
            po_dict['date_issued'] = None

        if po.date_expected:
            po_dict['date_expected'] = po.date_expected.isoformat()
        else:
            po_dict['date_expected'] = None

        po_dict['po_number'] = po.po_number
        po_dict['status'] = po.po_status
        if po.purchasing_agent:
            po_dict['purchasing_agent'] = po.purchasing_agent.username
        else:
            po_dict['purchasing_agent'] = 'Admin'
        if po.supplier:
            po_dict['supplier'] = po.supplier.contact_name
            po_dict['supplier_id'] = po.supplier.id
        else:
            po_dict['supplier'] = None

        # import pdb; pdb.set_trace()
        purchase_items = PurchaseItem.objects.filter(po=po)
        po_items = []
        for po_item in purchase_items:
            item = {}
            if po_item.item:
                item['item_number'] = po_item.item.item_number
                item['description'] = po_item.item.description
                if po_item.item.currency:
                    item['currency'] = po_item.item.currency.currency
                    item['currency_icon'] = po_item.item.currency.get_currency_icon()

            if po_item.job_number:
                item['job_number'] = po_item.job_number.job_number
            item['qty'] = po_item.qty.to_eng_string()
            item['cost'] = po_item.cost.to_eng_string()
            
            item['sub_total'] = po_item.sub_total.to_eng_string()
            if po_item.purchase_status:
                item['purchase_status'] = po_item.status_verbose()
            po_items.append(item)

        po_dict['items'] = po_items
        if po.po_currency:
            po_dict['po_currency'] = po.po_currency.currency
            po_dict['po_currency_icon'] = po.po_currency.get_currency_icon()

        po_list.append(po_dict)

    json_posts = json.dumps(po_list)
    return HttpResponse(json_posts, mimetype='application/json')


def view_purchase_order(request, pk):
    po = PurchaseOrder.objects.get(po_number=pk)
    pitems = PurchaseItem.objects.filter(po=po)
    status_comments = POStatus.objects.filter(po=po)
    phones = ContactPhone.objects.filter(contact=po.supplier)
    emails = ContactEmailAddress.objects.filter(contact=po.supplier)
    poecontacts = POContact.objects.filter(purchase_order=po.po_number)

    return render(request, "purchase/po-view.html", 
        {'po': po, 'extra_contacts': poecontacts, 'status_comments': status_comments,
        'purchase_items': pitems, 'phones': phones, 'emails': emails})

@csrf_exempt
def cancel_po_status(request, pk):
    if request.method == 'POST':
        # import pdb; pdb.set_trace()
        po_number = request.POST.get('purchase_order')
        po_comment = request.POST.get('status_comment')
        
        po_status = POStatus(status_comment=po_comment)
        po_status.save()
        po_status.status_by = request.user
        po = PurchaseOrder.objects.get(po_number=po_number)
        po_status.po = po
        po_status.datetime = datetime.now()
        po_status.status = 'Canceled'
        po_status.save()

        po.po_status = 'Canceled'
        po.save()
        return HttpResponse(po_status.pk)
    else:
        po = PurchaseOrder.objects.get(po_number=pk)
        po_status_form = POStatusForm()
        return render(request, "purchase/po-status-change.html", {'po_status_form': po_status_form, 'po_id': pk, 'po_number': po.po_number})



def change_po(request):
    form_init = {
        'status_by': request.user.pk,
        'status': 6,
    }
    if request.method == 'POST':
        # import pdb; pdb.set_trace()
        po_status_form = POStatusForm2(request.POST)
        if po_status_form.is_valid():
            try:
                po_status = po_status_form.save()
                po_status.datetime = datetime.now()
                # po_status.status = 'canceled'
                po_status.save()
                po = PurchaseOrder.objects.get(po_number=po_status.po.po_number)
                po.status = po_status.status
                po.save()
                messages.success(request, 'PO is canceled.')
            except:
                messages.error(request, 'Error in PO canceling.')
                pass
        
    po_status_form = POStatusForm2(initial=form_init)
    return render(request, "purchase/cancel-po.html", {'po_status_form': po_status_form})


@login_required
# @permission_required("purchase.change_purchaseorder")
@csrf_exempt
def edit_purchase_order(request, pk):
    try:
        sv = SystemVariable.objects.get(id=1)
        next_number = sv.next_po_number
    except Exception, e:
        pass
    po = PurchaseOrder.objects.get(id=pk)
    if po.supplier:
        contact_id = po.supplier.pk
    else:
        contact_id = None
    po_items = PurchaseItem.objects.filter(po=po)
    po_item_list = list(po_items)
    status_comments = POStatus.objects.filter(po=po)
    if request.method == 'POST':
        po_form = POFormEdit(request.POST, instance=po)

        if po_form.is_valid():
            po = po_form.save()
            po.save_final_draft = 1
            po.datetime = datetime.now()
            po.search_string = po.po_number + " "
            if po.supplier:
                po.search_string += po.supplier.contact_name + " "
        
            item_list = request.POST.getlist('added_item_number')
            if item_list:
                count = 0
                for item in item_list:

                    qty = float(request.POST.getlist('item_qty')[count])
                    comment = request.POST.getlist('item_comment')[count]
                    job_number = request.POST.getlist('item_job_number')[count]
                    job_id = request.POST.getlist('item_job_id')[count]
                    cost = float(request.POST.getlist('item_cost')[count])
                    sub_total = float(request.POST.getlist('item_sub_total')[count])
                    if(job_id):
                        try:
                            job = Job.objects.get(id=job_id)
                            po.search_string += job.job_number + " "

                        except Job.DoesNotExist:
                            job = None
                            pass
                    else:
                        job = None
                    try:
                        pi_id = request.POST.getlist('pi_id')[count]
                        pi = PurchaseItem.objects.get(id=pi_id)
                        pi.qty = qty
                        pi.comment = comment
                        pi.cost = cost
                        pi.sub_total = sub_total
                        pi.job_number = job
                        po_item_list.remove(pi)
                    except:
                        itemobj = Item.objects.get(item_number=item)
                        pi = PurchaseItem(po=po, item=itemobj, job_number=job,
                            qty=qty, cost=cost, sub_total=sub_total, comment=comment)
                    po.save()
                    pi.save()
                    count += 1

            for item in po_item_list:
                item.delete()
                    
                    # item_dict['item_recv'] = request.POST.getlist('item_recv')[count]
            return HttpResponseRedirect("/purchase/list-purchase-orders/")
        else:
            return HttpResponseRedirect("/purchase/edit/"+pk+"/")
    else:
        currencies = Currency.objects.all()
        delivery_choices = DeliveryChoice.objects.all()
        terms = PaymentTerm.objects.all()
        deliver_internals = DeliverInternal.objects.all()
        item_unit_measures = ItemUnitMeasure.objects.filter(is_active=True)
        users = User.objects.all().exclude(id__in=[-1]).order_by("username")
        adminusers = User.objects.filter(is_superuser=1)
        contacts = Contact.objects.all()
        po_contact_form = POContactForm()

        return render(request, "purchase/edit-po2.html", 
            {'po_id': pk, 'po_items': po_items, 'status_comments':status_comments,
            'po_contact_form': po_contact_form, 'currencies': currencies, 'item_unit_measures': item_unit_measures,
            'delivery_choices': delivery_choices, 'terms': terms, 'next_number': next_number,
            'deliver_internals': deliver_internals, 'users': users, 'contacts': contacts,
            'adminusers': adminusers, 'po': po})


def get_po_items(request, po_id):
    # import pdb; pdb.set_trace()
    # import json
    try:
        po = PurchaseOrder.objects.get(id=po_id)
    except PurchaseOrder.DoesNotExist:
        json_posts = {
            'PurchaseOrder DoesNotExist',
        }
        return HttpResponse(json_posts, mimetype='application/json')
        
    
    po_items = PurchaseItem.objects.filter(po=po)
    poitems = []
    for item in po_items:
        item_dict = {}
        item_dict['pi_id'] = item.id
        item_dict['item_number'] = item.item.item_number
        if item.item.currency:
            item_dict['currency'] = item.item.currency.currency
            item_dict['currency_icon'] = item.item.currency.currency_icon
        item_dict['description'] = item.item.description
        if item.job_number:
            item_dict['job_number'] = item.job_number.job_number
            item_dict['job_id'] = item.job_number.id
        else:
            item_dict['job_number'] = None

        item_dict['qty'] = float(item.qty)
        item_dict['cost'] = float(item.cost)
        item_dict['sub_total'] = float(item.sub_total)
        item_dict['purchase_status'] = item.status_verbose()
        item_dict['search_string'] = item.search_string
        poitems.append(item_dict)
    # print(poitems)

    json_posts = json.dumps(poitems)
    return HttpResponse(json_posts, mimetype='application/json')


@csrf_exempt
def delete_purchase_order(request):
    if request.method == "POST":
        po_id = request.POST.get("po_id")
        po = PurchaseOrder.objects.get(po_number=po_id)
        po.delete();
        return HttpResponse(po_id)


@csrf_exempt
def add_sl_soldto_extra_contact(request):
    if request.method == 'POST':
        # import pdb; pdb.set_trace();
        po_contact_type = request.POST.get('contact_type')
        po_contact = request.POST.get('contact')
        po_contact_name = request.POST.get('contact_name')
        pocontact = SLSoldToContact(contact_type=po_contact_type, 
            contact=po_contact, contact_name=po_contact_name)
        
        pocontact.save()
        return render(request, "purchase/extra-sl-soldto-contact.html", {'pocontact': pocontact})
    else:
        pocontactform = SLSoldToContactForm()

        return render(request, "purchase/add-sl-soldto-extra-contact-form.html", {'po_contact_form': pocontactform})

@csrf_exempt
def add_sl_shipto_extra_contact(request):
    if request.method == 'POST':
        # import pdb; pdb.set_trace();
        sl_contact_type = request.POST.get('contact_type')
        sl_contact = request.POST.get('contact')
        sl_contact_name = request.POST.get('contact_name')
        slcontact = SLShipToContact(contact_type=sl_contact_type, 
            contact=sl_contact, contact_name=sl_contact_name)
        
        slcontact.save()
        return render(request, "purchase/extra-sl-shipto-contact.html", {'slcontact': slcontact})
    else:
        slcontactform = SLShipToContactForm()

        return render(request, "purchase/add-sl-shipto-extra-contact-form.html", {'slcontactform': slcontactform})


@csrf_exempt
def add_extra_contact(request):
    if request.method == 'POST':
        # import pdb; pdb.set_trace();
        po_contact_type = request.POST.get('contact_type')
        po_contact = request.POST.get('contact')
        po_contact_name = request.POST.get('contact_name')
        pocontact = POContact(contact_type=po_contact_type, 
            contact=po_contact, contact_name=po_contact_name)
        
        pocontact.save()
        return render(request, "purchase/extra-po-contact.html", {'pocontact': pocontact})
    else:
        pocontactform = POContactForm()

        return render(request, "purchase/add-po-contact.html", {'po_contact_form': pocontactform})


@login_required
def extra_po_contact(request, po_id):
    # import pdb; pdb.set_trace();
    po_contacts = POContact.objects.filter(purchase_order=po_id)
    return render(request, "purchase/extra-po-contacts.html", {'po_contacts': po_contacts})


@csrf_exempt
def delete_extra_po_contact(request):
    poecid = request.POST.get("poecid")
    extra_contact = POContact.objects.get(id=poecid)
    extra_contact.delete()
    return HttpResponse(poecid)

@csrf_exempt
def delete_soldto_contact(request):
    # import pdb; pdb.set_trace();
    contactid = request.POST.get("contactid")
    extra_contact = SLSoldToContact.objects.get(id=contactid)
    extra_contact.delete()
    return HttpResponse(contactid)

@csrf_exempt
def delete_shipto_contact(request):
    contactid = request.POST.get("contactid")
    extra_contact = SLShipToContact.objects.get(id=contactid)
    extra_contact.delete()
    return HttpResponse(contactid)


@csrf_exempt
def delete_shipto_extra_po_contact(request):
    poecid = request.POST.get("poecid")
    extra_contact = POShipToContact.objects.get(id=poecid)
    extra_contact.delete()
    return HttpResponse(poecid)


def get_pending_list(request):
    # import pdb; pdb.set_trace();
    import json
    items = PurchaseItem.objects.filter(purchase_status__lte = 1)
    pending_items = []
    for item in items:
        item_dict = {}
        item_dict['purchase_item_id'] = item.id
        if item.po:
            item_dict['po_number'] = item.po.po_number
        item_dict['purchase_status'] = item.status_verbose()
        item_dict['search_string'] = item.search_string
        if item.job_number:
            item_dict['job_number'] = item.job_number.job_number
        else:
            item_dict['job_number'] = None

        if item.item:
            item_dict['item_number'] = item.item.item_number
            item_dict['item_description'] = item.item.description
            item_dict['sub_total'] = float(item.sub_total)
        else:
            item_dict['item_number'] = None
            item_dict['item_description'] = None

        item_dict['qty_ordered'] = float(item.qty)
        received_items = ReceivedItemHistory.objects.filter(purchase_item=item)
        item_dict['total_item_received'] = 0
        item_dict['sub_total_received'] = 0
        if received_items:
            for received_item in received_items:
                item_dict['total_item_received'] += float(received_item.qty_received)
                item_dict['sub_total_received'] += float(received_item.sub_total)

        pending_items.append(item_dict)

    json_pending_list = json.dumps(pending_items)
    return HttpResponse(json_pending_list, mimetype='application/json')
        
def purchase_pending_list(request):

    return render(request, 'purchase/purchase-pending-list.html', {})




def purchase_received_list(request):
    # import pdb; pdb.set_trace()
    items = ReceivedItemHistory.objects.all()
    received_items = []
    for item in items:
        item_dict = {}
        if item.item_po:
            item_dict['po_number'] = item.item_po.po_number
        else:
            item_dict['po_number'] = None

        if item.purchase_item:
            item_dict['item_number'] = item.purchase_item.item.item_number
        else:
            item_dict['item_number'] = None

        item_dict['qty_received'] = item.qty_received
        item_dict['sub_total'] = float(item.sub_total)
        item_dict['item_received_date'] = item.item_received_date
        item_dict['reveived_by'] = item.reveived_by
        item_dict['comment'] = item.comment
        item_dict['search_string'] = item.search_string

        received_items.append(item_dict)

    return render(request, 'purchase/purchase-received-list.html', 
        {'received_items': received_items})


@login_required
@permission_required("purchase.receive_purchase_item")
@csrf_exempt
def receive_item(request, item_id):
    purchase_item = PurchaseItem.objects.get(id=item_id)
    order_restriction = purchase_item.qty - purchase_item.item_recv
    if request.method == 'POST':
        item_rcv_form = ItemReeiveForm(request.POST)
        if item_rcv_form.is_valid():
            rcv_item = item_rcv_form.save()
            item = Item.objects.get(item_number=purchase_item.item.item_number)
            po = purchase_item.po

            # Update item receive history            
            rcv_item.purchase_item = purchase_item
            rcv_item.item_po = po
            rcv_item.sub_total = purchase_item.cost * rcv_item.qty_received
            rcv_item.item_received_date = datetime.now()
            rcv_item.reveived_by = request.user
            rcv_item.search_string = purchase_item.item.item_number + " " + rcv_item.item_po.po_number
            rcv_item.save()

            # Update PurchaseItem
            '''
            If purchase_item.purchase_status == 2 this purchase_item is then done with all
            '''
            
            purchase_item.item_recv += rcv_item.qty_received
            purchase_item.item_recv_date = datetime.now()
            if purchase_item.item_recv >= purchase_item.qty:
                purchase_item.purchase_status = 2
            else:
                purchase_item.purchase_status = 1

            purchase_item.save()
            # Update PO Status
            pitems = PurchaseItem.objects.filter(po=po, purchase_status__lte=1)
            if not pitems:
                po.po_status = 'Accounting Confirmed'
            else:
                po.po_status = 'Partial Received'
            po.save()

            # Update Inventory item
            if item.quantity_on_hand:
                item.quantity_on_hand = item.quantity_on_hand + rcv_item.qty_received
            else:
                item.quantity_on_hand = purchase_item.item_recv
            item.quantity_on_order = item.quantity_on_order - rcv_item.qty_received
            item.max_order_qty_remains = item.max_order_qty_remains + rcv_item.qty_received
            if item.qty_received:
                item.qty_received = item.qty_received + rcv_item.qty_received
            else:
                item.qty_received = rcv_item.qty_received
            item.qty_received_date = datetime.now()
            item.save()

            return HttpResponse(rcv_item.id)
    else:
        item_rcv_form = ItemReeiveForm()
        return render(request, "purchase/item-receive-form.html", 
            {'item_rcv_form': item_rcv_form, 'item_id': item_id, 
            'order_restriction':order_restriction})


def search_packing_list(request):
    query = request.GET.get('q','')
    # status = request.GET.get('status','')
    if query:
        pls = SearchQuerySet().using('pl').filter(content=AutoQuery(query)).load_all()[:10]
    else:
        pls = SearchQuerySet().using('pl').all().load_all()[:10]

    pl_list = []
    if pls:
        for pl in pls:
            if pl != None:
                pl_dict = {}
                pl_dict['pl_number'] = pl.pl_number
                pl_dict['job_number'] = pl.job_number
                pl_dict['sold_to'] = pl.sold_to
                pl_dict['ship_to'] = pl.ship_to
                pl_dict['status'] = pl.status
                if pl.date_shipped:
                    pl_dict['date_shipped'] = pl.date_shipped.isoformat()
                else:
                    pl_dict['date_shipped'] = None

                pl_list.append(pl_dict)
    try:
        page = int(request.GET.get('page','1'))
    except ValueError:
        page = 1
    paginator = Paginator(pl_list, 10)
    try:
        pages = paginator.page(page)
    except (EmptyPage, InvalidPage):
        pages = paginator.page(paginator.num_pages)

    results = pages.object_list

    data = json.dumps(results)
    return HttpResponse(data)

def search_shiping_list(request):
    query = request.GET.get('q','')
    if request.GET.get('q'):
        sls = SearchQuerySet().using('sl').filter(content=AutoQuery(query)).load_all()[:3]
    else:
        sls = SearchQuerySet().using('sl').all().load_all()[:10]

    sl_list = []
    if sls:
        for sl in sls:
            if sl != None:
                sl_dict = {}
                sl_dict['sl_number'] = sl.sl_number
                sl_dict['job_number'] = sl.job_number
                # import pdb; pdb.set_trace();
                if sl.sold_to:
                    slsoldtocontacts = SLSoldToContact.objects.filter(sl=sl.object)
                    soldto_contact_list = []
                    for sc in slsoldtocontacts:
                        soldto_contact = {}
                        soldto_contact['id'] = sc.id
                        soldto_contact['type'] = sc.contact_type
                        soldto_contact['number'] = sc.contact
                        soldto_contact['ext'] = ""
                        soldto_contact['contact_name'] = sc.contact_name
                        soldto_contact_list.append(soldto_contact)

                    sl_dict['sold_to'] = sl.sold_to
                    sl_dict['sold_to']['phones'] = soldto_contact_list
                    sl_dict['sold_to']['emails'] = []
                else:
                    sl_dict['sold_to'] = None

                if sl.ship_to:
                    slshiptocontacts = SLShipToContact.objects.filter(sl=sl.object)
                    shipto_contact_list = []
                    # import pdb; pdb.set_trace();
                    for sc in slshiptocontacts:
                        shipto_contact = {}
                        shipto_contact['id'] = sc.id
                        shipto_contact['type'] = sc.contact_type
                        shipto_contact['number'] = sc.contact
                        shipto_contact['ext'] = ""
                        shipto_contact['contact_name'] = sc.contact_name
                        shipto_contact_list.append(shipto_contact)

                    # import pdb; pdb.set_trace();
                    sl_dict['ship_to'] = sl.ship_to
                    sl_dict['ship_to']['phones'] = shipto_contact_list
                    sl_dict['ship_to']['emails'] = []
                else:
                    sl_dict['ship_to'] = None
                
                if sl.object.ordered_date:
                    sl_dict['ordered_date'] = sl.object.ordered_date.isoformat()
                else:
                    sl_dict['ordered_date'] = None
                if sl.object.date_required:
                    sl_dict['date_required'] = sl.object.date_required.isoformat()
                else:
                    sl_dict['date_required'] = None

                if sl.object.job_number:
                    sl_dict['job_number'] = sl.object.job_number.job_number
                else:
                    sl_dict['job_number'] = None

                sl_dict['customer_po_number'] = sl.object.customer_po_number
                sl_dict['customer_job_number'] = sl.object.customer_job_number
                if sl.object.ship_via:
                    sl_dict['ship_via'] = sl.object.ship_via.delivery_choice
                else:
                    sl_dict['ship_via'] = None
                if sl.sl_status:
                    sl_dict['sl_status'] = sl.status_verbose()
                items = []
                sl_items = ShippingItem.objects.filter(shipping_list=sl.object)
                for item in sl_items:
                    item_dict = {}
                    item_dict['item_number'] = item.item.item_number
                    item_dict['sl_item_id'] = item.id
                    item_dict['description'] = item.description

                    if item.ordered:
                        item_dict['ordered'] = item.ordered.to_eng_string()
                    else:
                        item_dict['ordered'] = None

                    if item.shipped:
                        item_dict['shipped'] = item.shipped.to_eng_string()
                    else:
                        item_dict['shipped'] = None

                    if item.shipped_total_to_date:
                        item_dict['shipped_total_to_date'] = item.shipped_total_to_date.to_eng_string()
                    else:
                        item_dict['shipped_total_to_date'] = None
                    if item.shipped_by:
                        item_dict['shipped_by'] = {}
                        item_dict['shipped_by']['id'] = item.shipped_by.id
                        item_dict['shipped_by']['username'] = item.shipped_by.username
                    else:
                        item.shipped_by = None

                    if item.last_shipped:
                        item_dict['last_shipped_date'] = item.last_shipped.isoformat()
                    else:
                        item_dict['last_shipped_date'] = None
                    if item.backordered:
                        item_dict['backordered'] = item.backordered.to_eng_string()
                    if item.filled:
                        item_dict['filled'] = item.filled.to_eng_string()
                    item_dict['item_ship_status'] = item.item_ship_status_verbose()
                    items.append(item_dict)

                sl_dict['items'] = items
                sl_list.append(sl_dict)
    try:
        page = int(request.GET.get('page','1'))
    except ValueError:
        page = 1
    paginator = Paginator(sl_list, 10)
    try:
        pages = paginator.page(page)
    except (EmptyPage, InvalidPage):
        pages = paginator.page(paginator.num_pages)

    results = pages.object_list

    data = json.dumps(results)
    return HttpResponse(data)

def add_packing_list(request):
    cuser =request.user
    sv = SystemVariable.objects.get(id=1)
    next_pl_number = sv.next_pl_number
    users = User.objects.all().exclude(id__in=[-1]).order_by("username")
    dcs = DeliveryChoice.objects.all()
    if request.method == 'POST':
        # import pdb; pdb.set_trace();
        pl_number = request.POST.get("pl_number", "")
        sl_number = request.POST.get("sl_number", "")
        if pl_number != "":
            pl = PackingList.objects.get(pl_number=pl_number)
            pl_form = PackingListForm(request.POST, instance=pl, request=request, action='update')
        else:
            pl_form = PackingListForm(request.POST, request=request, action='new')

        sl_item_ids = request.POST.getlist("sl_item_ids","")
        sl_item_unit = request.POST.getlist('sl_item_unit',"")
        sl_item_ordered = request.POST.getlist('sl_item_ordered')
        sl_item_shipped = request.POST.getlist('sl_item_shipped',"")

        pl_item_ids = request.POST.getlist("pl_item_ids","")
        pl_item_unit = request.POST.getlist('pl_item_unit',"")
        pl_item_ordered = request.POST.getlist('pl_item_ordered')
        pl_item_shipped = request.POST.getlist('pl_item_shipped',"")
        deleted_items = request.POST.getlist("removed_item")

        if pl_form.is_valid():
            try:
                pl = pl_form.save()
                if sl_number:
                    sl = ShippingList.objects.get(sl_number=sl_number)
                    pl.sl = sl
            except Exception, e:
                messages.warning(request, "Packing list cant saved.")
                return HttpResponseRedirect("/purchase/add-pl/")
            

            if deleted_items:
                for deleted_item in deleted_items:
                    di = PackingItem.objects.get(id=deleted_item)
                    sli = di.sl_item
                    sli.shipped = sli.shipped - di.qty_shipped
                    sli.backordered = sli.backordered + di.qty_shipped
                    sli.shipped_total_to_date = sli.shipped
                    sli.save()
                    di.delete()
            
            if sl_item_ids:
                for i, item in enumerate(sl_item_ids):
                    ship_item = ShippingItem.objects.get(id=sl_item_ids[i])
                    try:
                        packing_item = PackingItem.objects.create(pl=pl)
                        packing_item.sl_item = ship_item
                    except Exception, e:
                        raise e
                    
                    packing_item.unit = sl_item_unit[i]
                    # if packing_item.qty_shipped:
                    #     packing_item.qty_shipped = Decimal(sl_item_shipped[i]) + packing_item.qty_shipped
                    # else:
                    packing_item.qty_shipped = Decimal(sl_item_shipped[i])

                    packing_item.qty_ordered = ship_item.ordered
                    packing_item.qty_bo = ship_item.backordered - packing_item.qty_shipped
                    packing_item.save()

                    ship_item.backordered = ship_item.backordered - packing_item.qty_shipped
                    ship_item.shipped = ship_item.shipped_total_to_date + packing_item.qty_shipped
                    ship_item.shipped_total_to_date = ship_item.shipped
                    ship_item.save()


            if pl_item_ids:
                for i, item in enumerate(pl_item_ids):
                    try:
                        packing_item = PackingItem.objects.get(id=item)
                        packing_item.pl = pl
                        ship_item = packing_item.sl_item
                    except Exception, e:
                        pass

                    packing_item.unit = pl_item_unit[i]
                    ship_item.backordered = ship_item.backordered + packing_item.qty_shipped
                    ship_item.shipped_total_to_date = ship_item.shipped_total_to_date - packing_item.qty_shipped
                    # ship_item.shipped = ship_item.shipped_total_to_date

                    packing_item.qty_shipped = Decimal(pl_item_shipped[i])
                    packing_item.qty_ordered = ship_item.ordered
                    packing_item.qty_bo = ship_item.backordered - packing_item.qty_shipped
                    packing_item.save()

                    ship_item.backordered = ship_item.backordered - packing_item.qty_shipped
                    ship_item.shipped = ship_item.shipped_total_to_date + packing_item.qty_shipped
                    ship_item.shipped_total_to_date = ship_item.shipped
                    ship_item.save()




            '''
            if pl_number == "":
                deleted_items = request.POST.getlist("removed_item")
                if deleted_items:
                    for deleted_item in deleted_items:
                        di = PackingItem.objects.get(id=deleted_item)
                        di.delete()
                for i, item in enumerate(items):
                    item_obj = Item.objects.get(item_number=item)
                    if sl_id:
                        ship_item = ShippingItem.objects.get(id=sl_item_ids[i])
                    if pl_item_ids[i] != 'new':
                        try:
                            packing_item = PackingItem.objects.get(id=pl_item_ids[i])
                        except PackingItem.DoesNotExist:
                            raise
                    else:
                        if sl_id:
                            packing_item = PackingItem.objects.create(shipping_item=ship_item)
                        else:
                            packing_item = PackingItem.objects.create()
                        # For new packeing item
                        packing_item.status = 0
                    
                    packing_item.unit = item_unit[i]
                    if not item_shipped[i] == 'null' and not item_shipped[i] == 'undefined':
                        if packing_item.qty_shipped:
                            packing_item.qty_shipped = Decimal(item_shipped[i]) + packing_item.qty_shipped
                        else:
                            packing_item.qty_shipped = Decimal(item_shipped[i])
                    # if not item_ordered[i] == 'null' and not item_ordered[i] == 'undefined':
                    #     packing_item.qty_ordered = Decimal(item_ordered[i])
                    # if not item_qtybo[i] == 'null' and not item_qtybo[i] == 'undefined':
                    #     packing_item.qty_bo = Decimal(item_qtybo[i])
                    # packing_item.ship_status = 0
                    packing_item.pl = pl
                    packing_item.search_string = ship_item.shipping_list.sl_number + " "+ ship_item.item.item_number
                    # packing_item.save()

                    # import pdb; pdb.set_trace();

                    # Update ShippingItem object to check all its ordered item is shipped.
                    if sl_number:
                        if ship_item.shipped_total_to_date:
                            ship_item.shipped_total_to_date = ship_item.shipped_total_to_date + Decimal(item_shipped[i])
                        else:
                            ship_item.shipped_total_to_date = Decimal(item_shipped[i])
                        ship_item.last_shipped = datetime.datetime.now()
                        if item_shipped[i]:
                            ship_item.shipped = Decimal(item_shipped[i])
                        
                        if ship_item.ordered <= ship_item.shipped_total_to_date:
                            ship_item.item_ship_status = 2
                            ship_item.backordered = 0
                        else:
                            ship_item.item_ship_status = 1
                            ship_item.backordered = ship_item.ordered - ship_item.shipped_total_to_date

                        packing_item.qty_bo = ship_item.backordered
                        packing_item.qty_ordered = ship_item.ordered
                        ship_item.save()
                    else:
                        packing_item.qty_bo = packing_item.qty_ordered - packing_item.qty_shipped

                    packing_item.save()

                    # Update inventory item for this action
                    item = ship_item.item
                    # item.stock_status_type = 
                    item.quantity_on_hand = item.quantity_on_hand - packing_item.qty_shipped
                    item.save()

                
                if sl_id:
                    sl = ShippingList.objects.get(id=sl_id)
                    sl_unshipped_items = ShippingItem.objects.filter(shipping_list=sl, item_ship_status__lte=1)
                    if not sl_unshipped_items:
                        sl.sl_status = 2
                    sl.save()
            '''
            

            pl.save()
            return HttpResponseRedirect("/purchase/packing-list/")
        else:
            return HttpResponseRedirect("/purchase/add-pl/")
    else:
        form_init = {
            'shipped_by': cuser,
            'generated_by': cuser
        }
        pl_form = PackingListForm(initial=form_init)
        return render(request, "purchase/add-pl.html", 
            {'pl_form': pl_form, 'users': users, 'cuser': cuser, 'dcs': dcs, 'next_pl_number': next_pl_number})


def pl_list(request):
    # import pdb; pdb.set_trace()
    packing_list = PackingList.objects.filter(status__lte=2)
    pl_list = []
    for pl in packing_list:
        pack = {}
        pack['customer_po_number'] = pl.customer_po_number
        pack['pl_number'] = pl.pl_number
        if pl.sl:
            pack['sl_number'] = pl.sl.sl_number
        if pl.date_issued:
            pack['date_issued'] = pl.date_issued.isoformat()
        if pl.date_shipped:
            pack['date_shipped'] = pl.date_shipped.isoformat()
        
        if pl.sold_to:
            pack['sold_to'] = {}
            pack['sold_to']['contact_name'] = pl.sold_to.contact_name
            phone_list = ContactPhone.objects.filter(contact=pl.sold_to)
            if phone_list:
                pack['sold_to']['phones'] = []
                for ph in phone_list:                    
                    phone = {}
                    phone['type'] = ph.phone_type.phone_type
                    phone['number'] = ph.phone
                    phone['phone_ext'] = ph.phone_ext
                    pack['sold_to']['phones'].append(phone)
            else:
                pack['sold_to']['phones'] = None
            
            email_list = ContactEmailAddress.objects.filter(contact=pl.sold_to)
            if email_list:
                pack['sold_to']['emails'] = []
                for em in emails:
                    email = {}
                    email['email_address_type'] = em.email_address_type.email_type
                    email['email_address'] = em.email_address
                    pack['sold_to']['emails'].append(email)
            else:
                pack['sold_to']['emails'] = None
            
            pack['sold_to']['id'] = pl.sold_to.id
        else:
            pack['sold_to'] = None

        if pl.ship_to:
            pack['ship_to'] = {}
            pack['ship_to']['contact_name'] = pl.ship_to.contact_name
            phone_list = ContactPhone.objects.filter(contact=pl.ship_to)
            if phone_list:
                pack['ship_to']['phones'] = []
                for ph in phone_list:                    
                    phone = {}
                    phone['type'] = ph.phone_type.phone_type
                    phone['number'] = ph.phone
                    phone['phone_ext'] = ph.phone_ext
                    pack['ship_to']['phones'].append(phone)
            else:
                pack['ship_to']['phones'] = None
            
            email_list = ContactEmailAddress.objects.filter(contact=pl.ship_to)
            if email_list:
                pack['ship_to']['emails'] = []
                for em in emails:
                    email = {}
                    email['email_address_type'] = em.email_address_type.email_type
                    email['email_address'] = em.email_address
                    pack['ship_to']['emails'].append(email)

            else:
                pack['ship_to']['emails'] = None
            
            pack['ship_to']['id'] = pl.ship_to.id
        else:
            pack['ship_to'] = None

        if pl.customer_broker:
            pack['customer_broker'] = {}
            pack['customer_broker']['contact_name'] = pl.customer_broker.contact_name
            phone_list = ContactPhone.objects.filter(contact=pl.customer_broker)
            if phone_list:
                pack['customer_broker']['phones'] = []
                for ph in phone_list:                    
                    phone = {}
                    phone['type'] = ph.phone_type.phone_type
                    phone['number'] = ph.phone
                    phone['phone_ext'] = ph.phone_ext
                    pack['customer_broker']['phones'].append(phone)
            else:
                pack['customer_broker']['phones'] = None
            
            email_list = ContactEmailAddress.objects.filter(contact=pl.customer_broker)
            if email_list:
                pack['customer_broker']['emails'] = []
                for em in emails:
                    email = {}
                    email['email_address_type'] = em.email_address_type.email_type
                    email['email_address'] = em.email_address
                    pack['customer_broker']['emails'].append(email)

            else:
                pack['customer_broker']['emails'] = None
            
            pack['customer_broker']['id'] = pl.customer_broker.id
        else:
            pack['customer_broker'] = None


        if pl.shipped_by:
            pack['shipped_by'] = pl.shipped_by.username
        else:
            pack['shipped_by'] = None
        if pl.nel_packing_slip:
            pack['nel_packing_slip'] = pl.nel_packing_slip
        else:
            pack['nel_packing_slip'] = None
        
        if pl.job_number:
            job = {}
            job['job_number'] = pl.job_number.job_number
            job['job_name'] = pl.job_number.job_name
            job['id'] = pl.job_number.id
            pack['schedule_job'] = job
        else:
            pack['schedule_job'] = None

        if pl.generated_by:
            pack['generated_by'] = pl.generated_by.username
            pack['generated_by_id'] = pl.generated_by.id
        else:
            pack['generated_by'] = None
        
        if pl.ship_via:
            pack['ship_via'] = pl.ship_via.delivery_choice
            pack['ship_via_id'] = pl.ship_via.id
        else:
            pack['ship_via'] = None

        pack['hold_at_dept_for_pickup'] = pl.hold_at_dept_for_pickup
        
        pack['status'] = pl.status_verbose()
        if pl.invoiced_on:
            pack['invoiced_on'] = pl.invoiced_on.isoformat()
        else:
            pack['invoiced_on'] = None
        pack['order_type'] = pl.order_type
        if pl.freight_charges:
            pack['freight_charges'] = float(pl.freight_charges)
        else:
            pack['freight_charges'] = None

        pack['search_string'] = pl.search_string

        pl_items = PackingItem.objects.filter(pl=pl)
        items=[]
        for it in pl_items:
            # import pdb; pdb.set_trace()
            item = {}
            if it.sl_item:
                item['sl_item_id'] = it.sl_item.id
                item['item_number'] = it.sl_item.item.item_number
            item['description'] = it.description
            item['unit'] = it.unit
            if it.qty_ordered:
                item['qty_ordered'] = float(it.qty_ordered)
            if it.qty_bo:
                item['qty_bo'] = float(it.qty_bo)
            if it.qty_shipped:
                item['qty_shipped'] = float(it.qty_shipped)
            item['status'] = it.status
            # item['pl'] = it.pl.id
            item['search_string'] = it.search_string
            items.append(item)
        pack['items'] = items


        
        pl_list.append(pack)

    json_pending_list = json.dumps(pl_list)
    return HttpResponse(json_pending_list, mimetype='application/json')


def edit_packing_list(request, id):
    pl = PackingList.objects.get(id=id)
    if request.method == 'POST':
        
        pl_form = PackingListForm(request.POST, instance=pl)
        
        item_qtybo = request.POST.getlist('item_qtybo')
        item_ordered = request.POST.getlist('item_ordered')
        items = request.POST.getlist('item_item')
        item_shipped = request.POST.getlist('item_shipped')
        item_unit = request.POST.getlist('item_unit')
        pl_item_id = request.POST.getlist('item_id')
        sl_item_ids = request.POST.getlist("sl_item_id")

        sl_item_id = request.POST.getlist('sl_item_id')
        plitems = request.POST.getlist("plitems")
        myset = set(plitems) - set(pl_item_id)
        removed_items = list(myset)

        if pl_form.is_valid():
            new_pl = pl_form.save()
            for i, item in enumerate(items):
                item_obj = Item.objects.get(item_number=item)
                try:
                    packing_item = PackingItem.objects.get(id=pl_item_id[i])
                except:
                    sl_item = ShippingItem.objects.get(id=sl_item_ids[i])
                    packing_item = PackingItem(shipping_item=sl_item, description=item_obj.description)
                    packing_item.ship_status = 0
                    packing_item.pl = new_pl
                    packing_item.search_string = sl_item.shipping_list.sl_number + " "+ sl_item.item.item_number

                if item_ordered[i] != '':
                    packing_item.qty_ordered = Decimal(item_ordered[i])
                if item_shipped[i] != '':
                    packing_item.qty_shipped = Decimal(item_shipped[i])
                if item_qtybo[i] != '':
                    packing_item.qty_bo = Decimal(item_qtybo[i])
                if item_unit[i] != '':
                    packing_item.unit = item_unit[i]
                
                packing_item.save()

            new_pl.search_string = pl.pl_number + ' ' + pl.sl_number.sl_number + ' '
            if new_pl.sold_to:
                new_pl.search_string += new_pl.sold_to.contact_name + ' '

            new_pl.save()
            
            for rmitem in removed_items:
                remove_item = PackingItem.objects.get(id=rmitem)
                remove_item.delete()
            return HttpResponseRedirect("/purchase/packing-list/")
    else:
        pl_form = PackingListForm(instance=pl)
        pl_items = PackingItem.objects.filter(pl=pl)
        pl_form.fields['pl_number'].widget.attrs['readonly'] = True
        pl_form.fields['sl_number'].widget.attrs['readonly'] = True
        pl_form.fields['generated_by'].widget.attrs['readonly'] = True
    
    return render(request, 'purchase/edit-pl.html', {'pl_form': pl_form, 'pl_id': id, 'pl_items': pl_items})


def get_packing_list(request, pl_number):
    pl = PackingList.objects.get(pl_number=pl_number)
    serializer = PackingListSerializer(pl, context={'request': request})
    pk_items = PackingItem.objects.filter(pl=pl)
    data = json.dumps(serializer.data)
    return HttpResponse(data, content_type='application/json')

# supplier = Supplier.objects.get(id=supplier_id)
# supplier_company = SupplierCompany.objects.get(supplier=supplier)
# serializer = CompanySerializer(supplier_company)
# data = json.dumps(serializer.data)
# return HttpResponse(data, content_type='application/json')

def get_pl_items(request, pl_number=None):
    if pl_number:
        try:
            pl = PackingList.objects.get(pl_number=pl_number)
            pl_items = PackingItem.objects.filter(pl=pl, status=0)
        except PackingList.DoesNotExist:
            json_posts = {
                'PurchaseOrder DoesNotExist',
            }
            return HttpResponse(json_posts, mimetype='application/json')
    else:
        pl_items = PackingItem.objects.filter(status=0)
    
    
    plitems = []
    for item in pl_items:
        item_dict = {}
        item_dict['id'] = item.id
        item_dict['item_number'] = item.sl_item.item.item_number
        item_dict['sl_item_id'] = item.sl_item.id
        item_dict['item_number'] = item.sl_item.item.item_number
        item_dict['description'] = item.description
        item_dict['unit'] = item.unit
        if item.qty_ordered:
            item_dict['qty_ordered'] = float(item.qty_ordered)

        if item.qty_bo:
            item_dict['qty_bo'] = float(item.qty_bo)
        else:
            item_dict['qty_bo'] = 0.0

        if item.qty_shipped:
            item_dict['qty_shipped'] = float(item.qty_shipped)
        if item.sl_item.item.retail_price:
            item_dict['price'] = float(item.sl_item.item.retail_price)
            item_dict['sub_total'] = float(item.qty_shipped) * float(item.sl_item.item.retail_price)
        item_dict['shipped'] = float(item.qty_shipped)
            
        item_dict['pl'] = item.pl.pl_number

        
        
        plitems.append(item_dict)
    

    json_posts = json.dumps(plitems)
    return HttpResponse(json_posts, mimetype='application/json')

@csrf_exempt
def delete_packing_list(request):
    # import pdb; pdb.set_trace()
    plid = request.POST.get('pl_id', '')
    if plid:
        pl = PackingList.objects.get(id=plid)
        pl.status = 3
        pl.save()
        return HttpResponse(plid)
    else:
        return HttpResponse('failed')

def view_packing_list(request, id):
    # import pdb; pdb.set_trace()
    pl = PackingList.objects.get(pl_number=id)
    pl_items = pl.pl_items.all()
    return render(request, 'purchase/view-pl.html', {'pl': pl, 'pl_items': pl_items})

def packing_list(request):
    return render(request, "purchase/parking-list.html", {})


@csrf_exempt
def add_shipping_list(request):
    ship_vias = DeliveryChoice.objects.filter(is_active=True)
    # sv = SystemVariable.objects.get(id=1)
    # next_sl_number = sv.next_sl_number
    if request.method == 'POST':
        # import pdb; pdb.set_trace();
        user = request.user 
        sl_number = request.POST.get("sl_number","")
        
        if sl_number:
            try:
                sl = ShippingList.objects.get(sl_number=sl_number)
                sl_form = ShippingListForm(request.POST, request=request, instance=sl, action='update')    
            except ShippingList.DoesNotExist:
                sl_form = ShippingListForm(request.POST, request=request, action='new')
        else:
            try:
                sv = SystemVariable.objects.get(id=1)
                request.POST['sl_number'] = sv.get_next_sl_number
                sl_form = ShippingListForm(request.POST, request=request, action='new')    
            except Exception, e:
                raise e

        item_ordered = request.POST.getlist('item_ordered')
        if sl_form.is_valid():
            try:
                sl = sl_form.save()

                form_action = request.POST.get("form_action")
                if form_action == 'new':
                    # ============= add contacts for sold_to ==========

                    sold_to_phone_numbers = request.POST.getlist("sl_sold_to_phone_number", "")
                    sl_sold_to_emails = request.POST.getlist("sl_sold_to_email", "")
                    if sold_to_phone_numbers:
                        sl_sold_to_phone_types = request.POST.getlist("sl_sold_to_phone_type", "")
                        sl_sold_to_phone_exts = request.POST.getlist("sl_sold_to_phone_ext", "")
                        sl_sold_to_phone_attentions = request.POST.getlist("sl_sold_to_phone_attention", "")
                        i=0
                        for ph_num in sold_to_phone_numbers:
                            ph_type = sl_sold_to_phone_types[i]
                            ph_ext = sl_sold_to_phone_exts[i]
                            ph_number = ph_num
                            contact_name = sl_sold_to_phone_attentions[i]
                            if ph_ext != "":
                                phone_number = str(ph_number)+"-"+str(ph_ext)
                            else:
                                phone_number = str(ph_number)
                            sl_sold_contact = SLSoldToContact(sl=sl, contact_type=str(ph_type), contact=phone_number, contact_name=contact_name)
                            sl_sold_contact.save()
                            i = i+1
                    
                    if sl_sold_to_emails:
                        sl_sold_to_email_types = request.POST.getlist("sl_sold_to_email_type", "")
                        sl_sold_to_email_attentions = request.POST.getlist("sl_sold_to_email_attention", "")
                        i=0
                        for email in sl_sold_to_emails:
                            e_type = sl_sold_to_email_types[i]
                            contact_name = sl_sold_to_email_attentions[i]
                            sl_sold_contact = SLSoldToContact(sl=sl, contact_type=str(e_type), 
                                contact=email, contact_name=contact_name)
                            sl_sold_contact.save()
                            i = i+1

                    sl_soldto_extra_contacts = request.POST.getlist("sl_soldto_extra_contacts", "")
                    for extra_contact_id in sl_soldto_extra_contacts:
                        sl_sold_contact = SLSoldToContact.objects.get(id=extra_contact_id)
                        sl_sold_contact.sl = sl
                        sl_sold_contact.save()


                # ============= add contacts for ship_to ==========
                    # import pdb; pdb.set_trace();
                    ship_to_contact_ids = request.POST.getlist("sl_ship_to_contact_id")
                    ship_to_phone_numbers = request.POST.getlist("sl_ship_to_phone_number", "")
                    sl_ship_to_emails = request.POST.getlist("sl_ship_to_email", "")
                    if ship_to_phone_numbers:
                        sl_ship_to_phone_types = request.POST.getlist("sl_ship_to_phone_type", "")
                        sl_ship_to_phone_exts = request.POST.getlist("sl_ship_to_phone_ext", "")
                        sl_ship_to_phone_attentions = request.POST.getlist("sl_ship_to_phone_attention", "")
                        i=0
                        for ph_num in ship_to_phone_numbers:
                            ph_type = sl_ship_to_phone_types[i]
                            ph_ext = sl_ship_to_phone_exts[i]
                            ph_number = ph_num
                            contact_name = sl_ship_to_phone_attentions[i]
                            if ph_ext != "":
                                phone_number = str(ph_number)+"-"+str(ph_ext)
                            else:
                                phone_number = str(ph_number)
                            sl_ship_contact = SLShipToContact(sl=sl, contact_type=str(ph_type), contact=phone_number, contact_name=contact_name)
                            sl_ship_contact.save()
                            i = i+1
                    
                    if sl_ship_to_emails:
                        sl_ship_to_email_types = request.POST.getlist("sl_ship_to_email_type", "")
                        sl_ship_to_email_attentions = request.POST.getlist("sl_ship_to_email_attention", "")
                        i=0
                        for email in sl_ship_to_emails:
                            e_type = sl_ship_to_email_types[i]
                            contact_name = sl_ship_to_email_attentions[i]
                            sl_sold_contact = SLShipToContact(sl=sl, contact_type=str(e_type), 
                                contact=email, contact_name=contact_name)
                            sl_ship_contact.save()
                            i = i+1


                    sl_shipto_extra_contacts = request.POST.getlist("sl_shipto_extra_contacts", "")
                    for extra_contact_id in sl_shipto_extra_contacts:
                        sl_sold_contact = SLShipToContact.objects.get(id=extra_contact_id)
                        sl_sold_contact.sl = sl
                        sl_sold_contact.save()
                
                else:
                    sl_soldto_extra_contacts = request.POST.getlist("sl_soldto_extra_contacts", "")
                    for extra_contact_id in sl_soldto_extra_contacts:
                        sl_sold_contact = SLSoldToContact.objects.get(id=extra_contact_id)
                        sl_sold_contact.sl = sl
                        sl_sold_contact.save()

                    sl_shipto_extra_contacts = request.POST.getlist("sl_shipto_extra_contacts", "")
                    for extra_contact_id in sl_shipto_extra_contacts:
                        sl_sold_contact = SLShipToContact.objects.get(id=extra_contact_id)
                        sl_sold_contact.sl = sl
                        sl_sold_contact.save()

                    



            except Exception, e:
                raise e
            
            items = []
            items = request.POST.getlist('added_item_number')
            deleted_items = request.POST.getlist("removed_item")
            if deleted_items:
                for deleted_item in deleted_items:
                    si = ShippingItem.objects.get(id=deleted_item)
                    si.delete()
            for i, item in enumerate(items):
                item_obj = Item.objects.get(item_number=item)
                try:
                    shipping_item, yes = ShippingItem.objects.get_or_create(item=item_obj, shipping_list=sl)
                    shipping_item.description = item_obj.description
                except Exception, e:
                    # shipping_item= ShippingItem.objects.get(item=item_obj, shipping_list=sl)
                    pass

                if item_ordered[i] != '':
                    shipping_item.ordered = item_ordered[i]
                    if shipping_item.shipped_total_to_date:
                        shipping_item.backordered = Decimal(shipping_item.ordered) - shipping_item.shipped_total_to_date
                    else:
                        shipping_item.backordered = Decimal(shipping_item.ordered)
                # if item_shipped[i] !='':
                #     shipping_item.shipped = item_shipped[i]
                # if shipped_total_to_date[i] != '':
                #     shipping_item.shipped_total_to_date = shipped_total_to_date[i]
                # if item_backordered[i] != '':
                #     shipping_item.backordered = item_backordered[i]
                
                # item_ship_status value will only be changed in PL after actual shipment.
                shipping_item.item_ship_status = 0
                shipping_item.shipped_by = user
                shipping_item.save()
            
            # sl.search_string = sl.sl_number + " " + sl.customer_po_number + sl.customer_job_number
            # No need for search string now as we are using elasticsearch for search

            # if sl.job_number:
            #     sl.search_string += sl.job_number.job_number
            # if sl.sold_to:
            #     sl.search_string += sl.sold_to.contact_name
            # if sl.ship_via:
            #     sl.search_string += sl.ship_via.delivery_choice

            sl.sl_status = 0
            sl.save()

            
            return HttpResponseRedirect("/purchase/shipping-list/")
        else:
            return render(request, "purchase/sl-add.html", {'sl_form': sl_form, 'ship_vias': ship_vias})
    else:
        
        sl_form = ShippingListForm()
        return render(request, "purchase/sl-add.html", 
            {'sl_form': sl_form, 'ship_vias': ship_vias})

def get_sl_json(request):
    # import pdb; pdb.set_trace()
    cuser = request.user
    all_sl = ShippingList.objects.filter(sl_status__lt=2)
    sl_list = []
    for sl in all_sl:
        sl_dict = {}
        if cuser.is_superuser or cuser.has_perm("purchase.change_shippinglist"):
            sl_dict['can_edit'] = True
        else:
            sl_dict['can_edit'] = False

        if cuser.is_superuser or cuser.has_perm("purchase.delete_shippinglist"):
            sl_dict['can_delete'] = True
        else:
            sl_dict['can_delete'] = False

        sl_dict['sl_number'] = sl.sl_number
        if sl.sold_to:
            sl_dict['sold_to'] = {}
            sl_dict['sold_to']['contact_name'] = sl.sold_to.contact_name
            phone_list = ContactPhone.objects.filter(contact=sl.sold_to)
            if phone_list:
                sl_dict['sold_to']['phones'] = []
                for ph in phone_list:                    
                    phone = {}
                    phone['phone_type'] = ph.phone_type.phone_type
                    phone['phone'] = ph.phone
                    phone['phone_ext'] = ph.phone_ext
                    sl_dict['sold_to']['phones'].append(phone)
            else:
                sl_dict['sold_to']['phones'] = None
            
            email_list = ContactEmailAddress.objects.filter(contact=sl.sold_to)

            if email_list:
                sl_dict['sold_to']['emails'] = []
                for em in emails:
                    email = {}
                    email['email_address_type'] = em.email_address_type.email_type
                    email['email_address'] = em.email_address
                    sl_dict['sold_to']['emails'].append(email)
            else:
                sl_dict['sold_to']['emails'] = None
            
            sl_dict['sold_to']['id'] = sl.sold_to.id
        else:
            sl_dict['sold_to'] = None

        if sl.ship_to:
            sl_dict['ship_to'] = {}
            sl_dict['ship_to']['contact_name'] = sl.ship_to.contact_name
            phone_list = ContactPhone.objects.filter(contact=sl.ship_to)
            if phone_list:
                sl_dict['ship_to']['phones'] = []
                for ph in phone_list:                    
                    phone = {}
                    phone['phone_type'] = ph.phone_type.phone_type
                    phone['phone'] = ph.phone
                    phone['phone_ext'] = ph.phone_ext
                    sl_dict['ship_to']['phones'].append(phone)
            else:
                sl_dict['ship_to']['phones'] = None
            
            email_list = ContactEmailAddress.objects.filter(contact=sl.ship_to)
            if email_list:
                sl_dict['ship_to']['emails'] = []
                for em in emails:
                    email = {}
                    email['email_address_type'] = em.email_address_type.email_type
                    email['email_address'] = em.email_address
                    sl_dict['ship_to']['emails'].append(email)

            else:
                sl_dict['ship_to']['emails'] = None
            
            sl_dict['ship_to']['id'] = sl.ship_to.id
        else:
            sl_dict['ship_to'] = None
        
        if sl.ordered_date:
            sl_dict['ordered_date'] = sl.ordered_date.isoformat()
        else:
            sl_dict['ordered_date'] = None
        
        if sl.date_required:
            sl_dict['date_required'] = sl.date_required.isoformat()
        else:
            sl_dict['date_required'] = None

        if sl.job_number:
            sl_dict['job_number'] = sl.job_number.job_number
            sl_dict['job_number_id'] = sl.job_number.id
        else:
            sl_dict['job_number'] = None
        sl_dict['customer_po_number'] = sl.customer_po_number
        sl_dict['customer_job_number'] = sl.customer_job_number
        
        if sl.ship_via:
            sl_dict['ship_via'] = sl.ship_via.delivery_choice
            sl_dict['ship_via_id'] = sl.ship_via.id
        else:
            sl_dict['ship_via'] = None

        sl_items = ShippingItem.objects.filter(shipping_list=sl)
        item_list = []
        for sl_item in sl_items:
            item = {}
            item['item'] = sl_item.item.item_number
            item['sl_item_id'] = sl_item.id
            item['description'] = sl_item.description
            if sl_item.ordered:
                item['ordered'] = sl_item.ordered.to_eng_string()
            else:
                item['ordered'] = None
            if sl_item.shipped:
                item['shipped'] = sl_item.shipped.to_eng_string()
            else:
                item['shipped'] = None
            if sl_item.shipped_total_to_date:
                item['shipped_total_to_date'] = sl_item.shipped_total_to_date.to_eng_string()
            else:
                item['shipped_total_to_date'] = None
            if sl_item.shipped_by:
                item['shipped_by'] = sl_item.shipped_by.username
                item['shipped_by_id'] = sl_item.shipped_by.id
            else:
                item['shipped_by'] = None
            if sl_item.last_shipped:
                item['last_shipped'] = sl_item.last_shipped.isoformat()
            else:
                item['last_shipped'] = None
            if sl_item.backordered:
                item['backordered'] = sl_item.backordered.to_eng_string()
            else:
                item['backordered'] = None

            if sl_item.filled:
                item['filled'] = sl_item.filled.to_eng_string()
            else:
                item['filled'] = None
            item['item_ship_status'] = sl_item.item_ship_status
            item['search_string'] = sl_item.search_string
            item_list.append(item)

        sl_dict['items'] = item_list

        
        sl_dict['search_string'] = sl.search_string
        sl_list.append(sl_dict)
    json_posts = json.dumps(sl_list)
    return HttpResponse(json_posts, mimetype='application/json')

def get_sl_json_by_id(request, sl_id):
    sl = ShippingList.objects.get(sl_number=sl_id)
    sl_dict = {}
    
    sl_dict['sl_number'] = sl.sl_number
    if sl.sold_to:
        sl_dict['sold_to'] = {}
        sl_dict['sold_to']['id'] = sl.sold_to.id
        sl_dict['sold_to']['contact_name'] = sl.sold_to.contact_name
        sl_dict['sold_to']['city'] = sl.sold_to.city
        # sl_dict['sold_to']['phones'] = sl.sold_to.contact_phone.all()
        sl_dict['sold_to']['phones'] = []
        for em in sl.sold_to.contact_phone.all():
            email = {}
            email['phone'] = em.phone
            email['phone_ext'] = em.phone_ext
            sl_dict['sold_to']['phones'].append(email)
        # sl_dict['sold_to']['emails'] = sl.sold_to.contact_emails.all()

        sl_dict['sold_to']['emails'] = []
        for em in sl.sold_to.contact_emails.all():
            email = {}
            if em.email_address_type:
                email['email_type'] = em.email_address_type.email_type
            else:
                email['email_type'] = "Personal"
            email['email_address'] = em.email_address
            sl_dict['sold_to']['emails'].append(email)
    else:
        sl_dict['sold_to'] = None

    if sl.ship_to:
        sl_dict['ship_to'] = {}
        sl_dict['ship_to']['id'] = sl.ship_to.id
        sl_dict['ship_to']['contact_name'] = sl.ship_to.contact_name
        sl_dict['ship_to']['city'] = sl.ship_to.city
        # sl_dict['ship_to']['phones'] = sl.ship_to.contact_phone.all()
        sl_dict['ship_to']['phones'] = []
        for em in sl.ship_to.contact_phone.all():
            email = {}
            email['phone'] = em.phone
            email['phone_ext'] = em.phone_ext
            sl_dict['ship_to']['phones'].append(email)

        sl_dict['ship_to']['emails'] = []
        # import pdb; pdb.set_trace();
        for em in sl.ship_to.contact_emails.all():
            email = {}
            if em.email_address_type:
                email['email_type'] = em.email_address_type.email_type
            else:
                email['email_type'] = "Personal"
            email['email_address'] = em.email_address
            sl_dict['ship_to']['emails'].append(email)

    else:
        sl_dict['ship_to'] = None

    if sl.ordered_date:
        sl_dict['ordered_date'] = sl.ordered_date.isoformat()
    if sl.date_required:
        sl_dict['date_required'] = sl.date_required.isoformat()
    if sl.job_number:
        sl_dict['job_number'] = sl.job_number.job_number
    sl_dict['customer_po_number'] = sl.customer_po_number
    sl_dict['customer_job_number'] = sl.customer_job_number
    if sl.ship_via:
        sl_dict['ship_via'] = sl.ship_via.delivery_choice
    else:
        sl_dict['ship_via'] = None
    sl_dict['sl_status'] = sl.sl_status
    
    sl_items = ShippingItem.objects.filter(item_ship_status__lt = 2, shipping_list__sl_number=sl.sl_number)

    sl_item_list = []
    for sl_item in sl_items:
        sl_item_dict = {}
        sl_item_dict['sl_item_id'] = sl_item.id
        sl_item_dict['item_number'] = sl_item.item.item_number
        if sl_item.item.quantity_on_hand:
            sl_item_dict['quantity_on_hand'] = float(sl_item.item.quantity_on_hand)
        else:
            sl_item_dict['quantity_on_hand'] = None
        sl_item_dict['description'] = sl_item.description
        if sl_item.ordered:
            sl_item_dict['ordered'] = float(sl_item.ordered)
        else:
            sl_item_dict['ordered'] = None

        if sl_item.item.item_unit_measure:
            sl_item_dict['item_unit_measure'] = sl_item.item.item_unit_measure.unit_name
            sl_item_dict['item_unit_measure_id'] = sl_item.item.item_unit_measure.id
        else:
            sl_item_dict['item_unit_measure'] = None
        if sl_item.shipped:
            sl_item_dict['shipped'] = float(sl_item.shipped)
        else:
            sl_item_dict['shipped'] = None
        if sl_item.shipped_total_to_date:
            sl_item_dict['total_shipped'] = float(sl_item.shipped_total_to_date)
        else:
            sl_item_dict['total_shipped'] = None

        if sl_item.filled:
            sl_item_dict['filled'] = float(sl_item.filled)
        else:
            sl_item_dict['filled'] = None
        if sl_item.backordered:
            sl_item_dict['backordered'] = float(sl_item.backordered)
        else:
            sl_item_dict['backordered'] = None
        sl_item_dict['shipping_list'] = sl_item.shipping_list.sl_number
        sl_item_list.append(sl_item_dict)

    sl_dict['items'] = sl_item_list
    sl_json = json.dumps(sl_dict)

    return HttpResponse(sl_json, mimetype="application/json")



def get_sl_item_json(request, sl_number=None):
    if sl_number:
        sl_items = ShippingItem.objects.filter(item_ship_status__lt = 2, shipping_list__sl_number=sl_number)
    else:
        sl_items = ShippingItem.objects.filter(item_ship_status__lt = 2)

    sl_item_list = []
    for sl_item in sl_items:
        sl_item_dict = {}
        sl_item_dict['sl_item_id'] = sl_item.id
        sl_item_dict['item_number'] = sl_item.item.item_number
        if sl_item.item.quantity_on_hand:
            sl_item_dict['quantity_on_hand'] = float(sl_item.item.quantity_on_hand)
        else:
            sl_item_dict['quantity_on_hand'] = None
        sl_item_dict['description'] = sl_item.description
        if sl_item.ordered:
            sl_item_dict['ordered'] = float(sl_item.ordered)
        else:
            sl_item_dict['ordered'] = None

        if sl_item.item.item_unit_measure:
            sl_item_dict['item_unit_measure'] = sl_item.item.item_unit_measure.unit_name
            sl_item_dict['item_unit_measure_id'] = sl_item.item.item_unit_measure.id
        else:
            sl_item_dict['item_unit_measure'] = None
        if sl_item.shipped:
            sl_item_dict['shipped'] = float(sl_item.shipped)
        else:
            sl_item_dict['shipped'] = None
        if sl_item.shipped_total_to_date:
            sl_item_dict['total_shipped'] = float(sl_item.shipped_total_to_date)
        else:
            sl_item_dict['total_shipped'] = None

        if sl_item.filled:
            sl_item_dict['filled'] = float(sl_item.filled)
        else:
            sl_item_dict['filled'] = None
        if sl_item.backordered:
            sl_item_dict['backordered'] = float(sl_item.backordered)
        else:
            sl_item_dict['backordered'] = None
        sl_item_dict['shipping_list'] = sl_item.shipping_list.sl_number
        sl_item_list.append(sl_item_dict)

    json_posts = json.dumps(sl_item_list)
    return HttpResponse(json_posts, mimetype='application/json')


@csrf_exempt
def sl_delete(request):
    if request.method == 'POST':
        sl_id = request.POST.get('sl_id')
        sl = ShippingList.objects.get(sl_number=sl_id)
        sl.delete()
        return HttpResponse(sl_id)


def view_shipping_list(request, sl_id):
    # import pdb; pdb.set_trace();
    sl = ShippingList.objects.get(sl_number=sl_id)
    sl_items = ShippingItem.objects.filter(shipping_list=sl)
    sl_soldto_contacts = SLSoldToContact.objects.filter(sl=sl)
    sl_shipto_contacts = SLShipToContact.objects.filter(sl=sl)
    return render(request, "purchase/view-sl.html", {'sl': sl, 'sl_items': sl_items, 
        'sl_soldto_contacts': sl_soldto_contacts, 'sl_shipto_contacts': sl_shipto_contacts})


def edit_shipping_list(request, sl_id):
    slobj = ShippingList.objects.get(sl_number=sl_id)
    sl_items = ShippingItem.objects.filter(shipping_list=slobj)
    ship_vias = DeliveryChoice.objects.filter(is_active=True)
    if request.method == 'POST':
        sl_form = ShippingListForm(request.POST, instance=slobj)
        item_filled = request.POST.getlist('item_filled')
        item_ordered = request.POST.getlist('item_ordered')
        item_required = request.POST.getlist('item_required')
        item_shipped = request.POST.getlist('item_shipped')
        items = request.POST.getlist('item_item')
        sl_item_id = request.POST.getlist('sl_item_id')
        slitems = request.POST.getlist("slitems")
        myset = set(slitems) - set(sl_item_id)
        removed_items = list(myset)

        if sl_form.is_valid():
            try:
                sl = sl_form.save()
                
                sl.save()

            except:
                return HttpResponse('SL can not saved')
            for i, item in enumerate(items):
                try:
                    shipping_item = ShippingItem.objects.get(id=sl_item_id[i])
                    if item_ordered[i] != '':
                        shipping_item.ordered = item_ordered[i]
                    if item_shipped[i] !='':
                        shipping_item.shipped = item_shipped[i]
                    if item_required[i] != '':
                        shipping_item.required = item_required[i]
                    if item_filled[i] != '':
                        shipping_item.filled = item_filled[i]
                    shipping_item.save()
                except:

                    item_obj = Item.objects.get(item_number=item)
                    shipping_item = ShippingItem(item=item_obj, description=item_obj.description)
                    if item_ordered[i] != '':
                        shipping_item.ordered = item_ordered[i]
                    if item_shipped[i] !='':
                        shipping_item.shipped = item_shipped[i]
                    if item_required[i] != '':
                        shipping_item.required = item_required[i]
                    if item_filled[i] != '':
                        shipping_item.filled = item_filled[i]
                    shipping_item.item_ship_status = 0
                    shipping_item.shipping_list = sl
                    
                    shipping_item.save()
            for rmitem in removed_items:
                remove_item = ShippingItem.objects.get(id=rmitem)
                remove_item.delete()


            return HttpResponseRedirect("/purchase/shipping-list/")
        else:
            return HttpResponse("Not valid form")
    else:
        sl_form = ShippingListForm(instance=slobj)
        return render(request, "purchase/sl-edit.html", 
        {'sl_items': sl_items, 'sl': slobj, 'ship_vias': ship_vias})


def shipping_list(request):
    sl_list = ShippingList.objects.all()
    return render(request, "purchase/shipping-list.html", {'sl_list': sl_list})


# # Deliver Internal start here
# @login_required
# @permission_required("purchase.add_deliverinternal")
# @csrf_exempt
# def add_deliverinternal(request):
#     if request.method == "POST":
#         deliverinternal_frm = DeliverInternalForm(request.POST)
#         if deliverinternal_frm.is_valid():
#             deliverinternal_frm.save()
#             return HttpResponseRedirect("/purchase/deliverinternal-list/")
#     else:
#         deliverinternal_frm = DeliverInternalForm()
    
#     return render(request, "purchase/add-deliverinternal.html",
#             {'deliverinternal_frm': deliverinternal_frm, 'page_title': 'Add Unit Measure'})


# @login_required
# @permission_required("inventory.change_deliverinternal")
# @csrf_exempt
# def edit_deliverinternal(request, id):
#     deliverinternal = DeliverInternal.objects.get(id=id)
#     if request.method == "POST":
#         deliverinternal_frm = DeliverInternalForm(request.POST, instance=deliverinternal)
#         if deliverinternal_frm.is_valid():
#             deliverinternal_frm.save()
#             return HttpResponseRedirect("/purchase/deliverinternal-list/")
#     else:
#         deliverinternal_frm = DeliverInternalForm(instance=deliverinternal)
    
#     return render(request, "purchase/edit-deliverinternal.html",
#             {'deliverinternal_frm': deliverinternal_frm, 'id':id, 'page_title': 'Edit Unit Measure'})


# @csrf_exempt
# @login_required
# @permission_required("inventory.delete_deliverinternal")
# def delete_deliverinternal(request):
#     if request.method == "POST":
#         di_id = request.POST.get("id")
#         deliverinternal = DeliverInternal.objects.get(id=di_id)
#         deliverinternal.delete()
#         return HttpResponse(di_id)
#     else:
#         return HttpResponse("Hello World!")

# @login_required
# @permission_required("inventory.view_deliverinternal")
# def list_deliverinternal(request):
#     deliverinternals = DeliverInternal.objects.all()
#     return render(request, "purchase/list-deliverinternal.html", 
#         {'deliverinternals': deliverinternals, 'page_title': 'List Deliver Internal'})

# def list_deliverinternal_json(request):
#     deliverinternals = DeliverInternal.objects.all()
#     di_list = []
#     for di in deliverinternals:
#         di_dict = {}
#         di_dict['id'] = di.id
#         di_dict['department'] = di.department
#         di_dict['description'] = di.description
#         di_list.append(di_dict)

#     json_posts = json.dumps(di_list)
#     return HttpResponse(json_posts, mimetype='application/json')

@csrf_exempt
@login_required
def po_reindex(request):
    # import pdb; pdb.set_trace()
    pos = PurchaseOrder.objects.all()
    for po in pos:
        po.search_string = po.po_number + " "
        if po.supplier:
            po.search_string += po.supplier.contact_name + " "
        pis = PurchaseItem.objects.filter(po=po)
        for pi in pis:
            po.search_string += pi.item.item_number + " "
            if pi.job_number:
                po.search_string += pi.job_number.job_number + " "
        po.save()

    return HttpResponseRedirect("/")

@csrf_exempt
@login_required
def sl_reindex(request):
    # import pdb; pdb.set_trace()
    shipping_list = ShippingList.objects.all()
    for sl in shipping_list:
        sl.search_string = sl.sl_number + " " + sl.customer_po_number + sl.customer_job_number
        if sl.job_number:
            sl.search_string += sl.job_number.job_number
        if sl.sold_to:
            sl.search_string += sl.sold_to.contact_name
        if sl.ship_via:
            sl.search_string += sl.ship_via.delivery_choice
        sl.save()

    return HttpResponseRedirect("/")


def get_invoices(request):
    # invoices = Invoice.objects.filter(status=0)
    invoices = Invoice.objects.all()
    invoice_list = []
    for inv in invoices:
        invoice = {}
        inv_items = InvoicedItem.objects.filter(invoice=inv)
        if inv_items:
            items = []
            for inv_item in inv_items:
                item = {}
                item['id'] = inv_item.id
                item['packingitem_id'] = inv_item.item.id
                item['item_number'] = inv_item.item.sl_item.item.item_number
                item['unit'] = inv_item.unit
                item['qty'] = float(inv_item.qty)
                item['price'] = float(inv_item.price)
                item['sub_total'] = float(inv_item.sub_total)
                items.append(item)
            invoice['invoice_items'] = items
        else:
            invoice['invoice_items'] = None

        invoice['invoice_number'] = inv.invoice_number
        if inv.date:
            invoice['invoice_date'] = inv.date.isoformat()
        if inv.pl:
            invoice['pl_number'] = inv.pl.pl_number

        if inv.sold_to:
            sold_to = {}
            sold_to['id'] = inv.sold_to.id
            sold_to['contact_name'] = inv.sold_to.contact_name
            sold_to['city'] = inv.sold_to.city
            sold_to['province'] = inv.sold_to.province
            sold_to['country'] = inv.sold_to.country

            phone_list = ContactPhone.objects.filter(contact=inv.sold_to)
            if phone_list:
                sold_to['phones'] = []
                for ph in phone_list:                    
                    phone = {}
                    phone['phone_type'] = ph.phone_type.phone_type
                    phone['phone'] = ph.phone
                    phone['phone_ext'] = ph.phone_ext
                    sold_to['phones'].append(phone)
            else:
                sold_to['phones'] = None
            
            email_list = ContactEmailAddress.objects.filter(contact=inv.sold_to)
            if email_list:
                sold_to['emails'] = []
                for em in emails:
                    email = {}
                    email['email_address_type'] = em.email_address_type.email_type
                    email['email_address'] = em.email_address
                    sold_to['emails'].append(email)

            else:
                sold_to['emails'] = None

            invoice['sold_to'] = sold_to

        if inv.ship_to:
            ship_to = {}
            ship_to['id'] = inv.ship_to.id
            ship_to['contact_name'] = inv.ship_to.contact_name
            ship_to['city'] = inv.ship_to.city
            ship_to['province'] = inv.ship_to.province
            ship_to['country'] = inv.ship_to.country

            phone_list = ContactPhone.objects.filter(contact=inv.ship_to)
            if phone_list:
                ship_to['phones'] = []
                for ph in phone_list:                    
                    phone = {}
                    phone['phone_type'] = ph.phone_type.phone_type
                    phone['phone'] = ph.phone
                    phone['phone_ext'] = ph.phone_ext
                    ship_to['phones'].append(phone)
            else:
                ship_to['phones'] = None
            
            email_list = ContactEmailAddress.objects.filter(contact=inv.ship_to)
            if email_list:
                ship_to['emails'] = []
                for em in emails:
                    email = {}
                    email['email_address_type'] = em.email_address_type.email_type
                    email['email_address'] = em.email_address
                    ship_to['emails'].append(email)

            else:
                ship_to['emails'] = None

            invoice['ship_to'] = ship_to

        if inv.broker:
            broker = {}
            broker['id'] = inv.broker.id
            broker['contact_name'] = inv.broker.contact_name
            broker['city'] = inv.broker.city
            broker['province'] = inv.broker.province
            broker['country'] = inv.broker.country

            phone_list = ContactPhone.objects.filter(contact=inv.broker)
            if phone_list:
                broker['phones'] = []
                for ph in phone_list:                    
                    phone = {}
                    phone['phone_type'] = ph.phone_type.phone_type
                    phone['phone'] = ph.phone
                    phone['phone_ext'] = ph.phone_ext
                    broker['phones'].append(phone)
            else:
                broker['phones'] = None
            
            email_list = ContactEmailAddress.objects.filter(contact=inv.broker)
            if email_list:
                broker['emails'] = []
                for em in emails:
                    email = {}
                    email['email_address_type'] = em.email_address_type.email_type
                    email['email_address'] = em.email_address
                    broker['emails'].append(email)

            else:
                broker['emails'] = None

            invoice['broker'] = broker

        if inv.ship_via:
            invoice['ship_via'] = inv.ship_via.delivery_choice
            invoice['ship_via_id'] = inv.ship_via.id

        invoice['po'] = inv.po

        if inv.job:
            invoice['job'] = inv.job.job_number
            invoice['job_id'] = inv.job.id

        if inv.terms:
            invoice['term'] = inv.terms.term
            invoice['term_id'] = inv.terms.id

        invoice['fob'] = inv.fob
        if inv.invoice_qty:
            invoice['invoice_qty'] = float(inv.invoice_qty)
        else:
            invoice['invoice_qty'] = 0.0
        if inv.sub_total:
            invoice['sub_total'] = float(inv.sub_total)
        else:
            invoice['sub_total'] = 0.0
        if inv.discount:
            invoice['discount'] = float(inv.discount)
        else:
            invoice['discount'] = 0.0

        invoice['discount_type'] = inv.discount_type
        invoice['comment'] = inv.comment
        if inv.discounted_sub_total:
            invoice['discounted_sub_total'] = float(inv.discounted_sub_total)
        else:
            invoice['discounted_sub_total'] = 0.0
        invoice['hst_taxable'] = inv.hst_taxable

        if inv.hst_taxable_amount:
            invoice['hst_taxable_amount'] = float(inv.hst_taxable_amount)
        else:
            invoice['hst_taxable_amount'] = 0.0
        invoice['pst_taxable'] = inv.pst_taxable
        if inv.pst_taxable_amount:
            invoice['pst_taxable_amount'] = float(inv.pst_taxable_amount)
        else:
            invoice['pst_taxable_amount'] = 0.0

        if inv.invoice_currency:
            invoice['invoice_currency'] = inv.invoice_currency.currency
            invoice['invoice_currency_id'] = inv.invoice_currency.id
        invoice['status'] = inv.status

        if inv.total_amount:
            invoice['total_amount'] = float(inv.total_amount)
        else:
            invoice['total_amount'] = 0.0
        invoice_list.append(invoice)
    json_posts = json.dumps(invoice_list)
    return HttpResponse(json_posts, mimetype='application/json')



def get_invoice_items(request):
    invoice_items = InvoicedItem.objects.all(status=0)
    item_list = []
    for item in invoice_items:
        item_dict = {}
        item_dict['invoice_id'] = item.invoice.id
        item_dict['invoice_item_id'] = item.id
        item_dict['packing_item'] = item.item.id
        item_dict['unit'] = item.unit
        item_dict['qty'] = item.qty
        item_dict['price'] = item.price
        item_dict['sub_total'] = item.sub_total
        item_list.append(item_dict)

    json_posts = json.dumps(item_list)
    return HttpResponse(json_posts, mimetype='application/json')



@csrf_exempt
def add_invoice(request):
    # import pdb; pdb.set_trace()
    
    users = User.objects.all().exclude(id__in=[-1]).order_by("username")
    terms = PaymentTerm.objects.all()
    delivery_choices = DeliveryChoice.objects.all()
    currencies = Currency.objects.all()


    if request.method == 'POST':
        # import pdb; pdb.set_trace()
        invoice_id = request.POST.get("invoice_number","")
        if invoice_id != "":
            invoice = Invoice.objects.get(invoice_number=invoice_id)
            invoice_form = InvoiceForm(request.POST, instance=invoice, request=request, action='update')
        else:
            invoice_form = InvoiceForm(request.POST, request=request, action='new')
        
        units = request.POST.getlist('unit',"")
        items = request.POST.getlist("item","")
        qtys = request.POST.getlist("qty","")
        prices = request.POST.getlist("price","")
        sub_totals = request.POST.getlist("sub_total","")
        
        if invoice_form.is_valid():
            invoice = invoice_form.save()
            # update PL status=='invoicing'
            pl = invoice.pl
            pl.status = 3
            pl.save()
            if invoice_id != "":
                deleted_items = request.POST.getlist("removed_item")
                if deleted_items:
                    for deleted_item in deleted_items:
                        di = InvoicedItem.objects.get(id=deleted_item)
                        di.delete()
            for i, item  in enumerate(items):
                packingitem = PackingItem.objects.get(id=item)
                try:
                    invoice_item = InvoicedItem.objects.get(item=packingitem)
                except InvoicedItem.DoesNotExist:
                    invoice_item = InvoicedItem.objects.create(item=packingitem)
                    invoice_item.invoice = invoice
                    invoice_item.unit = units[i]
                    invoice_item.qty = qtys[i]
                    invoice_item.price = prices[i]
                    invoice_item.sub_total = sub_totals[i]
                    invoice_item.save()
                # TODO: Need to update packing item status=='invoiced' and also remove from
                # search result

            return HttpResponseRedirect("/purchase/invoice-list/")
        else:
            form = InvoiceForm(request.POST)
            return render(request, 'purchase/invoice/invoice.html', 
            {'form': form, 'currencies': currencies,
            'adminusers': users, 'terms': terms, 'delivery_choices': delivery_choices})
    else:
        form = InvoiceForm(request.POST)
        return render(request, 'purchase/invoice/invoice.html', 
            {'form': form, 'currencies': currencies,
            'adminusers': users, 'terms': terms, 'delivery_choices': delivery_choices})


def invoice_list(request):
    invoices = Invoice.objects.all()
    return render(request, 'purchase/invoice/invoice-list.html', 
        {'invoices': invoices})


def invoice_view(request, invoice_id):
    invoice = Invoice.objects.get(invoice_number=invoice_id)
    return render(request, 'purchase/invoice/invoice-view.html', 
        {'invoice': invoice})

@csrf_exempt
def delete_invoice(request):
    # import pdb; pdb.set_trace()
    invoice_number = request.POST.get("invoice_id","")
    if invoice_number:
        invoice = Invoice.objects.get(invoice_number=invoice_number)
        invoice.delete()
        return HttpResponse(invoice_number)


def pl_reindex(request):
    pass


def show_draft_po(request):
    pass