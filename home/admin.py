from django.contrib import admin
from .models import Hospital,Specialization,Doctor,Appointment
from django.utils.html import format_html

# Register your models here.

class HospitalAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="150" style="border-radius : 20px;" />'.format(object.h_image.url))

    thumbnail.short_description="Photo"
    prepopulated_fields={'slug':('h_name',)}

    list_display=(
        'id',
        'thumbnail',
        'h_name',
        'contact',
        'district',
        'state',
        'email',
        'is_active',
    )
    list_display_links=(
        'id',
        'h_name',
        'thumbnail',
    )
    list_editable=(
        'is_active',
    )
    search_fields=(
        'id',
        'h_name',
        'district',
        'state',
        
    )
    list_filter=(
        'district',
        'state',
        
    )


class DoctorAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" height="100" style="border-radius : 30px;" />'.format(object.d_image.url))

    thumbnail.short_description="Photo"

    list_display=(
        'id',
        'thumbnail',
        's_name',
        'd_name',
        'h_name',
        'contact',
        'email',
        'fee',
        'yos',
        'sex',
        'is_active',
        'qualification',
        'created_on',
    )
    list_display_links=(
        'id',
        'thumbnail',
        'h_name',
        's_name',
        'd_name',
    )
    list_editable=(
        'is_active',
    )
    search_fields=(
        'id',
        'h_name',
        's_name'
        
    )
    list_filter=(
        's_name',
        
    )




class SpecilizationAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('s_name',)}
    list_display=(
        'id',
        's_name',
        
        
    )
    list_display_links=(
        'id',
        's_name',
    )
    
    
class AppointmentAdmin(admin.ModelAdmin):
    list_display=(
        'id',
        'p_name',
        'd_name',
        'h_name',
        's_name',
        'date',
        'time',
        'fee',
        'created_on',
        
        
        
    )
    list_display_links=(
        'id',
        'p_name',
        'd_name',
        'h_name',
    )
    

admin.site.register(Hospital, HospitalAdmin)
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(Specialization, SpecilizationAdmin)
admin.site.register(Appointment, AppointmentAdmin)

