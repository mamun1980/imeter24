from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from inventory.forms import *
from inventory.models import *
# Create your views here.
from scomuser.models import *
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
import json

from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.contrib import messages, auth
from contacts.models import *
from haystack.forms import ModelSearchForm, SearchForm
from haystack.query import SearchQuerySet, EmptySearchQuerySet
from haystack.views import SearchView
from haystack.inputs import Raw, Clean, AutoQuery


def autocomplete(request):
    query = request.GET.get('q', '')
    suggestions = []
    if len(query) > 1:
        sqs = SearchQuerySet().using('inventory').filter(content=query)[:10]

        items_list = []
        for item in items:
            item_dict = {}
            item_dict['id'] = item.pk
            item_dict['item_number'] = item.item_number
            item_dict['description'] = item.description
            item_dict['primary_supplier'] = item.primary_supplier
            item_dict['last_PO'] = item.last_PO
            item_dict['terms'] = item.terms
            item_dict['cost'] = item.wholesale_cost
            item_dict['quantity_on_hand'] = item.quantity_on_hand

            items_list.append(item_dict)
        the_data = json.dumps({
            'results': items_list
        })
        return HttpResponse(the_data, content_type='application/json')


@login_required
@permission_required("inventory.add_item")
@csrf_exempt
def add_item(request):
    currencies = Currency.objects.all()
    departments = Department.objects.all()
    unit_measures = ItemUnitMeasure.objects.all()
    locations = Location.objects.all()
    production_types = ProductionType.objects.all()
    terms = PaymentTerm.objects.all()
    if request.method == "POST":
        # import pdb; pdb.set_trace()
        item_number = request.POST.get("item_number","")
        if not item_number == "":
            try:
                item = Item.objects.get(item_number=item_number)
                item_form = ItemForm(request.POST, request.FILES, instance=item)
            except Exception, e:
                item_form = ItemForm(request.POST, request.FILES)
                pass
            finally:
                if item_form.is_valid():
                    item = item_form.save()
        
            return HttpResponseRedirect("/inventory/list/#/inventory/items")  
    else:
        item_form = ItemForm()

    # return HttpResponse(item_form)

    # return render(request, "inventory/item/test.html", {'item_form': item_form, 'page_title': 'Add Item'})
    
    return render(request, "inventory/item/add-item-v2.html", 
        {'item_form': item_form, 'page_title': 'Add Item', 'currencies': currencies, 
        'departments': departments, 'unit_measures': unit_measures, 'locations': locations,
        'production_types': production_types, 'terms': terms})


def add_new_item(request):
    currencies = Currency.objects.all()
    departments = Department.objects.all()
    unit_measures = ItemUnitMeasure.objects.all()
    locations = Location.objects.all()
    production_types = ProductionType.objects.all()
    terms = PaymentTerm.objects.all()
    designations = CustomsDesignation.objects.all()
    deliver_internals = DeliverInternal.objects.all()
    if request.method == "POST":
        # import pdb; pdb.set_trace();
        item_number = request.POST.get("item_number","")
        if item_number:
            try:
                item = Item.objects.get(item_number=item_number)
                item_form = ItemForm(request.POST, request.FILES, instance=item, 
                    request=request, action='update')
            except Item.DoesNotExist:
                item_form = ItemForm(request.POST, request.FILES, request=request, action='new')
                pass
        else:
            sv = SystemVariable.objects.get(id=1)
            request.POST['item_number'] = sv.get_next_item_number
            

            item_form = ItemForm(request.POST, request.FILES, request=request, action='new')
            # return HttpResponseRedirect("/inventory/list/")
            
        if item_form.is_valid():
            try:
                item = item_form.save()
                # import pdb; pdb.set_trace();
                hst_taxable = request.POST.get("hst_taxable")
                pst_taxable = request.POST.get("pst_taxable")

                if not hst_taxable:
                    item.hst_taxable = False
                else:
                    item.hst_taxable = True

                if not pst_taxable:
                    item.pst_taxable = False
                else:
                    item.pst_taxable = True

                item.save()
                                
                return HttpResponseRedirect("/inventory/list/")
            except Exception, e:
                raise e           
            
    else:
        item_form = ItemForm()

    return render(request, "inventory/item/add-new-item.html", 
        {'item_form': item_form, 'page_title': 'Add Item', 'currencies': currencies, 
        'departments': departments, 'unit_measures': unit_measures, 'deliver_internals':deliver_internals,
        'production_types': production_types, 'terms': terms, 'designations': designations})


