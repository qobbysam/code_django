
from django.conf.urls import patterns, include, url


urlpatterns= patterns(
	'',
	url(r'^$', 'clients.views.firstvw', name = "firstvw"),
	url(r'^ad/', 'clients.views.myadmin', name="myadmin"),
	
	)


