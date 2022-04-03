from django.contrib import admin
from . models import Account
# Register your models here.
from django.contrib.auth import get_user_model
User=get_user_model()
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display=('username','email')
    search_fields=('email','username')
@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    fields=('firstname','lastname','email','phone_number','image')
    list_display=('firstname','lastname','email','phone_number','image')
    search_fields=('firstname',)
    list_display_links=('firstname',)
    empty_value_display=('blank',)