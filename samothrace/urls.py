from django.conf.urls import patterns, include, url
from django.views.generic.base import RedirectView
from django.contrib.auth.models import User
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers, serializers, viewsets
from samothrace.apps.sites.views import SiteViewSet, MarkerViewSet, KoinaViewSet, Inscriptions_Nodes, Inscriptions_NodesDistinct
from samothrace.apps.inscriptions.views import InscriptionViewSet
from samothrace.apps.people.views import IndividualViewSet, RoleViewSet, PriesthoodViewSet
from samothrace.apps.argonautica.views import Argo_Edges, Argo_Nodes1, Argo_Nodes2, Argo_EdgesNext, Argo_EdgesPrevious, Argo_EdgesIndirect, Argo_EdgesIndirectNext, Argo_Nodes3_AllIndirectDirect


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
#     url(r'^map/$', map, name='map'),
     url(r'^$', RedirectView.as_view(url='/admin', permanent=False)), # temp redirect to admin
     url(r'^admin/', include(admin.site.urls) ),
     url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
     url(r'^', include(router.urls)),
     url(r'^api/', include(router.urls)),
     url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
     url(r'^ArgoEdgeData/$', Argo_Edges, name="Argo Networks"),
     url(r'^ArgoNodeDataSource/$', Argo_Nodes1, name="Argo Networks2"),
     url(r'^ArgoNodeDataTarget/$', Argo_Nodes2, name="Argo Networks3"),
     url(r'^ArgoEdgeDataNext/$', Argo_EdgesNext, name="Argo Networks4"),
     url(r'^ArgoEdgeDataPrevious/$', Argo_EdgesPrevious, name="Argo Networks5"),
     url(r'^ArgoEdgeIndirectStops/$', Argo_EdgesIndirect, name="Argo Networks6"),
     url(r'^ArgoEdgeIndirectStopsNext/$', Argo_EdgesIndirectNext, name="Argo Networks7"),
     url(r'^ArgoNodeDataAllTarget/$', Argo_Nodes3_AllIndirectDirect, name="Argo Networks8"),
     url(r'^InscriptionSiteData/$', Inscriptions_Nodes, name="Inscription Network1"),
#     url(r'^InscriptionSiteDataDistinct/$', Inscriptions_NodesDistinct, name="Inscription Network2"),
)

urlpatterns+=url(r'^simple_import/', include('simple_import.urls')),
urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
