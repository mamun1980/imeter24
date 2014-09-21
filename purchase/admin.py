from django.contrib import admin
from purchase.models import *
# Register your models here.

admin.site.register(PurchaseItem)
admin.site.register(PurchaseOrder)
admin.site.register(PurchaseRequest)
admin.site.register(PurchaseRequestComment)
admin.site.register(POStatus)
admin.site.register(POContact)
admin.site.register(ReceivedItemHistory)
admin.site.register(PackingList)
admin.site.register(PackingItem)