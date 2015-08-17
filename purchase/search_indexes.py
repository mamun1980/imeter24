import datetime
from haystack import indexes
from purchase.models import PurchaseOrder, ShippingList, PackingList


class PurchaseOrderIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    po_number = indexes.CharField(model_attr='po_number', boost=2)
    # po_status = indexes.CharField(model_attr='po_status', indexed=False, null=True)
    supplier = indexes.CharField(model_attr='supplier__contact_name', null=True)
    terms = indexes.CharField(model_attr='terms__term',  null=True)
    shipping_inst = indexes.CharField(model_attr='shipping_inst', null=True)

    def get_model(self):
        return PurchaseOrder

    def prepare(self, obj):
        self.prepared_data = super(PurchaseOrderIndex, self).prepare(obj)
        
        self.prepared_data['po_status'] = obj.status_verbose
        return self.prepared_data

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()


class ShippingListIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    sl_number = indexes.CharField(model_attr='sl_number', boost=2)
    date_required = indexes.CharField(model_attr='date_required', indexed=False, null=True)
    job_number = indexes.CharField(model_attr='job_number__job_number', indexed=False, null=True)

    def get_model(self):
        return ShippingList

    def prepare(self, obj):
        self.prepared_data = super(ShippingListIndex, self).prepare(obj)
        sold_to = obj.sold_to
        if sold_to:
            sold_to_dict = {}
            sold_to_dict['id'] = sold_to.id
            sold_to_dict['contact_name'] = sold_to.contact_name
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
        # ============= Ship To =================
        ship_to = obj.ship_to
        if ship_to:
            ship_to_dict = {}
            ship_to_dict['id'] = ship_to.id
            ship_to_dict['contact_name'] = ship_to.contact_name
            phones = ship_to.contact_phone.all()
            phs = []
            for ph in phones:
                phone = {}
                phone['number'] = ph.phone
                phone['ext'] = ph.phone_ext
                phone['type'] = ph.phone_type.phone_type
                phs.append(phone)
            ship_to_dict['phones'] = phs
            emails = ship_to.contact_emails.all()
            elist = []
            for em in emails:
                email = {}
                email['email_type'] = em.email_address_type.email_type
                email['email_address'] = em.email_address
                elist.append(email)

            ship_to_dict['emails'] = elist

            self.prepared_data['ship_to'] = ship_to_dict
        return self.prepared_data

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()


class PackingListIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    pl_number = indexes.CharField(model_attr='pl_number', boost=2)
    date_issued = indexes.CharField(model_attr='date_issued', indexed=False, null=True)
    job_number = indexes.CharField(model_attr='job_number__job_number', indexed=False, null=True)

    def get_model(self):
        return PackingList

    def prepare(self, obj):
        self.prepared_data = super(PackingListIndex, self).prepare(obj)
        sold_to = obj.sold_to
        if obj.sold_to:
            sold_to_dict = {}
            sold_to_dict['contact_name'] = sold_to.contact_name
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
        # ============= Ship To =================
        if obj.ship_to:
            ship_to = obj.ship_to
            ship_to_dict = {}
            ship_to_dict['contact_name'] = ship_to.contact_name
            phones = ship_to.contact_phone.all()
            phs = []
            for ph in phones:
                phone = {}
                phone['number'] = ph.phone
                phone['ext'] = ph.phone_ext
                phone['type'] = ph.phone_type.phone_type
                phs.append(phone)
            ship_to_dict['phones'] = phs
            emails = ship_to.contact_emails.all()
            elist = []
            for em in emails:
                email = {}
                email['email_type'] = em.email_address_type.email_type
                email['email_address'] = em.email_address
                elist.append(email)

            ship_to_dict['emails'] = elist

            self.prepared_data['ship_to'] = ship_to_dict
        self.prepared_data['status'] = obj.status_verbose()
        self.prepared_data['date_shipped'] = obj.date_shipped
        return self.prepared_data

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()


