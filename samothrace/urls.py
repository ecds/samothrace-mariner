from django.conf.urls import re_path, include, url
from django.views.generic.base import RedirectView
from django.contrib.auth.models import User
from django.conf import settings
from django.conf.urls.static import static
#from rest_framework import routers, serializers, viewsets
from samothrace.apps.sites.views import Inscriptions_NodesPeopleSites, Inscriptions_Nodes, links, Inscriptions_NodesPeopleSitesDistinct, Grant_Edges2, Grant_Edges3, Grant_Nodes1, Grant_Nodes2
from samothrace.apps.inscriptions.views import Inscriptions_Edges
from samothrace.apps.people.views import InscriptionPeople_Edges, Bibliography, HowToGraph, InscriptionPeopleTime_Edges
from samothrace.apps.argonautica.views import Argo_Edges, Argo_Nodes1, Argo_Nodes2, Argo_EdgesNext, Argo_EdgesPrevious, Argo_EdgesIndirect, Argo_EdgesIndirectNext, Argo_Nodes3_AllIndirectDirect

from django.contrib import admin
admin.autodiscover()

# Routers provide an easy way of automatically determining the URL conf.
# router = routers.DefaultRouter()
# router.register(r'sites', SiteViewSet)
# router.register(r'markers', MarkerViewSet)
# router.register(r'koina', KoinaViewSet)
# router.register(r'inscriptions', InscriptionViewSet)
# router.register(r'individuals', IndividualViewSet)
# router.register(r'roles', RoleViewSet)
# router.register(r'priesthoods', PriesthoodViewSet)


urlpatterns = [
#     url(r'^map/$', map, name='map'),
     re_path(r'^$', RedirectView.as_view(url='/admin', permanent=False)), # temp redirect to admin
     re_path(r'^admin/', admin.site.urls ),
     #re_path(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
     #re_path(r'^', include(router.urls)),
     #re_path(r'^api/', include(router.urls)),
     #re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
     re_path(r'^ArgoEdgeData/$', Argo_Edges, name="Argo Networks"),
     re_path(r'^ArgoNodeDataSource/$', Argo_Nodes1, name="Argo Networks2"),
     re_path(r'^ArgoNodeDataTarget/$', Argo_Nodes2, name="Argo Networks3"),
     re_path(r'^ArgoEdgeDataNext/$', Argo_EdgesNext, name="Argo Networks4"),
     re_path(r'^ArgoEdgeDataPrevious/$', Argo_EdgesPrevious, name="Argo Networks5"),
     re_path(r'^ArgoEdgeIndirectStops/$', Argo_EdgesIndirect, name="Argo Networks6"),
     re_path(r'^ArgoEdgeIndirectStopsNext/$', Argo_EdgesIndirectNext, name="Argo Networks7"),
     re_path(r'^ArgoNodeDataAllTarget/$', Argo_Nodes3_AllIndirectDirect, name="Argo Networks8"),
     re_path(r'^InscriptionSiteData/$', Inscriptions_Nodes, name="Inscription Network1"),
#     url(r'^InscriptionSiteDataDistinct/$', Inscriptions_NodesDistinct, name="Inscription Network2"),
     re_path(r'^InscriptionBothSiteData/$', Inscriptions_NodesPeopleSites, name="Inscription Network3"),
     re_path(r'^links/$', links, name="links"),
     re_path(r'^InscriptionEdgeData/$', Inscriptions_Edges, name="Inscription Network 5"),
     re_path(r'^InscriptionPeopleSiteDistinct/$', Inscriptions_NodesPeopleSitesDistinct, name="Inscription Network4"),
     re_path(r'^PeopleInscriptionEdges/$', InscriptionPeople_Edges, name="Inscription Network 7"),
     re_path(r'^GrantEdgesRec/$', Grant_Edges2, name="Grant Network 2"),
     re_path(r'^GrantEdgesOther/$', Grant_Edges3, name="Grant Network 3"),
     re_path(r'^biblio/$', Bibliography, name="Bibliography"),
     re_path(r'^how_graph/$', HowToGraph, name="HowToGraph"),
     re_path(r'^GrantNodesGranting/$', Grant_Nodes1, name="Grant Nodes 1"),
     re_path(r'^GrantNodesReceiving/$', Grant_Nodes2, name="Grant Nodes 2"),
     re_path(r'^PeopleInscriptionEdgesTime/$', InscriptionPeopleTime_Edges, name="Inscription Time Edges"),
]

#urlpatterns+=url(r'^simple_import/', include('simple_import.urls')),
urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
