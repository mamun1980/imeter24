from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.contrib import messages
from django.core import serializers
# Create your views here.
from contacts.forms import *
from contacts.models import *
import json


from haystack.forms import ModelSearchForm, SearchForm
from haystack.query import SearchQuerySet, EmptySearchQuerySet
from haystack.views import SearchView
from haystack.inputs import Raw, Clean, AutoQuery
import re

from django.core.paginator import Paginator, EmptyPage, InvalidPage


def remove_qout(request):
    contacts = Contact.objects.all()
    for contact in contacts:
        contact.contact_name = re.sub('\"', '', contact.contact_name)
        contact.attention_to = re.sub('\"', '', contact.attention_to)
        contact.address_1 = re.sub('\"', '', contact.address_1)
        contact.address_2 = re.sub('\"', '', contact.address_2)
        contact.city = re.sub('\"', '', contact.city)
        contact.province = re.sub('\"', '', contact.province)
        contact.country = re.sub('\"', '', contact.country)
        contact.postal_code = re.sub('\"', '', contact.postal_code)
        contact.save()
    return HttpResponse('Hello')


def contact_test(request):
    return render_to_response("contacts/contact-test.html", {},
        context_instance=RequestContext(request))


def autocomplete(request):
    query = request.GET.get('q', '')
    suggestions = []
    if len(query) > 1:
        sqs = SearchQuerySet().using('default').filter(content=query)[:10]
        suggestions = []
        for con in sqs:
            contact_dict = {}
            contact_dict['id'] = con.pk
            contact_dict['contact_name'] = con.contact_name
            contact_dict['address_1'] = con.address_1
            contact_dict['attention_to'] = con.attention_to
            contact_dict['city'] = con.city
            contact_dict['province'] = con.province
            contact_dict['country'] = con.country
            contact_dict['postal_code'] = con.postal_code
            contact_dict['phones'] = con.phones
            contact_dict['emails'] = con.emails
            contact_dict['hst_tax_exempt'] = con.hst_tax_exempt
            contact_dict['hst_number'] = con.hst_number
            contact_dict['pst_tax_exempt'] = con.pst_tax_exempt
            contact_dict['pst_number'] = con.pst_number
            # contact_dict['search_string'] = con.search_string
            suggestions.append(contact_dict)

    # Make sure you return a JSON object, not a bare list.
    # Otherwise, you could be vulnerable to an XSS attack.
    the_data = json.dumps({
        'results': suggestions
    })
    return HttpResponse(the_data, content_type='application/json')

def search_contact(request):
    # import pdb; pdb.set_trace();
    query = request.GET.get('q','')
    if request.GET.get('q'):
        contacts = SearchQuerySet().using('default').filter(content=AutoQuery(query)).load_all()[:30]
    else:
        contacts = SearchQuerySet().using('default').all().load_all()[:30]

    contact_list = []
    if contacts:
        for con in contacts:
            if con != None:
                contact_dict = {}
                contact_dict['id'] = con.pk
                contact_dict['contact_name'] = con.contact_name
                contact_dict['address_1'] = con.address_1
                contact_dict['attention_to'] = con.attention_to
                contact_dict['city'] = con.city
                contact_dict['province'] = con.province
                contact_dict['country'] = con.country
                contact_dict['postal_code'] = con.postal_code
                # contact_dict['search_string'] = con.search_string
                contact_dict['phones'] = con.phones
                contact_dict['emails'] = con.emails

                contact_list.append(contact_dict)
    try:
        page = int(request.GET.get('page','1'))
    except ValueError:
        page = 1
    paginator = Paginator(contact_list, 20)
    try:
        pages = paginator.page(page)
    except (EmptyPage, InvalidPage):
        pages = paginator.page(paginator.num_pages)

    results = pages.object_list

    data = json.dumps(results)
    return HttpResponse(data)



def sc_contact_home(request):
    
    return render_to_response("contacts/contact-home.html", 
        {'page_title': 'Contact List'},
        context_instance=RequestContext(request))

def contact_list(request):
    # import pdb; pdb.set_trace();
    user = request.user
    
    contacts = Contact.objects.all() 
    #.values('id','contact_name', 'address_1', 'attention_to', 'city', 'province', 'country', 'postal_code', 'search_string')
    contact_dict_list = []
    for con in contacts:
        contact_dict = {}
        contact_dict['id'] = con.id
        contact_dict['contact_name'] = con.contact_name
        contact_dict['address_1'] = con.address_1
        contact_dict['attention_to'] = con.attention_to
        contact_dict['city'] = con.city
        contact_dict['province'] = con.province
        contact_dict['country'] = con.country
        contact_dict['postal_code'] = con.postal_code
        contact_dict['search_string'] = con.search_string
        try:
            contactprofile, created = ContactProfile.objects.get_or_create(contact=con)
        except Exception, e:
            raise e
        
        if contactprofile.fob:
            contact_dict['fob'] = contactprofile.fob
        if contactprofile.terms:
            contact_dict['terms'] = contactprofile.terms.term
            contact_dict['term_id'] = contactprofile.terms.id
        if contactprofile.shipping_method:
            contact_dict['shipvia'] = contactprofile.shipping_method.delivery_choice
            contact_dict['shipvia_id'] = contactprofile.shipping_method.id

        contact_dict['permission'] = {}
        contact_dict['permission']['can_add_contact'] = user.has_perm("contacts.add_contact")
        contact_dict['permission']['can_view_contact'] = user.has_perm("contacts.view_contact")
        contact_dict['permission']['can_change_contact'] = user.has_perm("contacts.change_contact")
        contact_dict['permission']['can_delete_contact'] = user.has_perm("contacts.delete_contact")
        cid = int(con.id)
        contact_dict['phones'] = []
        cphones = ContactPhone.objects.filter(contact=con)
        for cphone in cphones:
            phone = {}
            phone['type'] = cphone.phone_type.phone_type
            phone['number'] = cphone.phone
            phone['phone_ext'] = cphone.phone_ext
            contact_dict['phones'].append(phone)

        contact_dict['emails'] = []
        cemails = ContactEmailAddress.objects.filter(contact=con)

        for cemail in cemails:
            email = {}
            email['email_address_type'] = cemail.email_address_type.email_type
            email['email_address'] = cemail.email_address
            contact_dict['emails'].append(email)

        contact_dict_list.append(contact_dict)
    json_posts = json.dumps(contact_dict_list)
    return HttpResponse(json_posts, mimetype='application/json')