@login_required
@permission_required("inventory.add_item")
@csrf_exempt
def add_another_item(request):
    if request.method == "POST":
        # import pdb; pdb.set_trace()
        item_form = ItemForm(request.POST, request.FILES)
        if item_form.is_valid():
            item = item_form.save()
            # return HttpResponseRedirect("/contacts/edit/%d/" % cid)
            return HttpResponse(item.pk)
        else:
            return HttpResponse("error")
    else:
        item_form = ItemForm()
        return render(request, "inventory/item/add-another-item.html", {'item_form': item_form})


@login_required
@permission_required("inventory.change_item")
@csrf_exempt
def edit_item(request, itemid):
    item = Item.objects.get(item_number=itemid)
    if item.primary_supplier:
        contact_id = item.primary_supplier.id
    else:
        contact_id = None
    if item.producer_of_item:
        producer_of_item_id = item.producer_of_item.id
    else:
        producer_of_item_id = None
    if request.method == 'POST':
        item_form = ItemForm(request.POST,request.FILES, instance=item)
        if item_form.is_valid():
            item = item_form.save()
            hst_taxable = request.POST.get("hst_taxable")
            pst_taxable = request.POST.get("pst_taxable")

            if not hst_taxable:
                item.hst_taxable = False
            else:
                item.hst_taxable = True

            if not pst_taxable:
                item.pst_taxable = False
            else:
                item.pst_taxable = True
            item.save()
            return HttpResponseRedirect("/inventory/list/")
    else:
        item_comment_form = ItemCommentForm()
        currencies = Currency.objects.all()
        departments = Department.objects.all()
        production_types = ProductionType.objects.all()
        unit_measures = ItemUnitMeasure.objects.all()
        locations = Location.objects.all()
        myterms = PaymentTerm.objects.all()
        designations = CustomsDesignation.objects.all()
        item_comments = ItemComment.objects.filter(item=item).order_by("-id")
        return render(request, "inventory/item/edit-item.html", 
            {'item': item, 'itemid':itemid, 'contact_id': contact_id, 'producer_of_item_id': producer_of_item_id,
            'page_title': 'Update Item', 'item_comments': item_comments, 'currencies': currencies,
            'departments': departments, 'production_types': production_types, 'terms': myterms,
            'unit_measures': unit_measures, 'locations': locations, 'designations': designations,
            'item_comment_form': item_comment_form})

@csrf_exempt
@login_required
@permission_required('inventory.add_itemcomment')
def add_item_comment(request):
    if request.method == 'POST':
        # import pdb; pdb.set_trace()
        comment_form = ItemCommentForm(request.POST)
        item_id = request.POST.get('item_id')
        item = Item.objects.get(item_number=item_id)
        if comment_form.is_valid():
            com_form = comment_form.save()
            com_form.item = item
            com_form.comment_date = datetime.now()
            com_form.comment_by = request.user
            com_form.save()
            return render(request, 'inventory/item/item-comment.html', {'comment': com_form})
        else:
            return HttpResponse("Not Valid Form")


@login_required
@permission_required("inventory.view_item")
@csrf_exempt
def item_details(request, itemid):
    # import pdb; pdb.set_trace()
    from purchase.models import PurchaseOrder
    item = Item.objects.get(item_number=itemid)
    item_comment_form = ItemCommentForm()
    item_comments = ItemComment.objects.filter(item=item).order_by("-id")
    # purchase_items = item.purchaseitem_set.all()
    purchase_orders = []
    try:
        pis = item.purchaseitem_set.all()
        for pi in pis:
            po = pi.po
            purchase_orders.append(po)
    except IndexError:
        purchase_orders = []


    return render(request, "inventory/item/item-details.html", 
        {'item': item, 'page_title': 'Item Details', 'item_comments': item_comments,
            'item_comment_form': item_comment_form, 'purchase_orders': purchase_orders})


