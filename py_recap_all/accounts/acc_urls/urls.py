
from django.urls import path,include


urlpatterns = [

    path('blogs/',include('blogs.blog_urls.urls'))
]
