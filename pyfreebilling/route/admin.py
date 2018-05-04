# -*- coding: utf-8 -*-
# Copyright 2013 Mathias WOLFF
# This file is part of pyfreebilling.
#
# pyfreebilling is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pyfreebilling is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with pyfreebilling.  If not, see <http://www.gnu.org/licenses/>

from django.contrib import admin
from django import forms
from django.utils.translation import ugettext_lazy as _

from .models import RoutingGroup, PrefixRule, DestinationRule, CountryTypeRule, CountryRule, RegionTypeRule, RegionRule, DefaultRule


class PrefixRuleInline(admin.TabularInline):
    model = PrefixRule
    fields = ['provider_ratecard', 'prefix', 'destnum_length', 'route_type', 'weight', 'priority', 'provider_gateway_list', 'status']
    #formset = CustomerPrefixRateFormSet
    max_num = 40
    extra = 0


class DestinationRuleInline(admin.TabularInline):
    model = DestinationRule
    fields = ['provider_ratecard', 'destination', 'route_type', 'weight', 'priority', 'provider_gateway_list', 'status']
    #formset = CustomerPrefixRateFormSet
    max_num = 40
    extra = 0


class CountryTypeRuleInline(admin.TabularInline):
    model = CountryTypeRule
    fields = ['provider_ratecard', 'country', 'type', 'route_type', 'weight', 'priority', 'provider_gateway_list', 'status']
    #formset = CustomerPrefixRateFormSet
    max_num = 40
    extra = 0


class CountryRuleInline(admin.TabularInline):
    model = CountryRule
    fields = ['provider_ratecard', 'country', 'route_type', 'weight', 'priority', 'provider_gateway_list', 'status']
    #formset = CustomerPrefixRateFormSet
    max_num = 40
    extra = 0


class RegionTypeRuleInline(admin.TabularInline):
    model = RegionTypeRule
    fields = ['provider_ratecard', 'region', 'type', 'route_type', 'weight', 'priority', 'provider_gateway_list', 'status']
    #formset = CustomerPrefixRateFormSet
    max_num = 40
    extra = 0


class RegionRuleInline(admin.TabularInline):
    model = RegionRule
    fields = ['provider_ratecard', 'region', 'route_type', 'weight', 'priority', 'provider_gateway_list', 'status']
    #formset = CustomerPrefixRateFormSet
    max_num = 40
    extra = 0


class DefaultRuleInline(admin.TabularInline):
    model = DefaultRule
    fields = ['provider_ratecard', 'route_type', 'weight', 'priority', 'provider_gateway_list', 'status']
    #formset = CustomerPrefixRateFormSet
    max_num = 40
    extra = 0


class RoutingGroupAdminForm(forms.ModelForm):

    class Meta:
        model = RoutingGroup
        fields = '__all__'


class RoutingGroupAdmin(admin.ModelAdmin):
    form = RoutingGroupAdminForm
    list_display = ['id', 'name', 'status', 'created', 'modified']
    readonly_fields = ['slug', 'status_changed', 'created', 'modified']
    list_filter = ['status']
    search_fields = ['description', '^name']
    fieldsets = (
        (_(u'Ratecard details'), {
            'fields': (
                ('name', 'status'),
            ),
        }),
        (_(u'More -- view description and event dates'), {
            'fields': (
                'description',
                ('created', 'modified'),
                'status_changed',
            ),
            'classes': ('collapse',),
        }),
    )
    inlines = [
        PrefixRuleInline,
        DestinationRuleInline,
        CountryTypeRuleInline,
        CountryRuleInline,
        RegionTypeRuleInline,
        RegionRuleInline,
        DefaultRuleInline,
    ]

admin.site.register(RoutingGroup, RoutingGroupAdmin)


class PrefixRuleAdminForm(forms.ModelForm):

    class Meta:
        model = PrefixRule
        fields = '__all__'


class PrefixRuleAdmin(admin.ModelAdmin):
    form = PrefixRuleAdminForm
    list_display = ['prefix', 'destnum_length']
    readonly_fields = ['prefix', 'destnum_length']

admin.site.register(PrefixRule, PrefixRuleAdmin)


class DestinationRuleAdminForm(forms.ModelForm):

    class Meta:
        model = DestinationRule
        fields = '__all__'


class DestinationRuleAdmin(admin.ModelAdmin):
    form = DestinationRuleAdminForm


admin.site.register(DestinationRule, DestinationRuleAdmin)


class CountryTypeRuleAdminForm(forms.ModelForm):

    class Meta:
        model = CountryTypeRule
        fields = '__all__'


class CountryTypeRuleAdmin(admin.ModelAdmin):
    form = CountryTypeRuleAdminForm


admin.site.register(CountryTypeRule, CountryTypeRuleAdmin)


class CountryRuleAdminForm(forms.ModelForm):

    class Meta:
        model = CountryRule
        fields = '__all__'


class CountryRuleAdmin(admin.ModelAdmin):
    form = CountryRuleAdminForm


admin.site.register(CountryRule, CountryRuleAdmin)


class RegionTypeRuleAdminForm(forms.ModelForm):

    class Meta:
        model = RegionTypeRule
        fields = '__all__'


class RegionTypeRuleAdmin(admin.ModelAdmin):
    form = RegionTypeRuleAdminForm


admin.site.register(RegionTypeRule, RegionTypeRuleAdmin)


class RegionRuleAdminForm(forms.ModelForm):

    class Meta:
        model = RegionRule
        fields = '__all__'


class RegionRuleAdmin(admin.ModelAdmin):
    form = RegionRuleAdminForm


admin.site.register(RegionRule, RegionRuleAdmin)


class DefaultRuleAdminForm(forms.ModelForm):

    class Meta:
        model = DefaultRule
        fields = '__all__'


class DefaultRuleAdmin(admin.ModelAdmin):
    form = DefaultRuleAdminForm


admin.site.register(DefaultRule, DefaultRuleAdmin)
