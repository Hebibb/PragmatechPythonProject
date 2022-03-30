from django.contrib import admin
from . models import Cl_company,Cloth,Cl_type
# Register your models here.
admin.site.register(Cl_company)
admin.site.register(Cloth)
admin.site.register(Cl_type)