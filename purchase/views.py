from django.shortcuts import render
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

@login_required
@permission_required("purchase.add_purchaserequest")
@csrf_exempt
def add_purchase_request(request):
    if request.method == 'POST':
        pr_add_form = PRAddForm(request.POST)
        if pr_add_form.is_valid():
            pr = pr_add_form.save()
            pr.status = 0
            if not request.user.is_superuser:
                pr.user_requested = request.user
                
            if not pr.requeste_created_at:
                pr.requeste_created_at = datetime.datetime.now()
            pr.save()
            
            return HttpResponseRedirect("/purchase/list-purchase-requests/")

    else:
        form_init = {
            'user_requested' : request.user.id,
        }
        pr_add_form = PRAddForm(initial=form_init)
        if not request.user.is_superuser:
            pr_add_form.fields['user_requested'].widget.attrs['disabled'] = 'disabled'

        return render(request, "purchase/add_pr.html", {'pr_add_form': pr_add_form})


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
        # import pdb; pdb.set_trace()
        approved_qty = pr.approved_qty
        new_approved_qty = request.POST.get("approved_qty","")
        pr_approve_form = PRApproveForm(request.POST, instance=pr)
        comment = request.POST.get('comment','')
        prc = PurchaseRequestComment(
            purchase_request = pr,
            comment = comment,
            commnet_date = datetime.datetime.now(),
            user_commented = request.user
        )
        if pr_approve_form.is_valid():
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
            pr.approved_date = datetime.datetime.now()
            
            pr.save()
            prc.save()
            # Add request item
            ri = RequestItem(pr=pr, item=pr.item)
            ri.approved_qty = new_approved_qty
            ri.approved_date = pr.approved_date
            ri.status = 0
            ri.save()
        

        return HttpResponse(pk)
    else:
        pr_approve_form = PRApproveForm(instance=pr)
        pr_com_form = PRCAddForm()
        return render(request, "purchase/pr-approve.html", 
            {'pr_approve_form': pr_approve_form, 'pr_com_form': pr_com_form, 'pr_id': pk})

