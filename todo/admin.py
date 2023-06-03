from django.contrib import admin
from .models import Todo, TodoCategory, TodoTag
# Register your models here.


class TodoAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'category',
        'title',
        'is_active',
        'user',
        'created_at',
        'updated_at',

    ]
    list_editable =[
        'is_active',
    ]
    list_display_links = [
        'pk',
        'category',
        'title'
    ]

class TodoCategoryAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'slug',
        'is_active'
    ]
    list_display_links = [
        'slug',
        'title',
    ]
    list_editable =[
        'is_active',
    ]





admin.site.register(Todo, TodoAdmin)
admin.site.register(TodoCategory, TodoCategoryAdmin)
admin.site.register(TodoTag)