@login_required
@permission_required("contacts.view_contact")
def sc_contact_view(request, cid):
    contact = Contact.objects.get(id=cid)
    contact_profile, cp_created = ContactProfile.objects.get_or_create(contact=contact)
    contact_phones = ContactPhone.objects.filter(contact=contact)
    contact_emails = ContactEmailAddress.objects.filter(contact=contact)
    distribution_methods = ContactDistributionMethod.objects.filter(contact=contact)
    comments = Comment.objects.filter(contact=contact)
    page_title = 'Contact Details of ('+ contact.contact_name +')'
    return render_to_response("contacts/contact-details.html", 
        {'contact': contact, 'contact_profile': contact_profile, 'contact_phones': contact_phones, 'page_title': page_title,
        'contact_emails': contact_emails, 'comments': comments, 'distribution_methods': distribution_methods}, 
        context_instance=RequestContext(request))

@login_required
@permission_required('contacts.add_contact')
@csrf_exempt
def sc_contact_add(request):
    if request.method == "POST":
        CForm = ContactForm(request.POST)
        if CForm.is_valid():
            try:
                contact = CForm.save()
                messages.info(request, "Contact added successfully.")
                return HttpResponseRedirect("/contacts/edit/%d/" % contact.id)
            except Exception, e:
                messages.error(request, "An error occured. Please check log.")
                return render_to_response("contacts/add-contact.html", {'cform': CForm, 'page_title': 'Add Contact'},
        context_instance=RequestContext(request))
        else:
            CPForm = ContactProfileFrom(request.POST)

    else:
        CForm = ContactForm()

    return render_to_response("contacts/add-contact.html", {'cform': CForm, 'page_title': 'Add Contact'},
        context_instance=RequestContext(request))

@login_required
@csrf_exempt
@permission_required("contacts.add_contact")
def sc_contact_add_rel(request):
    if request.method == "POST":
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            cid = contact_form.save()
            # return HttpResponseRedirect("/contacts/edit/%d/" % cid)
            return HttpResponse(cid.id)
        else:
            return HttpResponse("error")
    else:
        contact_form = ContactForm()
        return render(request, "contacts/add-contact-rel.html", {'contact_form': contact_form})

@login_required
@csrf_exempt
@permission_required("contacts.add_contact")
def sc_contact_add_rel_item(request):
    if request.method == "POST":
        contact_form = ContactForm(request.POST)
        contact_phone_form = ContactPhoneForm(request.POST)
        contact_email_form = ContactEmailAddressForm(request.POST)
        if contact_form.is_valid():
            cid = contact_form.save()
            if contact_phone_form.is_valid():
                cpf = contact_phone_form.save()
                cpf.contact = cid
                cpf.save()
            if contact_email_form.is_valid():
                cef = contact_email_form.save()
                cef.contact = cid
                cef.save()

            # return HttpResponseRedirect("/contacts/edit/%d/" % cid)
            return HttpResponse(cid.id)
        else:
            return HttpResponse("error")
    else:
        contact_form = ContactForm()
        contact_phone_form = ContactPhoneForm()
        contact_email_form = ContactEmailAddressForm()

        return render(request, "contacts/add-contact-rel-item.html", 
            {'contact_form': contact_form, 'cpf': contact_phone_form, 'cef': contact_email_form})



@csrf_exempt
@login_required
@permission_required('contacts.delete_contact')
def contact_delete(request):
    if request.method == "POST":
        cid = request.POST.get("cid")
        if cid:
            contact = Contact.objects.get(id=cid)
            contact_profile = ContactProfile.objects.get(contact=contact)
        try:
            # contact_profile.delete()
            contact.delete()
            return HttpResponse(cid)
        except:
            return HttpResponse("not deleted")
    else:
        return HttpResponseRedirect("/contacts/")

@login_required
@csrf_protect
@permission_required('contacts.change_contact')
def contact_edit(request, pk):
    contact = Contact.objects.get(id=pk)
    contact_profile, ap_created = ContactProfile.objects.get_or_create(contact=contact)

    CForm = ContactForm(instance=contact)
    CPForm = ContactProfileForm(instance=contact_profile)
    CPHForm = ContactPhoneForm()
    CEForm = ContactEmailAddressForm()
    CDMForm = ContactDistributionMethodForm()
    CCTForm = ContactContactTypeForm()

    contact_phones = ContactPhone.objects.filter(contact=contact)
    contact_emails = ContactEmailAddress.objects.filter(contact=contact)
    contact_distribution_methods = ContactDistributionMethod.objects.filter(contact=contact)
    contact_contact_types = ContactContactType.objects.filter(contact=contact)
    comments = Comment.objects.filter(contact=contact)[:5]

    page_title = 'Edit contact for (' + contact.contact_name + ')'

    return render_to_response("contacts/edit-contact.html", 
        {'cform': CForm, 'cpform': CPForm, 'cphform':CPHForm, 'cid': pk, 'cpid': contact_profile.id, 'CDMForm': CDMForm,
        'contact_phones': contact_phones, 'contact_emails': contact_emails, 'ceform': CEForm, 'cctform': CCTForm,
        'comments': comments, 'contact_distribution_methods': contact_distribution_methods, 'page_title': page_title,
        'contact_contact_types': contact_contact_types, },
        context_instance=RequestContext(request))


