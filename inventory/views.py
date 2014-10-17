from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from inventory.forms import *
# Create your views here.
from scomuser.models import *
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
import json

from contacts.models import *

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
        item_form = ItemForm(request.POST, request.FILES)
        if item_form.is_valid():
            item = item_form.save()
            return HttpResponseRedirect("/inventory/list/#/inventory/items")  
    else:
        item_form = ItemForm()

    # return HttpResponse(item_form)

    # return render(request, "inventory/item/test.html", {'item_form': item_form, 'page_title': 'Add Item'})
    
    return render(request, "inventory/item/add-item.html", 
        {'item_form': item_form, 'page_title': 'Add Item', 'currencies': currencies, 
        'departments': departments, 'unit_measures': unit_measures, 'locations': locations,
        'production_types': production_types, 'terms': terms})

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
    # import pdb; pdb.set_trace()
    item = Item.objects.get(item_number=itemid)
    if item.primary_supplier:
        contact_id = item.primary_supplier.id
    else:
        contact_id = None
    if request.method == 'POST':
        # import pdb; pdb.set_trace();
        item_form = ItemForm(request.POST,request.FILES, instance=item)
        if item_form.is_valid():
            item_form.save()
            return HttpResponseRedirect("/inventory/list/#/inventory/items")
    else:
        item_form = ItemForm(instance=item)
        item_comment_form = ItemCommentForm()
        item_comments = ItemComment.objects.filter(item=item).order_by("-id")
        return render(request, "inventory/item/edit-item.html", 
            {'item_form': item_form, 'itemid':itemid, 'contact_id': contact_id, 
            'page_title': 'Update Item', 'item_comments': item_comments,
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
    # import pdb; pdb.set_trace();
    user = request.user
    items = Item.objects.all() #. 'production_type', 'search_string')
    inventory_dict_list = []
    for item in items:
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
            item_dict['item_unit_measure_id'] = item.item_unit_measure.id
        else:
            item_dict['item_unit_measure'] = 'Unit not configured'

        if item.terms:
            item_dict['terms'] = item.terms.term
            item_dict['terms_id'] = item.terms.id
        else:
            item_dict['terms'] = None

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



def inventory_items(request):
    return render(request, "inventory/item/items.html",{})

@csrf_exempt
@permission_required('inventory.delete_item')
def delete_item(request):
    '''
    Delete job of id = jobid. jobid is recieved from ajax call through request object.
    '''
    if request.method == "POST":
        itemid = request.POST.get("itemid")
        item = Item.objects.get(item_number=itemid)
        try:
            item.delete()
            return HttpResponse(itemid)
        except:
            return HttpResponse(itemid)


@login_required
@permission_required("inventory.view_itemunitmeasure")
def list_unit_measue(request):
    unit_measures = ItemUnitMeasure.objects.all()
    return render(request, "inventory/unit-measure/list-unit-measure.html", {'unit_measures': unit_measures, 'page_title': 'List Unit Measure'})

@login_required
def list_unit_measue_json(request):
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