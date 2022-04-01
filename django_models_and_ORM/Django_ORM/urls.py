"""Django_ORM URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blogs.views import blogs
from aircrafts.views import air
from django.conf.urls.static import static
from django.conf import settings

admin.site.site_header='welcOme_tO_Habib_s__'
admin.site.site_title='Welcome!!'
admin.site.site_index='10001101011'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('homepage', blogs, name='home' ),
    path('airliners/', air, name='airline' )
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)#modelleri yazmaq ucun bu settingsi de urle elave etmek lazimdi.
