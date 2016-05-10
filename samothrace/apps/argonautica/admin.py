from django.contrib import admin
from samothrace.apps.argonautica.models import Person, Stops, Places_Referenced
from samothrace.apps.sites.models import Site
from import_export import resources, fields
from import_export.admin import ImportExportModelAdmin
from import_export.widgets import ForeignKeyWidget, ManyToManyWidget

class StopsResource(resources.ModelResource):
    place_of_stop = fields.Field(
        column_name='place_of_stop',
        attribute='place_of_stop',
        widget=ForeignKeyWidget(Site, 'name'))
    previous_place = fields.Field(
        column_name='previous_place',
        attribute='previous_place',
        widget=ForeignKeyWidget(Site, 'name'))
    next_place = fields.Field(
        column_name='next_place',
        attribute='next_place',
        widget=ForeignKeyWidget(Site, 'name'))
    crew = fields.Field(
        column_name='crew',
        attribute='crew',
        widget=ManyToManyWidget(Person, separator=', ', field='name'))
    ritual_people = fields.Field(
        column_name='ritual_people',
        attribute='ritual_people',
        widget=ManyToManyWidget(Person, separator=', ', field='name'))
    class Meta:
        model = Stops
        fields = ('id','type_of_stop', 'line_number','place_of_stop','previous_place','next_place','ritual','ritual_deity','argonautica_edition','crew','ritual_people')
        
class Places_ReferencedResource(resources.ModelResource):
    place_referenced = fields.Field(
        column_name='place_referenced',
        attribute='place_referenced',
        widget=ForeignKeyWidget(Site, 'name'))
    previous_place = fields.Field(
        column_name='previous_place',
        attribute='previous_place',
        widget=ForeignKeyWidget(Site, 'name'))
    next_place = fields.Field(
        column_name='next_place',
        attribute='next_place',
        widget=ForeignKeyWidget(Site, 'name'))
    referenced_by = fields.Field(
        column_name='referenced_by',
        attribute='referenced_by',
        widget=ForeignKeyWidget(Person, 'name'))
    ritual_people = fields.Field(
        column_name='ritual_people',
        attribute='ritual_people',
        widget=ManyToManyWidget(Person, separator=', ', field='name'))
    class Meta:
        model = Places_Referenced
        fields = ('id','place_referenced', 'line_number', 'type_of_reference', 'referenced_by', 'previous_place', 'next_place', 'ritual', 'ritual_deity', 'ritual_people', 'argonautica_edition')

class PersonResource(resources.ModelResource):
    origin = fields.Field(
        column_name='origin',
        attribute='origin',
        widget=ForeignKeyWidget(Site, 'name'))
    class Meta:
        model = Person
        fields = ('id','name', 'origin')
                
class PersonAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = PersonResource
    pass     
    list_display = ['name']
    search_fields = ['name']

class StopsAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = StopsResource
    pass     
    list_display = ['type_of_stop','line_number','ritual','argonautica_edition']
    search_fields = ['type_of_stop','line_number','ritual','argonautica_edition']
    filter_horizontal = ['crew', 'ritual_people']
    
class Places_ReferencedAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = Places_ReferencedResource
    pass     
    list_display = ['type_of_reference','line_number','ritual','argonautica_edition']
    search_fields = ['type_of_reference','line_number','ritual','argonautica_edition']
    filter_horizontal = ['ritual_people']
    

admin.site.register(Person, PersonAdmin)
admin.site.register(Stops, StopsAdmin)
admin.site.register(Places_Referenced, Places_ReferencedAdmin)