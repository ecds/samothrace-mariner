from django.contrib import admin
from django.conf import settings

from samothrace.apps.admin.models import LinkedInline, get_admin_url
from samothrace.apps.sites.models import Site, Marker, Koina, Ancient_Sources
from samothrace.apps.inscriptions.models import Inscription, Grant
from samothrace.apps.people.models import Individual
from samothrace.apps.argonautica.models import Stops, Places_Referenced, Person
from import_export import resources, fields
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ForeignKeyWidget, ManyToManyWidget


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

class IndividualInline(LinkedInline):
    model = Individual
    extra = 0
    fields = ['individual_id', 'inscription']
    admin_model_parent = "people"
    admin_model_path = "individual"
    fk_name = 'site' #or 'world', as applicable.
    verbose_name_plural = "Related Individuals"
    can_delete = False

class IndividualOriginInline(LinkedInline):
    model = Individual
    extra = 0
    fields = ['individual_id', 'inscription']
    admin_model_parent = "people"
    admin_model_path = "individual"
    fk_name = 'site_origin' #or 'world', as applicable.
    verbose_name_plural = "Related Individuals Site of Origin"
    can_delete = False

class StopInline(LinkedInline):
    model = Stops
    extra = 0
    fields = ['line_number', 'type_of_stop']
    admin_model_parent = "argonautica"
    admin_model_path = "stop"
    fk_name = 'place_of_stop' #or 'world', as applicable.
    verbose_name_plural = "Related Argonautic Stops"
    can_delete = False

class Places_ReferencedInline(LinkedInline):
    model = Places_Referenced
    extra = 0
    fields = ['line_number', 'type_of_reference']
    admin_model_parent = "argonautica"
    admin_model_path = "places_referenced"
    fk_name = 'place_referenced' #or 'world', as applicable.
    verbose_name_plural = "Related Argonautic Referenced Places"
    can_delete = False

class PersonInline(LinkedInline):
    model = Person
    extra = 0
    fields = ['name', 'source']
    admin_model_parent = "argonautica"
    admin_model_path = "person"
    fk_name = 'origin' #or 'world', as applicable.
    verbose_name_plural = "Related Argonautic People Origin"
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

class GrantInline(LinkedInline):
    model = Grant
    extra = 0
    fields = ['inscription']
    admin_model_parent = "inscriptions"
    admin_model_path = "grant"
    fk_name = 'granting_name' #or 'world', as applicable.
    verbose_name_plural = "Related Grants Granting"
    can_delete = False

class Grant2Inline(LinkedInline):
    model = Grant
    extra = 0
    fields = ['inscription']
    admin_model_parent = "inscriptions"
    admin_model_path = "grant"
    fk_name = 'receiving_name' #or 'world', as applicable.
    verbose_name_plural = "Related Grants Receiving"
    can_delete = False

   
class SiteResource(resources.ModelResource):
    class Meta:
        model = Site
        fields = ('site_id','name', 'mod_name', 'alt_name', 'latitude', 'longitude', 'elevation', 'batlas', 'pleiades_url' , 'perseus_url', 'caption', 'paragraph', 'natural_marker')
        import_id_fields = ('site_id','name')
        
class SiteAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = SiteResource
    pass     
    class Media:
      js = (settings.STATIC_URL + 'js/admin/collapseTabularInlines.js',)
      css = { "all" : (settings.STATIC_URL +"css/admin/admin_styles.css",) }
    list_display = ['site_id', 'name', 'mod_name', 'pleiades_url', 'perseus_url']
    search_fields = ['site_id', 'name', 'mod_name', 'alt_name', 'natural_marker']
    inlines = [
        InscriptionInline,
        MarkerInline,
        KoinaInline,
        IndividualOriginInline,
        IndividualInline,
        StopInline,
        Places_ReferencedInline,
        PersonInline,
        GrantInline,
        Grant2Inline
        ]

admin.site.register(Site, SiteAdmin)


class MarkerAdmin(admin.ModelAdmin):
    list_display = ['marker_id', 'site', 'type']
    search_fields = ['marker_id', 'type']

admin.site.register(Marker, MarkerAdmin)


class KoinaAdmin(admin.ModelAdmin):
    list_display = ['koina_id', 'site', 'inscription', 'member_count', 'activities']
    search_fields = ['koina_id', 'site__name', 'inscription__name', 'activities']

class Ancient_SourcesResource(resources.ModelResource):
    cityname = fields.Field(
        column_name='cityname',
        attribute='cityname',
        widget=ForeignKeyWidget(Site, 'name'))
    class Meta:
        model = Ancient_Sources
        fields = ('id','cityname', 'author', 'reference', 'author_date', 'language', 'citation_url', 'bibliographic_reference')

class Ancient_SourcesAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = Ancient_SourcesResource
    pass     
    list_display = ['author', 'reference', 'author_date', 'language']
    search_fields = ['author', 'reference', 'author_date', 'language']
    
admin.site.register(Koina, KoinaAdmin)
admin.site.register(Ancient_Sources, Ancient_SourcesAdmin)