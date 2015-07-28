from django.conf.urls import url
from samothrace.apps.sites.views import SiteList

urlpatterns = [
    url(r'^$', SiteList.as_view(), name='list'),
]
