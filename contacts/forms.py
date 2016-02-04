from django import forms
from contacts.models import *
from contacts.choices import *

class PaymentTermForm(forms.ModelForm):
    term = forms.CharField( max_length=25,
        widget=forms.TextInput(attrs={"class": "form-control", 'required': 'True', 'placeholder':"Pament Term"}))

    class Meta:
        model = PaymentTerm
        exclude = ['is_active',]

class DistributionMethodForm(forms.ModelForm):
    distribution_method = forms.CharField( max_length=100,
        widget=forms.TextInput(attrs={"class": "form-control", 'required': 'True', 
            'placeholder':"Distribution Method"}))

    class Meta:
        model = DistributionMethod
        exclude = ['is_active',]

class ContactContactTypeForm(forms.ModelForm):
    contact_type = forms.ModelChoiceField(required=False, queryset=ContactType.objects.filter(is_active=True),
        widget=forms.Select(attrs={"class": "form-control"}))
    description = forms.CharField(max_length=200, required=False,
        widget=forms.Textarea(attrs={"class": "form-control", "rows":2, 'placeholder':"Brif description"}))

    class Meta:
        model = ContactContactType
        exclude = ['contact',]


class ContactDistributionMethodForm(forms.ModelForm):
    distribution_method = forms.ModelChoiceField(required=False, queryset=DistributionMethod.objects.filter(is_active=True),
        widget=forms.Select(attrs={"class": "form-control"}))
    description = forms.CharField(max_length=200, required=False,
        widget=forms.Textarea(attrs={"class": "form-control", "rows":2, 'placeholder':"Brif description"}))

    class Meta:
        model = ContactDistributionMethod
        exclude = ['contact',]


class DeliveryChoiceForm(forms.ModelForm):
    delivery_choice = forms.CharField( max_length=100,
        widget=forms.TextInput(attrs={"class": "form-control", 'required': 'True', 'placeholder':"Delivery Choice"}))

    class Meta:
        model = DeliveryChoice
        exclude = ['is_active',]

class CurrencyForm(forms.ModelForm):
    currency = forms.CharField( max_length=15,
        widget=forms.TextInput(attrs={"class": "form-control", 'required': 'True', 
            'placeholder':"Currency"}))
    currency_icon = forms.ChoiceField(
        choices=currency_choices,
        required=True,
        label="Currency Icon",
        widget=forms.Select(attrs={"class": "form-control"}))

    class Meta:
        model = Currency

class EmailAddressTypeForm(forms.ModelForm):
    email_type = forms.CharField( max_length=25,
        widget=forms.TextInput(attrs={"class": "form-control", 'required': 'True', 'placeholder':"Email Address Type"}))

    class Meta:
        model = EmailAddressType
        exclude = ['is_active',]

class ContactTypeForm(forms.ModelForm):
    contact_type = forms.CharField( max_length=25,
        widget=forms.TextInput(attrs={"class": "form-control", 'required': 'True', 'placeholder':"Contact Type"}))

    class Meta:
        model = ContactType
        exclude = ['is_active',]

