import datetime
from haystack import indexes
from purchase.models import PurchaseOrder, ShippingList, PackingList, PurchaseItem, POContact


class PurchaseOrderIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    po_number = indexes.CharField(model_attr='po_number', boost=2)
    po_status = indexes.CharField(model_attr='po_status', indexed=False, null=True)
    # supplier = indexes.CharField(model_attr='supplier__contact_name', null=True)
    terms = indexes.CharField(model_attr='terms__term',  null=True)
    shipping_inst = indexes.CharField(model_attr='shipping_inst', null=True)
    hst_taxable = indexes.CharField(model_attr='hst_taxable', null=True)
    hst_taxable_amount = indexes.CharField(model_attr='hst_taxable_amount', null=True)
    total_hst_tax = indexes.CharField(model_attr='total_hst_tax', null=True)
    pst_taxable = indexes.CharField(model_attr='pst_taxable', null=True)
    pst_taxable_amount = indexes.CharField(model_attr='pst_taxable_amount', null=True)
    total_pst_tax = indexes.CharField(model_attr='total_pst_tax', null=True)
    total_tax = indexes.CharField(model_attr='total_tax', null=True)

    def get_model(self):
        return PurchaseOrder

    def prepare(self, obj):
        self.prepared_data = super(PurchaseOrderIndex, self).prepare(obj)
        supplier = obj.supplier
        supplier_dict = {}
        if supplier:
            supplier_dict['id'] = supplier.id
            supplier_dict['contact_name'] = supplier.contact_name
            supplier_dict['attention_to'] = supplier.attention_to
            supplier_dict['address_1'] = supplier.address_1
            supplier_dict['address_2'] = supplier.address_2
            supplier_dict['city'] = supplier.city
            supplier_dict['province'] = supplier.province
            supplier_dict['country'] = supplier.country
            supplier_dict['postal_code'] = supplier.postal_code
            phones = supplier.contact_phone.all()
            phs = []
            for ph in phones:
                phone = {}
                phone['number'] = ph.phone
                phone['ext'] = ph.phone_ext
                phone['type'] = ph.phone_type.phone_type
                phs.append(phone)
            supplier_dict['phones'] = phs
            emails = supplier.contact_emails.all()
            elist = []
            for em in emails:
                email = {}
                email['email_type'] = em.email_address_type.email_type
                email['email_address'] = em.email_address
                elist.append(email)

            supplier_dict['emails'] = elist

            self.prepared_data['supplier'] = supplier_dict
        else:
            self.prepared_data['supplier'] = supplier_dict

        items = PurchaseItem.objects.filter(po=obj)
        item_list = []
        if items:
            for item in items:
                item_dic = {}
                item_dic['item_number'] = item.item.item_number
                item_dic['description'] = item.item.description
                item_dic['qty_ordered'] = item.qty
                item_dic['item_recv'] = item.item_recv
                item_dic['sub_total'] = item.sub_total

                item_list.append(item_dic)

        self.prepared_data['po_items'] = item_list

        extra_contacts = POContact.objects.filter(purchase_order=obj)
        ec_list = []
        if extra_contacts:
            for ec in extra_contacts:
                ex_con = {}
                ex_con['id'] = ec.pk
                ex_con['contact_type'] = ec.contact_type
                ex_con['contact'] = ec.contact
                ex_con['contact_name'] = ec.contact_name
                ec_list.append(ex_con)
        self.prepared_data['extra_contacts'] = ec_list


        # self.prepared_data['po_status'] = obj.po_status
        return self.prepared_data

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()


class ShippingListIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    sl_number = indexes.CharField(model_attr='sl_number', boost=2)
    date_required = indexes.CharField(model_attr='date_required', indexed=False, null=True)
    ordered_date = indexes.DateField(model_attr='ordered_date', indexed=False, null=True)
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
        # ============= Ship To =================
        ship_to = obj.ship_to
        if ship_to:
            ship_to_dict = {}
            ship_to_dict['id'] = ship_to.id
            ship_to_dict['contact_name'] = ship_to.contact_name
            ship_to_dict['attention_to'] = ship_to.attention_to
            ship_to_dict['address_1'] = ship_to.address_1
            ship_to_dict['address_2'] = ship_to.address_2
            ship_to_dict['city'] = ship_to.city
            ship_to_dict['province'] = ship_to.province
            ship_to_dict['country'] = ship_to.country
            ship_to_dict['postal_code'] = ship_to.postal_code
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
        # self.prepared_data['status'] = obj.status_verbose()
        self.prepared_data['date_shipped'] = obj.date_shipped
        return self.prepared_data

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()


