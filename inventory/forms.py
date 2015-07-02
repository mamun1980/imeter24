from django import forms
from django.contrib import admin
from inventory.models import *
from inventory.lookups import *
from inventory.choices import *
from contacts.models import *
import selectable
from django.db import models
from django.utils.safestring import mark_safe
from premierelevator.models import SystemVariable
from django.forms import Widget, TextInput
import re
import datetime


class PremierTextInput(TextInput):
	"""docstring for PremierTextInput"""
	# def __init__(self, arg):
	# 	super(PremierTextInput, self).__init__()
	
	def render(self, name, value, attrs=None):
		str1 = TextInput.render(self, name, value, attrs)
		str2 = '<a href="/admin/contacts/contact/add/" class="add-another" id="add_id_primary_supplier" onclick="return showAddAnotherPopup(this);"> <img src="/statics/admin/img/icon_addlink.gif" width="10" height="10" alt="Add Another"></a>'
		output = str1 + str2
		return mark_safe(output)

		

class ItemUnitMeasureForm(forms.ModelForm):
	unit_name = forms.CharField( max_length=25,
        widget=forms.TextInput(attrs={"class": "form-control", 'required': 'True', 'placeholder':"Item Unit Measure"}))

	class Meta:
		model = ItemUnitMeasure
		exclude = ['is_active',]


class ProductionTypeForm(forms.ModelForm):
	production_type_name = forms.CharField( max_length=25,
        widget=forms.TextInput(attrs={"class": "form-control", 'required': 'True', 'placeholder': "Production Type"}))

	class Meta:
		model = ProductionType
		exclude = ['is_active',]


class CustomsDesignationForm(forms.ModelForm):
	designation = forms.CharField( max_length=25,
        widget=forms.TextInput(attrs={"class": "form-control", 'required': 'True', 'placeholder': "Custom Designation"}))

	class Meta:
		model = CustomsDesignation
		exclude = ['is_active',]


