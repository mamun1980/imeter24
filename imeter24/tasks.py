from __future__ import absolute_import

from celery import shared_task
from django.core.management import call_command

@shared_task
def run_update_index():
	print "From celery task"
	call_command('update_index')



@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)