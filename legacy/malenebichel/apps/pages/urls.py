from django.conf.urls import patterns, url

urlpatterns = patterns('pages.views',
    url(r'^(?P<parent_slug>[-\w]+)/(?P<child_slug>[-\w]+)/$', 'legacy_page_detail'),
    url(r'^(?P<slug>[-\w]+)/$', 'page_detail',
        name='page_detail'
    )
)