from django import forms
from purchase.models import *
from purchase.choices import *
from contacts.models import *
from premierelevator.models import SystemVariable
import datetime
import re


class CustomModelChoiceField(forms.ModelChoiceField):
     def label_from_instance(self, obj):
         return "%s %s" % (obj.first_name, obj.last_name)


class PRAddForm(forms.ModelForm):
    user_requested = CustomModelChoiceField(required=False, queryset=User.objects.filter(id__gte=0), 
        widget=forms.Select(attrs={"class": "form-control"}))
    item = forms.ModelChoiceField(required=False, queryset=Item.objects.all(), 
        widget=forms.Select(attrs={"class": "form-control"}))
    description = forms.CharField(required=False,
        widget=forms.Textarea(attrs={"class": "form-control", "rows":3, 'placeholder':"Describe why needed.."}))
    order_qty = forms.DecimalField( max_digits=10, required=False, decimal_places=2,
        widget=forms.NumberInput(attrs={"class": "form-control decimal", 'placeholder': "qty"}))
    item_require_before = forms.DateField(required=False, widget=forms.DateInput(
        attrs={"class": "form-control datepicker", 'placeholder':"Item Require Before",}))

    class Meta:
        """docstring for Meta"""
        model = PurchaseRequest
        exclude = ['approved_qty', 'requeste_created_at', 'status', 'approved_date']


class PRApproveForm(forms.ModelForm):
    approved_qty = forms.DecimalField( max_digits=10, required=False, decimal_places=2,
        widget=forms.NumberInput(attrs={"class": "form-control decimal", 'placeholder': "qty"}))
    
    class Meta:
        """docstring for Meta"""
        model = PurchaseRequest
        exclude = ['user_requested', 'status', 'item', 'description', 'order_qty', 'item_require_before',  'requeste_created_at', 'approved_date']

class PRCAddForm(forms.ModelForm):
    comment = forms.CharField(required=True,
        widget=forms.Textarea(attrs={"class": "form-control", "rows":3}))

    class Meta:
        """docstring for Meta"""
        model = PurchaseRequestComment
        exclude = ['purchase_request', 'commnet_date', 'user_commented']


