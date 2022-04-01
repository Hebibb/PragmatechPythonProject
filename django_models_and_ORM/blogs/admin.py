from django.contrib import admin
from . models import Blog,Author

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display=('author','title','price','published','image',)
    empty_value_display='blank'
    list_filter=('author',)
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    exclude=('about',)



# admin.site.register(Blog)
# admin.site.register(Author)


