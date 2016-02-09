from django.contrib import admin
from schedule.models import *
# Register your models here.

admin.site.register(Job)
admin.site.register(Comment)
admin.site.register(JobStatus)
admin.site.register(JobControl)