def contact_edit_basic(request, pk):
    contact = Contact.objects.get(id=pk)

    if request.method == 'POST':
        # import pdb; pdb.set_trace();
        CForm = ContactForm(request.POST, instance=contact)
        if CForm.is_valid():
            CForm.save()
            return HttpResponse(pk)
    else:
        CForm = ContactForm(instance=contact)

    return render(request, "contacts/contact-basic-edit.html", {'contact_basic_form': CForm, 'cid': pk})





@csrf_protect
def contact_update(request):
    if request.method == "POST":
        cid = request.POST.get("cid")
        contact = Contact.objects.get(id=cid)
        contact_profile = ContactProfile.objects.get(contact=contact)

        CForm = ContactForm(request.POST, instance=contact)
        CPForm = ContactProfileForm(request.POST, instance=contact_profile)

        if CForm.is_valid() and CPForm.is_valid():
            CForm.save()
            CPForm.save()
            return HttpResponse("success")
        else:
            return HttpResponse("error")
        
@csrf_protect
def profile_update(request):
    if request.method == "POST":
        cpid = request.POST.get("cpid")
        contact_profile = ContactProfile.objects.get(id=cpid)
        CPForm = ContactProfileForm(request.POST, instance=contact_profile)
        cid = contact_profile.contact.id

        if CPForm.is_valid():
            CPForm.save()
            return HttpResponse("success")
        else:
            return HttpResponse("error")


@login_required
@csrf_protect
def sc_profile(request, profile_id=False):
    
    if request.method == "POST":
        profile_id = request.POST.get("contact_id")
        profile = ContactProfile.objects.get(id=profile_id)                
        profile_form = ContactProfileFrom(request.POST, request.FILES, instance=profile)
        #user_form = UserForm(request.POST, instance=user)
        if profile_form.is_valid():
            profile_form.save()
            return HttpResponseRedirect("/contacts/")
            # user_form.save()
    else:
        profile = ContactProfile.objects.get(pk=profile_id)
        contact_phone_form = ContactPhoneForm()
        contact_phones = ContactPhone.objects.filter(contact_profile=profile)

        profile_form = ContactProfileFrom(instance=profile)
    

    page_title = 'Profile Update for (' + profile.contact.contact_name + ')'

    return render_to_response("contacts/contact-profile.html", 
        { 'profile_form': profile_form, 'cpform': contact_phone_form,
        'contact_phones':contact_phones, 'page_title': page_title, 'pid': profile.id }, 
        context_instance=RequestContext(request))


@login_required
@csrf_exempt
def sc_phone_list(request):
    if request.method == 'POST':
        name = request.POST.get("autocomplete")
        contact_phones = ContactPhone.objects.filter(contact_profile__contact__username__icontains=name)
    else:
        contact_phones = ContactPhone.objects.all()

    phone_filte_form = ContactPhoneLookupForm()
    return render_to_response("contacts/phone-list.html",
        {'contact_phones': contact_phones, 'phone_filte_form': phone_filte_form, 'page_title': 'Phone List'},
        context_instance=RequestContext(request))



@login_required
@csrf_exempt
def contact_phone_add(request):

    if request.method == 'POST':
        
        phone_type_id = request.POST.get("phone_type")
        phone_type = PhoneType.objects.get(id=phone_type_id)
        phone = request.POST.get("phone")
        phone_ext = request.POST.get("phone_ext")
        cid = request.POST.get("cid")

        profile = Contact.objects.get(id=cid)
        contact_phone = ContactPhone(contact=profile,phone_type=phone_type, phone=phone, phone_ext=phone_ext)
        contact_phone.save()
        profile.save()
        
        return render_to_response("contacts/partials/contact-phone-item-partial.html",
            {"contact_phone": contact_phone},
            context_instance=RequestContext(request))

@login_required
@csrf_exempt
@permission_required("contacts.change_contactphone")
def contact_phone_edit(request, pid):
    
    if request.method == "POST":
        
        pid = request.POST.get("pid")
        phone = ContactPhone.objects.get(id=pid)
        contact_phone_form = ContactPhoneForm(request.POST, instance=phone)
        if contact_phone_form.is_valid():
            contact_phone = contact_phone_form.save()
            try:
                contact = phone.contact
                contact.save()
            except Exception, e:
                pass
            return render_to_response("contacts/partials/phone-item-tmpl.html",
            {'contact_phone': contact_phone},context_instance=RequestContext(request))
    elif request.method == "GET":
        
        phone = ContactPhone.objects.get(id=pid)
        contact_phone_form = ContactPhoneForm(instance=phone)

        return render_to_response("contacts/partials/edit-phone-tmpl.html",
            {'cphform':contact_phone_form, 'pid': pid},context_instance=RequestContext(request))


@csrf_exempt
@permission_required("contacts.add_contactcontacttype")
def contact_contact_type_add(request):
    if request.method == 'POST':
        cid = request.POST.get("cid")
        ctid = request.POST.get("contact_type")

        contact = Contact.objects.get(id=cid)
        contact_type = ContactType.objects.get(id=ctid)
        description = request.POST['description']

        contact_contact_type = ContactContactType(contact=contact, contact_type=contact_type, description=description)
        contact_contact_type.save()
        return render_to_response("contacts/partials/contact-contact-type-item-tmpl.html",
            {"contact_contact_type": contact_contact_type, 'page_title': 'Add Contact Type'},
            context_instance=RequestContext(request))

