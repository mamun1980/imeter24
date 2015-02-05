import datetime
from haystack import indexes
from schedule.models import Job


class JobIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
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