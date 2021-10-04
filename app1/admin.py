from django.contrib import admin

# Register your models here.
from app1.models import Registration

class AdminRegistration(admin.ModelAdmin):
    list_display = ['firstname', 'lastname', 'email', 'password', 'mobile', 'gender']

admin.site.register(Registration, AdminRegistration)