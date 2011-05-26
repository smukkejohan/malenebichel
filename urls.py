from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^a/doc/', include('django.contrib.admindocs.urls')),
    url(r'^a/', include(admin.site.urls)),



    url(r'^$', 'views.index', name='index'),

    url(r'^', include('courses.urls')),
    url(r'^', include('pages.urls')),
)