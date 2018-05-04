from django import forms
from .models import RoutingGroup, PrefixRule, DestinationRule, CountryTypeRule, CountryRule, RegionTypeRule, RegionRule, DefaultRule


class RoutingGroupForm(forms.ModelForm):
    class Meta:
        model = RoutingGroup
        fields = ['name', 'status', 'status_changed', 'created', 'modified', 'description']


class PrefixRuleForm(forms.ModelForm):
    class Meta:
        model = PrefixRule
        fields = ['prefix', 'destnum_length', 'c_route', 'status', 'route_type', 'weight', 'priority', 'provider_ratecard', 'provider_gateway_list']


class DestinationRuleForm(forms.ModelForm):
    class Meta:
        model = DestinationRule
        fields = ['c_route', 'destination', 'status', 'route_type', 'weight', 'priority', 'provider_ratecard', 'provider_gateway_list']


class CountryTypeRuleForm(forms.ModelForm):
    class Meta:
        model = CountryTypeRule
        fields = ['c_route', 'country', 'type', 'status', 'route_type', 'weight', 'priority', 'provider_ratecard', 'provider_gateway_list']


class CountryRuleForm(forms.ModelForm):
    class Meta:
        model = CountryRule
        fields = ['c_route', 'country', 'status', 'route_type', 'weight', 'priority', 'provider_ratecard', 'provider_gateway_list']


class RegionTypeRuleForm(forms.ModelForm):
    class Meta:
        model = RegionTypeRule
        fields = ['c_route', 'region', 'type', 'status', 'route_type', 'weight', 'priority', 'provider_ratecard', 'provider_gateway_list']


class RegionRuleForm(forms.ModelForm):
    class Meta:
        model = RegionRule
        fields = ['c_route', 'region', 'status', 'route_type', 'weight', 'priority', 'provider_ratecard', 'provider_gateway_list']


class DefaultRuleForm(forms.ModelForm):
    class Meta:
        model = DefaultRule
        fields = ['c_route', 'status', 'route_type', 'weight', 'priority', 'provider_ratecard', 'provider_gateway_list']
