from django.contrib import admin
from django.conf import settings

from samothrace.apps.admin.models import LinkedInline, get_admin_url
from samothrace.apps.inscriptions.models import Inscription, ReferenceSite
from samothrace.apps.people.models import Individual
from samothrace.apps.sites.models import Koina

class IndividualInline(LinkedInline):
    model = Individual
    extra = 0
    fields = ['individual_id', 'name', 'patronym']
    admin_model_parent = "people"
    admin_model_path = "individual"
    verbose_name_plural = "Related Individuals"
    can_delete = False


class KoinaInline(LinkedInline):
    model = Koina
    extra = 0
    fields = ['koina_id', 'site', 'member_count', 'activities']
    admin_model_parent = "sites"
    admin_model_path = "koina"
    verbose_name_plural = "Related Koina"
    can_delete = False


class ReferenceSiteInline(admin.TabularInline):
    model = ReferenceSite
    extra = 1
    verbose_name_plural = "Referenced Sites"

    
class InscriptionAdmin(admin.ModelAdmin):
    class Media:
      js = (settings.STATIC_URL + 'js/admin/collapseTabularInlines.js',)
      css = { "all" : (settings.STATIC_URL +"css/admin/admin_styles.css",) }
    list_display = ['inscription_id', 'name', 'source', 'find_spot', 'start_date', 'end_date']
    search_fields = ['inscription_id', 'name', 'source', 'alt_name']
    inlines = [
        ReferenceSiteInline,
        IndividualInline,
        KoinaInline
        ]


    
admin.site.register(Inscription, InscriptionAdmin)

