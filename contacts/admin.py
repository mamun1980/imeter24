from django.contrib import admin
from contacts.models import *
# Register your models here.

admin.site.register(Contact)
admin.site.register(ContactProfile)
admin.site.register(ContactPhone)
admin.site.register(PaymentTerm)
admin.site.register(DeliveryChoice)
admin.site.register(EmailAddressType)
admin.site.register(ContactEmailAddress)
admin.site.register(Comment)
