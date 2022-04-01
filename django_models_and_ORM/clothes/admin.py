from django.contrib import admin
from . models import Cl_company,Cloth,Cl_type,Tax_Office,Store
# Register your models here.
@admin.register(Cloth)
class ClothAdmin(admin.ModelAdmin):
    def company_name(self,obj):
        return obj.company.name #to intercept relational fields through overwriting them
    def clothing_types(self,obj):
        return obj.cl_type.name
#if inputs are more you can show them in fieldsets
    list_display=('company_name','cl_type','size','price','rating','genders')
  
    list_display_links=('company_name','size',)
   
    empty_value_display='blank'

    fieldsets=(('Main Parts',
                {'fields': ('company','cl_type','stores')}
                ),
               ('Individual Features',
                {'fields': ('genders','info','size')}
                ),
               ('Numeric parts',
                {'fields': ('price','rating')})
               )
@admin.register(Tax_Office)
class Tax_OfficeAdmin(admin.ModelAdmin):
    fields=('address','TIN')
  
@admin.register(Cl_company)
class Cl_companyAdmin(admin.ModelAdmin):
    def tax_id_num(self,obj):
        return obj.TIN
    list_display=('name','city_address','tax_id_num')
    search_fields=('name','city_address',)
@admin.register(Cl_type)
class Cl_typeAdmin(admin.ModelAdmin):
    fields=('name','about')
    list_display=('name',
                  )

@admin.register(Store)
class  StoreAdmin(admin.ModelAdmin):
    search_fields=('title',)
    fields=('title','address','link')
    list_display=('title','address','link')






