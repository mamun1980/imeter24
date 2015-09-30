import datetime
from haystack import indexes
from inventory.models import Item
from contacts.models import ContactPhone, ContactEmailAddress


class ItemIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    item_number = indexes.CharField(model_attr='item_number', boost=1.5)
    description = indexes.CharField(model_attr='description')
    primary_supplier = indexes.CharField(model_attr='primary_supplier__contact_name', indexed=False, null=True)
    last_PO = indexes.CharField(model_attr='last_PO', indexed=False, null=True)
    terms = indexes.CharField(model_attr='terms__term', indexed=False, null=True)
    quantity_on_hand = indexes.CharField(model_attr='quantity_on_hand', indexed=False, null=True)
    max_single_order_qty = indexes.CharField(model_attr='max_single_order_qty', indexed=False, null=True)
    max_order_qty_remains = indexes.CharField(model_attr='max_order_qty_remains', indexed=False, null=True)
    max_order_qty = indexes.CharField(model_attr='max_order_qty', indexed=False, null=True)
    wholesale_cost = indexes.CharField(model_attr='wholesale_cost', indexed=False, null=True)
    item_unit_measure = indexes.CharField(model_attr='item_unit_measure__unit_name', indexed=False, null=True)
    item_unit_measure_id = indexes.CharField(model_attr='item_unit_measure__pk', indexed=False, null=True)
    currency = indexes.CharField(model_attr='currency__currency', indexed=False, null=True)
    warehouse_location = indexes.CharField(model_attr='warehouse_location__warehouse_location', indexed=False, null=True)
    production_type = indexes.CharField(model_attr='production_type__production_type_name', indexed=False, null=True)

    def get_model(self):
        return Item


    def prepare(self, obj):
        self.prepared_data = super(ItemIndex, self).prepare(obj)
        currency = obj.currency
        terms = obj.terms
        if currency:
            self.prepared_data['currency'] = currency.currency
            self.prepared_data['currency_id'] = currency.id
        else:
            self.prepared_data['currency'] = None
            self.prepared_data['currency_id'] = None

        if terms:
            self.prepared_data['terms'] = terms.term
            self.prepared_data['terms_id'] = terms.id
        else:
            self.prepared_data['terms'] = None
            self.prepared_data['terms_id'] = None

        self.prepared_data['order_restriction'] = obj.order_restriction
        self.prepared_data['quantity_on_order'] = obj.quantity_on_order
        self.prepared_data['qty_on_request'] = obj.qty_on_request
        self.prepared_data['hst_taxable'] = obj.hst_taxable
        self.prepared_data['pst_taxable'] = obj.pst_taxable

        
        supplier = obj.primary_supplier
        supplier_doc = {}
        if supplier:
            supplier_profile = obj.primary_supplier.contactprofile
            if supplier_profile:
                if supplier_profile.fob:
                    supplier_doc['fob'] = supplier_profile.fob
                if supplier_profile.terms:
                    supplier_doc['terms'] = supplier_profile.terms.term
                    supplier_doc['term_id'] = supplier_profile.terms.id
                if supplier_profile.shipping_method:
                    supplier_doc['shipvia'] = supplier_profile.shipping_method.delivery_choice
                    supplier_doc['shipvia_id'] = supplier_profile.shipping_method.id
            supplier_doc['hst_tax'] = supplier_profile.hst_tax_exempt
            supplier_doc['pst_tax'] = supplier_profile.pst_tax_exempt
        
            supplier_doc['contact_name'] = supplier.contact_name
        
            supplier_doc['id'] = supplier.pk
            supplier_doc['address_1'] = supplier.address_1
            supplier_doc['attention_to'] = supplier.attention_to
            supplier_doc['city'] = supplier.city
            supplier_doc['province'] = supplier.province
            supplier_doc['country'] = supplier.country
            supplier_doc['postal_code'] = supplier.postal_code
            supplier_doc['postal_code'] = supplier.postal_code
            supplier_doc['postal_code'] = supplier.postal_code
            supplier_doc['postal_code'] = supplier.postal_code

        

            supplier_doc['phones'] = []
            phones = ContactPhone.objects.filter(contact=supplier)
            for cphone in phones:
                phone = {}
                phone['type'] = cphone.phone_type.phone_type
                phone['number'] = cphone.phone
                phone['phone_ext'] = cphone.phone_ext
                supplier_doc['phones'].append(phone)

            supplier_doc['emails'] = []
            cemails = ContactEmailAddress.objects.filter(contact=supplier)

            for cemail in cemails:
                email = {}
                email['email_address_type'] = cemail.email_address_type.email_type
                email['email_address'] = cemail.email_address
                supplier_doc['emails'].append(email)

        

        self.prepared_data['supplier'] = supplier_doc
        

        return self.prepared_data


    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()

    # def prepare_department(self, obj):
    #     if obj.department:
    #         return obj.department.name
    #     else:
    #         return 'None'

    # def prepare_item_unit_measure(self, obj):
    #     if obj.item_unit_measure:
    #         return obj.item_unit_measure.unit_name
    #     else:
    #         return 'None'

    # def prepare_currency(self, obj):
    #     if obj.currency:
    #         return obj.currency.currency
    #     else:
    #         return 'None'

    # def prepare_warehouse_location(self, obj):
    #     if obj.warehouse_location:
    #         return obj.warehouse_location.warehouse_location
    #     else:
    #         return 'None'

    # def prepare_production_type(self, obj):
    #     if obj.production_type:
    #         return obj.production_type.production_type_name
    #     else:
    #         return 'None'

    