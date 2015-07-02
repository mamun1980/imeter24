from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from scomuser.models import *
from scomuser.lookups import UserLookup
import selectable
from report.models import Printer


class ChangePasswordForm(forms.Form):
    current_password = forms.CharField( max_length=25, required=True, label="Current Password", 
        widget=forms.PasswordInput(render_value=True, attrs={"class": "form-control", 'placeholder':"Current Password"}))
    new_password = forms.CharField( max_length=25, required=True, label="New Password", 
        widget=forms.PasswordInput(render_value=True, attrs={"class": "form-control", 'placeholder':"New Password"}))
    confirm_password = forms.CharField( max_length=25, required=True, label="Confirm Password", 
        widget=forms.PasswordInput(render_value=True, attrs={"class": "form-control", 'placeholder':"Confirm Password"}))

    def clean(self):
        cleaned_data = super(ChangePasswordForm, self).clean()
        pass1 = cleaned_data.get("new_password")
        pass2 = cleaned_data.get("confirm_password")
        if pass1 != pass2:
            raise forms.ValidationError("Password must match.")

class ScomUserLoginForm(forms.Form):
    username = forms.CharField(max_length=50, 
           required=True, 
           label="Email address",
           widget=forms.TextInput(attrs={'autofocus': 'autofocus', "class": "form-control", 'placeholder':"Enter user id"}))
    
    password = forms.CharField(max_length=25,
           required=True,
           label="Password",
           widget=forms.PasswordInput(render_value=True, attrs={"class": "form-control", 'placeholder':"Password"}))


