from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView
from django.http import HttpResponse, HttpResponseRedirect
from controllers.forms import *

class ControllerFormAction(TemplateView):
	template_name = 'controllers/controller-action.html'
	form_class = ControllerForm

	def get(self, request):
		return render(request, self.template_name, {})

	def post(self, request):
		controller_form = ControllerForm(request.POST)
		if controller_form.is_valid():
			try:
				controller = controller_form.save()
				con_descriptions = request.POST.getlist("con_description")
				con_ids = request.POST.getlist("con_id")

				i = 0
				for con_id in con_ids:
					con_c = ControllerContact.objects.create(controller=controller)
					con_c.contact_id = int(con_id)
					con_c.description = con_descriptions[i]
					try:
						i = i+1
						con_status = request.POST.get("controler_status_"+str(i))
						if not con_status:
							con_c.status = 'off'
						else:
							con_c.status = con_status
					except Exception, e:
						pass
					con_c.save()

			except Exception, e:
				return HttpResponseRedirect("/controllers/add/")

			return HttpResponseRedirect("/controllers/list/")

		else:
			return HttpResponseRedirect("/controllers/list/")

			
		
class ControllerList(ListView):
	
	def get(self, request):
		return HttpResponse("Controller List")