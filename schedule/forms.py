from django import forms
from schedule.models import *
from schedule.choices import *
from schedule.lookups import JobLookup
import selectable
from premierelevator.models import SystemVariable
# from schedule.custom_field import MultiEmailField
from django.core.validators import validate_email
from datetime import datetime
import re

class JobForm(forms.ModelForm):
    job_number = forms.CharField( max_length=20,
        widget=forms.TextInput(attrs={"class": "form-control", "value": "NEW", "readonly": 'readonly'}))
    cab_designation = forms.CharField( max_length=50, required=False,
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder':"Cab Designation"}))
    date_opened = forms.DateField(required=False, widget=forms.DateInput(
        attrs={"class": "form-control datetimepicker", "ng-model":"date_opened", 'placeholder':"Opned Date"}))
    date_required = forms.DateField(required=False, widget=forms.DateInput(
        attrs={"class": "form-control datetimepicker", "ng-model":"date_required", 'placeholder':"Date Required"}))
    status = forms.ChoiceField(required=False, choices=STATUS_CHOICE,
        widget=forms.Select(attrs={"class": "form-control"}))
    job_name = forms.CharField(required=False, max_length=150,
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder':"Job Name"}))
    address_1 = forms.CharField( max_length=250, required=False,
        widget=forms.Textarea(attrs={"class": "form-control no-resize", 'rows':2, 'placeholder':"Address 1"}))
    customer = forms.CharField(required=False, max_length=100,
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder':"customer"}))
    customer_contact_name = forms.CharField(required=False, max_length=100,
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder':"customer contact name"}))
    customer_contact_phone_number = forms.CharField(required=False, max_length=100,
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder':"customer contact phone number"}))

    contact_email = forms.CharField(label="Contact Email", required=False,
      widget=forms.TextInput(attrs={"class": "form-control", 'placeholder':"Contact Email"}))
    number_of_cabs = forms.IntegerField(required=False, max_value=999,
        widget=forms.NumberInput(attrs={"class": "form-control", 'placeholder':"Number of Cabs"}))
    description = forms.CharField(required=False, max_length=200,
        widget=forms.Textarea(attrs={"class": "form-control no-resize", "rows":2, 'placeholder': "Description"}))
    po_number = forms.CharField( max_length=40, required=False,
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder':"Purchase order number"}))
    status_notes = forms.CharField(max_length=500, required=False,
        widget=forms.Textarea(attrs={"class": "form-control no-resize", "rows":2, 'placeholder': "Status Notes"}))
    drawing_req_date = forms.DateField(required=False, widget=forms.DateInput(
        attrs={"class": "form-control datetimepicker", "ng-model":"drawing_req_date", 'placeholder':"Drawing required date",
        "ng-class":"{ 'bg-danger' :jobform.drawing_req_date.$invalid }"}))
    drawing_sent_to_customer_date = forms.DateField(required=False, widget=forms.DateInput(
        attrs={"class": "form-control datetimepicker", "ng-model":"drawing_sent_to_customer_date", 'placeholder':"Drawing sent to customer date"}))
    drawing_approved_date = forms.DateField(required=False, widget=forms.DateInput(
        attrs={"class": "form-control datetimepicker", "ng-model":"drawing_approved_date", 'placeholder':"Drawing approved date"}))
    eng_comment = forms.CharField( max_length=250, required=False,
        widget=forms.Textarea(attrs={"class": "form-control no-resize", 'rows':2, 'placeholder':"Engineer Comments"}))
    
    class Meta:
        model = Job
        exclude = ['id', 'search_string']

    def clean_contact_email(self):

        import re
        contact_email = self.cleaned_data['contact_email']
        email_list = re.split("[, ]+", contact_email)
        emails = []
        for email in email_list:
            if email != '':
                email = email.strip()
                validate_email(email)
                emails.append(email)

        return ",".join(emails)


    def clean(self):
        cleaned_data = super(JobForm, self).clean()
        date_opened = cleaned_data.get('date_opened', '')
        drawing_req_date = cleaned_data.get('drawing_req_date','')

        if drawing_req_date != None:
            if date_opened == None:
                msg = "Date Oppend must be set before setting drawing_req_date"
                # self.add_error('date_opened', msg)
                raise forms.ValidationError("Date Oppend must be set before setting drawing_req_date")
        return self.cleaned_data


    def save(self, commit=True):
        # import pdb; pdb.set_trace()
        job = super(JobForm, self).save(commit=False)
        job.job_number = "J"+str(re.sub(r"[A-Za-z]","",job.job_number))
        # sv = SystemVariable.objects.get(id=1)
        # job.job_number = str(sv.next_job_number)
        # sv.next_job_number = int(job.job_number[1:]) + 1
        # sv.save()

        job.search_string = job.job_number + " " + job.cab_designation + " " + job.job_name + " " + job.customer + " " + job.status + " " + job.description+ " " + job.address_1 + " " + job.customer_contact_name + " " + job.customer_contact_phone_number
        id = job.save()
        
        try:
            job_status, create = JobStatus.objects.get_or_create(job=job)
            job_status.save()
        except Exception, e:
            raise e
        
        return job_status


class CommentForm(forms.ModelForm):
    job_comment = forms.CharField( max_length=500, required=False,
        widget=forms.Textarea(attrs={"class": "form-control", 'rows':2}))

    class Meta:
        model = Comment
        exclude = ['id',]

    def save(self, commit=True):
        comment = super(CommentForm, self).save(commit=False)
        # import pdb; pdb.set_trace();
        comment.datetime = datetime.now()
        comment.save()
        return comment



class CommentEditForm(forms.ModelForm):
    job_comment = forms.CharField( max_length=500, required=False,
        widget=forms.Textarea(attrs={"class": "form-control", 'rows':2}))

    class Meta:
        model = Comment
        exclude = ['id', 'comment_by', 'datetime', 'job_number']



class JobStatusForm(forms.ModelForm):
    fixtures_req_by = forms.CharField( max_length=20, required=False,
        widget=forms.DateInput(attrs={"name":"fixtures_req_by", "class": "form-control datetimepicker", 
            "ng-disabled":"formDisable", "ng-model":"statusform.fixtures_req_by", 'placeholder':"Fixture required by",
            "ng-class":"{ 'bg-danger' :jobStatusForm.fixtures_req_by.$invalid }"}))
    fixtures_is_done = forms.ChoiceField(required=False, choices=DONE_CHOICES,
        widget=forms.Select(attrs={"class": "form-control"}))
    fixtures_comment = forms.CharField( max_length=250, required=False,
        widget=forms.Textarea(attrs={"class": "form-control no-resize", 'rows':1, "ng-model":"statusform.fixtures_comment", "ng-disabled":"formDisable", 'placeholder':"Comments for fixture"}))

    wood_shop_req_by = forms.CharField( max_length=20, required=False,
        widget=forms.DateInput(attrs={"class": "form-control datetimepicker", "ng-disabled":"formDisable", "ng-model":"statusform.wood_shop_req_by", 'placeholder':"Wood Shop Requested By",
            "ng-class":"{ 'bg-danger' :jobStatusForm.wood_shop_req_by.$invalid}"}))
    wood_shop_is_done = forms.ChoiceField(required=False, choices=DONE_CHOICES,
        widget=forms.Select(attrs={"class": "form-control"}))
    wood_shop_req_by_comment = forms.CharField( max_length=250, required=False,
        widget=forms.Textarea(attrs={"class": "form-control no-resize", 'rows':1, "ng-model":"statusform.wood_shop_req_by_comment", "ng-disabled":"formDisable",  'placeholder':"Comments for wood shop"}))

    machine_shop_req_by = forms.CharField( max_length=20, required=False,
        widget=forms.DateInput(attrs={"class": "form-control datetimepicker", "ng-disabled":"formDisable", "ng-model":"statusform.machine_shop_req_by", 'placeholder':"Machine Shop Requested By",
            "ng-class":"{ 'bg-danger' :jobStatusForm.machine_shop_req_by.$invalid}"}))
    machine_shop_is_done = forms.ChoiceField(required=False, choices=DONE_CHOICES,
        widget=forms.Select(attrs={"class": "form-control"}))
    machine_shop_req_by_comment = forms.CharField( max_length=250, required=False,
        widget=forms.Textarea(attrs={"class": "form-control no-resize", 'rows':1,"ng-model":"statusform.machine_shop_req_by_comment", "ng-disabled":"formDisable", 'placeholder':"Comments for machine shop"}))

    welding = forms.CharField( max_length=20, required=False,
        widget=forms.DateInput(attrs={"class": "form-control datetimepicker", "ng-disabled":"formDisable", "ng-model":"statusform.welding", 'placeholder':"Welding", 
            "ng-class":"{ 'bg-danger' :jobStatusForm.welding.$invalid}"}))
    welding_is_done = forms.ChoiceField(required=False, choices=DONE_CHOICES,
        widget=forms.Select(attrs={"class": "form-control"}))
    welding_comment = forms.CharField( max_length=250, required=False,
        widget=forms.Textarea(attrs={"class": "form-control no-resize", 'rows':1,"ng-model":"statusform.welding_comment", "ng-disabled":"formDisable", 'placeholder':"Comments for welding"}))

    lacquer = forms.CharField( max_length=20, required=False,
        widget=forms.DateInput(attrs={"class": "form-control datetimepicker","ng-disabled":"formDisable", "ng-model":"statusform.lacquer", 'placeholder':"Lacquer",
            "ng-class":"{ 'bg-danger' :jobStatusForm.lacquer.$invalid}"}))
    lacquer_is_done = forms.ChoiceField(required=False, choices=DONE_CHOICES,
        widget=forms.Select(attrs={"class": "form-control"}))
    lacquer_comment = forms.CharField( max_length=250, required=False,
        widget=forms.Textarea(attrs={"class": "form-control no-resize", 'rows':1,"ng-model":"statusform.lacquer_comment", "ng-disabled":"formDisable", 'placeholder':"Comments for lacquer"}))

    trim_shop_req_by = forms.CharField( max_length=20, required=False,
        widget=forms.DateInput(attrs={"class": "form-control datetimepicker","ng-disabled":"formDisable", "ng-model":"statusform.trim_shop_req_by", 'placeholder':"Trim shop requested by",
            "ng-class":"{ 'bg-danger' :jobStatusForm.trim_shop_req_by.$invalid}"}))
    trim_shop_is_done = forms.ChoiceField(required=False, choices=DONE_CHOICES,
        widget=forms.Select(attrs={"class": "form-control"}))
    trim_shop_req_by_comment = forms.CharField( max_length=250, required=False,
        widget=forms.Textarea(attrs={"class": "form-control no-resize", 'rows':1, "ng-model":"statusform.trim_shop_req_by_comment", "ng-disabled":"formDisable", 'placeholder':"Comments for trim shop"}))

    cab_assemply_req_by = forms.CharField( max_length=20, required=False,
        widget=forms.DateInput(attrs={"class": "form-control datetimepicker","ng-disabled":"formDisable", "ng-model":"statusform.cab_assemply_req_by", 'placeholder':"Cab assemply requested by",
            "ng-class":"{ 'bg-danger' :jobStatusForm.cab_assemply_req_by.$invalid}"}))
    cab_assemply_is_done = forms.ChoiceField(required=False, choices=DONE_CHOICES,
        widget=forms.Select(attrs={"class": "form-control"}))
    cab_assemply_req_by_comment = forms.CharField( max_length=250, required=False,
        widget=forms.Textarea(attrs={"class": "form-control no-resize", 'rows':1, "ng-model":"statusform.cab_assemply_req_by_comment", "ng-disabled":"formDisable", 'placeholder':"Comments for cab assemply"}))

    install_date = forms.CharField( max_length=20, required=False,
        widget=forms.DateInput(attrs={"class": "form-control datetimepicker","ng-disabled":"formDisable", "ng-model":"statusform.install_date", 'placeholder':"Install date",
            "ng-class":"{ 'bg-danger' :jobStatusForm.install_date.$invalid}"}))
    install_is_done = forms.ChoiceField(required=False, choices=DONE_CHOICES,
        widget=forms.Select(attrs={"class": "form-control"}))
    install_date_comment = forms.CharField( max_length=250, required=False,
        widget=forms.Textarea(attrs={"class": "form-control no-resize", 'rows':1, "ng-model":"statusform.install_date_comment", "ng-disabled":"formDisable",'placeholder':"Comments for install date"}))

    premier_glass = forms.CharField( max_length=20, required=False,
        widget=forms.DateInput(attrs={"class": "form-control datetimepicker","ng-disabled":"formDisable", "ng-model":"statusform.premier_glass", 'placeholder':"Premier Glass",
            "ng-class":"{ 'bg-danger' :jobStatusForm.premier_glass.$invalid}"}))
    premier_glass_is_done = forms.ChoiceField(required=False, choices=DONE_CHOICES,
        widget=forms.Select(attrs={"class": "form-control"}))
    premier_glass_comment = forms.CharField( max_length=250, required=False,
        widget=forms.Textarea(attrs={"class": "form-control no-resize", 'rows':1, "ng-model":"statusform.premier_glass_comment", "ng-disabled":"formDisable", 'placeholder':"Comments for premier glass"}))

    tile_installer = forms.CharField( max_length=20, required=False,
        widget=forms.DateInput(attrs={"class": "form-control datetimepicker","ng-disabled":"formDisable", "ng-model":"statusform.tile_installer", 'placeholder':"Tile Installer",
            "ng-class":"{ 'bg-danger' :jobStatusForm.tile_installer.$invalid}"}))
    tile_installer_is_done = forms.ChoiceField(required=False, choices=DONE_CHOICES,
        widget=forms.Select(attrs={"class": "form-control"}))
    tile_installer_comment = forms.CharField( max_length=250, required=False,
        widget=forms.Textarea(attrs={"class": "form-control no-resize", 'rows':1, "ng-model":"statusform.tile_installer_comment", "ng-disabled":"formDisable",'placeholder':"Comments for tile installer"}))


    misc_del = forms.CharField( max_length=20, required=False,
        widget=forms.DateInput(attrs={"class": "form-control datetimepicker", "ng-disabled":"formDisable","ng-model":"statusform.misc_del", 'placeholder':"Misc del",
            "ng-class":"{ 'bg-danger' :jobStatusForm.misc_del.$invalid}"}))
    misc_del_is_done = forms.ChoiceField(required=False, choices=DONE_CHOICES,
        widget=forms.Select(attrs={"class": "form-control"}))
    misc_del_comment = forms.CharField( max_length=250, required=False,
        widget=forms.Textarea(attrs={"class": "form-control no-resize", 'rows':1,"ng-model":"statusform.misc_del_comment", "ng-disabled":"formDisable",'placeholder':"Comments for misc del"}))

    bill = forms.CharField( max_length=20, required=False,
        widget=forms.DateInput(attrs={"class": "form-control datetimepicker", "ng-disabled":"formDisable", "ng-model":"statusform.bill", 'placeholder':"Bill",
            "ng-class":"{ 'bg-danger' :jobStatusForm.bill.$invalid}"}))
    bill_is_done = forms.ChoiceField(required=False, choices=DONE_CHOICES,
        widget=forms.Select(attrs={"class": "form-control"}))
    bill_comment = forms.CharField( max_length=250, required=False,
        widget=forms.Textarea(attrs={"class": "form-control no-resize", 'rows':1, "ng-model":"statusform.bill_comment", "ng-disabled":"formDisable",'placeholder':"Comments for bill"}))

    hayward = forms.CharField( max_length=20, required=False,
        widget=forms.DateInput(attrs={"class": "form-control datetimepicker", "ng-disabled":"formDisable","ng-model":"statusform.hayward", 'placeholder':"Haywrd",
            "ng-class":"{ 'bg-danger' :jobStatusForm.hayward.$invalid}"}))
    hayward_is_done = forms.ChoiceField(required=False, choices=DONE_CHOICES,
        widget=forms.Select(attrs={"class": "form-control"}))
    hayward_comment = forms.CharField( max_length=250, required=False,
        widget=forms.Textarea(attrs={"class": "form-control no-resize", 'rows':1, "ng-model":"statusform.hayward_comment", "ng-disabled":"formDisable", 'placeholder':"Comments for hayward"}))

    glenn = forms.CharField( max_length=20, required=False,
        widget=forms.DateInput(attrs={"class": "form-control datetimepicker","ng-disabled":"formDisable", "ng-model":"statusform.glenn", 'placeholder':"Glenn",
            "ng-class":"{ 'bg-danger' :jobStatusForm.glenn.$invalid}"}))
    glenn_is_done = forms.ChoiceField(required=False, choices=DONE_CHOICES,
        widget=forms.Select(attrs={"class": "form-control"}))
    glenn_comment = forms.CharField( max_length=250, required=False,
        widget=forms.Textarea(attrs={"class": "form-control no-resize", 'rows':1, "ng-model":"statusform.glenn_comment", "ng-disabled":"formDisable",'placeholder':"Comments for glenn"}))

    suren = forms.CharField( max_length=20, required=False,
        widget=forms.DateInput(attrs={"class": "form-control datetimepicker","ng-disabled":"formDisable", "ng-model":"statusform.suren", 'placeholder':"Suren",
            "ng-class":"{ 'bg-danger' :jobStatusForm.suren.$invalid}"}))
    suren_is_done = forms.ChoiceField(required=False, choices=DONE_CHOICES,
        widget=forms.Select(attrs={"class": "form-control"}))
    suren_comment = forms.CharField( max_length=250, required=False,
        widget=forms.Textarea(attrs={"class": "form-control no-resize", 'rows':1, "ng-model":"statusform.suren_comment", "ng-disabled":"formDisable",'placeholder':"Comments for suren"}))

    roger = forms.CharField( max_length=20, required=False,
        widget=forms.DateInput(attrs={"class": "form-control datetimepicker","ng-disabled":"formDisable", "ng-model":"statusform.roger", 'placeholder':"Roger",
            "ng-class":"{ 'bg-danger' :jobStatusForm.roger.$invalid}"}))
    roger_is_done = forms.ChoiceField(required=False, choices=DONE_CHOICES,
        widget=forms.Select(attrs={"class": "form-control"}))
    roger_comment = forms.CharField( max_length=250, required=False,
        widget=forms.Textarea(attrs={"class": "form-control no-resize", 'rows':1, "ng-model":"statusform.roger_comment", "ng-disabled":"formDisable", 'placeholder':"Comments for roger"}))

    matt = forms.CharField( max_length=20, required=False,
        widget=forms.DateInput(attrs={"class": "form-control datetimepicker", "ng-disabled":"formDisable","ng-model":"statusform.matt", 'placeholder':"Matt",
            "ng-class":"{ 'bg-danger' :jobStatusForm.matt.$invalid}"}))
    matt_is_done = forms.ChoiceField(required=False, choices=DONE_CHOICES,
        widget=forms.Select(attrs={"class": "form-control"}))
    matt_comment = forms.CharField( max_length=250, required=False,
        widget=forms.Textarea(attrs={"class": "form-control no-resize", 'rows':1, "ng-model":"statusform.matt_comment", "ng-disabled":"formDisable", 'placeholder':"Comments for matt"}))

    third_party_install = forms.CharField( max_length=20, required=False,
        widget=forms.DateInput(attrs={"class": "form-control datetimepicker", "ng-disabled":"formDisable","ng-model":"statusform.third_party_install", 'placeholder':"3rd party Install",
            "ng-class":"{ 'bg-danger' :jobStatusForm.third_party_install.$invalid}"}))
    third_party_install_is_done = forms.ChoiceField(required=False, choices=DONE_CHOICES,
        widget=forms.Select(attrs={"class": "form-control"}))
    third_party_install_comment = forms.CharField( max_length=250, required=False,
        widget=forms.Textarea(attrs={"class": "form-control no-resize", 'rows':1, "ng-model":"statusform.third_party_install_comment", "ng-disabled":"formDisable",'placeholder':"Comments for 3rd party install"}))

    tssa_submitted_date = forms.CharField( max_length=20, required=False,
        widget=forms.DateInput(attrs={"class": "form-control datetimepicker", "ng-disabled":"formDisable","ng-model":"statusform.tssa_submitted_date", 'placeholder':"TSSA submitted date status",
            "ng-class":"{ 'bg-danger' :jobStatusForm.tssa_submitted_date.$invalid}"}))
    tssa_submitted_date_is_done = forms.ChoiceField(required=False, choices=DONE_CHOICES,
        widget=forms.Select(attrs={"class": "form-control"}))
    tssa_submitted_date_comment = forms.CharField( max_length=250, required=False,
        widget=forms.Textarea(attrs={"class": "form-control no-resize", 'rows':1, "ng-model":"statusform.tssa_submitted_date_comment", "ng-disabled":"formDisable",'placeholder':"Comments for TSSA "}))

    safety_test_schedule_date = forms.CharField( max_length=20, required=False,
        widget=forms.DateInput(attrs={"class": "form-control datetimepicker", "ng-disabled":"formDisable","ng-model":"statusform.safety_test_schedule_date", 'placeholder':"Safety tester shcedule",
            "ng-class":"{ 'bg-danger' :jobStatusForm.safety_test_schedule_date.$invalid}"}))
    who_will_test = forms.CharField( max_length=200, required=False,
        widget=forms.TimeInput(attrs={"class": "form-control", 'placeholder':"Name of the tester.", "ng-model":"statusform.who_will_test",  "ng-disabled":"formDisable"}))
    test_comment = forms.CharField( max_length=250, required=False,
        widget=forms.Textarea(attrs={"class": "form-control no-resize", 'rows':1, "ng-model":"statusform.safety_test_schedule_date_comment", "ng-disabled":"formDisable",'placeholder':"Tester comments "}))

    class Meta:
        model = JobStatus
        exclude = ['job', ]


class JobEditForm(JobForm):
    pass


# =========== Lookup forms

class JobLookupForm(forms.Form):
    autocomplete = forms.CharField(
          label='Type for auto suggession',
          widget=selectable.forms.AutoCompleteWidget(JobLookup, 
          attrs={"class": "form-control", 'placeholder': "Filter jobs by address, customer and description", 'name': 'job-autocomplete-filter'}),
          required=False,

      )

class JobControlForm(forms.ModelForm):
    class Meta:
        model = JobControl
        exclude = ['job_number',]

    def __init__(self, *args, **kwargs):
        # self.request = kwargs.pop('request', None)
        self.action = kwargs.pop('action', None)
        super(JobControlForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        job_control = super(JobControlForm, self).save(commit=False)
        if self.action == 'new':
            # import pdb; pdb.set_trace();
            sv = SystemVariable.objects.get(id=1)
            job_control.job_number = 'J'+str(sv.next_job_number)
            job_control.save()

            sv.next_job_number = int(sv.next_job_number) + 1
            sv.save()
        else:
            job_control.save()
        return job_control

class ElevetorTypeForm(forms.ModelForm):
    elevetor_type = forms.CharField( max_length=50, required=False,
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder':"Elevetor type"}))
    description = forms.CharField( max_length=200, required=False,
        widget=forms.Textarea(attrs={"class": "form-control", 'rows':2,'placeholder':"Description"}))
    class Meta:
        model = ElevetorType
        exclude = ['id', ]