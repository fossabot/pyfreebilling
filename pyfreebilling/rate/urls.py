from django.conf.urls import url, include
from rest_framework import routers

from . import api
from . import views

router = routers.DefaultRouter()
router.register(r'callernumlist', api.CallerNumListViewSet)
router.register(r'providerratecard', api.ProviderRatecardViewSet)
router.register(r'customerratecard', api.CustomerRatecardViewSet)
router.register(r'customerprefixrate', api.CustomerPrefixRateViewSet)
router.register(r'providerprefixrate', api.ProviderPrefixRateViewSet)
router.register(r'customerdestinationrate', api.CustomerDestinationRateViewSet)
router.register(r'providerdestinationrate', api.ProviderDestinationRateViewSet)
router.register(r'customercountrytyperate', api.CustomerCountryTypeRateViewSet)
router.register(r'providercountrytyperate', api.ProviderCountryTypeRateViewSet)
router.register(r'customercountryrate', api.CustomerCountryRateViewSet)
router.register(r'providercountryrate', api.ProviderCountryRateViewSet)
router.register(r'customerregiontyperate', api.CustomerRegionTypeRateViewSet)
router.register(r'providerregiontyperate', api.ProviderRegionTypeRateViewSet)
router.register(r'customerregionrate', api.CustomerRegionRateViewSet)
router.register(r'providerregionrate', api.ProviderRegionRateViewSet)
router.register(r'customerdefaultrate', api.CustomerDefaultRateViewSet)
router.register(r'providerdefaultrate', api.ProviderDefaultRateViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    url(r'^api/v1/', include(router.urls)),
)

urlpatterns += (
    # urls for CallerNumList
    url(r'^rate/callernumlist/$', views.CallerNumListListView.as_view(), name='rate_callernumlist_list'),
    url(r'^rate/callernumlist/create/$', views.CallerNumListCreateView.as_view(), name='rate_callernumlist_create'),
    url(r'^rate/callernumlist/detail/(?P<slug>\S+)/$', views.CallerNumListDetailView.as_view(), name='rate_callernumlist_detail'),
    url(r'^rate/callernumlist/update/(?P<slug>\S+)/$', views.CallerNumListUpdateView.as_view(), name='rate_callernumlist_update'),
)

urlpatterns += (
    # urls for ProviderRatecard
    url(r'^rate/providerratecard/$', views.ProviderRatecardListView.as_view(), name='rate_providerratecard_list'),
    url(r'^rate/providerratecard/create/$', views.ProviderRatecardCreateView.as_view(), name='rate_providerratecard_create'),
    url(r'^rate/providerratecard/detail/(?P<slug>\S+)/$', views.ProviderRatecardDetailView.as_view(), name='rate_providerratecard_detail'),
    url(r'^rate/providerratecard/update/(?P<slug>\S+)/$', views.ProviderRatecardUpdateView.as_view(), name='rate_providerratecard_update'),
)

urlpatterns += (
    # urls for CustomerRatecard
    url(r'^rate/customerratecard/$', views.CustomerRatecardListView.as_view(), name='rate_customerratecard_list'),
    url(r'^rate/customerratecard/create/$', views.CustomerRatecardCreateView.as_view(), name='rate_customerratecard_create'),
    url(r'^rate/customerratecard/detail/(?P<slug>\S+)/$', views.CustomerRatecardDetailView.as_view(), name='rate_customerratecard_detail'),
    url(r'^rate/customerratecard/update/(?P<slug>\S+)/$', views.CustomerRatecardUpdateView.as_view(), name='rate_customerratecard_update'),
)

urlpatterns += (
    # urls for CustomerPrefixRate
    url(r'^rate/customerprefixrate/$', views.CustomerPrefixRateListView.as_view(), name='rate_customerprefixrate_list'),
    url(r'^rate/customerprefixrate/create/$', views.CustomerPrefixRateCreateView.as_view(), name='rate_customerprefixrate_create'),
    url(r'^rate/customerprefixrate/detail/(?P<pk>\S+)/$', views.CustomerPrefixRateDetailView.as_view(), name='rate_customerprefixrate_detail'),
    url(r'^rate/customerprefixrate/update/(?P<pk>\S+)/$', views.CustomerPrefixRateUpdateView.as_view(), name='rate_customerprefixrate_update'),
)