@csrf_exempt
def declien_purchase_request(request):
    if request.method == 'POST':
        pr_id = request.POST.get('pr_id')
        pr = PurchaseRequest.objects.get(id=pr_id)
        pr.status = 3
        pr.save()
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
        po_form = POForm(request.POST)
        if po_form.is_valid():
            po = po_form.save()
            po.po_created_by = request.user
            po.datetime = datetime.datetime.now()
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
        now = datetime.datetime.now()
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
def add_po(request):
    try:
        sv = SystemVariable.objects.get(id=1)
        next_number = sv.next_po_number
        if not next_number:
            messages.warning(request, "System varible is not set for PO. Please ask your admin to update System variable.")
            return HttpResponseRedirect("/")
    except Exception, e:
        messages.warning(request, "System varible is not set for PO. Please ask your admin to update System variable.")
        return HttpResponseRedirect("/")
        pass
    if request.method == 'POST':
        po_form = POForm(request.POST)
        if po_form.is_valid():
            po = po_form.save()
            po.po_created_by = request.user
            po.datetime = datetime.datetime.now()
            po.save_final_draft = 0
            po.search_string = po.po_number + " "
            if po.supplier:
                po.search_string += po.supplier.contact_name + " "
        
            items = []
            item_list = request.POST.getlist('added_item_number')
            if item_list:
                count = 0
                for item in item_list:
                    item_dict = {}
                    item_dict['item_number'] = item
                    item_dict['qty'] = float(request.POST.getlist('item_qty')[count])
                    item_dict['comment'] = request.POST.getlist('item_comment')[count]
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

                    except:
                        job = None
                    pi = PurchaseItem(po=po, item=itemobj, job_number=job,
                        qty=item['qty'], cost=item['cost'], sub_total=item['sub_total'],
                        comment=item['comment'])
                    pi.purchase_status = 0
                    pi.save()
                    # Update inventory item for Last PO info
                    itemobj.last_PO = po.po_number
                    itemobj.last_PO_date_ordered = po.date_issued
                    itemobj.last_PO_date_expected = po.date_expected
                    itemobj.last_cost_paid = item['cost']
                    itemobj.last_PO_ordered_by = po.po_created_by
                    itemobj.last_PO_supplier = po.supplier
                    itemobj.save()
            
            po.save()
            
            po_extra_contacts = POContact.objects.filter(purchase_order=po.po_number)
            po_items = PurchaseItem.objects.filter(po=po)
            return render(request, "purchase/show_draft_po.html", {'po': po, 'extra_contacts': po_extra_contacts, 'po_items': po_items})
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

        return render(request, "purchase/add-po2.html", 
            {"po_number":'NEW' , 'next_number': next_number,
            'po_contact_form': po_contact_form, 'currencies': currencies,
            'delivery_choices': delivery_choices, 'terms': terms,
            'deliver_internals': deliver_internals, 'users': users, 'item_unit_measures':item_unit_measures,
            'adminusers': adminusers})

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
        po_dict['id'] = po.id
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
    po = PurchaseOrder.objects.get(pk=pk)
    po_items = po.purchaseitem_set.all()
    # po_contact = POContact.objects.filter(purchase_order=po.po_number)

    po_dict = {}
    po_dict['id'] = str(po.id)
    po_dict['po_number'] = po.po_number
    po_dict['next_number'] = po.next_number
    if po.date_issued:
        po_dict['date_issued'] = po.date_issued.isoformat()

    if po.date_expected:
        po_dict['date_expected'] = po.date_expected.isoformat()
    else:
        po_dict['date_expected'] = None

    if po.po_status:
        po_status = {}
        po_status['id'] = po.po_status
        po_status['label'] = po.status_verbose()
        po_dict['po_status'] = po_status
    if po.supplier:
        supplier = {}
        supplier['id'] = str(po.supplier.id)
        supplier['contact_name'] = po.supplier.contact_name
        supplier['city'] = po.supplier.city
        supplier['province'] = po.supplier.province
        supplier['emails'] = []
        for email in po.supplier.contactemailaddress_set.all():
            email_dict = {}
            email_dict['email_type'] = email.email_address_type.email_type
            email_dict['email_address'] = email.email_address
            supplier['emails'].append(email_dict)
        po_dict['supplier'] = supplier
    else:
        po_dict['supplier'] = 'None'

    if po.ship_to:
        ship_to = {}
        ship_to['id'] = str(po.ship_to.id)
        ship_to['contact_name'] = po.ship_to.contact_name
        ship_to['city'] = po.ship_to.city
        ship_to['province'] = po.ship_to.province
        ship_to['emails'] = []
        for email in po.ship_to.contactemailaddress_set.all():
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
    po_dict['items_total'] = po.items_total.to_eng_string()
    po_dict['hst_taxable'] = po.hst_taxable
    if po.hst_taxable_amount:
        po_dict['hst_taxable_amount'] = po.hst_taxable_amount.to_eng_string()
    po_dict['pst_taxable'] = po.pst_taxable
    if po.pst_taxable_amount:
        po_dict['pst_taxable_amount'] = po.pst_taxable_amount.to_eng_string()
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

    json_posts = json.dumps(po_dict)
    return HttpResponse(json_posts, mimetype='application/json')


def get_purchase_orders(request):
    # import pdb; pdb.set_trace()
    
    purchase_orders = PurchaseOrder.objects.filter(save_final_draft=1)
    po_list = []
    for po in purchase_orders:
        po_dict = {}
        po_dict['id'] = po.id
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
        po_dict['status'] = po.status_verbose()
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
    po = PurchaseOrder.objects.get(id=pk)
    pitems = PurchaseItem.objects.filter(po=po)
    status_comments = POStatus.objects.filter(po=po)

    poecontacts = POContact.objects.filter(purchase_order=po.po_number)

    return render(request, "purchase/po-view.html", 
        {'po': po, 'extra_contacts': poecontacts, 'status_comments': status_comments,
        'purchase_items': pitems})

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
        po_status.datetime = datetime.datetime.now()
        po_status.status = 6
        po_status.save()

        po.po_status = 6
        po.save()
        return HttpResponse(po_status.pk)
    else:
        po = PurchaseOrder.objects.get(id=pk)
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
                po_status.datetime = datetime.datetime.now()
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
            po.datetime = datetime.datetime.now()
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
        po = PurchaseOrder.objects.get(id=po_id)
        po.delete();
        return HttpResponse(po_id)



