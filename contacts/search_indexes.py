import datetime
from haystack import indexes
from contacts.models import Contact


class ContactIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    contact_name = indexes.CharField(model_attr='contact_name', boost=1.125)
    city = indexes.CharField(model_attr='city')
    province = indexes.CharField(model_attr='province')
    address_1 = indexes.CharField(model_attr='address_1')
    attention_to = indexes.CharField(model_attr='attention_to')
    content_auto = indexes.EdgeNgramField(model_attr='contact_name')

    def get_model(self):
        return Contact

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()