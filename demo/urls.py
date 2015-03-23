from django.conf.urls import patterns, include, url
from django.contrib import admin
from oscar.app import application

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'artlor.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'', include(application.urls)),

    url(r'^admin/', include(admin.site.urls)),
)
