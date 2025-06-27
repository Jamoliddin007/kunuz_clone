from django.contrib import admin
from news.models import Category, News

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created_at", "updated_at")
    search_fields = ("name",)

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "slug", "is_published", "created_at")
    list_filter = ("is_published", "category")
    search_fields = ("title", "body")
    prepopulated_fields = {"slug": ("title",)}