@csrf_exempt
def add_po_contact(request, po_id):
    if request.method == 'POST':
        # import pdb; pdb.set_trace();
        po_number = request.POST.get('purchase_order')
        po_contact_type = request.POST.get('contact_type')
        po_contact = request.POST.get('contact')
        po_contact_name = request.POST.get('contact_name')
        pocontact = POContact(purchase_order=po_number, 
            contact_type=po_contact_type, 
            contact=po_contact, contact_name=po_contact_name)
        
        pocontact.save()
        return render(request, "purchase/extra-po-contact.html", {'pocontact': pocontact})
    else:
        pocontactform = POContactForm()

        return render(request, "purchase/add-po-contact.html", {'po_contact_form': pocontactform, 'po_number': po_id})


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
    if request.method == 'POST':
        # import pdb; pdb.set_trace()
        item_rcv_form = ItemReeiveForm(request.POST)
        if item_rcv_form.is_valid():
            rcv_item = item_rcv_form.save()
            purchase_item = PurchaseItem.objects.get(id=item_id)
            po = purchase_item.po

            # Update item receive history            
            rcv_item.purchase_item = purchase_item
            rcv_item.item_po = po
            rcv_item.sub_total = purchase_item.cost * rcv_item.qty_received
            rcv_item.item_received_date = datetime.datetime.now()
            rcv_item.reveived_by = request.user
            rcv_item.search_string = purchase_item.item.item_number + " " + rcv_item.item_po.po_number
            rcv_item.save()

            # Update PurchaseItem
            '''
            If purchase_item.purchase_status == 2 this purchase_item is then done with all
            '''
            
            purchase_item.item_recv += rcv_item.qty_received
            purchase_item.item_recv_date = datetime.datetime.now()
            if purchase_item.item_recv >= purchase_item.qty:
                purchase_item.purchase_status = 2
            else:
                purchase_item.purchase_status = 1

            purchase_item.save()
            return HttpResponse(rcv_item.id)
    else:
        item_rcv_form = ItemReeiveForm()
        return render(request, "purchase/item-receive-form.html", 
            {'item_rcv_form': item_rcv_form, 'item_id': item_id})




def add_packing_list(request):
    cuser =request.user
    users = User.objects.all().exclude(id__in=[-1]).order_by("username")
    dcs = DeliveryChoice.objects.all()
    if request.method == 'POST':
        return HttpResponse("under construction..")
        pl_form = PackingListForm(request.POST)
        item_unit = request.POST.getlist('item_unit')
        item_qtybo = request.POST.getlist('item_qtybo')
        item_ordered = request.POST.getlist('item_ordered')
        items = request.POST.getlist('item_item')
        sl_items = request.POST.getlist("sl_items")
        sl_item_ids = request.POST.getlist("sl_item_id")
        item_shipped = request.POST.getlist('item_shipped')

        if pl_form.is_valid():
            pl = pl_form.save()
            pl.generated_by = request.user
            for i, item in enumerate(items):
                item_obj = Item.objects.get(item_number=item)
                ship_item = ShippingItem.objects.get(id=sl_item_ids[i])
                packing_item = PackingItem(shipping_item=ship_item, description=item_obj.description)
                packing_item.unit = item_unit[i]
                if item_shipped[i]:
                    packing_item.qty_shipped = Decimal(item_shipped[i])
                if item_ordered[i]:
                    packing_item.qty_ordered = Decimal(item_ordered[i])
                if item_qtybo[i]:
                    packing_item.qty_bo = Decimal(item_qtybo[i])
                packing_item.ship_status = 0
                packing_item.pl = pl
                packing_item.search_string = ship_item.shipping_list.sl_number + " "+ ship_item.item.item_number
                packing_item.save()
                # Update ShippingItem object to check all its ordered item is shipped.
                ship_item.shipped += Decimal(item_shipped[i])
                if ship_item.ordered <= ship_item.shipped:
                    ship_item.item_ship_status = 2
                else:
                    ship_item.item_ship_status = 1
                ship_item.save()

            pl.search_string = pl.pl_number + ' '
            if pl.sold_to:
                pl.search_string += pl.sold_to.contact_name + ' '

            pl.save()
            return HttpResponseRedirect("/purchase/packing-list/")
    else:
        form_init = {
            'shipped_by': cuser,
            'generated_by': cuser
        }
        pl_form = PackingListForm(initial=form_init)
        return render(request, "purchase/add-pl.html", 
            {'pl_form': pl_form, 'users': users, 'cuser': cuser, 'dcs': dcs})


