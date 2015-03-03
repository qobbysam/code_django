from django.conf.urls import patterns, include, url
from django.contrib import admin
from clients import urls
from django.views.generic import TemplateView
# from rest_framework.authtoken.views import obtain_auth_token
# from clients.urls import router

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'client.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^firstview/', include('clients.urls')),
    url(r'^myadmin/', include('clients.urls')),
    # url(r'^api/token',obtain_auth_token, name = 'api-token'),
    # url(r'api/', include(router.urls)),
    # url(r'^$', TemplateView.as_view(template_name='home.html'))
    url (r'^$', 'clients.views.home'),
    url (r'^loginU/', 'clients.views.loginU')
)
