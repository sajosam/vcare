from django.contrib import admin
from .models import Disease

# Register your models here.

class diseaseAdmin(admin.ModelAdmin):
    list_display = ('name', 'symptoms','preventions', 'primarymedication')
    list_display_links = ('name',)
    

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Disease,diseaseAdmin)