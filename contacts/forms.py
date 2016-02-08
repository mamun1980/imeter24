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

    class Meta:
        model = Contact


class ContactEmailAddressForm(forms.ModelForm):
    email_address_type = forms.ModelChoiceField(required=True,  label="Email Type",
        queryset=EmailAddressType.objects.all(),        
        widget=forms.Select(attrs={"class": "form-control"}))
    email_address = forms.CharField(max_length=100, required=True, label="Email Address",
        widget=forms.EmailInput(attrs={"class": "form-control", 'placeholder': 'email address'}))

    class Meta:
        model = ContactEmailAddress
        exclude = ['contact', ]



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
