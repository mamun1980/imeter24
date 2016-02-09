from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView
from django.http import HttpResponse
from controllers.forms import *

class ControllerFormAction(TemplateView):
	template_name = 'controllers/controller-action.html'
	form_class = ControllerForm

	def get(self, request):
		return render(request, self.template_name, {})
		
class ControllerList(ListView)