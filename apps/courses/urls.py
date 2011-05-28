from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('courses.views',
    url(r'^signup/$', 'signup', name='course_signup'),
    #url(r'^(?P<slug>[-\w]+)/$', 'detail',
    #    name='course_detail'
)