class POForm(forms.ModelForm):
    po_number = forms.CharField( max_length=20, required=False,
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': "PO Number", 'readonly':'readonly'}))
    next_number = forms.CharField( max_length=20, required=False,
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': "Next PO Number", 'readonly':'readonly'}))
    date_issued = forms.DateField(required=False, widget=forms.DateInput(
        attrs={"class": "form-control", 'placeholder':"date issued",  'readonly':'readonly'}))
    date_expected = forms.DateField(required=False, widget=forms.DateInput(
        attrs={"class": "form-control datepicker", 'placeholder':"date expected"}))
    supplier = forms.ModelChoiceField(required=False, queryset=Contact.objects.all(), 
        widget=forms.Select(attrs={"class": "form-control"}))
    ship_to = forms.ModelChoiceField(required=False, queryset=Contact.objects.all(), 
        widget=forms.Select(attrs={"class": "form-control"}))
    ship_via = forms.ModelChoiceField(required=False, queryset=DeliveryChoice.objects.filter(is_active=True), 
        widget=forms.Select(attrs={"class": "form-control"}))
    terms = forms.ModelChoiceField(required=False, queryset=PaymentTerm.objects.filter(is_active=True), 
        widget=forms.Select(attrs={"class": "form-control"}))
    fob = forms.CharField( max_length=200, required=False,
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': "FOB"}))
    shipping_inst = forms.CharField(required=False,
        widget=forms.Textarea(attrs={"class": "form-control", "rows":3, 'placeholder':"Shipping Inst"}))
    deliver_internal = forms.ModelChoiceField(required=False, label='Department', queryset=DeliverInternal.objects.all(), 
        widget=forms.Select(attrs={"class": "form-control"}))
    date_confirmed = forms.DateField(required=False,
        widget=forms.DateInput(attrs={"class": "form-control datepicker", 'placeholder': "Date Confirmed"}))

    blanket_po = forms.ChoiceField(choices=((0, 'NO'), (1,'YES')), required=False,
        widget=forms.Select(attrs={"class": "form-control", 'placeholder': "Blanket PO"}))
    
    purchasing_agent = CustomModelChoiceField(required=False, queryset=User.objects.filter(id__gte=0), 
        widget=forms.Select(attrs={"class": "form-control"}))
    
    returned_type = forms.ChoiceField( choices = RETURN_TYPE, required=False,
        widget=forms.Select(attrs={"class": "form-control"}), label='Type')
    items_total = forms.DecimalField(label='Items Total Qty', max_digits=10, required=False, decimal_places=4,
        widget=forms.NumberInput(attrs={"class": "form-control", 'placeholder': "Items Total", 'readonly': 'readonly'}))
    hst_taxable = forms.ChoiceField(choices=((0, 'NO'), (1,'YES')), required=False,
        widget=forms.Select(attrs={"class": "form-control", 'placeholder': "Blanket PO"}))
    pst_taxable = forms.ChoiceField(choices=((0, 'NO'), (1,'YES')), required=False,
        widget=forms.Select(attrs={"class": "form-control", 'placeholder': "Blanket PO"}))
    total_po_amount = forms.DecimalField( max_digits=10, required=False, decimal_places=4,
        widget=forms.NumberInput(attrs={"class": "form-control", 'placeholder': "Total PO Amount", 'readonly': 'readonly'}))
    po_currency = forms.ModelChoiceField(required=False, queryset=Currency.objects.all(), 
        widget=forms.Select(attrs={"class": "form-control"}))
    po_overwridden_by = CustomModelChoiceField(required=False, queryset=User.objects.filter(id__gte=0, is_superuser__exact=1), 
        widget=forms.Select(attrs={"class": "form-control"}))
    datetime = forms.CharField(required=False,
        widget=forms.DateTimeInput(attrs={"class": "form-control", 'placeholder': "YYYY-MM-DD HH:MM:SS"}))
    po_status = forms.ChoiceField(required=False, choices=PO_STATUS_ADD,
        widget=forms.Select(attrs={"class": "form-control"}))
    po_que = forms.ChoiceField(required=False, choices=PO_QUE,
        widget=forms.Select(attrs={"class": "form-control"}))

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        self.action = kwargs.pop('action', None)
        super(POForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        po = super(POForm, self).save(commit=False)
        sv = SystemVariable.objects.get(id=1)
        if self.action == 'new':
            po.po_created_by = self.request.user
            po.datetime = datetime.datetime.now()
            po_number = re.sub(r"[A-Za-z]+","",self.request.POST['po_number_search'])
            po.po_number = 'P'+str(po_number)
            sv.next_po_number = int(po_number) + 1
        elif self.action == 'update':
            po.po_created_by = self.request.user
            po.datetime = datetime.datetime.now()
            # po_number = re.sub(r"[^\w]+","",po.po_number)
            # po.po_number = 'P'+str(po_number)
            # sv.next_po_number = int(po_number) + 1
        sv.save()
        po.save()
        return po
    


    class Meta:
        """docstring for Meta"""
        model = PurchaseOrder
        exclude = ['sub_total', 'po_created_by', 'search_string', 'datetime']


class POFormEdit(POForm):
    po_status = forms.ChoiceField(required=False, choices=PO_STATUS,
        widget=forms.Select(attrs={"class": "form-control"}))


class POStatusForm(forms.ModelForm):
    status_comment = forms.CharField(max_length=1000, required=False,
        widget=forms.Textarea(attrs={"class": "form-control", "rows":2, 'placeholder':"Put Status Comments"}))

    class Meta:
        model = POStatus
        exclude = ['status', 'po', 'datetime', 'status_by']


class POStatusForm2(forms.ModelForm):
    po = forms.ModelChoiceField(required=False, queryset=PurchaseOrder.objects.all(), 
        widget=forms.Select(attrs={"class": "form-control"}))
    status = forms.ChoiceField(required=False, choices=PO_STATUS,
        widget=forms.Select(attrs={"class": "form-control"}))
    status_by = CustomModelChoiceField(required=False, queryset=User.objects.filter(id__gte=0), 
        widget=forms.Select(attrs={"class": "form-control", 'disabled':True}))
    status_comment = forms.CharField(max_length=1000, required=False,
        widget=forms.Textarea(attrs={"class": "form-control", "rows":2, 'placeholder':"Put Status Comments"}))

    class Meta:
        model = POStatus
        exclude = ['datetime',]


class POContactForm(forms.ModelForm):
    contact_type = forms.ChoiceField(required=False, choices=CON_TYPE,
        widget=forms.Select(attrs={"class": "form-control"}))
    contact = forms.CharField( max_length=100, required=False, label='Contact Info',
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': "type contact"}))
    contact_name = forms.CharField( max_length=100, required=False, label='Contact Name',
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': "contact name"}))
    
    class Meta:
        model = POContact
        exclude = ['purchase_order',]




class ItemReeiveForm(forms.ModelForm):
    # purchase_item = forms.ModelChoiceField(required=False, queryset=PurchaseItem.objects.all(), 
    #   widget=forms.Select(attrs={"class": "form-control", 'readonly':'readonly'}))
    # item_po = forms.ModelChoiceField(required=False, queryset=PurchaseOrder.objects.all(), 
    #   widget=forms.Select(attrs={"class": "form-control"}))
    qty_received = forms.DecimalField( max_digits=10, required=False, decimal_places=2,
        widget=forms.NumberInput(attrs={"class": "form-control decimal", 'placeholder': "qty received"}))
    comment = forms.CharField(max_length=1000, required=False,
        widget=forms.Textarea(attrs={"class": "form-control", "rows":2, 'placeholder':"Comments"}))

    class Meta:
        model = ReceivedItemHistory
        exclude = ['item_received_date', 'status', 'sub_total', 'reveived_by', 'search_string', 'purchase_item', 'item_po']



class PackingListForm(forms.ModelForm):
    pl_number = forms.CharField( max_length=20, required=False, label='PL Number',
        widget=forms.TextInput(attrs={"class": "form-control"}))
    sl_number = forms.ModelChoiceField(required=False, label='SL Number', queryset=ShippingList.objects.all(), 
        widget=forms.Select(attrs={"class": "form-control"}))
    sold_to = forms.ModelChoiceField(required=False, queryset=Contact.objects.all(), 
        widget=forms.Select(attrs={"class": "form-control"}))
    ship_to = forms.ModelChoiceField(required=False, queryset=Contact.objects.all(), 
        widget=forms.Select(attrs={"class": "form-control"}))
    date_issued = forms.DateField(required=False,
        widget=forms.DateInput(attrs={"class": "form-control datepicker", 'placeholder': "Date Issued"}))
    date_shipped = forms.DateField(required=False,
        widget=forms.DateInput(attrs={"class": "form-control datepicker", 'placeholder': "Date Shipped"}))
    
    shipped_by = CustomModelChoiceField(required=False, queryset=User.objects.filter(id__gte=0), 
        widget=forms.Select(attrs={"class": "form-control"}))
    nel_packing_slip = forms.ChoiceField(required=False, choices=((1, 'YES'),(0, 'NO')),
        widget=forms.Select(attrs={"class": "form-control"}))
    job_number = forms.ModelChoiceField(required=False, queryset=Job.objects.all(), 
        widget=forms.Select(attrs={"class": "form-control"}))
    generated_by = CustomModelChoiceField(required=False, queryset=User.objects.filter(id__gte=0), 
        widget=forms.Select(attrs={"class": "form-control"}))
    order_type = forms.ChoiceField(required=False, choices=PL_TYPE,
        widget=forms.Select(attrs={"class": "form-control"}))
    customer_broker = forms.ModelChoiceField(required=False, queryset=Contact.objects.all(), 
        widget=forms.Select(attrs={"class": "form-control"}))
    customer_po_number = forms.CharField( max_length=20, required=False,
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': "Customer PO Number"}))
    ship_via = forms.ModelChoiceField(required=False, queryset=DeliveryChoice.objects.filter(is_active=True), 
        widget=forms.Select(attrs={"class": "form-control"}))
    hold_at_dept_for_pickup = forms.ChoiceField(required=False, choices=((1, 'YES'),(0, 'NO')),
        widget=forms.Select(attrs={"class": "form-control"}))
    freight_charges = forms.DecimalField( max_digits=10, required=False, decimal_places=2,
        widget=forms.NumberInput(attrs={"class": "form-control", 'placeholder': "freight charges"}))
    invoiced_on = forms.DateField(required=False,
        widget=forms.DateInput(attrs={"class": "form-control datepicker", 'placeholder': 'Invoiced On'}))

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        self.action = kwargs.pop('action', None)
        super(PackingListForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        # import pdb; pdb.set_trace();
        pl = super(PackingListForm, self).save(commit=False)
        sv = SystemVariable.objects.get(id=1)
        # pl.generated_by = self.request.user
        if self.action == 'new':
            pl_number = re.sub(r"[A-Za-z]+","",self.request.POST['pl_number_search'])
            pl.pl_number = 'PL'+str(pl_number)
            sv.next_pl_number = int(pl_number) + 1
            # po_number = re.sub(r"[^\w]+","",po.po_number)
            # po.po_number = 'P'+str(po_number)
            # sv.next_po_number = int(po_number) + 1
        sv.save()
        pl.save()
        return pl

    class Meta:
        model = PackingList
        exclude = ['status', 'search_string']



class ShippingListForm(forms.ModelForm):
    sl_number = forms.CharField( max_length=20, required=True, label='SL Number',
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': "SL Number"}))
    sold_to = forms.ModelChoiceField(required=False, queryset=Contact.objects.all(), 
        widget=forms.Select(attrs={"class": "form-control"}))
    ship_to = forms.ModelChoiceField(required=False, queryset=Contact.objects.all(), 
        widget=forms.Select(attrs={"class": "form-control"}))

    ordered_date = forms.DateField(required=False,
        widget=forms.DateInput(attrs={"class": "form-control datepicker", 'placeholder': "Ordered Date"}))
    date_required = forms.DateField(required=False,
        widget=forms.DateInput(attrs={"class": "form-control datepicker", 'placeholder': "Date Required"}))

    job_number = forms.ModelChoiceField(required=False, queryset=Job.objects.all(), 
        widget=forms.Select(attrs={"class": "form-control"}))
    customer_po_number = forms.CharField( max_length=20, required=False,
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': "Customer PO Number"}))
    customer_job_number = forms.CharField( max_length=20, required=False,
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': "Customer Job Number"}))

    ship_via = forms.ModelChoiceField(required=False, queryset=DeliveryChoice.objects.filter(is_active=True), 
        widget=forms.Select(attrs={"class": "form-control"}))


    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        self.action = kwargs.pop('action', None)
        super(ShippingListForm, self).__init__(*args, **kwargs)

    class Meta:
        model = ShippingList
        exclude = ['search_string', 'sl_status']

    def save(self, commit=True):
        sl = super(ShippingListForm, self).save(commit=False)
        sv = SystemVariable.objects.get(id=1)
        if self.action == 'new':
            sl_number = re.sub(r"[A-Za-z]+","",self.request.POST['sl_number_search'])
            sl.sl_number = 'SL'+str(sl_number)
            sv.next_sl_number = int(sl_number) + 1
        elif self.action == 'update':
            pass
            # po_number = re.sub(r"[^\w]+","",po.po_number)
            # po.po_number = 'P'+str(po_number)
            # sv.next_po_number = int(po_number) + 1
        sv.save()
        sl.save()
        return sl




class DeliverInternalForm(forms.ModelForm):
    department = forms.CharField( max_length=50,
        widget=forms.TextInput(attrs={"class": "form-control", 'required': 'True', 'placeholder':"Department"}))
    description = forms.CharField( max_length=250, required=False,
        widget=forms.Textarea(attrs={"class": "form-control", 'rows':2, 'required': 'False', 'placeholder':"Department Description"}))
    
    class Meta:
        model = DeliverInternal 









