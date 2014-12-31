from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^blogs/index/$','blogs.views.index'),
    url(r'^blogs/index$','blogs.views.index'),
    #url(r'^blogs/index/\d{2}$',index),
    url(r'^blogs/index/(?P<id>\d+)/$','blogs.views.index'),
    url(r'^blogs/index1/(?P<id>\d+)/$','blogs.views.index1'),
    url(r'^blogs/index2/(?P<id>\d+)/$','blogs.views.index2'),
)
