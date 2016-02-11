import datetime
from haystack import indexes
from contacts.models import Contact, ContactContactType, ContactPhone, ContactEmailAddress, ContactDistributionMethod


class ContactIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    contact_name = indexes.CharField(model_attr='contact_name', boost=2)
    attention_to = indexes.CharField(model_attr='attention_to', indexed=False)
    address_1 = indexes.CharField(model_attr='address_1')
    address_2 = indexes.CharField(model_attr='address_2')
    city = indexes.CharField(model_attr='city', indexed=False)
    province = indexes.CharField(model_attr='province', indexed=False)
    country = indexes.CharField(model_attr='country', indexed=False)
    postal_code = indexes.CharField(model_attr='postal_code', indexed=False)
    webpage = indexes.CharField(model_attr='webpage', indexed=False)
    gst_number = indexes.CharField(model_attr='gst_number', indexed=False)
    gst_tax_exempt = indexes.BooleanField(model_attr='gst_tax_exempt', indexed=False)
    hst_number = indexes.CharField(model_attr='hst_number', indexed=False)
    hst_tax_exempt = indexes.BooleanField(model_attr='hst_tax_exempt', indexed=False)
    pst_tax_exempt = indexes.BooleanField(model_attr='pst_tax_exempt', indexed=False)
    pst_number = indexes.CharField(model_attr='pst_number', indexed=False)
    foreign_account = indexes.CharField(model_attr='foreign_account', indexed=False)
    mail_list = indexes.CharField(model_attr='mail_list', indexed=False)
    ship_collect = indexes.BooleanField(model_attr='ship_collect', indexed=False)
    fob = indexes.CharField(model_attr='fob', indexed=False)
    ap_contact = indexes.CharField(model_attr='ap_contact', indexed=False)
    bv_ap_account = indexes.CharField(model_attr='bv_ap_account', indexed=False)
    bv_ar_account = indexes.CharField(model_attr='bv_ar_account', indexed=False)

    def get_model(self):
        return Contact

    def prepare(self, obj):
        self.prepared_data = super(ContactIndex, self).prepare(obj)
        # phones = obj.contact_phone.all()
        phones = ContactPhone.objects.filter(contact=obj)
        phs = []
        for ph in phones:
            phone = {}
            phone['id'] = ph.id
            phone['number'] = ph.phone
            phone['ext'] = ph.phone_ext
            phone['type'] = ph.phone_type.phone_type
            phs.append(phone)
        self.prepared_data['phones'] = phs
        # emails = obj.contact_emails.all()
        emails = ContactEmailAddress.objects.filter(contact=obj)
        elist = []
        for em in emails:
            email = {}
            email['email_type'] = em.email_address_type.email_type
            email['email_address'] = em.email_address
            email['id'] = em.id
            elist.append(email)

        self.prepared_data['emails'] = elist

        distribution_methods = ContactDistributionMethod.objects.filter(contact=obj)
        dmlist = []
        for em in distribution_methods:
            dm = {}
            dm['distribution_method'] = em.distribution_method.distribution_method
            dm['description'] = em.description
            dm['id'] = em.id
            dmlist.append(dm)

        self.prepared_data['distribution_methods'] = dmlist

        contact_types = ContactContactType.objects.filter(contact=obj)
        ctlist = []
        for ct in contact_types:
            ctd = {}
            ctd['contact_type'] = ct.contact_type.contact_type
            ctd['description'] = ct.description
            ctd['id'] = ct.id
            ctlist.append(ctd)

        self.prepared_data['contact_types'] = ctlist

        
        if obj.terms:
            term = {}
            term['id'] = obj.terms.id
            term['term'] = obj.terms.term
            self.prepared_data['terms'] = term
        else:
            self.prepared_data['terms'] = None

        if obj.shipping_method:
            sm = {}
            sm['id'] = obj.shipping_method.id
            sm['method'] = obj.shipping_method.delivery_choice
            self.prepared_data['shipping_method'] = sm
        else:
            self.prepared_data['shipping_method'] = None

        if obj.currency:
            cr = {}
            cr['id'] = obj.currency.id
            cr['method'] = obj.currency.currency
            self.prepared_data['currency'] = cr
        else:
            self.prepared_data['currency'] = None 

        return self.prepared_data

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()