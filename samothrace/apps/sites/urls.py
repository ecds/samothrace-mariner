from django.conf.urls import url
from samothrace.apps.sites.views import SiteList, SiteDetail

urlpatterns = [
    url(r'^$', SiteList.as_view(), name='list'),
    url(r'^(?P<pk>[^/]+)/$', SiteDetail.as_view(), name='site'),
]
