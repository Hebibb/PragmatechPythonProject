from django.contrib import admin
from . models import Blog

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display=('author','title','category_tag','date','image',)
    empty_value_display='blank'
    list_filter=('author','category_tag')


# Register your models here.
