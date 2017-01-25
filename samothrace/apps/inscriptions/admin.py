from django.contrib import admin
from django.conf import settings

from samothrace.apps.admin.models import LinkedInline, get_admin_url
from samothrace.apps.inscriptions.models import Inscription, ReferenceSite, Grant
from samothrace.apps.people.models import Individual
from samothrace.apps.sites.models import Koina, Site
from import_export import resources, fields
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ForeignKeyWidget, ManyToManyWidget

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

class GrantResource(resources.ModelResource):
    granting_name = fields.Field(
        column_name='granting_name',
        attribute='granting_name',
        widget=ForeignKeyWidget(Site, 'name'))
    receiving_name = fields.Field(
        column_name='receiving_name',
        attribute='receiving_name',
        widget=ForeignKeyWidget(Site, 'name'))
    class Meta:
        model = Grant
        fields = ('granting_name', 'receiving_name', 'id', 'number_of_people', 'inscription', 'inscription_text', 'bibliographic', 'date_range', 'date_begin', 'date_end', 'inscriptionlink', 'notes')

class GrantAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = GrantResource
    pass
    list_display = ['id', 'inscription', 'number_of_people', 'date_range', 'bibliographic']
    search_fields = ['inscription', 'bibliographic']
    
admin.site.register(Inscription, InscriptionAdmin)
admin.site.register(Grant, GrantAdmin)

