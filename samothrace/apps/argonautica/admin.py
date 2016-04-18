from django.contrib import admin
from samothrace.apps.argonautica.models import Person, Stops, Places_Referenced
from samothrace.apps.sites.models import Site




admin.site.register(Person)
admin.site.register(Stops)
admin.site.register(Places_Referenced)