from django.contrib import admin
from samothrace.apps.argonautica.models import Person, Stops, Places_Referenced
from samothrace.apps.sites.models import Site

class PersonAdmin(admin.ModelAdmin):
    list_display = ['name', 'tribe']
    search_fields = ['name', 'tribe']

class StopsAdmin(admin.ModelAdmin):
    list_display = ['type_of_stop','line_number','ritual']
    search_fields = ['type_of_stop','line_number','ritual']
    
class Places_ReferencedAdmin(admin.ModelAdmin):
    list_display = ['type_of_reference','line_number','ritual']
    search_fields = ['type_of_reference','line_number','ritual']
    

admin.site.register(Person, PersonAdmin)
admin.site.register(Stops, StopsAdmin)
admin.site.register(Places_Referenced, Places_ReferencedAdmin)