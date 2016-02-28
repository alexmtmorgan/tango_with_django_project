# At the top of your urls.py file, add the following line:
from django.conf import settings

from django.conf.urls import patterns, include, url
from django.contrib import admin

from registration.backends.simple.views import RegistrationView


# Create a new class that redirects the user to the index page, if successful at logging
class MyRegistrationView(RegistrationView):
    def get_success_url(self, request, user):
        return '/rango/'

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'tango_with_django_project_17.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^rango/', include('rango.urls')),
                       url(r'^accounts/', include('registration.backends.simple.urls')),
                       url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
                       )

# UNDERNEATH your urlpatterns definition, add the following two lines:
if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
         'serve',
         {'document_root': settings.MEDIA_ROOT}), )
