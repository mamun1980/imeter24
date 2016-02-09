import datetime
from haystack import indexes
from events.models import Events


class EventsIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    eventid = indexes.IntegerField(model_attr='eventid')
    name = indexes.CharField(model_attr='name', null=True)
    doorname = indexes.CharField(model_attr='doorname', null=True)
    cardnumber = indexes.CharField(model_attr='cardnumber', null=True)
    zonename = indexes.CharField(model_attr='zonename', null=True)
    
    def get_model(self):
        return Events
    # phones = indexes.MultiValueField(indexed=False, null=True)
    # search_string = indexes.NgramField(model_attr='search_string')
