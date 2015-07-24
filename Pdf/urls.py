from django.conf.urls import patterns, include, url

urlpatterns = patterns('Pdf.views',
	url(r'^pdf_show/(.*?)/$','pdf_show'),
	url(r'^upload_pdf/$', 'upload_pdf'),
	url(r'^pdf_search/$', 'pdf_search'),	
)

