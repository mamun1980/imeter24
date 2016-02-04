from django.db.models.signals import post_syncdb
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import models as auth_models
from django.contrib.auth.models import Permission

def add_user_permissions(sender, **kwargs):
	
	ct = ContentType.objects.get(app_label='auth', model='user')
	ctg = ContentType.objects.get(app_label='auth', model='group')
	perm, created = Permission.objects.get_or_create(codename='can_view_user', name='Can View Users', content_type=ct)
	p2, c2 = Permission.objects.get_or_create(codename='view_utility', name='Can View Utility', content_type=ct)
	pe, cre = Permission.objects.get_or_create(codename='can_view_group', name='Can View Groups', content_type=ctg)
	pe2, cre2 = Permission.objects.get_or_create(codename='can_change_password', name='Can Change User Password', content_type=ct)

post_syncdb.connect(add_user_permissions, sender=auth_models)