@login_required
@csrf_exempt
@permission_required("contacts.change_contactcontacttype")
def contact_contact_type_edit(request, cctid):
    if request.method == "POST":
        cctid = request.POST.get("cctid")
        contact_contact_type = ContactContactType.objects.get(id=cctid)
        contact_contact_type_form = ContactContactTypeForm(request.POST, instance=contact_contact_type)
        if contact_contact_type_form.is_valid():
            contact_contact_type = contact_contact_type_form.save()
            return render_to_response("contacts/partials/contact-contact-type-item-tmpl.html",
                {'contact_contact_type': contact_contact_type},context_instance=RequestContext(request))

    elif request.method == "GET":
        contact_contact_type = ContactContactType.objects.get(id=cctid)
        contact_contact_type_form = ContactContactTypeForm(instance=contact_contact_type)

        return render_to_response("contacts/partials/edit-contact-contact-type-tmpl.html",
            {'cctform': contact_contact_type_form, 'cctid': cctid},context_instance=RequestContext(request))



@login_required
@csrf_exempt
@permission_required("contacts.delete_contactcontacttype")
def contact_contact_type_delete(request):
    if request.method == 'POST':
        cctid = request.POST.get("cctid")
        contact_contact_type = ContactContactType.objects.get(id=cctid)
        try:
            contact_contact_type.delete()
            return HttpResponse(cctid)
        except:
            messages.errors(request, "Contact's contact type is not deleted.")
            return True

    else:
        return HttpResponse("User contact's contact type is added.")


@login_required
@csrf_exempt
@permission_required("contacts.add_contactdistributionmethod")
def contact_distribution_method_add(request):
    if request.method == 'POST':

        cid = request.POST.get("cid")
        dmid = request.POST.get("distribution_method")

        contact = Contact.objects.get(id=cid)
        distribution_method = DistributionMethod.objects.get(id=dmid)
        description = request.POST['description']

        contact_distribution_method = ContactDistributionMethod(contact=contact, distribution_method=distribution_method, description=description)
        contact_distribution_method.save()
        return render_to_response("contacts/partials/contact-distribution-method-item-tmpl.html",
            {"contact_distribution_method": contact_distribution_method, 'page_title': 'Add Distribution Method'},
            context_instance=RequestContext(request))

@login_required
@csrf_exempt
@permission_required("contacts.change_contactdistributionmethod")
def contact_distribution_method_edit(request, cdmid):
    if request.method == "POST":
        cdmid = request.POST.get("cdmid")
        contact_distribution_method = ContactDistributionMethod.objects.get(id=cdmid)
        contact_distribution_method_form = ContactDistributionMethodForm(request.POST, instance=contact_distribution_method)
        if contact_distribution_method_form.is_valid():
            contact_distribution_method = contact_distribution_method_form.save()
            return render_to_response("contacts/partials/contact-distribution-method-item-tmpl.html",
                {'contact_distribution_method': contact_distribution_method},context_instance=RequestContext(request))

    elif request.method == "GET":
        contact_distribution_method = ContactDistributionMethod.objects.get(id=cdmid)
        contact_distribution_method_form = ContactDistributionMethodForm(instance=contact_distribution_method)

        return render_to_response("contacts/partials/edit-contact-distribution-method-tmpl.html",
            {'cmdform': contact_distribution_method_form, 'cdmid': cdmid},context_instance=RequestContext(request))


@login_required
@csrf_exempt
@permission_required("contacts.delete_contactdistributionmethod")
def contact_distribution_method_delete(request):
    if request.method == 'POST':
        cdmid = request.POST.get("cdmid")
        contact_distribution_method = ContactDistributionMethod.objects.get(id=cdmid)
        try:
            contact_distribution_method.delete()
            return HttpResponse(cdmid)
        except:
            messages.errors(request, "Distribution Method is not deleted.")
            return True

    else:
        return HttpResponse("User contact Distribution Method is added.")


@login_required
@csrf_exempt
@permission_required("contacts.add_contactemailaddress")
def contact_email_add(request):
    if request.method == "POST":
        # import pdb; pdb.set_trace();
        cid = request.POST.get("cid")
        etype_id = request.POST.get("email_address_type")
        email_add = request.POST.get("email_address")

        contact = Contact.objects.get(id=cid)
        email_type = EmailAddressType.objects.get(id=etype_id)

        contact_email_address = ContactEmailAddress(contact=contact, email_address_type=email_type, email_address=email_add)
        contact_email_address.save()
        contact.save()
        return render_to_response("contacts/partials/email-item-tmpl.html", {"contact_email": contact_email_address},
            context_instance=RequestContext(request))

@login_required
@csrf_exempt
@permission_required("contacts.change_contactemailaddress")
def contact_email_edit(request, eid):
    if request.method == "POST":
        
        eid = request.POST.get("eid")
        email = ContactEmailAddress.objects.get(id=eid)
        contact = email.contact
        contact_email_form = ContactEmailAddressForm(request.POST, instance=email)
        if contact_email_form.is_valid():
            contact_email = contact_email_form.save()
            contact.save()
            return render_to_response("contacts/partials/email-item-tmpl.html",
            {'contact_email': contact_email},context_instance=RequestContext(request))
    elif request.method == "GET":
        
        email = ContactEmailAddress.objects.get(id=eid)
        contact_email_form = ContactEmailAddressForm(instance=email)

        return render_to_response("contacts/partials/edit-email-tmpl.html",
            {'ceform': contact_email_form, 'eid': eid},context_instance=RequestContext(request))





