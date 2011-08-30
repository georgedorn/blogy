from django.core.urlresolvers import reverse_lazy
from django.utils.feedgenerator import Atom1Feed
from django.views.generic.list import ListView
from django.views.generic.dates import DateDetailView

from django.contrib.comments.models import Comment
from django.contrib.sites.models import Site
from django.contrib.syndication.views import Feed

from taggit.models import Tag

from .models import Post


class ContextMixin(object):
    def get_context_data(self, **kwargs):
        c = super(ContextMixin, self).get_context_data(**kwargs)
        c['global_tags'] = Tag.objects.all()
        return c


class PostIndex(ContextMixin, ListView):
    def get_queryset(self):
        qs = Post.published.order_by('-pub_date')
        if 'tag' in self.kwargs:
            qs = qs.filter(tags__slug = self.kwargs['tag'])
        qs = qs.all()
        return qs


index = PostIndex.as_view()


class PostDetail(ContextMixin, DateDetailView):
    queryset=Post.published.all()
    date_field='pub_date'
    month_format='%m'


detail = PostDetail.as_view()


class PostFeed(Feed):
    feed_type = Atom1Feed

    title = Site.objects.get_current().name
    link = reverse_lazy('blogy:index')

    def get_object(self, request, tag=None):
        if tag:
            return Tag.objects.get(slug=tag)

    def items(self, obj):
        posts = Post.published.order_by('-pub_date')
        if obj:
            posts = posts.filter(tags = obj)
        return posts[:5]

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.text


feed = PostFeed()


class CommentFeed(Feed):
    feed_type = Atom1Feed

    title = Site.objects.get_current().name
    link = reverse_lazy('blogy:index')

    def get_object(self, request, post=None):
        if post:
            return Post.objects.get(pk=post)

    def items(self, obj):
        if obj:
            comments = Comment.objects.for_model(obj)
        else:
            comments = Comment.objects.all()
        return comments.order_by('-submit_date')[:10]

    def item_title(self, item):
        return u'Comment from %s at %s' % (item.name, item.submit_date)

    def item_description(self, item):
        return item.comment


comment_feed = CommentFeed()