def pl_list(request):
    # import pdb; pdb.set_trace()
    packing_list = PackingList.objects.all()
    pl_list = []
    for pl in packing_list:
        pack = {}
        pack['id'] = pl.id
        pack['pl_number'] = pl.pl_number
        if pl.date_issued:
            pack['date_issued'] = pl.date_issued.isoformat()
        if pl.date_shipped:
            pack['date_shipped'] = pl.date_shipped.isoformat()
        if pl.sold_to:
            pack['sold_to'] = pl.sold_to.contact_name
        else:
            pack['sold_to'] = None
        if pl.ship_to:
            pack['ship_to'] = pl.ship_to.contact_name
        else:
            pack['ship_to'] = None
        if pl.shipped_by:
            pack['shipped_by'] = pl.shipped_by.username
        else:
            pack['shipped_by'] = None
        pack['nel_packing_slip'] = pl.nel_packing_slip
        if pl.job_number:
            pack['job_number'] = pl.job_number.job_number
        else:
            pack['job_number'] = None
        if pl.generated_by:
            pack['generated_by'] = pl.generated_by.username
        else:
            pack['generated_by'] = None
        
        if pl.ship_via:
            pack['ship_via'] = pl.ship_via.delivery_choice
        else:
            pack['ship_via'] = None

        pack['hold_at_dept_for_pickup'] = pl.hold_at_dept_for_pickup
        
        pack['status'] = pl.status
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

def get_pl_items(request, id):
    try:
        pl = PackingList.objects.get(id=id)
    except PackingList.DoesNotExist:
        json_posts = {
            'PurchaseOrder DoesNotExist',
        }
        return HttpResponse(json_posts, mimetype='application/json')
        
    
    pl_items = pl.items.all()
    plitems = []
    for item in pl_items:
        item_dict = {}
        item_dict['item_number'] = item.item.item_number
        item_dict['description'] = item.item.description

        item_dict['ordered'] = float(item.ordered)
        item_dict['qty_bo'] = float(item.qty_bo)
        item_dict['shipped'] = float(item.shipped)
        item_dict['ship_status'] = item.ship_status
        
        plitems.append(item_dict)
    

    json_posts = json.dumps(plitems)
    return HttpResponse(json_posts, mimetype='application/json')

@csrf_exempt
def delete_packing_list(request):
    # import pdb; pdb.set_trace()
    plid = request.POST.get('pl_id', '')
    if plid:
        pl = PackingList.objects.get(id=plid)
        pl.delete()
        return HttpResponse(plid)
    else:
        return HttpResponse('failed')

def view_packing_list(request, id):
    # import pdb; pdb.set_trace()
    pl = PackingList.objects.get(id=id)
    pl_items = PackingItem.objects.filter(pl=pl)
    return render(request, 'purchase/view-pl.html', {'pl': pl, 'pl_items': pl_items})

def packing_list(request):
    return render(request, "purchase/parking-list.html", {})


