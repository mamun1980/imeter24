
def site_name(request):
	from django.conf import settings
	if settings.PROJECT_LINK == 'test.imeter24.com':
		site_name = 'Test Site'
	elif settings.PROJECT_LINK == 'www.imeter24.com':
		site_name = 'Live'
	else:
		site_name = 'localhost'

	return {'site_name': site_name}