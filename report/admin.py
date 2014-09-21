from django.contrib import admin
from report.models import *
# Register your models here.

admin.site.register(Printer)
admin.site.register(Report)
admin.site.register(RecuringReport)