@csrf_exempt
def add_shipping_list(request):
    if request.method == 'POST':
        # import pdb; pdb.set_trace()  
        user = request.user 
        sl_form = ShippingListForm(request.POST)

        item_ordered = request.POST.getlist('item_ordered')
        item_shipped = request.POST.getlist('item_shipped')
        item_backordered = request.POST.getlist('item_backordered')
        shipped_total_to_date = request.POST.getlist('shipped_total_to_date')
        
        items = request.POST.getlist('added_item_number')

        if sl_form.is_valid():
            # import pdb; pdb.set_trace()
            try:
                sl = sl_form.save()
                try:
                    sv = SystemVariable.objects.get(id=1)
                    if(sv.next_sl_number):
                        sl.sl_number = 'SL'+str(sv.next_sl_number)
                        sl.save()
                        sv.next_sl_number = sv.next_sl_number + 1
                        sv.save()
                    else:
                        import random
                        sl.sl_number = random.randint(100, 10000)
                        sl.save()
                except Exception, e:
                    pass

                for i, item in enumerate(items):
                    item_obj = Item.objects.get(item_number=item)
                    shipping_item = ShippingItem(item=item_obj, description=item_obj.description, shipping_list=sl)
                    if item_ordered[i] != '':
                        shipping_item.ordered = item_ordered[i]
                    if item_shipped[i] !='':
                        shipping_item.shipped = item_shipped[i]
                    if shipped_total_to_date[i] != '':
                        shipping_item.shipped_total_to_date = shipped_total_to_date[i]
                    if item_backordered[i] != '':
                        shipping_item.backordered = item_backordered[i]
                    

                    shipping_item.item_ship_status = 0
                    shipping_item.shipped_by = user
                    shipping_item.search_string = item + " " + sl.sl_number + " "
                    shipping_item.save()
                    # sl.items.add(shipping_item)
                sl.search_string = sl.sl_number + " " + sl.customer_po_number + sl.customer_job_number
                if sl.job_number:
                    sl.search_string += sl.job_number.job_number
                if sl.sold_to:
                    sl.search_string += sl.sold_to.contact_name
                if sl.ship_via:
                    sl.search_string += sl.ship_via.delivery_choice
                sl.sl_status = 0
                sl.save()

            except:
                return HttpResponse('SL can not saved')
            return HttpResponseRedirect("/purchase/shipping-list/")
        else:
            return HttpResponse("Not valid form")
    else:
        ship_vias = DeliveryChoice.objects.filter(is_active=True)
        sl_form = ShippingListForm()
        return render(request, "purchase/sl-add.html", {'sl_form': sl_form, 'ship_vias': ship_vias})

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

        sl_dict['id'] = sl.id
        sl_dict['sl_number'] = sl.sl_number
        if sl.sold_to:
            sl_dict['sold_to'] = {}
            sl_dict['sold_to']['contact_name'] = sl.sold_to.contact_name
            phone_list = sl.sold_to.contactphone_set.all()
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
            
            email_list = sl.sold_to.contactemailaddress_set.all()
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
            phone_list = sl.ship_to.contactphone_set.all()
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
            
            email_list = sl.ship_to.contactemailaddress_set.all()
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
        
        sl_dict['search_string'] = sl.search_string
        sl_list.append(sl_dict)
    json_posts = json.dumps(sl_list)
    return HttpResponse(json_posts, mimetype='application/json')

def get_sl_json_by_id(request, sl_id):
    sl = ShippingList.objects.get(id=sl_id)
    sl_dict = {}
    sl_dict['id'] = sl.id
    sl_dict['sl_number'] = sl.sl_number
    if sl.sold_to:
        sl_dict['sold_to'] = {}
        sl_dict['sold_to']['id'] = sl.sold_to.id
        sl_dict['sold_to']['contact_name'] = sl.sold_to.contact_name
        sl_dict['sold_to']['city'] = sl.sold_to.city
    else:
        sl_dict['sold_to'] = None

    if sl.ship_to:
        sl_dict['ship_to'] = {}
        sl_dict['ship_to']['id'] = sl.ship_to.id
        sl_dict['ship_to']['contact_name'] = sl.ship_to.contact_name
        sl_dict['ship_to']['city'] = sl.ship_to.city
    else:
        sl_dict['ship_to'] = None

    sl_dict['ordered_date'] = sl.ordered_date.isoformat()
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
    sl_dict['search_string'] = sl.search_string

    sl_json = json.dumps(sl_dict)

    return HttpResponse(sl_json, mimetype="application/json")



