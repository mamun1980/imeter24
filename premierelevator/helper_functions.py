from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

def get_permissions():
    apps = ['inventory', 'auth', 'contacts', 'scomuser', 'schedule', 'report', 'events']
    all_permissions = []
    for app in apps:
        parm_obj = {}

        content_types = ContentType.objects.filter(app_label=app)
        for content_type in content_types:
            permissions = Permission.objects.filter(content_type=content_type)
            # parm_obj['app_label'] = app
            # parm_obj['permissions'] = permissions
            all_permissions.extend(permissions)

    return all_permissions