import datetime
from haystack import indexes
from controllers.models import Controller, ControllerContact

class ControllerIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    controller_id = indexes.CharField(model_attr='controller_id', boost=2)
    controller_type = indexes.CharField(model_attr='controller_type', indexed=False)
    
    def get_model(self):
        return Controller


    def prepare(self, obj):
        self.prepared_data = super(ControllerIndex, self).prepare(obj)
        controller_contacts = ControllerContact.objects.filter(controller=obj)
        cons = []
        for con in controller_contacts:
            con_dic = {}
            con_dic['id'] = con.id
            con_dic['contact_id'] = con.contact_id
            con_dic['description'] = con.description
            con_dic['status'] = con.status
            cons.append(con_dic)
        self.prepared_data['controller_contacts'] = cons

        sold_to = obj.sold_to
        if sold_to:
            sold_to_dict = {}
            sold_to_dict['id'] = sold_to.id
            sold_to_dict['contact_name'] = sold_to.contact_name
            sold_to_dict['attention_to'] = sold_to.attention_to
            sold_to_dict['address_1'] = sold_to.address_1
            sold_to_dict['address_2'] = sold_to.address_2
            sold_to_dict['city'] = sold_to.city
            sold_to_dict['province'] = sold_to.province
            sold_to_dict['country'] = sold_to.country
            sold_to_dict['postal_code'] = sold_to.postal_code
            phones = sold_to.contact_phone.all()
            phs = []
            for ph in phones:
                phone = {}
                phone['number'] = ph.phone
                phone['ext'] = ph.phone_ext
                phone['type'] = ph.phone_type.phone_type
                phs.append(phone)
            sold_to_dict['phones'] = phs
            emails = sold_to.contact_emails.all()
            elist = []
            for em in emails:
                email = {}
                email['email_type'] = em.email_address_type.email_type
                email['email_address'] = em.email_address
                elist.append(email)

            sold_to_dict['emails'] = elist

            self.prepared_data['sold_to'] = sold_to_dict

        location = obj.location
        if location:
            sold_to_dict = {}
            sold_to_dict['id'] = location.id
            sold_to_dict['contact_name'] = location.contact_name
            sold_to_dict['attention_to'] = location.attention_to
            sold_to_dict['address_1'] = location.address_1
            sold_to_dict['address_2'] = location.address_2
            sold_to_dict['city'] = location.city
            sold_to_dict['province'] = location.province
            sold_to_dict['country'] = location.country
            sold_to_dict['postal_code'] = location.postal_code
            phones = location.contact_phone.all()
            phs = []
            for ph in phones:
                phone = {}
                phone['number'] = ph.phone
                phone['ext'] = ph.phone_ext
                phone['type'] = ph.phone_type.phone_type
                phs.append(phone)
            sold_to_dict['phones'] = phs
            emails = location.contact_emails.all()
            elist = []
            for em in emails:
                email = {}
                email['email_type'] = em.email_address_type.email_type
                email['email_address'] = em.email_address
                elist.append(email)

            sold_to_dict['emails'] = elist

            self.prepared_data['location'] = sold_to_dict

        return self.prepared_data



    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()