@login_required
@csrf_exempt
@permission_required("contacts.delete_contactemailaddress")
def sc_email_delete(request):

    if request.method == 'POST':
        email_id = request.POST.get("email_id")
        email = ContactEmailAddress.objects.get(id=email_id)
        contact = email.contact
        try:
            email.delete()
            contact.save()
            return HttpResponse(email_id)
        except:
            messages.errors(request, "Email is not deleted.")
            return True

    else:
        return HttpResponse("User contact email is added.")
# def sc_phone_add(request):
#     if request.method == 'POST':
        
#         contact_phone_form = ContactPhoneForm2(request.POST)
#         if contact_phone_form.is_valid():
#             contact_phone_form.save()


#     else:
#         contact_phone_form = ContactPhoneForm2()
          
#     return render_to_response("contacts/phone-add.html", 
#             {'phone_form': contact_phone_form}, 
#             context_instance=RequestContext(request))

@login_required
@csrf_exempt
def sc_phone_delete(request):

    if request.method == 'POST':
        # import pdb; pdb.set_trace()
        
        phone_id = request.POST.get("phone_id")
        phone = ContactPhone.objects.get(id=phone_id)
        try:
            contact = phone.contact
            phone.delete()
            contact.save()

            return HttpResponse(phone_id)
        except:
            messages.errors(request, "Phone is not deleted.")
            return True

    else:
        return HttpResponse("User contact phone is added.")


@login_required
@csrf_exempt
@permission_required("contacts.add_comment")
def contact_comment_add(request):
    if request.method == "POST":
        cid = request.POST.get("cid")
        com = request.POST.get("comment")
        contact = Contact.objects.get(id=cid)
        user = request.user
        comment = Comment(contact=contact, staff=user, comment=com)
        try:
            comment.save()
            return render_to_response("contacts/partials/comment-partial.html",
                {'comment': comment},
                context_instance=RequestContext(request))
        except:
            return HttpResponse("error")

@login_required
@csrf_exempt
@permission_required("contacts.change_comment")
def contact_comment_edit(request, com_id):
    comment = Comment.objects.get(id=com_id)
    if request.method == "POST":
        # com_id = request.POST.get("com_id")
        # comment = Comment.objects.get(id=com_id)
        comment_form = CommentForm(request.POST, instance=comment)
        if comment_form.is_valid():
            comment = comment_form.save()
            return render_to_response("contacts/partials/comment-partial.html",
            {'comment': comment},context_instance=RequestContext(request))
    elif request.method == "GET":
        
        
        comment_form = CommentForm(instance=comment)

        return render_to_response("contacts/partials/edit-comment-tmpl.html",
            {'comform': comment_form, 'com_id': com_id},context_instance=RequestContext(request))

@csrf_exempt
@login_required
def contact_comment_delete(request):
    if request.method == "POST":
        
        com_id = request.POST.get("com_id")
        try:
            comment = Comment.objects.get(id=com_id)
            comment.delete()
            return HttpResponse(com_id)
        except:
            return HttpResponse('error')

def view_terms_json(request):
    payment_terms = PaymentTerm.objects.all()
    term_list = []
    for pt in payment_terms:
        pt_dict = {}
        pt_dict['id'] = pt.id
        pt_dict['term'] = pt.term
        pt_dict['is_active'] = pt.is_active
        term_list.append(pt_dict)


    json_pt = json.dumps(term_list)
    return HttpResponse(json_pt, mimetype='application/json')

def view_terms(request):
    payment_terms = PaymentTerm.objects.all()
    
    return render_to_response("contacts/list-terms.html",
        {'payment_terms': payment_terms, 'page_title': 'Payment Term List'}, 
        context_instance=RequestContext(request))

@csrf_exempt
@permission_required("contacts.add_paymentterm")
def term_add(request):
    if request.method == "POST":
        term = request.POST.get("term")
        try:
            payment_term = PaymentTerm.objects.create(term=term, is_active=True)
            return render_to_response("contacts/partials/add-paymentterm-partial.html",
                {'payment_term': payment_term, 'page_title': 'Add Payment Term'}, 
                context_instance=RequestContext(request))
        except:
            return HttpResponse("error")
    else:
        payment_terms = PaymentTerm.objects.all()
        term_form = PaymentTermForm()

        return render_to_response("contacts/list-paymentterm.html",
            {'payment_terms': payment_terms, 'term_form': term_form, 'page_title': 'Add Payment Term'}, 
            context_instance=RequestContext(request))

@csrf_exempt
@login_required
@permission_required("contacts.change_paymentterm")
def term_edit(request, ptid):
    if request.method == "POST":
        # import pdb; pdb.set_trace();
        ptid = request.POST.get("ptid")
        payment_term = PaymentTerm.objects.get(id=ptid)
        term_form = PaymentTermForm(request.POST, instance=payment_term)
        if term_form.is_valid():
            payment_term = term_form.save()
            return render_to_response("contacts/partials/add-paymentterm-partial.html",
            {'payment_term': payment_term}, context_instance=RequestContext(request))
    elif request.method == "GET":
        
        payment_term = PaymentTerm.objects.get(id=ptid)
        term_form = PaymentTermForm(instance=payment_term)

        return render_to_response("contacts/partials/edit-term-tmpl.html",
            {'ptform': term_form, 'ptid': ptid}, context_instance=RequestContext(request))



@csrf_exempt
@login_required
@permission_required("contacts.delete_paymentterm")
def term_delete(request):
    if request.method == "POST":
        ptid = request.POST.get("ptid")
        payment_term = PaymentTerm.objects.get(id=ptid)
        payment_term.delete()
        return HttpResponse(ptid)
    else:
        return HttpResponse("Hello World!")


