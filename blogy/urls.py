from django.conf.urls.defaults import patterns, include, url

from .utils import rst_directive

blogy_urlpatterns = patterns('blogy.views',
    url('^$', 'index', name='index'),
    url('^tag/(?P<tag>[\w-]+)/$', 'index', name='tag'),

    url('^feed/comments/$', 'comment_feed', name='comment_feed'),
    url('^feed/comments/(?P<post>\d+)/$', 'comment_feed', name='post_feed'),

    url('^feed/$', 'feed', name='feed'),
    url('^feed/(?P<tag>[\w-]+)/$', 'feed', name='tag_feed'),

    url('^(?P<year>\d{4})/(?P<month>\d|1\d)/(?P<day>\d|(?:[123]\d))/(?P<slug>[\w-]+)/$',
        'detail', name='detail'),
)

urlpatterns = patterns('',
    url('^comments/', include('django.contrib.comments.urls')),
    url('^', include((blogy_urlpatterns, 'blogy', 'blogy'))),
)
