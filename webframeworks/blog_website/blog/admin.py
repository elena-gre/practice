from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'status', 'when_created']
    list_filter = ['status', 'author']
    search_fields = ['title']
    date_hierarchy = 'when_created'
    ordering = ['status', 'when_created']