@csrf_exempt
@login_required
@permission_required("contacts.add_contacttype")
def contact_type_add(request):
    if request.method == "POST":
        
        contact_type = request.POST.get("contact_type")
        try:
            contact_type = ContactType.objects.create(contact_type=contact_type, is_active=True)
            return render_to_response("contacts/partials/add-contact-type-partial.html",
                {'contact_type': contact_type}, 
                context_instance=RequestContext(request))
        except:
            return HttpResponse("error")
    else:
        contact_types = ContactType.objects.all()
        contact_type_form = ContactTypeForm()

        return render_to_response("contacts/list-contact-type.html",
            {'contact_types': contact_types, 'contact_type_form': contact_type_form}, 
            context_instance=RequestContext(request))

@csrf_exempt
def contact_type_edit(request, ctid):

    if request.method == "POST":
        ctid = request.POST.get("ctid")
        contact_type = ContactType.objects.get(id=ctid)
        contact_type_form = ContactTypeForm(request.POST, instance=contact_type)
        if contact_type_form.is_valid():
            contact_type = contact_type_form.save()
            return render_to_response("contacts/partials/add-contact-type-partial.html",
            {'contact_type': contact_type}, context_instance=RequestContext(request))
    elif request.method == "GET":
        
        contact_type = ContactType.objects.get(id=ctid)
        contact_type_form = ContactTypeForm(instance=contact_type)

        return render_to_response("contacts/partials/edit-contact-type-tmpl.html",
            {'ctform': contact_type_form, 'ctid': ctid}, context_instance=RequestContext(request))

@csrf_exempt
def contact_type_delete(request):
    if request.method == "POST":
        ctid = request.POST.get("ctid")
        contact_type = ContactType.objects.get(id=ctid)
        contact_type.delete()
        return HttpResponse(ctid)
    else:
        return HttpResponse("Hello World!")


def view_contact_types(request):
    
    contact_types = ContactType.objects.all()

    return render_to_response("contacts/list-contact-types.html",
        {'contact_types': contact_types, 'page_title': 'Contact Type List' }, context_instance=RequestContext(request))

@csrf_exempt
@permission_required("contacts.add_emailaddresstype")
def contact_email_type_add(request):
    if request.method == "POST":
        
        email_type = request.POST.get("email_type")
        try:
            email_address_type = EmailAddressType.objects.create(email_type=email_type, is_active=True)
            return render_to_response("contacts/partials/add-email-address-type-partial.html",
                {'email_type': email_address_type}, 
                context_instance=RequestContext(request))
        except:
            return HttpResponse("error")
    else:
        email_types = EmailAddressType.objects.all()
        email_type_form = EmailAddressTypeForm()

        return render_to_response("contacts/list-email-address-type.html",
            {'email_types': email_types, 'email_type_form': email_type_form, 'page_title': 'Add Email Type'}, 
            context_instance=RequestContext(request))


def view_email_types(request):
    
    email_types = EmailAddressType.objects.all()

    return render_to_response("contacts/list-email-types.html",
        {'email_types': email_types, 'page_title': 'List Email Type' }, context_instance=RequestContext(request))

@csrf_exempt
@permission_required("contacts.change_emailaddresstype")
def email_type_edit(request, etid):

    if request.method == "POST":

        
        etid = request.POST.get("etid")
        email_type = EmailAddressType.objects.get(id=etid)
        email_type_form = EmailAddressTypeForm(request.POST, instance=email_type)
        if email_type_form.is_valid():
            email_type = email_type_form.save()
            return render_to_response("contacts/partials/add-email-address-type-partial.html",
            {'email_type': email_type}, context_instance=RequestContext(request))
    elif request.method == "GET":
        
        email_type = EmailAddressType.objects.get(id=etid)
        email_type_form = EmailAddressTypeForm(instance=email_type)

        return render_to_response("contacts/partials/edit-email-type-tmpl.html",
            {'etform': email_type_form, 'etid': etid}, context_instance=RequestContext(request))

@csrf_exempt
@permission_required("contacts.delete_emailaddresstype")
def email_type_delete(request):
    if request.method == "POST":
        etid = request.POST.get("etid")
        email_type = EmailAddressType.objects.get(id=etid)
        email_type.delete()
        return HttpResponse(etid)
    else:
        return HttpResponse("Hello World!")



def view_delivery_choices(request):
    
    delivery_choices = DeliveryChoice.objects.all()
    delivery_choice_form = DeliveryChoiceForm()

    return render_to_response("contacts/delivery-choices.html",
        {'delivery_choices': delivery_choices, 'delivery_choice_form': delivery_choice_form, 'page_title': 'List Delivery Choice'}, 
        context_instance=RequestContext(request))

@login_required
@csrf_exempt
@permission_required("contacts.add_deliverychoice")
def add_delivery_choices(request):
    if request.method == "POST":
        delivery_choice = request.POST.get("delivery_choice")
        try:
            delivery_choice = DeliveryChoice.objects.create(delivery_choice=delivery_choice, is_active=True)
            return render_to_response("contacts/partials/add-delivery-choice-partial.html",
                {'delivery_choice': delivery_choice}, 
                context_instance=RequestContext(request))
        except:
            return HttpResponse("error")
    else:
        delivery_choices = DeliveryChoice.objects.all()
        delivery_choice_form = DeliveryChoiceForm()

        return render_to_response("contacts/list-delivery-choice.html",
            {'delivery_choices': delivery_choices, 'delivery_choice_form': delivery_choice_form, 'page_title': 'Add Delivery Choice'}, 
            context_instance=RequestContext(request))


