from django.contrib import admin
from .models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'author', 'comment')
    list_filter = ("author",)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'body')
    list_filter = ("author",)


admin.site.register(Post)
admin.site.register(Comment)