@csrf_exempt
@login_required
def item_details_filtered(request):
    if request.method == "POST":
        itemid = request.POST.get("autocomplete")
        return HttpResponseRedirect("/inventory/item/view/%s/" % itemid)


def list_item(request):
    user = request.user
    items = Item.objects.all() #. 'production_type', 'search_string')
    inventory_dict_list = []
    for item in items:
        item_dict = {}
        item_dict['item_number'] = item.item_number
        item_dict['label'] = item.item_number
        item_dict['description'] = item.description
        if item.order_restriction:
            item_dict['order_restriction'] = float(item.order_restriction)
        else:
            item_dict['order_restriction'] = -1
        if item.qty_received:
            item_dict['qty_received'] = float(item.qty_received)
        else:
            item_dict['qty_received'] = 0.0

        if item.max_order_qty:
            item_dict['max_order_qty'] = float(item.max_order_qty)
        else:
            item_dict['max_order_qty'] = 0.0

        if item.max_order_qty_remains:
            item_dict['max_order_qty_remains'] = float(item.max_order_qty_remains)
        else:
            item_dict['max_order_qty_remains'] = -1

        if item.max_single_order_qty:
            item_dict['max_single_order_qty'] = float(item.max_single_order_qty)
        else:
            item_dict['max_single_order_qty'] = 0.0

        if item.qty_on_request:
            item_dict['qty_on_request'] = float(item.qty_on_request)
        else:
            item_dict['qty_on_request'] = 0.0

        if item.qty_received_date:
            item_dict['qty_received_date'] = item.qty_received_date.strftime('%b, %d %Y')
        else:
            item_dict['qty_received_date'] = None

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
            item_dict['primary_supplier'] = {}
            item_dict['primary_supplier']['contact_name'] = item.primary_supplier.contact_name
            item_dict['primary_supplier']['id'] = item.primary_supplier.id
            item_dict['primary_supplier']['city'] = item.primary_supplier.city
            item_dict['primary_supplier']['address_1'] = item.primary_supplier.address_1
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
            item_dict['item_unit_measure_id'] = item.item_unit_measure.id
        else:
            item_dict['item_unit_measure'] = 'Unit not configured'

        if item.terms:
            item_dict['terms'] = item.terms.term
            item_dict['terms_id'] = item.terms.id
        else:
            item_dict['terms'] = None

        if item.warehouse_location != '':
            item_dict['warehouse_location'] = item.warehouse_location
            # item_dict['location_description'] = item.warehouse_location.description
        if item.production_type:
            item_dict['production_type'] = item.production_type.production_type_name
        else:
            item_dict['production_type'] = None

        item_dict['search_string'] = item.search_string


        item_dict['permission'] = {}
        item_dict['permission']['can_add_item'] = user.has_perm("inventory.add_item")
        item_dict['permission']['can_view_item'] = user.has_perm("inventory.view_item")
        item_dict['permission']['can_change_item'] = user.has_perm("inventory.change_item")
        item_dict['permission']['can_delete_item'] = user.has_perm("inventory.delete_item")


        inventory_dict_list.append(item_dict)
    json_posts = json.dumps(inventory_dict_list)
    return HttpResponse(json_posts, mimetype='application/json')


def get_filtered_items(request):
    if request.method == "GET":
        terms = request.GET.get('term','')
        if terms:
            items = Item.objects.filter(item_number__contains=terms) #. 'production_type', 'search_string')
        else:
            items = Item.objects.all()
        inventory_dict_list = []
        for item in items:
            item_dict = {}
            item_dict['label'] = item.item_number
            item_dict['value'] = item.item_number
            inventory_dict_list.append(item_dict)

        json_posts = json.dumps(inventory_dict_list)
        return HttpResponse(json_posts, mimetype='application/json')