@login_required
@csrf_exempt
@permission_required("contacts.change_deliverychoice")
def edit_delivery_choices(request, dcid):
    if request.method == "POST":
        dcid = request.POST.get("dcid")
        delivery_choice = DeliveryChoice.objects.get(id=dcid)
        delivery_choice_form = DeliveryChoiceForm(request.POST, instance=delivery_choice)
        if delivery_choice_form.is_valid():
            delivery_choice = delivery_choice_form.save()
            return render_to_response("contacts/partials/add-delivery-choice-partial.html",
            {'delivery_choice': delivery_choice}, context_instance=RequestContext(request))
    elif request.method == "GET":
        
        delivery_choice = DeliveryChoice.objects.get(id=dcid)
        delivery_choice_form = DeliveryChoiceForm(instance=delivery_choice)

        return render_to_response("contacts/partials/edit-delivery-choice-tmpl.html",
            {'dcform': delivery_choice_form, 'dcid': dcid}, context_instance=RequestContext(request))


@csrf_exempt
@login_required
@permission_required("contacts.delete_deliverychoice")
def delivery_choices_delete(request):
    if request.method == "POST":
        dcid = request.POST.get("dcid")
        delivery_choice = DeliveryChoice.objects.get(id=dcid)
        delivery_choice.delete()
        return HttpResponse(dcid)
    else:
        return HttpResponse("Hello World!")


def list_delivery_choices(request):
    delivery_choices = DeliveryChoice.objects.all()
    delivery_choice_list = []
    for dc in delivery_choices:
        dc_dict = {}
        dc_dict['id'] = dc.id
        dc_dict['delivery_choice'] = dc.delivery_choice
        dc_dict['is_active'] = dc.is_active
        delivery_choice_list.append(dc_dict)


    json_delivery_choices = json.dumps(delivery_choice_list)
    return HttpResponse(json_delivery_choices, mimetype='application/json')

@login_required
@csrf_exempt
@permission_required("contacts.add_currency")
def add_currency(request):
    currencies = Currency.objects.all()
    if request.method == "POST":
        currency_form = CurrencyForm(request.POST)
        if currency_form.is_valid():
            currency_form.save()
            currencies = Currency.objects.all()

            return HttpResponseRedirect("/contacts/currency/")
        else:
            return render_to_response("contacts/add-currency.html",
            {'currencies': currencies, 'currency_form': currency_form, 'page_title': 'Add Currency'}, 
            context_instance=RequestContext(request))        
    else:
        currency_form = CurrencyForm()

        return render_to_response("contacts/add-currency.html",
            {'currencies': currencies, 'currency_form': currency_form, 'page_title': 'Add Currency'}, 
            context_instance=RequestContext(request))


@login_required
@csrf_exempt
@permission_required("contacts.change_currency")
def edit_currency(request, curid):
    if request.method == "POST":
        currency = Currency.objects.get(id=curid)
        currency_form = CurrencyForm(request.POST, instance=currency)
        if currency_form.is_valid():
            currency = currency_form.save()
            return HttpResponse(curid)
    elif request.method == "GET":
        
        currency = Currency.objects.get(id=curid)
        currency_form = CurrencyForm(instance=currency)

        return render_to_response("contacts/partials/edit-currency-tmpl.html",
            {'currency_form': currency_form, 'curid': curid}, context_instance=RequestContext(request))

@csrf_exempt
@login_required
@permission_required("contacts.delete_currency")
def delete_currency(request):
    if request.method == "POST":
        curid = request.POST.get("currency_id")
        currency = Currency.objects.get(id=curid)
        currency.delete()
        return HttpResponse(curid)
    else:
        return HttpResponse("Hello World!")


def view_currency(request):
    currencies = Currency.objects.all()

    return render_to_response("contacts/list-currency.html",
        {'currencies': currencies, 'page_title': 'List Currency'},
        context_instance=RequestContext(request))


def get_currencies(request):
    currencies = Currency.objects.all()
    currency_list = []
    for currency in currencies:
        cur_dict = {}
        cur_dict['id'] = currency.id
        cur_dict['currency'] = currency.currency
        cur_dict['currency_icon'] = currency.currency_icon

        currency_list.append(cur_dict)



    currency_json = json.dumps(currency_list)
    return HttpResponse(currency_json, mimetype='application/json')



@csrf_exempt
@login_required
@permission_required("contacts.add_phonetype")
def add_phone_type(request):
    if request.method == "POST":
        phone_type = request.POST.get("phone_type")
        try:
            phone_type = PhoneType.objects.create(phone_type=phone_type)
            return render_to_response("contacts/partials/add-phone-type-partial.html",
                {'phone_type': phone_type}, 
                context_instance=RequestContext(request))
        except:
            return HttpResponse("error")
    elif request.method == "GET":
        
        phone_types = PhoneType.objects.all()
        phone_type_form = PhoneTypeForm()

        return render_to_response("contacts/list-phone-type.html",
            {'ptform': phone_type_form, 'phone_types': phone_types, 'page_title': 'Add Phone Type'}, context_instance=RequestContext(request))


def view_phone_type(request):
    phone_types = PhoneType.objects.all()

    return render_to_response("contacts/phone-type-list.html",
        {'phone_types': phone_types, 'page_title': 'List Phone Type'},
        context_instance=RequestContext(request))

@csrf_exempt
@login_required
@permission_required("contacts.change_phonetype")
def edit_phone_type(request, ptid):
    if request.method == "POST":
        ptid = request.POST.get("ptid")
        phone_type = PhoneType.objects.get(id=ptid)
        phone_type_form = PhoneTypeForm(request.POST, instance=phone_type)
        if phone_type_form.is_valid():
            phone_type = phone_type_form.save()
            return render_to_response("contacts/partials/add-phone-type-partial.html",
            {'phone_type': phone_type}, context_instance=RequestContext(request))
    elif request.method == "GET":
        
        phone_type = PhoneType.objects.get(id=ptid)
        phone_type_form = PhoneTypeForm(instance=phone_type)

        return render_to_response("contacts/partials/edit-phone-type-tmpl.html",
            {'ptform': phone_type_form, 'ptid': ptid}, context_instance=RequestContext(request))

