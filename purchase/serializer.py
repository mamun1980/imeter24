from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer, Field
from purchase.models import *
from contacts.models import Contact
from schedule.models import Job
from django.contrib.auth.models import User
from inventory.models import Item

class ShippingListSerializer(ModelSerializer):
    class Meta:
        model = ShippingList

class ContactSerializer(ModelSerializer):
    class Meta:
        model = Contact

class JobSerializer(ModelSerializer):

    class Meta:
        model = Job

class UserSerializer(ModelSerializer):

    class Meta:
        model = User

class ShippingItemSerializer(ModelSerializer):
    item = Field(source="item.item_number")
    class Meta:
        model = ShippingItem

class ReversePackingItemSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = PackingItem
        fields = ('id', 'description', 'unit', 'qty_ordered', 'qty_bo', 'qty_shipped',)

class PackingListSerializer(ModelSerializer):
    sl = ShippingListSerializer()
    sold_to = ContactSerializer()
    ship_to = ContactSerializer()
    shipped_by = UserSerializer()
    job_number = JobSerializer()
    generated_by = UserSerializer()
    customer_broker = ContactSerializer()
    pl_items = ReversePackingItemSerializer(many=True, read_only=True)

    class Meta:
        model = PackingList