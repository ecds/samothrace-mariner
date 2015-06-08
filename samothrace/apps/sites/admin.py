from django.contrib import admin
from django.conf import settings

from samothrace.apps.admin.models import LinkedInline, get_admin_url
from samothrace.apps.sites.models import Site, Marker, Koina
from samothrace.apps.inscriptions.models import Inscription
from samothrace.apps.people.models import Individual


#--More than one foreign key with Individual
# class IndividualInline(LinkedInline):
#     model = Individual.site.through # this doesn't work
#     extra = 0
#     fields = ['individual_id', 'name', 'patronym']
#     admin_model_parent = "people"
#     admin_model_path = "individual"
#     verbose_name_plural = "Related Individuals"
#     can_delete = False


class KoinaInline(LinkedInline):
    model = Koina
    extra = 0
    fields = ['koina_id', 'site', 'member_count', 'activities']
    admin_model_parent = "sites"
    admin_model_path = "koina"
    verbose_name_plural = "Related Koina"
    can_delete = False


class MarkerInline(LinkedInline):
    model = Marker
    extra = 0
    fields = ['marker_id', 'type']
    admin_model_parent = "sites"
    admin_model_path = "marker"
    verbose_name_plural = "Related Markers"
    can_delete = False


class InscriptionInline(LinkedInline):
    model = Inscription
    extra = 0
    fields = ['inscription_id', 'name']
    admin_model_parent = "inscriptions"
    admin_model_path = "inscription"
    verbose_name_plural = "Related Inscriptions"
    can_delete = False

    

class SiteAdmin(admin.ModelAdmin):
    class Media:
      js = (settings.STATIC_URL + 'js/admin/collapseTabularInlines.js',)
      css = { "all" : (settings.STATIC_URL +"css/admin/admin_styles.css",) }
    list_display = ['site_id', 'name', 'mod_name', 'pleiades_url', 'perseus_url']
    search_fields = ['site_id', 'name', 'mod_name', 'alt_name']
    inlines = [
        InscriptionInline,
        #IndividualInline,
        MarkerInline,
        KoinaInline
        ]

admin.site.register(Site, SiteAdmin)


class MarkerAdmin(admin.ModelAdmin):
    list_display = ['marker_id', 'site', 'type']
    search_fields = ['marker_id', 'type']

admin.site.register(Marker, MarkerAdmin)


class KoinaAdmin(admin.ModelAdmin):
    list_display = ['koina_id', 'site', 'inscription', 'member_count', 'activities']
    search_fields = ['koina_id', 'site__name', 'inscription__name', 'activities']


admin.site.register(Koina, KoinaAdmin)