@csrf_exempt
@login_required
@permission_required("contacts.delete_phonetype")
def delete_phone_type(request):
    if request.method == "POST":
        phtid = request.POST.get("phtid")
        phone_type = PhoneType.objects.get(id=phtid)
        phone_type.delete()
        return HttpResponse(phtid)
    else:
        return HttpResponse("Hello World!")

def view_distribution_method(request):
    distribution_methods = DistributionMethod.objects.all()

    return render_to_response("contacts/distribution-method-list.html",
        {'distribution_methods': distribution_methods, 'page_title': 'List Distribution Method'},
        context_instance=RequestContext(request))

@csrf_exempt
@login_required
@permission_required("contacts.add_distributionmethod")
def add_distribution_method(request):
    if request.method == "POST":
        distribution_method = request.POST.get("distribution_method")
        try:
            distribution_method = DistributionMethod.objects.create(distribution_method=distribution_method)
            return render_to_response("contacts/partials/add-distribution-method-partial.html",
                {'distribution_method': distribution_method}, 
                context_instance=RequestContext(request))
        except:
            return HttpResponse("error")
    elif request.method == "GET":
        
        distribution_methods = DistributionMethod.objects.all()
        distribution_method_form = DistributionMethodForm()

        return render_to_response("contacts/list-distribution-method.html",
            {'dmform': distribution_method_form, 'distribution_methods': distribution_methods, 'page_title': 'Add Distribution Method'}, context_instance=RequestContext(request))


@csrf_exempt
@login_required
@permission_required("contacts.change_distributionmethod")
def edit_distribution_method(request, dmid):
    if request.method == "POST":
        dmid = request.POST.get("dmid")
        distribution_method = DistributionMethod.objects.get(id=dmid)
        distribution_method_form = DistributionMethodForm(request.POST, instance=distribution_method)
        if distribution_method_form.is_valid():
            distribution_method = distribution_method_form.save()
            return render_to_response("contacts/partials/add-distribution-method-partial.html",
            {'distribution_method': distribution_method}, context_instance=RequestContext(request))
    elif request.method == "GET":
        
        distribution_method = DistributionMethod.objects.get(id=dmid)
        distribution_method_form = DistributionMethodForm(instance=distribution_method)

        return render_to_response("contacts/partials/edit-distribution-method-tmpl.html",
            {'dmform': distribution_method_form, 'dmid': dmid}, context_instance=RequestContext(request))


@csrf_exempt
@login_required
@permission_required("contacts.delete_distributionmethod")
def delete_distribution_method(request):
    if request.method == "POST":
        distid = request.POST.get("distid")
        distribution_method = DistributionMethod.objects.get(id=distid)
        distribution_method.delete()
        return HttpResponse(distid)
    else:
        return HttpResponse("Hello World!")




def get_contact(request, pk):
    # import pdb; pdb.set_trace()
    import json, datetime
    from django.core.serializers.json import DjangoJSONEncoder
    contact = Contact.objects.get(pk=pk)
    cprofile = ContactProfile.objects.get(contact=contact)

    con_dict = {}
    con_dict['id'] = contact.id
    con_dict['contact_name'] = contact.contact_name
    con_dict['address_1'] = contact.address_1
    con_dict['city'] = contact.city
    con_dict['province'] = contact.province
    con_dict['country'] = contact.country

    if cprofile.terms:
        con_dict['terms'] = cprofile.terms.term

    if cprofile.shipping_method:
        con_dict['shipping_method'] = cprofile.shipping_method.delivery_choice
        con_dict['shipping_method_id'] = cprofile.shipping_method.id
    # con_dict['city'] = cprofile.city
    # con_dict['city'] = cprofile.city

    cphones = ContactPhone.objects.filter(contact=contact)
    phones = []
    for cphone in cphones:
        phone = {}
        phone['type'] = cphone.phone_type.phone_type
        phone['number'] = cphone.phone
        phone['phone_ext'] = cphone.phone_ext
        phones.append(phone)

    con_dict['contact_numbers'] = phones
    json_posts = json.dumps(con_dict, cls=DjangoJSONEncoder)
    return HttpResponse(json_posts, mimetype='application/json')


def get_contact_hover(request, pk):
    import json, datetime
    # from django.core.serializers.json import DjangoJSONEncoder
    contact = Contact.objects.get(pk=pk)
    con_dict = {}
    con_dict['contact_name'] = contact.contact_name
    con_dict['address_1'] = contact.address_1
    con_dict['city'] = contact.city

    cphones = ContactPhone.objects.filter(contact=contact)
    phones = []
    for cphone in cphones:
        phone = {}
        phone['type'] = cphone.phone_type.phone_type
        phone['number'] = cphone.phone
        phone['phone_ext'] = cphone.phone_ext
        phones.append(phone)

    con_dict['contact_numbers'] = phones

    return render(request, "contacts/supplier-contact-for-hover.html", {'contact': con_dict})

@csrf_exempt
def make_call(request):
    if request.method == 'POST':
        phone_number = request.POST.get("phone_number")
        phone_ext = request.POST.get("extension")
        return HttpResponse(phone_number)



@csrf_exempt
@login_required
def contact_reindex(request):
    contacts = Contact.objects.all()
    for contact in contacts:
        contact.search_string = contact.contact_name + " " + contact.city + " " + contact.province + " " + contact.attention_to
        contact.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

