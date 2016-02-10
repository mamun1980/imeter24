from django import forms
from controllers.models import *


class ControllerForm(forms.ModelForm):
	
    class Meta:
        model = Controller