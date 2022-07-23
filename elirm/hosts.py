from django.conf import settings
from django_hosts import patterns, host

host_patterns = patterns('',
    host('www', settings.ROOT_URLCONF, name='www'),
    host('api', 'api.urls', name='api'),
) 
