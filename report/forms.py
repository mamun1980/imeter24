from django import forms
from report.models import *
from report.choices import *
from report.lookups import ReportLookup
import selectable


class PrinterForm(forms.ModelForm):
	printer_id = forms.CharField( max_length=50,
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': "Printer id"}))
	network_que_location = forms.CharField( max_length=200,
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': "Printer Network Que Location"}))
	# printer_type = forms.ChoiceField(required=False, choices=PRINTER_TYPE,
 #        widget=forms.Select(attrs={"class": "form-control"}))
	printer_status = forms.ChoiceField(required=False, choices=PRINTER_STATUS,
        widget=forms.Select(attrs={"class": "form-control"}))
	

	class Meta:
		model = Printer
		exclude = ['printer_type',]
		

class PrinterEditForm(forms.ModelForm):
	network_que_location = forms.CharField(max_length=200, required=False,
        widget=forms.TextInput(attrs={"class": "form-control", "rows":2, 'placeholder':"printer location"}))
	
	printer_status = forms.ChoiceField(required=False, choices=PRINTER_STATUS,
        widget=forms.Select(attrs={"class": "form-control"}))
	
	
	class Meta:
		model = Printer
		exclude = ['printer_id', 'printer_type']
		


class ReportForm(forms.ModelForm):
	report_type = forms.CharField( max_length=100, required=False,
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder':"Report Type"}))
	
	comments = forms.CharField( max_length=200, required=False,
        widget=forms.Textarea(attrs={"class": "form-control", 'rows':2, 'required': 'False', 'placeholder':"Comments"}))
	python_script = forms.CharField( max_length=200, required=False,
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder':"Python script"}))
		

	class Meta:
		model = Report
		exclude = ['id',]
		fields = ['report_type', 'comments', 'python_script']

class RecuringReportForm(forms.ModelForm):
	report = forms.ModelChoiceField(required=False, queryset=Report.objects.all(),
        widget=forms.Select(attrs={"class": "form-control"}))
	report_description = forms.CharField( max_length=500, required=False,
        widget=forms.Textarea(attrs={"class": "form-control", 'rows':2, 'required': 'False', 'placeholder':"Report Description"}))
	script_name = forms.CharField( max_length=200, required=False,
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder':"Report Description"}))
	que_type = forms.ChoiceField( required=False, choices=QUE_TYPE,
        widget=forms.Select(attrs={"class": "form-control", 'placeholder':"Report Description"}))
	email = forms.CharField( max_length=500, required=False,
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder':"Report Description"}))
	printer = forms.ModelChoiceField(required=False, queryset=Printer.objects.all(),
        widget=forms.Select(attrs={"class": "form-control", 'placeholder':"Report Description"}))
	fax = forms.CharField( max_length=500, required=False,
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder':"Report Description"}))
	# current_job_status = forms.CharField( max_length=20, required=False,
 #        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder':"Report Description"}))
	# date_submitted = forms.DateField( required=False,
 #        widget=forms.DateInput(attrs={"class": "form-control", 'placeholder':"Report Description"}))
	# time_submitted = forms.CharField( required=False,
 #        widget=forms.TextInput(attrs={"class": "form-control",  'placeholder':"Report Description"}))
	# date_finished = forms.DateField( required=False,
 #        widget=forms.DateInput(attrs={"class": "form-control",  'placeholder':"Report Description"}))
	# time_finished = forms.CharField( required=False,
 #        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder':"Report Description"}))

	# unix_que = forms.CharField( max_length=100, required=False,
 #        widget=forms.TextInput(attrs={"class": "form-control", 
 #            'placeholder':"Range"}))
	comment = forms.CharField( max_length=500, required=False,
        widget=forms.Textarea(attrs={"class": "form-control", 'rows':2, 'required': 'False', 'placeholder':"Report Description"}))
	schedule_type = forms.ChoiceField(required=False, choices=SCHEDULE_TYPE,
        widget=forms.Select(attrs={"class": "form-control", 'placeholder':"Report Description", 
        	'ng-model':"schedule_type"}))
	week_day = forms.CharField( max_length=200, required=False,
        widget=forms.TimeInput(attrs={"class": "form-control", 'ng-model':"week_day", 'placeholder':"Report Description"}))
	randomdays = forms.CharField( max_length=500, required=False,
        widget=forms.TimeInput(attrs={"class": "form-control",'placeholder':"Report Description"}))
	daytime = forms.CharField( max_length=50, required=False,
        widget=forms.TimeInput(attrs={"class": "form-control", 'placeholder':"Report Description"}))

	# schedule_type = forms.ChoiceField(required=False, choices=SCHEDULE_TYPE,
 #        widget=forms.Select(attrs={"class": "form-control"}))
	# week_day = forms.CharField( max_length=25, required=False,
 #        widget=forms.TextInput(attrs={"class": "form-control", 
 #            'placeholder':"Range"}))
	

	class Meta:
		model = RecuringReport
		exclude = ['unix_que', 'time_finished', 'date_finished', 'time_submitted', 'date_submitted', 'current_job_status']

	def save(self, commit=True):
		rreport = super(RecuringReportForm, self).save(commit=False)
		rreport.search_string = rreport.report.report_type + " " + rreport.report_description + " " + rreport.que_type + " "
		id = rreport.save()
		
		return rreport



class SingleReportForm(forms.ModelForm):
	class Meta:
		model = SingleReport






