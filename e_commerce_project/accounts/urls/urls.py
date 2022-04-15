from django.urls import path,re_path
from accounts.views import register,activate,signin
#you have to figure out how to add two 
urlpatterns = [
    path('login/',register, name='register'),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,33})/$',
            activate, name='activate'),
]