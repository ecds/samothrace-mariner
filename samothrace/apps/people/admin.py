from django.conf import settings
from django.contrib import admin

from samothrace.apps.admin.models import LinkedInline, get_admin_url
from samothrace.apps.people.models import Individual, Role, Priesthood
from samothrace.apps.inscriptions.models import Inscription

class InscriptionInline(admin.TabularInline):
    model = Inscription
    extra = 1
    

class RoleInline(admin.TabularInline):
    model = Role
    extra = 0
    exclude = ["comments"]


class PriesthoodInline(admin.TabularInline):
    model = Priesthood
    extra = 0
    fields = ["priesthood_id", "name", "title"]
    read_only = ["priesthood_id", "name", "title"]
    max_num=0

class IndividualAdmin(admin.ModelAdmin):
    list_display = ['individual_id', 'name', 'patronym', 'inscription', 'site']
    search_fields = ['individual_id', 'name', 'patronym', 'inscription__name', 'comments']
    inlines =[
        RoleInline
    ]
    
admin.site.register(Individual, IndividualAdmin)


class RoleAdmin(admin.ModelAdmin):
    list_display = ['role_id', 'title', 'certainty', 'individual']
    search_fields = ['role_id', 'title', 'individual__name', 'comments']
    list_filter = ['title']
    inlines =[
        PriesthoodInline
    ]
    
admin.site.register(Role, RoleAdmin)


class PriesthoodAdmin(admin.ModelAdmin):
    list_display = ['priesthood_id', 'name', 'title', 'location', ]
    search_fields = ['priesthood_id', 'name', 'title', 'location__name', 'deity']
    filter_horizontal = ['inscription']
    inlines =[
        
    ]
    
admin.site.register(Priesthood, PriesthoodAdmin)

