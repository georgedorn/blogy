from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

    fieldsets = (
        (None, {'fields': (('title', 'slug'), 'text', 'tags')}),
        ('Publishing options', {'fields': (('public', 'author'),
                                    ('pub_date', 'last_updated'))})
    )

    list_display = ('title',)


admin.site.register(Post, PostAdmin)
