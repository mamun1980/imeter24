from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

def get_permissions():
    apps = ['inventory', 'auth', 'contacts', 'scomuser', 'schedule', 'report', 'events', 'purchase']
    all_permissions = []
    # import pdb; pdb.set_trace()
    for app in apps:
        parm_obj = {}
        parm_obj['app_label'] = app
        parm_obj['content_type'] = []
        content_types = ContentType.objects.filter(app_label=app)
        for content_type in content_types:
            content = {}
            content['name'] = content_type.name
            content['permissions'] = []
            permissions = Permission.objects.filter(content_type=content_type)
            content['permissions'].extend(permissions)
            parm_obj['content_type'].append(content)
        
        all_permissions.append(parm_obj)

    return all_permissions
