from django import forms
from django.contrib.auth.models import Group


class GroupForm(forms.Form):
	name = forms.CharField( max_length=25, required=True,
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': "Group Name"}))
