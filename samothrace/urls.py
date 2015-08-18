from django.conf.urls import patterns, include, url
from django.views.generic.base import RedirectView
from django.contrib.auth.models import User
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers, serializers, viewsets
from samothrace.apps.sites.views import SiteViewSet, MarkerViewSet, KoinaViewSet
from samothrace.apps.inscriptions.views import InscriptionViewSet
from samothrace.apps.people.views import IndividualViewSet, RoleViewSet, PriesthoodViewSet

from django.contrib import admin
admin.autodiscover()

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'sites', SiteViewSet)
router.register(r'markers', MarkerViewSet)
router.register(r'koina', KoinaViewSet)
router.register(r'inscriptions', InscriptionViewSet)
router.register(r'individuals', IndividualViewSet)
router.register(r'roles', RoleViewSet)
router.register(r'priesthoods', PriesthoodViewSet)


urlpatterns = patterns('',
     # until we have a public-facing site homepage, redirect to sites
    url(r'^$', RedirectView.as_view(url='/sites/', permanent=False), name='site-index'),
    url(r'^sites/', include('samothrace.apps.sites.urls', namespace='sites')),
    #url(r'^inscriptions/', include('samothrace.apps.inscriptions.urls', namespace='inscriptions')),
    #url(r'^people/', include('samothrace.apps.people.urls', namespace='people')),
    url(r'^admin/', include(admin.site.urls) ),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)

urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