def get_item(request, itemnumber):
    # import pdb; pdb.set_trace();
    user = request.user
    item = Item.objects.get(item_number=itemnumber)
    item_dict = {}
    item_dict['item_number'] = item.item_number
    item_dict['label'] = item.item_number
    item_dict['description'] = item.description
    if item.qty_received:
        item_dict['qty_received'] = float(item.qty_received)
    else:
        item_dict['qty_received'] = 0.0

    if item.qty_received_date:
        item_dict['qty_received_date'] = item.qty_received_date.strftime('%b, %d %Y')
    else:
        item_dict['qty_received_date'] = None

    if item.wholesale_cost:
        item_dict['wholesale_cost'] = item.wholesale_cost.to_eng_string()
    else:
        item_dict['wholesale_cost'] = 0.0

    if item.lead_time:
        item_dict['lead_time'] = item.lead_time
    else:
        item_dict['lead_time'] = None

    if item.retail_price:
        item_dict['retail_price'] = item.retail_price.to_eng_string()
    else:
        item_dict['retail_price'] = 0.0

    if item.estimated_wholesale_cost:
        item_dict['estimated_wholesale_cost'] = float(item.estimated_wholesale_cost)
    else:
        item_dict['estimated_wholesale_cost'] = 0.0

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
    
    if not item.qty_on_request:
        item_dict['qty_on_request'] = 0
    else:
        item_dict['qty_on_request'] = float(item.quantity_on_order)

    if not item.quantity_on_order:
        item_dict['quantity_on_order'] = 0
    else:
        item_dict['quantity_on_order'] = float(item.quantity_on_order)

    if item.primary_supplier:
        item_dict['primary_supplier'] = {}
        item_dict['primary_supplier']['contact_name'] = item.primary_supplier.contact_name
        item_dict['primary_supplier']['id'] = item.primary_supplier.id
        item_dict['primary_supplier']['city'] = item.primary_supplier.city
        item_dict['primary_supplier']['address_1'] = item.primary_supplier.address_1

        phones = ContactPhone.objects.filter(contact=item.primary_supplier)
        if phones:
            phone_list = []
            for phone in phones:
                phone_dict = {}
                phone_dict['type'] = phone.phone_type.phone_type
                phone_dict['number'] = phone.phone
                phone_dict['ext'] = phone.phone_ext
                phone_list.append(phone_dict)
            item_dict['primary_supplier']['phones'] = phone_list

    else:
        item_dict['primary_supplier'] = None

    if item.last_PO_date_ordered:
        item_dict['last_ordered'] = item.last_PO_date_ordered.isoformat()
    else:
        item_dict['last_ordered'] = None

    if item.last_PO:
        item_dict['last_po'] = item.last_PO
    else:
        item_dict['last_po'] = None


    if item.department:
        item_dict['department'] = item.department.name
        item_dict['department_id'] = item.department.id
    else:
        item_dict['department'] = 'Not Configured'

    if item.item_unit_measure:
        item_dict['item_unit_measure'] = item.item_unit_measure.unit_name
        item_dict['item_unit_measure_id'] = item.item_unit_measure.id
    else:
        item_dict['item_unit_measure'] = 'Unit not configured'

    if item.terms:
        item_dict['terms'] = item.terms.term
        item_dict['terms_id'] = item.terms.id
    else:
        item_dict['terms'] = None

    if item.warehouse_location:
        item_dict['warehouse_location'] = item.warehouse_location
        # item_dict['warehouse_location_id'] = item.warehouse_location.id
        # item_dict['location_description'] = item.warehouse_location.description
    if item.production_type:
        item_dict['production_type'] = item.production_type.production_type_name
        item_dict['production_type_id'] = item.production_type.id
    else:
        item_dict['production_type'] = None

    item_dict['customer_tariff_number'] = item.customer_tariff_number
    item_dict['preference_criteria'] = item.preference_criteria

    if item.shipping_weight:
        item_dict['shipping_weight'] = float(item.shipping_weight)
    else:
        item_dict['shipping_weight'] = 0.0
    # import pdb; pdb.set_trace();
    if item.minimum_qty_on_hand:
        item_dict['minimum_qty_on_hand'] = float(item.minimum_qty_on_hand)
    else:
        item_dict['minimum_qty_on_hand'] = 0

    if item.catalog_number:
        item_dict['catalog_number'] = item.catalog_number
    else:
        item_dict['catalog_number'] = None
    
    if item.max_order_qty:
        item_dict['max_order_qty'] = float(item.max_order_qty)
    else:
        item_dict['max_order_qty'] = 0
    
    if item.max_single_order_qty:
        item_dict['max_single_order_qty'] = float(item.max_single_order_qty)
    else:
        item_dict['max_single_order_qty'] = 0

    if item.duty_percentage:
        item_dict['duty_percentage'] = float(item.duty_percentage)
    else:
        item_dict['duty_percentage'] = 0.0
    item_dict['website'] = item.website

    if item.producer_of_item:        
        item_dict['producer_of_item'] = {}
        item_dict['producer_of_item']['contact_name'] = item.producer_of_item.contact_name
        item_dict['producer_of_item']['id'] = item.producer_of_item.id
        item_dict['producer_of_item']['city'] = item.producer_of_item.city
        item_dict['producer_of_item']['address_1'] = item.producer_of_item.address_1

        phones = ContactPhone.objects.filter(contact=item.producer_of_item)
        if phones:
            
            phone_list = []
            for phone in phones:
                phone_dict = {}
                phone_dict['phone_type'] = phone.phone_type.phone_type
                phone_dict['phone'] = phone.phone
                phone_dict['phone_ext'] = phone.phone_ext
                phone_list.append(phone_dict)
            item_dict['producer_of_item']['phones'] = phone_list
    else:
        item_dict['producer_of_item'] = None

    if item.customs_designation:
        item_dict['customs_designation'] = item.customs_designation.designation
        item_dict['customs_designation_id'] = item.customs_designation.id
    else:
        item_dict['customs_designation'] = None

    if item.country_of_origin:
        item_dict['country_of_origin'] = item.country_of_origin
    else:
        item_dict['country_of_origin'] = None

    item_dict['search_string'] = item.search_string

    if item.item_image:
        item_dict['item_image'] = item.item_image.url


    item_dict['permission'] = {}
    item_dict['permission']['can_add_item'] = user.has_perm("inventory.add_item")
    item_dict['permission']['can_view_item'] = user.has_perm("inventory.view_item")
    item_dict['permission']['can_change_item'] = user.has_perm("inventory.change_item")
    item_dict['permission']['can_delete_item'] = user.has_perm("inventory.delete_item")

    item_json = json.dumps(item_dict)
    return HttpResponse(item_json, mimetype='application/json')