class ScomUserAddForm(UserCreationForm):
    username = forms.CharField( max_length=25, required=True, label="User Name",
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder':"User Name"}))
    first_name = forms.CharField(   max_length=25, required=True, label="First Name",
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder':"First Name"}))
    last_name = forms.CharField( max_length=25, required=True, label="Last Name",
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder':"Last Name"}))
    email = forms.EmailField( label="Email Address", initial="@premierelevator.com",
      widget=forms.EmailInput(attrs={"class": "form-control", 'placeholder':"youemailid@premierelevator.com"}))
    password1 = forms.CharField( max_length=25, required=True, label="Password", 
        widget=forms.PasswordInput(render_value=True, attrs={"class": "form-control", 'placeholder':"Password"}))
    
    password2 = forms.CharField( max_length=25, required=True, label="Confirm Password", 
        widget=forms.PasswordInput(attrs={"class": "form-control", 'placeholder':"Confirm Password"}))
    is_active = forms.BooleanField(widget=forms.CheckboxInput(), required=False)
    is_staff = forms.BooleanField(widget=forms.CheckboxInput(), required=False)
    is_superuser = forms.BooleanField(widget=forms.CheckboxInput(), required=False)
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser')
        
    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.set_password(self.cleaned_data['password1'])
        active = self.cleaned_data['is_active']
        is_staff = self.cleaned_data['is_staff']
        is_superuser = self.cleaned_data['is_superuser']
        if active:
            user.is_active = True
        if is_staff:
            user.is_staff = True
        if is_superuser:
          user.is_superuser = True

        if commit:
            user.save()

        return user


class ScomUserEditForm(forms.ModelForm):
    username = forms.CharField( max_length=25, required=True, label="User Name",
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder':"User Name"}))
    first_name = forms.CharField( max_length=25, required=True, label="First Name",
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder':"First Name"}))
    last_name = forms.CharField(  max_length=25, required=True, label="Last Name",
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder':"Last Name"}))
    email = forms.EmailField( label="Email Address",
      widget=forms.EmailInput(attrs={"class": "form-control", 'placeholder':"Email Address"}))
    is_active = forms.BooleanField(widget=forms.CheckboxInput(), required=False)
    is_staff = forms.BooleanField(widget=forms.CheckboxInput(), required=False)
    is_superuser = forms.BooleanField(widget=forms.CheckboxInput(), required=False)
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'is_active', 'is_staff', 'is_superuser')
        exclude = ['password2', 'password1']


class ScomUserProfileForm(forms.ModelForm):
    address_1 = forms.CharField( max_length=25, required=False, label="Address 1",
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder':"Address 1"}))
    address_2 = forms.CharField( max_length=25, required=False, label="Address 2",
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder':"Address 2"}))
    address_3 = forms.CharField( max_length=25, required=False, label="Address 3",
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder':"Address 3"}))
    city = forms.CharField( max_length=25, required=False, label="City",
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder':"City"}))
    province = forms.CharField( max_length=25, required=False, label="Province",
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder':"Province"}))
    postal = forms.CharField( max_length=25, required=False, label="Postal Code",
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder':"Postal Code"}))
    home_phone = forms.CharField( max_length=25, required=False, label="Home Phone",
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder':"Home Phone"}))
    cell_phone = forms.CharField( max_length=25, required=False, label="Cell Phone",
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder':"Cell Phone"}))
    other_phone = forms.CharField( max_length=25, required=False, label="Other Phone",
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder':"Other Phone"}))
    internal_extension = forms.CharField( max_length=5, required=False, label="Internal Extension",
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder':"Internal Extension"}))
    em_contact_1 = forms.CharField( max_length=25, required=False, label="Emergency Contact 1",
        widget=forms.Textarea(attrs={"class": "form-control", "rows":2, 'placeholder':"Emergency Contact 1"}))
    em_contact_2 = forms.CharField( max_length=250, required=False, label="Emergency Contact 2",
        widget=forms.Textarea(attrs={"class": "form-control", "rows":2, 'placeholder':"Emergency Contact 2"}))
    max_amount_allowed_to_purchase = forms.CharField( max_length=20, required=False,
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder':""}))
    max_purchase_per_po = forms.CharField( max_length=20, required=False,
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder':""}))
    
    class Meta:
        model = ScomUserProfile
        exclude = ['user', "search_string"]

    def save(self, commit=True):
        scuser = super(ScomUserProfileForm, self).save(commit=False)
        scuser.search_string = scuser.user.email + " " + scuser.user.last_name + " " + scuser.user.first_name + " " + scuser.user.username + " " + scuser.address_1 + " " + scuser.city + " " + scuser.province + " " + scuser.cell_phone
        uid = scuser.save()
        
        return scuser


class PayTypeForm(forms.ModelForm):
    pay_type = forms.CharField( max_length=20,
          widget=forms.TextInput(attrs={"class": "form-control", 'required': 'True', 'placeholder':"Pay Type"}))
    class Meta:
      model = PayType
      exclude = ['is_active',]

class PayrollForm(forms.ModelForm):
    sin = forms.CharField( max_length=25, required=False, label="Employee sin",
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder':"Employee sin"}))
    inital = forms.CharField( max_length=25, required=False, label="Initial",
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder':"Initial(max 3 character)"}))
    department = forms.ModelChoiceField( queryset=Department.objects.all(), required=False, label="Department",
        widget=forms.Select(attrs={"class": "form-control", 'placeholder':"Department"}))
    rate_of_pay = forms.CharField( max_length=25, required=False, label="Rate of Pay",
        widget=forms.NumberInput(attrs={"class": "form-control", 'placeholder':"Rate of Pay"}))
    rate_of_pay_type = forms.ModelChoiceField( queryset=PayType.objects.filter(is_active=True), required=False, label="Pay Type",
        widget=forms.Select(attrs={"class": "form-control", 'placeholder':"Pay Type"}))

    class Meta:
        model = Payroll
        exclude = ['user', ]

class DepartmentForm(forms.ModelForm):
    name = forms.CharField( max_length=25, required=True, label="Name",
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder':"Name"}))

    class Meta:
        model = Department
        exclude = ['is_active', ]


class UserLookupForm(forms.Form):
    autocomplete = forms.CharField( label='Type for auto suggession', widget=selectable.forms.AutoCompleteWidget(UserLookup, 
      attrs={"class": "form-control", 'placeholder': "Find User", 'name': 'userlookup-autocomplete'}),
      required=False, )

class MassMailForm(forms.ModelForm):
    email_id = forms.CharField( max_length=20, required=False, label="Email Token",
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder':"Email Token"}))
    subject = forms.CharField( max_length=200, required=False, label="Subject",
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder':"Subject"}))
    body = forms.CharField( max_length=500, required=True, label="Email Body",
        widget=forms.Textarea(attrs={"class": "form-control", "rows":3, 'placeholder':"Email Body"}))

    class Meta:
        model = MassMail
        exclude = ['id', 'to_all_users', 'mail_status', 'reciever', 'request_datetime', 'delivered_datetime', 'sender', 'search_string']



class UserReportForm(forms.ModelForm):
    report_type = forms.ChoiceField(required=True,  label="Report Type",
        choices=(('email', 'Email'), ('fax', 'Fax'), ('print', 'Print'), ('pdf', 'PDF')),        
        widget=forms.Select(attrs={"class": "form-control"}))
    report_printer = forms.ModelChoiceField( required=True, label="Report Printer", queryset=Printer.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}))
    report_fax = forms.CharField(max_length=50, required=True, label="Report Fax",
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Fax Number'}))
    report_email = forms.CharField(max_length=100, required=True, label="Report Email",
        widget=forms.EmailInput(attrs={"class": "form-control", 'placeholder': 'email address'}))


    class Meta:
        model = UserReport
        exclude = ['user', ]








    