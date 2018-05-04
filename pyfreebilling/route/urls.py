from django.conf.urls import url, include
from rest_framework import routers

from . import api
from . import views

router = routers.DefaultRouter()
router.register(r'routinggroup', api.RoutingGroupViewSet)
router.register(r'prefixrule', api.PrefixRuleViewSet)
router.register(r'destinationrule', api.DestinationRuleViewSet)
router.register(r'countrytyperule', api.CountryTypeRuleViewSet)
router.register(r'countryrule', api.CountryRuleViewSet)
router.register(r'regiontyperule', api.RegionTypeRuleViewSet)
router.register(r'regionrule', api.RegionRuleViewSet)
router.register(r'defaultrule', api.DefaultRuleViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    url(r'^api/v1/', include(router.urls)),
)

urlpatterns += (
    # urls for RoutingGroup
    url(r'^route/routinggroup/$', views.RoutingGroupListView.as_view(), name='route_routinggroup_list'),
    url(r'^route/routinggroup/create/$', views.RoutingGroupCreateView.as_view(), name='route_routinggroup_create'),
    url(r'^route/routinggroup/detail/(?P<slug>\S+)/$', views.RoutingGroupDetailView.as_view(), name='route_routinggroup_detail'),
    url(r'^route/routinggroup/update/(?P<slug>\S+)/$', views.RoutingGroupUpdateView.as_view(), name='route_routinggroup_update'),
)

urlpatterns += (
    # urls for PrefixRule
    url(r'^route/prefixrule/$', views.PrefixRuleListView.as_view(), name='route_prefixrule_list'),
    url(r'^route/prefixrule/create/$', views.PrefixRuleCreateView.as_view(), name='route_prefixrule_create'),
    url(r'^route/prefixrule/detail/(?P<pk>\S+)/$', views.PrefixRuleDetailView.as_view(), name='route_prefixrule_detail'),
    url(r'^route/prefixrule/update/(?P<pk>\S+)/$', views.PrefixRuleUpdateView.as_view(), name='route_prefixrule_update'),
)

urlpatterns += (
    # urls for DestinationRule
    url(r'^route/destinationrule/$', views.DestinationRuleListView.as_view(), name='route_destinationrule_list'),
    url(r'^route/destinationrule/create/$', views.DestinationRuleCreateView.as_view(), name='route_destinationrule_create'),
    url(r'^route/destinationrule/detail/(?P<pk>\S+)/$', views.DestinationRuleDetailView.as_view(), name='route_destinationrule_detail'),
    url(r'^route/destinationrule/update/(?P<pk>\S+)/$', views.DestinationRuleUpdateView.as_view(), name='route_destinationrule_update'),
)

urlpatterns += (
    # urls for CountryTypeRule
    url(r'^route/countrytyperule/$', views.CountryTypeRuleListView.as_view(), name='route_countrytyperule_list'),
    url(r'^route/countrytyperule/create/$', views.CountryTypeRuleCreateView.as_view(), name='route_countrytyperule_create'),
    url(r'^route/countrytyperule/detail/(?P<pk>\S+)/$', views.CountryTypeRuleDetailView.as_view(), name='route_countrytyperule_detail'),
    url(r'^route/countrytyperule/update/(?P<pk>\S+)/$', views.CountryTypeRuleUpdateView.as_view(), name='route_countrytyperule_update'),
)

urlpatterns += (
    # urls for CountryRule
    url(r'^route/countryrule/$', views.CountryRuleListView.as_view(), name='route_countryrule_list'),
    url(r'^route/countryrule/create/$', views.CountryRuleCreateView.as_view(), name='route_countryrule_create'),
    url(r'^route/countryrule/detail/(?P<pk>\S+)/$', views.CountryRuleDetailView.as_view(), name='route_countryrule_detail'),
    url(r'^route/countryrule/update/(?P<pk>\S+)/$', views.CountryRuleUpdateView.as_view(), name='route_countryrule_update'),
)

urlpatterns += (
    # urls for RegionTypeRule
    url(r'^route/regiontyperule/$', views.RegionTypeRuleListView.as_view(), name='route_regiontyperule_list'),
    url(r'^route/regiontyperule/create/$', views.RegionTypeRuleCreateView.as_view(), name='route_regiontyperule_create'),
    url(r'^route/regiontyperule/detail/(?P<pk>\S+)/$', views.RegionTypeRuleDetailView.as_view(), name='route_regiontyperule_detail'),
    url(r'^route/regiontyperule/update/(?P<pk>\S+)/$', views.RegionTypeRuleUpdateView.as_view(), name='route_regiontyperule_update'),
)

urlpatterns += (
    # urls for RegionRule
    url(r'^route/regionrule/$', views.RegionRuleListView.as_view(), name='route_regionrule_list'),
    url(r'^route/regionrule/create/$', views.RegionRuleCreateView.as_view(), name='route_regionrule_create'),
    url(r'^route/regionrule/detail/(?P<pk>\S+)/$', views.RegionRuleDetailView.as_view(), name='route_regionrule_detail'),
    url(r'^route/regionrule/update/(?P<pk>\S+)/$', views.RegionRuleUpdateView.as_view(), name='route_regionrule_update'),
)

urlpatterns += (
    # urls for DefaultRule
    url(r'^route/defaultrule/$', views.DefaultRuleListView.as_view(), name='route_defaultrule_list'),
    url(r'^route/defaultrule/create/$', views.DefaultRuleCreateView.as_view(), name='route_defaultrule_create'),
    url(r'^route/defaultrule/detail/(?P<pk>\S+)/$', views.DefaultRuleDetailView.as_view(), name='route_defaultrule_detail'),
    url(r'^route/defaultrule/update/(?P<pk>\S+)/$', views.DefaultRuleUpdateView.as_view(), name='route_defaultrule_update'),
)