def inventory_items(request):
    return render(request, "inventory/item/items.html",{})


def search_item(request):
    # import pdb; pdb.set_trace()
    query = request.GET.get('q','')
    if request.GET.get('q'):
        items = SearchQuerySet().using('inventory').filter(content=AutoQuery(query)).load_all()[:20]
        # items = SearchQuerySet().models(Item).filter(content=AutoQuery(query)).models(Item).load_all()[:20]
    else:
        items = SearchQuerySet().using('inventory').all().load_all()[:20]

    item_list = []
    for item in items:

        item_dict = {}
        item_dict['item_number'] = item.item_number
        if item.date_added:
            item_dict['date_added'] = item.date_added.strftime('%b, %d %Y')
        else:
            item_dict['date_added'] = None
        item_dict['description'] = item.description
        item_dict['primary_supplier'] = item.primary_supplier
        item_dict['last_PO'] = item.last_PO
        if item.terms:
            item_dict['terms'] = item.terms
            item_dict['terms_id'] = item.terms_id
        item_dict['cost'] = item.wholesale_cost
        item_dict['quantity_on_hand'] = item.quantity_on_hand
        item_dict['quantity_on_order'] = item.quantity_on_order
        item_dict['qty_on_request'] = item.qty_on_request
        item_dict['max_single_order_qty'] = item.max_single_order_qty
        item_dict['max_order_qty_remains'] = item.max_order_qty_remains
        item_dict['max_order_qty'] = item.max_order_qty
        item_dict['production_type'] = item.production_type
        item_dict['order_restriction'] = item.order_restriction
        if item.currency:
            item_dict['currency'] = item.currency
            item_dict['currency_id'] = item.currency_id
        item_dict['department'] = item.department
        item_dict['item_unit_measure'] = item.item_unit_measure
        item_dict['item_unit_measure_id'] = item.item_unit_measure_id
        item_dict['warehouse_location'] = item.warehouse_location
        # item_dict['hst_taxable'] = item.hst_taxable
        # item_dict['pst_taxable'] = item.pst_taxable
        if item.supplier:
            supplier_doc = {}
            supplier_doc['contact_name'] = item.supplier['contact_name']
            supplier_doc['hst_tax'] = item.supplier['hst_tax']
            supplier_doc['pst_tax'] = item.supplier['pst_tax']
            supplier_doc['id'] = item.supplier['id']
            supplier_doc['address_1'] = item.supplier['address_1']
            supplier_doc['attention_to'] = item.supplier['attention_to']
            supplier_doc['city'] = item.supplier['city']
            supplier_doc['province'] = item.supplier['province']
            supplier_doc['country'] = item.supplier['country']
            supplier_doc['postal_code'] = item.supplier['postal_code']
            supplier_doc['phones'] = item.supplier['phones']
            supplier_doc['emails'] = item.supplier['emails']
            

            item_dict['supplier'] = supplier_doc


        item_list.append(item_dict)
    
    try:
        page = int(request.GET.get('page','1'))
    except ValueError:
        page = 1
    paginator = Paginator(item_list, 20)
    try:
        pages = paginator.page(page)
    except (EmptyPage, InvalidPage):
        pages = paginator.page(paginator.num_pages)

    results = pages.object_list

    data = json.dumps(results)
    return HttpResponse(data)