def get_sl_item_json(request, sl_id=None):
    if sl_id:
        sl_items = ShippingItem.objects.filter(item_ship_status__lt = 2, shipping_list__id=sl_id)
    else:
        sl_items = ShippingItem.objects.filter(item_ship_status__lt = 2)

    sl_item_list = []
    for sl_item in sl_items:
        sl_item_dict = {}
        sl_item_dict['id'] = sl_item.id
        sl_item_dict['item_number'] = sl_item.item.item_number
        sl_item_dict['description'] = sl_item.description
        if sl_item.ordered:
            sl_item_dict['ordered'] = float(sl_item.ordered)
        if sl_item.shipped:
            sl_item_dict['shipped'] = float(sl_item.shipped)
        if sl_item.filled:
            sl_item_dict['filled'] = float(sl_item.filled)
        sl_item_dict['shipping_list'] = sl_item.shipping_list.sl_number
        sl_item_list.append(sl_item_dict)

    json_posts = json.dumps(sl_item_list)
    return HttpResponse(json_posts, mimetype='application/json')


@csrf_exempt
def sl_delete(request):
    if request.method == 'POST':
        sl_id = request.POST.get('sl_id')
        sl = ShippingList.objects.get(id=sl_id)
        sl.delete()
        return HttpResponse(sl_id)


def view_shipping_list(request, sl_id):
    sl = ShippingList.objects.get(id=sl_id)
    sl_items = ShippingItem.objects.filter(shipping_list=sl)
    return render(request, "purchase/view-sl.html", {'sl': sl, 'sl_items': sl_items})


def edit_shipping_list(request, sl_id):
    slobj = ShippingList.objects.get(id=sl_id)
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
                sl.search_string = sl.sl_number + " " + sl.customer_po_number + sl.customer_job_number
                if sl.job_number:
                    sl.search_string += sl.job_number.job_number
                if sl.sold_to:
                    sl.search_string += sl.sold_to.contact_name
                if sl.ship_via:
                    sl.search_string += sl.ship_via.delivery_choice
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
                    shipping_item.search_string = item + " " + sl.sl_number
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


# Deliver Internal start here
@login_required
@permission_required("purchase.add_deliverinternal")
@csrf_exempt
def add_deliverinternal(request):
    if request.method == "POST":
        deliverinternal_frm = DeliverInternalForm(request.POST)
        if deliverinternal_frm.is_valid():
            deliverinternal_frm.save()
            return HttpResponseRedirect("/purchase/deliverinternal-list/")
    else:
        deliverinternal_frm = DeliverInternalForm()
    
    return render(request, "purchase/add-deliverinternal.html",
            {'deliverinternal_frm': deliverinternal_frm, 'page_title': 'Add Unit Measure'})


@login_required
@permission_required("inventory.change_deliverinternal")
@csrf_exempt
def edit_deliverinternal(request, id):
    deliverinternal = DeliverInternal.objects.get(id=id)
    if request.method == "POST":
        deliverinternal_frm = DeliverInternalForm(request.POST, instance=deliverinternal)
        if deliverinternal_frm.is_valid():
            deliverinternal_frm.save()
            return HttpResponseRedirect("/purchase/deliverinternal-list/")
    else:
        deliverinternal_frm = DeliverInternalForm(instance=deliverinternal)
    
    return render(request, "purchase/edit-deliverinternal.html",
            {'deliverinternal_frm': deliverinternal_frm, 'id':id, 'page_title': 'Edit Unit Measure'})


@csrf_exempt
@login_required
@permission_required("inventory.delete_deliverinternal")
def delete_deliverinternal(request):
    if request.method == "POST":
        di_id = request.POST.get("id")
        deliverinternal = DeliverInternal.objects.get(id=di_id)
        deliverinternal.delete()
        return HttpResponse(di_id)
    else:
        return HttpResponse("Hello World!")

@login_required
@permission_required("inventory.view_deliverinternal")
def list_deliverinternal(request):
    deliverinternals = DeliverInternal.objects.all()
    return render(request, "purchase/list-deliverinternal.html", 
        {'deliverinternals': deliverinternals, 'page_title': 'List Deliver Internal'})

def list_deliverinternal_json(request):
    deliverinternals = DeliverInternal.objects.all()
    di_list = []
    for di in deliverinternals:
        di_dict = {}
        di_dict['id'] = di.id
        di_dict['department'] = di.department
        di_dict['description'] = di.description
        di_list.append(di_dict)

    json_posts = json.dumps(di_list)
    return HttpResponse(json_posts, mimetype='application/json')

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
