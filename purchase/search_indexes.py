import datetime
from haystack import indexes
from purchase.models import PurchaseOrder


class PurchaseOrderIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    po_number = indexes.CharField(model_attr='po_number', boost=2)
    po_status = indexes.CharField(model_attr='po_status', indexed=False, null=True)
    supplier = indexes.CharField(model_attr='supplier__contact_name', null=True)
    terms = indexes.CharField(model_attr='terms__term',  null=True)
    shipping_inst = indexes.CharField(model_attr='shipping_inst', null=True)

    def get_model(self):
        return PurchaseOrder

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()