urlpatterns += (
    # urls for ProviderPrefixRate
    url(r'^rate/providerprefixrate/$', views.ProviderPrefixRateListView.as_view(), name='rate_providerprefixrate_list'),
    url(r'^rate/providerprefixrate/create/$', views.ProviderPrefixRateCreateView.as_view(), name='rate_providerprefixrate_create'),
    url(r'^rate/providerprefixrate/detail/(?P<pk>\S+)/$', views.ProviderPrefixRateDetailView.as_view(), name='rate_providerprefixrate_detail'),
    url(r'^rate/providerprefixrate/update/(?P<pk>\S+)/$', views.ProviderPrefixRateUpdateView.as_view(), name='rate_providerprefixrate_update'),
)

urlpatterns += (
    # urls for CustomerDestinationRate
    url(r'^rate/customerdestinationrate/$', views.CustomerDestinationRateListView.as_view(), name='rate_customerdestinationrate_list'),
    url(r'^rate/customerdestinationrate/create/$', views.CustomerDestinationRateCreateView.as_view(), name='rate_customerdestinationrate_create'),
    url(r'^rate/customerdestinationrate/detail/(?P<pk>\S+)/$', views.CustomerDestinationRateDetailView.as_view(), name='rate_customerdestinationrate_detail'),
    url(r'^rate/customerdestinationrate/update/(?P<pk>\S+)/$', views.CustomerDestinationRateUpdateView.as_view(), name='rate_customerdestinationrate_update'),
)

urlpatterns += (
    # urls for ProviderDestinationRate
    url(r'^rate/providerdestinationrate/$', views.ProviderDestinationRateListView.as_view(), name='rate_providerdestinationrate_list'),
    url(r'^rate/providerdestinationrate/create/$', views.ProviderDestinationRateCreateView.as_view(), name='rate_providerdestinationrate_create'),
    url(r'^rate/providerdestinationrate/detail/(?P<pk>\S+)/$', views.ProviderDestinationRateDetailView.as_view(), name='rate_providerdestinationrate_detail'),
    url(r'^rate/providerdestinationrate/update/(?P<pk>\S+)/$', views.ProviderDestinationRateUpdateView.as_view(), name='rate_providerdestinationrate_update'),
)

urlpatterns += (
    # urls for CustomerCountryTypeRate
    url(r'^rate/customercountrytyperate/$', views.CustomerCountryTypeRateListView.as_view(), name='rate_customercountrytyperate_list'),
    url(r'^rate/customercountrytyperate/create/$', views.CustomerCountryTypeRateCreateView.as_view(), name='rate_customercountrytyperate_create'),
    url(r'^rate/customercountrytyperate/detail/(?P<pk>\S+)/$', views.CustomerCountryTypeRateDetailView.as_view(), name='rate_customercountrytyperate_detail'),
    url(r'^rate/customercountrytyperate/update/(?P<pk>\S+)/$', views.CustomerCountryTypeRateUpdateView.as_view(), name='rate_customercountrytyperate_update'),
)

urlpatterns += (
    # urls for ProviderCountryTypeRate
    url(r'^rate/providercountrytyperate/$', views.ProviderCountryTypeRateListView.as_view(), name='rate_providercountrytyperate_list'),
    url(r'^rate/providercountrytyperate/create/$', views.ProviderCountryTypeRateCreateView.as_view(), name='rate_providercountrytyperate_create'),
    url(r'^rate/providercountrytyperate/detail/(?P<pk>\S+)/$', views.ProviderCountryTypeRateDetailView.as_view(), name='rate_providercountrytyperate_detail'),
    url(r'^rate/providercountrytyperate/update/(?P<pk>\S+)/$', views.ProviderCountryTypeRateUpdateView.as_view(), name='rate_providercountrytyperate_update'),
)

urlpatterns += (
    # urls for CustomerCountryRate
    url(r'^rate/customercountryrate/$', views.CustomerCountryRateListView.as_view(), name='rate_customercountryrate_list'),
    url(r'^rate/customercountryrate/create/$', views.CustomerCountryRateCreateView.as_view(), name='rate_customercountryrate_create'),
    url(r'^rate/customercountryrate/detail/(?P<pk>\S+)/$', views.CustomerCountryRateDetailView.as_view(), name='rate_customercountryrate_detail'),
    url(r'^rate/customercountryrate/update/(?P<pk>\S+)/$', views.CustomerCountryRateUpdateView.as_view(), name='rate_customercountryrate_update'),
)

urlpatterns += (
    # urls for ProviderCountryRate
    url(r'^rate/providercountryrate/$', views.ProviderCountryRateListView.as_view(), name='rate_providercountryrate_list'),
    url(r'^rate/providercountryrate/create/$', views.ProviderCountryRateCreateView.as_view(), name='rate_providercountryrate_create'),
    url(r'^rate/providercountryrate/detail/(?P<pk>\S+)/$', views.ProviderCountryRateDetailView.as_view(), name='rate_providercountryrate_detail'),
    url(r'^rate/providercountryrate/update/(?P<pk>\S+)/$', views.ProviderCountryRateUpdateView.as_view(), name='rate_providercountryrate_update'),
)

