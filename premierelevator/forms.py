from django import forms
from django.contrib.auth.models import Group
from premierelevator.models import SystemVariable
from schedule.models import Job, JobControl
from inventory.models import Item
from purchase.models import *
from django.core.exceptions import ValidationError

class GroupForm(forms.Form):
	name = forms.CharField( max_length=25, required=True,
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': "Group Name"}))


class SystemVariableForm(forms.ModelForm):

	def save(self, commit=False):
		# import pdb; pdb.set_trace()
		sv = super(SystemVariableForm, self).save(commit=False)
		check = True
		while check:
			try:
				job = Job.objects.get(job_number=sv.next_job_number)
				sv.next_job_number = sv.next_job_number + 1
			except Job.DoesNotExist:
				check = False
				pass
		check = True
		while check:
			try:
				job = JobControl.objects.get(job_number=sv.next_job_control_number)
				sv.next_job_control_number = sv.next_job_control_number + 1
			except JobControl.DoesNotExist:
				check = False
				pass
		check = True
		while check:
			try:
				item = Item.objects.get(item_number=sv.next_item_number)
				sv.next_item_number = sv.next_item_number + 1
			except Item.DoesNotExist:
				check = False
				pass
		check = True
		while check:
			try:
				po_number = 'P'+str(sv.next_po_number)
				po = PurchaseOrder.objects.get(po_number=po_number)
				sv.next_po_number = sv.next_po_number + 1
			except PurchaseOrder.DoesNotExist:
				check = False
				pass
		check = True
		while check:
			try:
				sl_number = 'SL'+str(sv.next_sl_number)
				sl = ShippingList.objects.get(sl_number=sl_number)
				sv.next_sl_number = sv.next_sl_number + 1
			except ShippingList.DoesNotExist:
				check = False
				pass
		check = True
		while check:
			try:
				pl_number = 'PL'+str(sv.next_pl_number)
				pl = PackingList.objects.get(pl_number=pl_number)
				sv.next_pl_number = sv.next_pl_number + 1
			except PackingList.DoesNotExist:
				check = False
				pass			

		sv.save()
		return sv

	def clean_next_job_number(self):
		next_job_number = self.cleaned_data['next_job_number']
		try:
			job = Job.objects.get(job_number=next_job_number)
			raise ValidationError('Job number already exist ...')
		except Job.DoesNotExist:
			return next_job_number

	def clean_next_job_control_number(self):
		next_job_control_number = self.cleaned_data['next_job_control_number']
		try:
			job = JobControl.objects.get(job_number=next_job_control_number)
			raise ValidationError('Job number already exist ...')
		except JobControl.DoesNotExist:
			return next_job_control_number

	def clean_next_item_number(self):
		next_item_number = self.cleaned_data['next_item_number']
		try:
			item = Item.objects.get(item_number=next_item_number)
			raise ValidationError('Item number already exist ...')
		except Item.DoesNotExist:
			return next_item_number

	def clean_next_po_number(self):
		next_po_number = self.cleaned_data['next_po_number']
		try:
			po_number = 'P'+str(next_po_number)
			po = PurchaseOrder.objects.get(po_number=po_number)
			raise ValidationError('PO number already exist ...')
		except PurchaseOrder.DoesNotExist:
			return next_po_number

	def clean_next_sl_number(self):
		next_sl_number = self.cleaned_data['next_sl_number']
		try:
			sl_number = 'SL'+str(next_sl_number)
			sl = ShippingList.objects.get(sl_number=sl_number)
			raise ValidationError('SL number already exist ...')
		except ShippingList.DoesNotExist:
			return next_sl_number

	def clean_next_pl_number(self):
		next_pl_number = self.cleaned_data['next_pl_number']
		try:
			pl_number = 'PL'+str(next_pl_number)
			pl = PackingList.objects.get(pl_number=pl_number)
			raise ValidationError('PL number already exist ...')
		except PackingList.DoesNotExist:
			return next_pl_number

	def clean_next_invoice_number(self):
		next_invoice_number = self.cleaned_data['next_invoice_number']
		return next_invoice_number
		
	class Meta:
		model = SystemVariable
