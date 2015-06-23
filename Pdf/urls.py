from django.conf.urls import patterns, include, url

urlpatterns = patterns('Pdf.views',
	url(r'^show/$', 'show'),
	
)
