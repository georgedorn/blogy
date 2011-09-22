from django.contrib import admin
from django.db import models

from markitup.widgets import MarkItUpWidget

from .models import Post


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

    fieldsets = (
        (None, {'fields': (('title', 'slug'), 'text', 'tags')}),
        ('Publishing options', {'fields': (('public', 'author', 'pub_date'),)})
    )

    list_display = ('title',)

    formfield_overrides = {
        models.TextField: {'widget': MarkItUpWidget()}
    }

    class Media:
        css = {
            'all': ('blogy/css/admin.css',)
        }


admin.site.register(Post, PostAdmin)
