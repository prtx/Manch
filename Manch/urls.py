from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    
	#url(r'^$', 'OnYourPoint.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    (r'^', include('User.urls')),
    #(r'^', include('Article.urls')),
    #(r'^', include('Social_Oauth.urls')),
	#(r'complete/twitter',include()
    #url(r'', include('social_auth.urls')),
)
