from django.conf.urls import patterns, include, url

urlpatterns = patterns('User.views',
	url(r'^register/$', 'register'),
	url(r'^login/$', 'login'),
	url(r'^profile/$', 'profile'),
	url(r'^update/$', 'update'),
	url(r'^logout/$', 'logout'),
	
)
