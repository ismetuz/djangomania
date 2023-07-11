from django.contrib import admin
from .models import BlogCategory, BlogTag, Post


@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'is_active'
    ]

@admin.register(BlogTag)
class BlogTagAdmin(admin.ModelAdmin):
    pass
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'is_active'
    ]