@csrf_exempt
@permission_required('inventory.delete_item')
def delete_item(request):
    '''
    Delete job of id = jobid. jobid is recieved from ajax call through request object.
    '''
    if request.method == "POST":
        item_number = json.loads(request.body).get('item_number')
        item = Item.objects.get(item_number=item_number)
        try:
            item.delete()
            return HttpResponse(item_number)
        except:
            return HttpResponse(item_number)


@login_required
@permission_required("inventory.view_itemunitmeasure")
def list_unit_measue(request):
    unit_measures = ItemUnitMeasure.objects.all()
    return render(request, "inventory/unit-measure/list-unit-measure.html", {'unit_measures': unit_measures, 'page_title': 'List Unit Measure'})

# @login_required
def list_unit_measue_json2(request):
    unit_measures = ItemUnitMeasure.objects.filter(is_active=True)
    ums = []
    for unit in unit_measures:
        um = {}
        um['id'] = unit.id
        um['unit_name'] = unit.unit_name
        ums.append(um)
    um_json = json.dumps(ums)
    return HttpResponse(um_json, mimetype='application/json')

@login_required
@permission_required("inventory.add_itemunitmeasure")
@csrf_exempt
def add_unit_measue(request):
    if request.method == "POST":
        unit_name = request.POST.get("unit_name")
        try:
            unit_measure = ItemUnitMeasure.objects.create(unit_name=unit_name, is_active=True)
            return render(request, "inventory/unit-measure/add-unit-measure-partial.html",
                {'unit_measure': unit_measure})
        except:
            return HttpResponse("error")
    else:
        unit_measures = ItemUnitMeasure.objects.all()
        unit_measure_form = ItemUnitMeasureForm()

        return render(request, "inventory/unit-measure/add-list-unit-measure.html",
            {'unit_measures': unit_measures, 'unit_measure_form': unit_measure_form, 'page_title': 'Add Unit Measure'})