class ItemForm(forms.ModelForm):
	item_number = forms.CharField( max_length=25,
        widget=forms.TextInput(attrs={"class": "form-control", "value": 'NEW', 'readonly': 'readonly'}))
	description = forms.CharField( max_length=250, required=False,
        widget=forms.Textarea(attrs={"class": "form-control", 'rows':2, 'required': 'False', 'placeholder':"Item Description"}))
	currency = forms.ModelChoiceField(required=False, queryset=Currency.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}))
	wholesale_cost = forms.DecimalField(max_digits=10, decimal_places=4, required=False,
        widget=forms.NumberInput(attrs={"class": "form-control decimal", 'placeholder':"Wholesale cost"}))
	quantity_on_hand = forms.DecimalField(max_digits=10, decimal_places=4, required=False,
        widget=forms.NumberInput(attrs={"class": "form-control decimal", 'placeholder':"Quantity on hand", "step": 1}))
	quantity_on_order = forms.DecimalField(max_digits=10, decimal_places=4, required=False,
        widget=forms.NumberInput(attrs={"class": "form-control decimal", 'placeholder':"Quantity on order", "step": 1}))
	
	department = forms.ModelChoiceField(required=False, queryset=Department.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}))

	primary_supplier = forms.ModelChoiceField(required=False, queryset=Contact.objects.all(), 
		widget=forms.Select(attrs={"class": "form-control"}))
	
	
	# comments = forms.CharField( max_length=250, required=False,
 #        widget=forms.Textarea(attrs={"class": "form-control", 'rows':2, 'placeholder':"Comments"}))
	item_unit_measure = forms.ModelChoiceField(required=False, queryset=ItemUnitMeasure.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}), label='Production Type List')

	# stock_status_type = forms.ChoiceField(required=False, choices=STOCK_STATUS_TYPE,
 #        widget=forms.Select(attrs={"class": "form-control"}))
	warehouse_location = forms.ModelChoiceField(required=False, queryset=Location.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}))

	# lowest_price_supplier = forms.ModelChoiceField(required=False, queryset=Contact.objects.all(), 
	# 	widget=forms.Select(attrs={"class": "form-control"}))
	# lowest_price_paid = forms.DecimalField(max_digits=10, decimal_places=2, required=False,
 #        widget=forms.NumberInput(attrs={"class": "form-control", 'placeholder':"Lowest price paid"}))
	# lowest_price_last_buy_date = forms.DateField(required=False, widget=forms.DateInput(
 #        attrs={"class": "form-control datepicker", 'placeholder':""}))
	# lowest_price_last_buy_PO = forms.ModelChoiceField(required=False, queryset=PurchaseOrder.objects.all(), 
	# 	widget=forms.Select(attrs={"class": "form-control"}))


	# qty_on_request = forms.DecimalField(max_digits=10, decimal_places=2, required=False,
 #        widget=forms.NumberInput(attrs={"class": "form-control decimal", 'placeholder':"Quantity on request"}))
	
	max_order_qty = forms.DecimalField(max_digits=10, decimal_places=4, required=False,
        widget=forms.NumberInput(attrs={"class": "form-control decimal", 'placeholder':"Maximum Order Quenty"}))
	max_single_order_qty = forms.DecimalField(max_digits=10, decimal_places=4, required=False,
        widget=forms.NumberInput(attrs={"class": "form-control decimal", 'placeholder':"Maximum Single Order Quenty"}))
	retail_price = forms.DecimalField(max_digits=10, decimal_places=4, required=False,
        widget=forms.NumberInput(attrs={"class": "form-control decimal", 'placeholder':"Retail Price"}))
	estimated_wholesale_cost = forms.DecimalField(max_digits=10, decimal_places=4, required=False,
        widget=forms.NumberInput(attrs={"class": "form-control decimal", 'placeholder':"Estimated wholesale cost"}))
	production_type = forms.ModelChoiceField(required=False, queryset=ProductionType.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}))
	
	catalog_number = forms.CharField( max_length=25, required=False,
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder':"Catalog Number"}))
	country_of_origin = forms.CharField( max_length=25, required=False,
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder':"Country of Origin"}))
	lead_time = forms.CharField( max_length=25, required=False,
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder':"Lead Time"}))
	customs_designation = forms.ModelChoiceField(required=False, queryset=CustomsDesignation.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}))
	customer_tariff_number = forms.CharField(max_length=25, required=False,
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder':"Lead Time"}))
	preference_criteria = forms.CharField(max_length=25, required=False,
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder':"Preference Criteria"}))
	producer_of_item = forms.ModelChoiceField(required=False, queryset=Contact.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}))
	shipping_weight = forms.DecimalField(max_digits=10, decimal_places=4, required=False,
        widget=forms.NumberInput(attrs={"class": "form-control", 'placeholder':"Shipping weight"}))
	minimum_qty_on_hand = forms.DecimalField(max_digits=10, decimal_places=4, required=False,
        widget=forms.NumberInput(attrs={"class": "form-control decimal", 'placeholder':"Minimum quantity on hand"}))
	duty_percentage = forms.DecimalField(max_digits=10, decimal_places=4, required=False,
        widget=forms.NumberInput(attrs={"class": "form-control decimal", 'placeholder':"Duty percentage"}))
	# site = forms.ModelChoiceField(required=False, queryset=Contact.objects.all(),
 #        widget=forms.Select(attrs={"class": "form-control"}))
	terms = forms.ModelChoiceField(required=False, queryset=PaymentTerm.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}))
	website = forms.CharField(max_length=250, required=False,
        widget=forms.URLInput(attrs={"class": "form-control", 'placeholder':"product page url"}))
	# item_image = forms.CharField(max_length=250, required=False,
 #        widget=forms.ClearableFileInput(attrs={"class": "form-control"}))
	# date_added = forms.DateTimeField(required=False, 
	# 	widget=forms.DateTimeInput(attrs={"class": "form-control datetimepicker", 'placeholder':"Date added"}))
	
	# def __init__(self, *args, **kwargs):
	# 	super(ItemForm, self).__init__(*args, **kwargs)
	# 	# rel = models.ManyToOneRel(Contact, 'id', '')
	# 	self.fields['primary_supplier'].widget = admin.widgets.RelatedFieldWidgetWrapper(
	# 		self.fields['primary_supplier'].widget, 
	# 		Item._meta.get_field('primary_supplier').rel,
	# 		self.admin_site)
	def __init__(self, *args, **kwargs):
		self.request = kwargs.pop('request', None)
		self.action = kwargs.pop('action', None)
		super(ItemForm, self).__init__(*args, **kwargs)

	class Meta:
		model = Item
		fields = ('item_number', 'description', 'currency', 'wholesale_cost', 'quantity_on_hand', 
			'quantity_on_order', 'qty_on_request', 'department', 'primary_supplier', 
			'item_unit_measure', 'warehouse_location', 'max_order_qty', 
			'max_single_order_qty', 'estimated_wholesale_cost', 'retail_price', 'production_type',
			'catalog_number', 'country_of_origin', 'lead_time', 'customs_designation', 
			'customer_tariff_number', 'preference_criteria', 'producer_of_item', 'shipping_weight', 
			'minimum_qty_on_hand', 'duty_percentage', 'terms', 'website', 'item_image')

	def save(self, commit=True):
		item = super(ItemForm, self).save(commit=False)
		if self.action == 'new':
			item.max_order_qty_remains = item.max_order_qty
			item.quantity_on_hand = 0.0;
			item.quantity_on_order = 0.0;
			item.qty_received = 0.0;
			item.qty_on_request = 0.0;
			item.date_added = datetime.datetime.now();
			item.stock_status_type = 'no-stock';
		
		item.save()
		return item


class ItemCommentForm(forms.ModelForm):
	comment = forms.CharField( max_length=250, required=False,
        widget=forms.Textarea(attrs={"class": "form-control", 'rows':2, 'placeholder':"Item Comment"}))
	
	class Meta:
		model = ItemComment
		exclude = ['item', 'comment_date', 'comment_by']


class ItemLookupForm(forms.Form):
	autocomplete = forms.CharField(
          label='Type for auto suggession',
          widget=selectable.forms.AutoCompleteWidget(ContactLookup, 
          attrs={"class": "form-control", 'placeholder': "Filter item but item number, department and product type", 'name': 'item-autocomplete-filter'}),
          required=False,

      )



class LocationForm(forms.ModelForm):
	warehouse_location = forms.CharField( max_length=50,
        widget=forms.TextInput(attrs={"class": "form-control", 'required': 'True', 'placeholder':"Location"}))
	description = forms.CharField( max_length=250, required=False,
        widget=forms.Textarea(attrs={"class": "form-control", 'rows':2, 'required': 'False', 'placeholder':"Location Description"}))
	
	class Meta:
		model = Location	





