from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DeleteView
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from controllers.forms import *
from haystack.query import SearchQuerySet, EmptySearchQuerySet
import json


class ControllerFormAction(TemplateView):
    template_name = 'controllers/controller-action.html'
    form_class = ControllerForm

    def get(self, request):
        return render(request, self.template_name, {})

    def post(self, request):
        controller_id = request.POST.get("controller_id")
        try:
            cont = Controller.objects.get(controller_id=controller_id)
            controller_form = ControllerForm(request.POST, instance=cont)
        except Exception, e:
            controller_form = ControllerForm(request.POST)
            

        if controller_form.is_valid():
            try:
                controller = controller_form.save()
                con_descriptions = request.POST.getlist("con_description")
                con_ids = request.POST.getlist("con_id")

                i = 0
                for con_id in con_ids:
                    con_c, created = ControllerContact.objects.get_or_create(controller=controller, contact_id=int(con_id))
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

                controller.save()

            except Exception, e:
                return HttpResponseRedirect("/controllers/add/")

            return HttpResponseRedirect("/controllers/list-json/")

        else:
            return HttpResponseRedirect("/controllers/list-json/")
    
class ControllerList(ListView):
    
    def get(self, request):
        query = request.GET.get('q','')
        if query:
            controllers = SearchQuerySet().using('controller').filter(content=query).load_all()[:20]
        else:
            controllers = SearchQuerySet().using('controller').load_all()[:20]

        controller_list = []

        if controllers:
            con_dict = {}
            for con in controllers:
                con_dict['controller_id'] = con.controller_id
                con_dict['controller_type'] = con.controller_type
                con_dict['sold_to'] = con.sold_to
                con_dict['location'] = con.location
                con_dict['controller_contacts'] = con.controller_contacts

                controller_list.append(con_dict)

        data = json.dumps({'results': controller_list})
        return HttpResponse(data, content_type='application/json')

@csrf_exempt
def contact_delete(request):
    # import pdb; pdb.set_trace();
    con_id = request.POST.get("id")
    try:
        con = ControllerContact.objects.get(id=con_id)
        controller = con.controller
        con.delete() 
        controller.save()
        return HttpResponse("true")
    except Exception, e:
        return HttpResponse("false")
    