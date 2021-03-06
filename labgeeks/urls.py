from django.conf.urls.defaults import *
from django.views.generic.simple import redirect_to
import os
import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
                       # (r'^accounts/login/$', 'django.contrib.auth.views.login'),
                       (r'^login/$', 'labgeeks.views.labgeeks_login'),
                       (r'^logout/$', 'labgeeks.views.labgeeks_logout'),
                       (r'^inactive/$', 'labgeeks.views.inactive'),
                       # Example:
                       # (r'^labgeeksrpg/', include('labgeeksrpg.foo.urls')),
                       (r'^chronos/', include('labgeeks_chronos.urls')),
                       (r'^people/', include('labgeeks_people.urls')),
                       (r'^schedule/', include('labgeeks_horae.urls')),
                       (r'^$', redirect_to, {'url': 'chronos/'}),
                       (r'^badger/', include('badger.urls')),
                       # Uncomment the admin/doc line below and add 'django.contrib.admindocs'
                       # to INSTALLED_APPS to enable admin documentation:
                       # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       # Uncomment the next line to enable the admin:
                       (r'^admin/', include(admin.site.urls)),
                       )

# only serve static files through the django server if debug is enabled. Only for development instances.
if settings.DEBUG:
    urlpatterns += patterns('',
                            (r'^uploads/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
                            )