@login_required
@permission_required("inventory.change_itemunitmeasure")
@csrf_exempt
def edit_unit_measue(request, unit_mes_id):
    if request.method == "POST":
        unit_mes_id = request.POST.get("unit_mes_id")
        unit_measure = ItemUnitMeasure.objects.get(id=unit_mes_id)
        unit_measure_form = ItemUnitMeasureForm(request.POST, instance=unit_measure)
        if unit_measure_form.is_valid():
            unit_measure = unit_measure_form.save()
            return render(request, "inventory/unit-measure/add-unit-measure-partial.html",
            {'unit_measure': unit_measure})
    elif request.method == "GET":
        unit_measure = ItemUnitMeasure.objects.get(id=unit_mes_id)
        unit_measure_form = ItemUnitMeasureForm(instance=unit_measure)

        return render(request, "inventory/unit-measure/edit-unit-measure-tmpl.html",
            {'unit_measure_form': unit_measure_form, 'unit_mes_id': unit_mes_id})


@csrf_exempt
@login_required
@permission_required("inventory.delete_itemunitmeasure")
def delete_unit_measue(request):
    if request.method == "POST":
        unit_measure_id = request.POST.get("unit_measure_id")
        unit_measure = ItemUnitMeasure.objects.get(id=unit_measure_id)
        unit_measure.delete()
        return HttpResponse(unit_measure_id)
    else:
        return HttpResponse("Hello World!")


# location start here
@login_required
@permission_required("inventory.add_location")
@csrf_exempt
def add_location(request):
    if request.method == "POST":
        location_frm = LocationForm(request.POST)
        if location_frm.is_valid():
            location_frm.save()
            return HttpResponseRedirect("/inventory/location-list/")
    else:
        location_frm = LocationForm()
    
    return render(request, "inventory/location/add-location.html",
            {'location_frm': location_frm, 'page_title': 'Add Unit Measure'})


@login_required
@permission_required("inventory.change_location")
@csrf_exempt
def edit_location(request, loc_id):
    location = Location.objects.get(id=loc_id)
    if request.method == "POST":
        location_frm = LocationForm(request.POST, instance=location)
        if location_frm.is_valid():
            location_frm.save()
            return HttpResponseRedirect("/inventory/location-list/")
    else:
        location_frm = LocationForm(instance=location)
    
    return render(request, "inventory/location/edit-location.html",
            {'location_frm': location_frm, 'loc_id':loc_id, 'page_title': 'Edit Unit Measure'})


@csrf_exempt
@login_required
@permission_required("inventory.delete_location")
def delete_location(request):
    if request.method == "POST":
        loc_id = request.POST.get("loc_id")
        location = Location.objects.get(id=loc_id)
        location.delete()
        return HttpResponse(loc_id)
    else:
        return HttpResponse("Hello World!")

@login_required
@permission_required("inventory.view_location")
def list_location(request):
    locations = Location.objects.all()
    return render(request, "inventory/location/list-location.html", 
        {'locations': locations, 'page_title': 'List Location'})



@login_required
@permission_required("inventory.view_productiontype")
def list_production_type(request):
    production_types = ProductionType.objects.all()
    return render(request, "inventory/production-type/list-production-type.html", 
        {'production_types': production_types, 'page_title': 'List Production Type'})


@login_required
@permission_required("inventory.add_productiontype")
@csrf_exempt
def add_production_type(request):
    if request.method == "POST":
        production_type_name = request.POST.get("production_type_name")
        try:
            production_type = ProductionType.objects.create(production_type_name=production_type_name, is_active=True)
            return render(request, "inventory/production-type/add-production-type-partial.html",
                {'production_type': production_type})
        except:
            return HttpResponse("error")
    else:
        production_types = ProductionType.objects.all()
        production_type_form = ProductionTypeForm()

        return render(request, "inventory/production-type/add-list-production-type.html",
            {'production_types': production_types, 'production_type_form': production_type_form, 'page_title': 'Add Production Type'})


@login_required
@permission_required("inventory.change_productiontype")
@csrf_exempt
def edit_production_type(request, prod_type_id):
    if request.method == "POST":
        prod_type_id = request.POST.get("prod_type_id")
        production_type = ProductionType.objects.get(id=prod_type_id)
        production_type_form = ProductionTypeForm(request.POST, instance=production_type)
        if production_type_form.is_valid():
            production_type = production_type_form.save()
            return render(request, "inventory/production-type/add-production-type-partial.html",
            {'production_type': production_type})
    elif request.method == "GET":
        production_type = ProductionType.objects.get(id=prod_type_id)
        production_type_form = ProductionTypeForm(instance=production_type)

        return render(request, "inventory/production-type/edit-production-type-tmpl.html",
            {'production_type_form': production_type_form, 'prod_type_id': prod_type_id})


