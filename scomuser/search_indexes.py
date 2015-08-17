import datetime
from haystack import indexes
from django.contrib.auth.models import User


class UserIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    uid = indexes.IntegerField(model_attr='id')
    username = indexes.CharField(model_attr='username', boost=2)
    first_name = indexes.CharField(model_attr='first_name', null=True)
    last_name = indexes.CharField(model_attr='last_name', null=True)
    email = indexes.CharField(model_attr='email', null=True)
    is_superuser = indexes.CharField(model_attr='is_superuser')
    last_login = indexes.CharField(model_attr='last_login', indexed=False)
    
    def get_model(self):
        return User
    # phones = indexes.MultiValueField(indexed=False, null=True)
    # search_string = indexes.NgramField(model_attr='search_string')
