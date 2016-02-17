# At the top of your urls.py file, add the following line:
from django.conf import settings

from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'tango_with_django_project_17.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^rango/', include('rango.urls')),
                       )

# UNDERNEATH your urlpatterns definition, add the following two lines:
if settings.DEBUG:
    urlpatterns += patterns(
            'django.views.static',
            (r'^media/(?P<path>.*)',
             'serve',
             {'document_root': settings.MEDIA_ROOT}), )
