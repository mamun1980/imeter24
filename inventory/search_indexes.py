import datetime
from haystack import indexes
from inventory.models import Item


class ItemIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    item_number = indexes.CharField(model_attr='item_number', boost=1.125)
    description = indexes.CharField(model_attr='description')
    quantity_on_hand = indexes.CharField(model_attr='quantity_on_hand', indexed=False, null=True)
    department = indexes.CharField(model_attr='department', indexed=False, null=True)
    item_unit_measure = indexes.CharField(model_attr='item_unit_measure', indexed=False, null=True)
    currency = indexes.CharField(model_attr='currency', indexed=False, null=True)
    warehouse_location = indexes.CharField(model_attr='warehouse_location', indexed=False, null=True)
    production_type = indexes.CharField(model_attr='production_type', indexed=False, null=True)
    search_string = indexes.EdgeNgramField(model_attr='search_string')

    def get_model(self):
        return Item

    def prepare_department(self, obj):
    	if obj.department:
        	return "%s" % (obj.department.name)
        else:
        	return None

    def prepare_item_unit_measure(self, obj):
    	if obj.item_unit_measure:
        	return "%s" % (obj.item_unit_measure.unit_name)
        else:
        	return None

    def prepare_currency(self, obj):
    	if obj.currency:
        	return "%s" % (obj.currency.currency)
        else:
        	return None

    def prepare_warehouse_location(self, obj):
    	if obj.warehouse_location:
        	return "%s" % (obj.warehouse_location.warehouse_location)
        else:
        	return None

    def prepare_production_type(self, obj):
    	if obj.production_type:
        	return "%s" % (obj.production_type.production_type_name)
        else:
        	return None

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()