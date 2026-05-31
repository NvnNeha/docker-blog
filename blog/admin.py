from django.contrib import admin
from .models import Post, Comment, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "user", "created_at")
    search_fields = ("title", "content")
    list_filter = ("tags",)


admin.site.register(Comment)
admin.site.register(Tag)
