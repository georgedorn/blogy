from django.contrib.auth.models import User
from django.db import models

from taggit.managers import TaggableManager


class PostManager(models.Manager):
    def get_query_set(self):
        return super(PostManager, self).get_query_set().filter(public = True)


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.PROTECT)

    title = models.CharField(max_length=255)
    slug = models.SlugField()

    text = models.TextField()

    pub_date = models.DateTimeField()
    last_updated = models.DateTimeField(auto_now=True)

    public = models.BooleanField()

    tags = TaggableManager()

    objects = models.Manager()
    published = PostManager()

    def __unicode__(self):
        return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('blogy:detail', (), {
            'year': self.pub_date.year,
            'month': self.pub_date.month,
            'day': self.pub_date.day,
            'slug': self.slug})