@csrf_exempt
@login_required
@permission_required("inventory.delete_productiontype")
def delete_production_type(request):
    if request.method == "POST":
        production_type_id = request.POST.get("production_type_id")
        production_type = ProductionType.objects.get(id=production_type_id)
        production_type.delete()
        return HttpResponse(production_type_id)
    else:
        return HttpResponse("Hello World!")




@login_required
@permission_required("inventory.view_customdesignation")
def list_custom_designation(request):
    custom_designations = CustomsDesignation.objects.all()
    return render(request, "inventory/custom-designation/list-custom-designation.html", 
        {'custom_designations': custom_designations, 'page_title': 'List Custom Designation'})


@login_required
@permission_required("inventory.add_customdesignation")
@csrf_exempt
def add_custom_designation(request):
    if request.method == "POST":
        designation = request.POST.get("designation")
        try:
            custom_designation = CustomsDesignation.objects.create(designation=designation, is_active=True)
            return render(request, "inventory/custom-designation/add-custom-designation-partial.html",
                {'custom_designation': custom_designation})
        except:
            return HttpResponse("error")
    else:
        custom_designations = CustomsDesignation.objects.all()
        custom_designation_form = CustomsDesignationForm()

        return render(request, "inventory/custom-designation/add-list-custom-designation.html",
            {'custom_designations': custom_designations, 'custom_designation_form': custom_designation_form, 'page_title': 'Add Custom Designation'})


@login_required
@permission_required("inventory.change_customdesignation")
@csrf_exempt
def edit_custom_designation(request, cus_des_id):
    if request.method == "POST":
        cus_des_id = request.POST.get("cus_des_id")
        custom_designation = CustomsDesignation.objects.get(id=cus_des_id)
        custom_designation_form = CustomsDesignationForm(request.POST, instance=custom_designation)
        if custom_designation_form.is_valid():
            custom_designation = custom_designation_form.save()
            return render(request, "inventory/custom-designation/add-custom-designation-partial.html",
            {'custom_designation': custom_designation})
    elif request.method == "GET":
        custom_designation = CustomsDesignation.objects.get(id=cus_des_id)
        custom_designation_form = CustomsDesignationForm(instance=custom_designation)

        return render(request, "inventory/custom-designation/edit-custom-designation-tmpl.html",
            {'custom_designation_form': custom_designation_form, 'cus_des_id': cus_des_id})


@csrf_exempt
@login_required
@permission_required("inventory.delete_customdesignation")
def delete_custom_designation(request):
    if request.method == "POST":
        custom_designation_id = request.POST.get("custom_designation_id")
        custom_designation = CustomsDesignation.objects.get(id=custom_designation_id)
        custom_designation.delete()
        return HttpResponse(custom_designation_id)
    else:
        return HttpResponse("Hello World!")

@csrf_exempt
@login_required
def item_reindex(request):
    items = Item.objects.all()
    for item in items:
        item.search_string = item.item_number + " " + item.description
        if item.primary_supplier:
            item.search_string += " " + item.primary_supplier.contact_name
        item.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])





# Deliver Internal start here
@login_required
@permission_required("purchase.add_deliverinternal")
@csrf_exempt
def add_deliverinternal(request):
    if request.method == "POST":
        deliverinternal_frm = DeliverInternalForm(request.POST)
        if deliverinternal_frm.is_valid():
            deliverinternal_frm.save()
            return HttpResponseRedirect("/inventory/deliverinternal-list/")
    else:
        deliverinternal_frm = DeliverInternalForm()
    
    return render(request, "inventory/add-deliverinternal.html",
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
            return HttpResponseRedirect("/inventory/deliverinternal-list/")
    else:
        deliverinternal_frm = DeliverInternalForm(instance=deliverinternal)
    
    return render(request, "inventory/edit-deliverinternal.html",
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
    return render(request, "inventory/list-deliverinternal.html", 
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
