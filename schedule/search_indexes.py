import datetime
from haystack import indexes
from schedule.models import Job, JobControl
from contacts.models import ContactPhone, ContactEmailAddress


class JobIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    job_id = indexes.CharField(model_attr='id')
    job_number = indexes.CharField(model_attr='job_number', boost=2)
    cab_designation = indexes.CharField(model_attr='cab_designation', indexed=False, null=True)
    job_name = indexes.CharField(model_attr='job_name', indexed=False, null=True)
    customer_contact_name = indexes.CharField(model_attr='customer_contact_name', indexed=False,  null=True)
    address_1 = indexes.CharField(model_attr='address_1', indexed=False, null=True)
    customer_contact_phone_number = indexes.CharField(model_attr='customer_contact_phone_number', indexed=False,  null=True)
    po_number = indexes.CharField(model_attr='po_number', indexed=False,  null=True)
    # phones = indexes.MultiValueField(indexed=False, null=True)
    # search_string = indexes.NgramField(model_attr='search_string')

    def get_model(self):
        return Job

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()

class JobControlIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    job_number = indexes.CharField(model_attr='job_number', boost=2)
    job_name = indexes.CharField(model_attr='job_name', boost=2)
    # sold_to = indexes.CharField(model_attr='sold_to__contact_name', indexed=False, null=True)
    # ship_to = indexes.CharField(model_attr='ship_to__contact_name', indexed=False, null=True)
    elevetor_type = indexes.CharField(model_attr='elevetor_type__elevetor_type', indexed=False, null=True)
    number_of_cabs = indexes.IntegerField(model_attr='number_of_cabs', indexed=False, null=True)
    number_of_floors = indexes.IntegerField(model_attr='number_of_floors', indexed=False, null=True)
    front = indexes.CharField(model_attr='front', indexed=False, null=True)
    rear = indexes.CharField(model_attr='rear', indexed=False, null=True)
    rgw = indexes.CharField(model_attr='rgw', indexed=False, null=True)
    capacity = indexes.CharField(model_attr='capacity', indexed=False, null=True)
    customer_po_number = indexes.CharField(model_attr='customer_po_number', indexed=False, null=True)
    delivery_date = indexes.CharField(model_attr='delivery_date', indexed=False, null=True)
    start_date = indexes.CharField(model_attr='start_date', indexed=False, null=True)
    # installed_by = indexes.CharField(model_attr='installed_by__contact_name', indexed=False, null=True)
    estimated_price_for_job = indexes.CharField(model_attr='estimated_price_for_job', indexed=False, null=True)
    

    def get_model(self):
        return JobControl

    def prepare(self, obj):
        self.prepared_data = super(JobControlIndex, self).prepare(obj)
        
        sold_to_contact = obj.sold_to
        sold_dict = {}
        if sold_to_contact:
            # self.prepared_data['sold_to_id'] = sold_to_contact.id
            sold_dict['contact_name'] = sold_to_contact.contact_name
            sold_dict['city'] = sold_to_contact.city
            sold_dict['id'] = sold_to_contact.id
            phones = ContactPhone.objects.filter(contact=sold_to_contact)
            phs = []
            for ph in phones:
                phone = {}
                phone['number'] = ph.phone
                phone['ext'] = ph.phone_ext
                phone['type'] = ph.phone_type.phone_type
                phs.append(phone)

            sold_dict['phones'] = phs
            
            emails = ContactEmailAddress.objects.filter(contact=sold_to_contact)
            elist = []
            for em in emails:
                email = {}
                email['email_type'] = em.email_address_type.email_type
                email['email_address'] = em.email_address
                elist.append(email)

            sold_dict['emails'] = elist
        self.prepared_data['sold_to'] = sold_dict

        # =============== Ship To =================================
        
        ship_to_contact = obj.ship_to
        ship_dict = {}
        if ship_to_contact:
            # self.prepared_data['sold_to_id'] = sold_to_contact.id
            ship_dict['contact_name'] = ship_to_contact.contact_name
            ship_dict['city'] = ship_to_contact.city
            ship_dict['id'] = ship_to_contact.id
            phones = ContactPhone.objects.filter(contact=ship_to_contact)
            phs = []
            for ph in phones:
                phone = {}
                phone['number'] = ph.phone
                phone['ext'] = ph.phone_ext
                phone['type'] = ph.phone_type.phone_type
                phs.append(phone)

            ship_dict['phones'] = phs
            
            emails = ContactEmailAddress.objects.filter(contact=ship_to_contact)
            elist = []
            for em in emails:
                email = {}
                email['email_type'] = em.email_address_type.email_type
                email['email_address'] = em.email_address
                elist.append(email)

            ship_dict['emails'] = elist
        self.prepared_data['ship_to'] = ship_dict
        
        # ==================== Installed By =========================

        installed_by_contact = obj.installed_by
        installed_by_dict = {}
        if installed_by_contact:
            # self.prepared_data['sold_to_id'] = sold_to_contact.id
            installed_by_dict['contact_name'] = installed_by_contact.contact_name
            installed_by_dict['city'] = installed_by_contact.city
            installed_by_dict['id'] = installed_by_contact.id
            phones = ContactPhone.objects.filter(contact=installed_by_contact)
            phs = []
            for ph in phones:
                phone = {}
                phone['number'] = ph.phone
                phone['ext'] = ph.phone_ext
                phone['type'] = ph.phone_type.phone_type
                phs.append(phone)

            installed_by_dict['phones'] = phs
            
            emails = ContactEmailAddress.objects.filter(contact=installed_by_contact)
            elist = []
            for em in emails:
                email = {}
                email['email_type'] = em.email_address_type.email_type
                email['email_address'] = em.email_address
                elist.append(email)

            installed_by_dict['emails'] = elist
        self.prepared_data['installed_by'] = installed_by_dict
        
        return self.prepared_data

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()
