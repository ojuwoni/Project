from django.contrib import admin
# Register your models here.
from django.contrib import admin
from .models import UserProfile


#class RegistrationAdmin(admin.ModelAdmin):
#    list_display = ('birth_name', 'last_name', 'first_name')

admin.site.register(UserProfile)
#admin.site.register(Naissances)
