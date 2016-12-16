from django.conf import settings
from django_hosts import patterns, host

host_patterns = patterns('',
    host(r'www', settings.ROOT_URLCONF, name='www'),
    host(r'(?!www).*', 'dock.hostsconf.urls', name='wildcard'),
)


'''
from dock.hostsconf import urls
host_patterns = [
    host(r'www', settings.ROOT_URLCONF, name='www'),
    host(r'(?!www).*', 'dock.hostsconf.urls', name='wildcard'),
]
'''