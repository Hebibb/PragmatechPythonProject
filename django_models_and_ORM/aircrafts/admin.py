from django.contrib import admin
from . models import Aircraft,Airliner
# Register your models here.
@admin.register(Aircraft,Airliner)
class AircraftAdmin(admin.ModelAdmin):
    exclude=('about',)
class AirlinerAdmin(admin.ModelAdmin):
    fields=('bio',)
# admin.site.register(Aircraft)
# admin.site.register(Airliner)