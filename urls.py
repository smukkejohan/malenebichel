from django.conf.urls.defaults import patterns, include, url

from django.contrib import admin
import settings

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^a/doc/', include('django.contrib.admindocs.urls')),
    url(r'^a/', include(admin.site.urls)),

    url(r'^recommendations/$', 'praise.views.index', name='praises'),

    url(r'^$', 'views.index', name='index'),

    url(r'^c/', include('courses.urls')),
    
    url(r'^', include('pages.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('django.views.static',
    (r'^media/(?P<path>.*)$',
        'serve', {
        'document_root': settings.MEDIA_ROOT,
        'show_indexes': True }),)