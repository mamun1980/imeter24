import datetime
from haystack import indexes
from contacts.models import Contact, ContactPhone


class ContactIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    contact_name = indexes.CharField(model_attr='contact_name', boost=2)
    city = indexes.CharField(model_attr='city', indexed=False)
    country = indexes.CharField(model_attr='country', indexed=False)
    province = indexes.CharField(model_attr='province', indexed=False)
    address_1 = indexes.CharField(model_attr='address_1')
    attention_to = indexes.CharField(model_attr='attention_to', indexed=False)
    postal_code = indexes.CharField(model_attr='postal_code', indexed=False)
    # phones = indexes.MultiValueField(indexed=False, null=True)
    # search_string = indexes.NgramField(model_attr='search_string')

    def get_model(self):
        return Contact

    def prepare(self, obj):
        self.prepared_data = super(ContactIndex, self).prepare(obj)
        phones = obj.contact_phone.all()
        phs = []
        for ph in phones:
            phone = {}
            phone['number'] = ph.phone
            phone['ext'] = ph.phone_ext
            phone['type'] = ph.phone_type.phone_type
            phs.append(phone)
        self.prepared_data['phones'] = phs
        emails = obj.contact_emails.all()
        elist = []
        for em in emails:
            email = {}
            email['email_type'] = em.email_address_type.email_type
            email['email_address'] = em.email_address
            elist.append(email)

        self.prepared_data['emails'] = elist

        
        # if obj.contactprofile:
        #     con_profile = obj.contactprofile
        #     term = {}
        #     if con_profile.terms:
        #         term['id'] = con_profile.terms.id
        #         term['term'] = con_profile.terms.term
        #         self.prepared_data['term'] = term
            

        return self.prepared_data

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()