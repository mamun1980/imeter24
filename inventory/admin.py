from django.contrib import admin
from inventory.forms import *
# # Register your models here.
# class ItemAdmin(admin.ModelAdmin):
#     form = ItemForm

#     def __init__(self, model, admin_site):
#         super(ItemAdmin,self).__init__(model,admin_site)
#         self.form.admin_site = admin_site # capture the admin_site

admin.site.register(Item)