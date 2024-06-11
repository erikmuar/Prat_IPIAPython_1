from django.contrib import admin
from hackathon.models import MiUser

class MiUserAdmin(admin.ModelAdmin):
    list_display = '_all_'
    
admin.site.register(MiUser, MiUserAdmin)
