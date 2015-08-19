from django.conf.urls import url
from samothrace.apps.people.views import IndividualList, IndividualDetail

urlpatterns = [
    url(r'^$', IndividualList.as_view(), name='list'),
    url(r'^(?P<pk>[^/]+)/$', IndividualDetail.as_view(), name='individual'),
]