urlpatterns += (
    # urls for CustomerRegionTypeRate
    url(r'^rate/customerregiontyperate/$', views.CustomerRegionTypeRateListView.as_view(), name='rate_customerregiontyperate_list'),
    url(r'^rate/customerregiontyperate/create/$', views.CustomerRegionTypeRateCreateView.as_view(), name='rate_customerregiontyperate_create'),
    url(r'^rate/customerregiontyperate/detail/(?P<pk>\S+)/$', views.CustomerRegionTypeRateDetailView.as_view(), name='rate_customerregiontyperate_detail'),
    url(r'^rate/customerregiontyperate/update/(?P<pk>\S+)/$', views.CustomerRegionTypeRateUpdateView.as_view(), name='rate_customerregiontyperate_update'),
)

urlpatterns += (
    # urls for ProviderRegionTypeRate
    url(r'^rate/providerregiontyperate/$', views.ProviderRegionTypeRateListView.as_view(), name='rate_providerregiontyperate_list'),
    url(r'^rate/providerregiontyperate/create/$', views.ProviderRegionTypeRateCreateView.as_view(), name='rate_providerregiontyperate_create'),
    url(r'^rate/providerregiontyperate/detail/(?P<pk>\S+)/$', views.ProviderRegionTypeRateDetailView.as_view(), name='rate_providerregiontyperate_detail'),
    url(r'^rate/providerregiontyperate/update/(?P<pk>\S+)/$', views.ProviderRegionTypeRateUpdateView.as_view(), name='rate_providerregiontyperate_update'),
)

urlpatterns += (
    # urls for CustomerRegionRate
    url(r'^rate/customerregionrate/$', views.CustomerRegionRateListView.as_view(), name='rate_customerregionrate_list'),
    url(r'^rate/customerregionrate/create/$', views.CustomerRegionRateCreateView.as_view(), name='rate_customerregionrate_create'),
    url(r'^rate/customerregionrate/detail/(?P<pk>\S+)/$', views.CustomerRegionRateDetailView.as_view(), name='rate_customerregionrate_detail'),
    url(r'^rate/customerregionrate/update/(?P<pk>\S+)/$', views.CustomerRegionRateUpdateView.as_view(), name='rate_customerregionrate_update'),
)

urlpatterns += (
    # urls for ProviderRegionRate
    url(r'^rate/providerregionrate/$', views.ProviderRegionRateListView.as_view(), name='rate_providerregionrate_list'),
    url(r'^rate/providerregionrate/create/$', views.ProviderRegionRateCreateView.as_view(), name='rate_providerregionrate_create'),
    url(r'^rate/providerregionrate/detail/(?P<pk>\S+)/$', views.ProviderRegionRateDetailView.as_view(), name='rate_providerregionrate_detail'),
    url(r'^rate/providerregionrate/update/(?P<pk>\S+)/$', views.ProviderRegionRateUpdateView.as_view(), name='rate_providerregionrate_update'),
)

urlpatterns += (
    # urls for CustomerDefaultRate
    url(r'^rate/customerdefaultrate/$', views.CustomerDefaultRateListView.as_view(), name='rate_customerdefaultrate_list'),
    url(r'^rate/customerdefaultrate/create/$', views.CustomerDefaultRateCreateView.as_view(), name='rate_customerdefaultrate_create'),
    url(r'^rate/customerdefaultrate/detail/(?P<pk>\S+)/$', views.CustomerDefaultRateDetailView.as_view(), name='rate_customerdefaultrate_detail'),
    url(r'^rate/customerdefaultrate/update/(?P<pk>\S+)/$', views.CustomerDefaultRateUpdateView.as_view(), name='rate_customerdefaultrate_update'),
)

urlpatterns += (
    # urls for ProviderDefaultRate
    url(r'^rate/providerdefaultrate/$', views.ProviderDefaultRateListView.as_view(), name='rate_providerdefaultrate_list'),
    url(r'^rate/providerdefaultrate/create/$', views.ProviderDefaultRateCreateView.as_view(), name='rate_providerdefaultrate_create'),
    url(r'^rate/providerdefaultrate/detail/(?P<pk>\S+)/$', views.ProviderDefaultRateDetailView.as_view(), name='rate_providerdefaultrate_detail'),
    url(r'^rate/providerdefaultrate/update/(?P<pk>\S+)/$', views.ProviderDefaultRateUpdateView.as_view(), name='rate_providerdefaultrate_update'),
)
