from django.contrib import admin

# Register your models here.

from .models import ContactList
 
@admin.register(ContactList)
class RequestDemoAdmin(admin.ModelAdmin):
  list_display = ['name', 'email', 'phone_no']