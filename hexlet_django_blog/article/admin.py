from django.contrib import admin
from .models import Article
from django.contrib.admin import DateFieldListFilter, AllValuesFieldListFilter

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    search_fields = ['name', 'body']
    search_fields = ('name', 'timestamp')
    list_filter = (('timestamp', DateFieldListFilter), ('name', AllValuesFieldListFilter))
