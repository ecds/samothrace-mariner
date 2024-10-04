from django.conf.urls import patterns, include, url
from django.views.generic.base import RedirectView
from django.contrib.auth.models import User
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers, serializers, viewsets
from samothrace.apps.sites.views import SiteViewSet, MarkerViewSet, KoinaViewSet, Inscriptions_Nodes, Inscriptions_NodesPeopleSites, links, Inscriptions_NodesPeopleSitesDistinct, Grant_Edges2, Grant_Edges3, Grant_Nodes1, Grant_Nodes2, Networks_Game
from samothrace.apps.inscriptions.views import InscriptionViewSet, Inscriptions_Edges, Inscriptions_Edges2, Grant_Edges1, Grant_Edges4
from samothrace.apps.people.views import IndividualViewSet, RoleViewSet, PriesthoodViewSet, InscriptionPeople_Edges, Bibliography, HowToGraph
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
     #url(r'^InscriptionSiteDataDistinct/$', Inscriptions_NodesDistinct, name="Inscription Network2"),
     url(r'^InscriptionBothSiteData/$', Inscriptions_NodesPeopleSites, name="Inscription Network3"),
     url(r'^links/$', links, name="links"), 
     url(r'^InscriptionPeopleSiteDistinct/$', Inscriptions_NodesPeopleSitesDistinct, name="Inscription Network4"),
     url(r'^InscriptionEdgeData/$', Inscriptions_Edges, name="Inscription Network 5"),
     url(r'^InscriptionEdgesData/$', Inscriptions_Edges2, name="Inscription Network 6"),
     url(r'^PeopleInscriptionEdges/$', InscriptionPeople_Edges, name="Inscription Network 7"),
     url(r'^GrantEdgesGrant/$', Grant_Edges1, name="Grant Network 1"),
     url(r'^GrantEdgesRec/$', Grant_Edges2, name="Grant Network 2"),
     url(r'^GrantEdgesOther/$', Grant_Edges3, name="Grant Network 3"),
     url(r'^GrantEdgesReceivings/$', Grant_Edges4, name="Grant Network 4"),
     url(r'^biblio/$', Bibliography, name="Bibliography"), 
     url(r'^how_graph/$', HowToGraph, name="HowToGraph"),
     url(r'^GrantNodesGranting/$', Grant_Nodes1, name="Grant Nodes 1"),
     url(r'^GrantNodesReceiving/$', Grant_Nodes2, name="Grant Nodes 2"),
     url(r'^NetworksGameID/$', Networks_Game, name="Networks_Game"),
)

urlpatterns+=url(r'^simple_import/', include('simple_import.urls')),
urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