class ContactForm(forms.ModelForm):    
    contact_name = forms.CharField( max_length=64, required=False,
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder':"Contact Name", "autofocus":"autofocus"}))
    attention_to = forms.CharField( max_length=64, required=False,
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder':"Attention to"}))
    address_1 = forms.CharField(max_length=64, required=False,
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder':"Address 1"}))
    address_2 = forms.CharField(max_length=64, required=False,
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder':"Address 2"}))
    city = forms.CharField(max_length=64, required=False,
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder':"City"}))
    province = forms.CharField(max_length=64, required=False, initial="Ontario",
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder':"Province"}))
    country = forms.CharField(max_length=40, required=False, initial="Canada",
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder':"Country"}))
    postal_code = forms.CharField(max_length=15, required=False,
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder':"Postal Code"}))
    webpage = forms.URLField(max_length=200, required=False,
        widget=forms.URLInput(attrs={"class": "form-control", 'placeholder':"Webpage URL"}))


    class Meta:
        model = Contact
        exclude = ("search_string",)

    def save(self, commit=True):
        
        contact = super(ContactForm, self).save(commit=False)
        try:
            contact.save()    
            return contact
        except Exception, e:
            raise e
        
        

class ContactProfileForm(forms.ModelForm):
    gst_number = forms.CharField(max_length=17, required=False,
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder':"gst number"}))
    hst_number = forms.CharField(max_length=17, required=False,
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder':"hst number"}))
    pst_number = forms.CharField(max_length=11, required=False,
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder':"pst number"}))
    gst_tax_exempt = forms.BooleanField(required=False,
        widget=forms.CheckboxInput())
    hst_tax_exempt = forms.BooleanField(required=False,
        widget=forms.CheckboxInput())
    pst_tax_exempt = forms.BooleanField(required=False,
        widget=forms.CheckboxInput())
    foreign_account = forms.CharField(max_length=30, required=False,
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder':"foreign account"}))
    shipping_method = forms.ModelChoiceField(required=False, 
        queryset=DeliveryChoice.objects.filter(is_active=True),
        widget=forms.Select(attrs={"class": "form-control", 'placeholder':"delivery choice"}))
    ship_collect = forms.BooleanField(required=False,
        widget=forms.CheckboxInput())
    currency = forms.ModelChoiceField(required=False, queryset=Currency.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}))
    terms = forms.ModelChoiceField(required=False,
        queryset=PaymentTerm.objects.filter(is_active=True),
        widget=forms.Select(attrs={"class": "form-control", 'placeholder':"Terms"}))
    fob = forms.CharField(max_length=50, required=False, initial="Oshawa, Ontario, Canada",
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder':"FOB"}))
    ap_contact = forms.CharField(max_length=200, required=False,
        widget=forms.Textarea(attrs={"class": "form-control", "rows":5, 'placeholder':"ap contact"}))
    bv_ap_account = forms.CharField(max_length=50, required=False,
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder':"BV A/P Account"}))
    bv_ar_account = forms.CharField(max_length=50, required=False,
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder':"BV A/R Account"}))

    class Meta:
        model = ContactProfile
        exclude = ['contact', 'mail_list', 'record_created', 'last_activity']


class ContactEmailAddressForm(forms.ModelForm):
    email_address_type = forms.ModelChoiceField(required=True,  label="Email Type",
        queryset=EmailAddressType.objects.all(),        
        widget=forms.Select(attrs={"class": "form-control"}))
    email_address = forms.CharField(max_length=100, required=True, label="Email Address",
        widget=forms.EmailInput(attrs={"class": "form-control", 'placeholder': 'email address'}))

    class Meta:
        model = ContactEmailAddress
        exclude = ['contact', ]



class ContactPhoneForm2(forms.ModelForm):
  contact_profile = forms.ModelChoiceField(queryset=ContactProfile.objects.all(),
    required=True,
    label="Contact",
    widget=forms.Select(attrs={"class": "form-control"}))
  phone_type = forms.ChoiceField(
    choices=phone_type_choices,
    required=False,
    label="Type",
    widget=forms.Select(attrs={"class": "form-control"}))
  phone = forms.CharField(
    max_length=13,
    required=False,
    label="Phone Number",
    widget=forms.NumberInput(attrs={"class": "form-control", 'placeholder': 'phone number'}))
  phone_ext = forms.CharField(
    max_length=3,
    required=False,
    label="Phone Ext.",
    widget=forms.NumberInput(attrs={"class": "form-control", 'placeholder': 'phone ext'}))

  class Meta:
    model = ContactPhone

class ContactPhoneForm(forms.ModelForm):
  phone_type = forms.ModelChoiceField(required=False, queryset=PhoneType.objects.all(),
    widget=forms.Select(attrs={"class": "form-control"}))
  phone = forms.CharField(
    max_length=13,
    required=False,
    label="Phone Number",
    widget=forms.NumberInput(attrs={"class": "form-control", 'placeholder': 'phone number'}))
  phone_ext = forms.CharField(
    max_length=3,
    required=False,
    label="Phone Ext.",
    widget=forms.NumberInput(attrs={"class": "form-control", 'placeholder': 'phone ext'}))
  class Meta:
    model= ContactPhone
    exclude = ['contact', ]


# class ContactPhoneForm(forms.ModelForm):
#     phone_type = forms.ChoiceField(
#         choices=phone_type_choices,
#         required=False,
#         label="Type",
#         widget=forms.Select(attrs={"class": "form-control"}))
#     phone = forms.CharField(
#         max_length=13,
#         required=False,
#         label="Phone Number",
#         widget=forms.NumberInput(attrs={"class": "form-control", 'placeholder': 'phone number'}))
#     phone_ext = forms.CharField(
#         max_length=3,
#         required=False,
#         label="Phone Ext.",
#         widget=forms.NumberInput(attrs={"class": "form-control", 'placeholder': 'phone ext'}))
#     class Meta:
#         model= ContactPhone
#         exclude = ['contact',]


class UserForm(forms.ModelForm):
    username = forms.CharField(
        max_length=25, 
        required=False, 
        label="User Name",
        widget=forms.TextInput(attrs={"class": "form-control"}))
    email = forms.CharField(
        max_length=50,
        required=True,
        label="Eamil",
        widget=forms.EmailInput(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = ['username', 'email']

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.save()
        return user


class PhoneTypeForm(forms.ModelForm):
    phone_type = forms.CharField( max_length=15,
        widget=forms.TextInput(attrs={"class": "form-control", 'required': 'True', 
            'placeholder':"Phone Type"}))

    class Meta:
        model = PhoneType


class CommentForm(forms.ModelForm):
    comment = forms.CharField(max_length=200, required=False,
        widget=forms.Textarea(attrs={"class": "form-control", "rows":3, 'placeholder':"put your comments here."}))

    class Meta:
        model = Comment
        exclude = ['contact', 'comment_date', 'staff']
