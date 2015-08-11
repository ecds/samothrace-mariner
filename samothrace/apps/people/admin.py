from django.conf import settings
from django.contrib import admin

from samothrace.apps.admin.models import LinkedInline, get_admin_url
from samothrace.apps.people.models import Individual, Role, Priesthood
from samothrace.apps.inscriptions.models import Inscription

class InscriptionInline(admin.TabularInline):
    model = Inscription
    extra = 1
    

class RoleInline(LinkedInline):
    model = Role
    extra = 0


class PriesthoodInline(LinkedInline):
    model = Priesthood
    extra = 0


class IndividualAdmin(admin.ModelAdmin):
    list_display = ['individual_id', 'name', 'patronym', 'inscription', 'site']
    search_fields = ['individual_id', 'name', 'patronym', 'inscription__name', 'title', 'comments']
    inlines =[
        RoleInline
    ]
    
admin.site.register(Individual, IndividualAdmin)


class RoleAdmin(admin.ModelAdmin):
    list_display = ['role_id', 'name', 'individual']
    search_fields = ['role_id', 'name', 'individual__name', 'comments']
    inlines =[
        PriesthoodInline
    ]
    
admin.site.register(Role, RoleAdmin)


class PriesthoodAdmin(admin.ModelAdmin):
    list_display = ['priesthood_id', 'name', 'title', 'location', ]
    search_fields = ['priesthood_id', 'name', 'title', 'location__name', 'deity']
    inlines =[
        
    ]
    
admin.site.register(Priesthood, PriesthoodAdmin)

