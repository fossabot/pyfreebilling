import unittest
from django.core.urlresolvers import reverse
from django.test import Client
from .models import Rule, RoutingGroup, PrefixRule, DestinationRule, CountryTypeRule, CountryRule, RegionTypeRule, RegionRule, DefaultRule
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType


def create_django_contrib_auth_models_user(**kwargs):
    defaults = {}
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_django_contrib_auth_models_group(**kwargs):
    defaults = {}
    defaults["name"] = "group"
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_django_contrib_contenttypes_models_contenttype(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_rule(**kwargs):
    defaults = {}
    defaults["status"] = "status"
    defaults["route_type"] = "route_type"
    defaults["weight"] = "weight"
    defaults["priority"] = "priority"
    defaults.update(**kwargs)
    if "provider_ratecard" not in defaults:
        defaults["provider_ratecard"] = create_providerratecard()
    if "provider_gateway_list" not in defaults:
        defaults["provider_gateway_list"] = create_sofiagateway()
    return Rule.objects.create(**defaults)


def create_routinggroup(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["status"] = "status"
    defaults["status_changed"] = "status_changed"
    defaults["created"] = "created"
    defaults["modified"] = "modified"
    defaults["description"] = "description"
    defaults.update(**kwargs)
    return RoutingGroup.objects.create(**defaults)


def create_prefixrule(**kwargs):
    defaults = {}
    defaults["prefix"] = "prefix"
    defaults["destnum_length"] = "destnum_length"
    defaults.update(**kwargs)
    if "c_route" not in defaults:
        defaults["c_route"] = create_routinggroup()
    return PrefixRule.objects.create(**defaults)


def create_destinationrule(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    if "c_route" not in defaults:
        defaults["c_route"] = create_routinggroup()
    if "destination" not in defaults:
        defaults["destination"] = create_destination()
    return DestinationRule.objects.create(**defaults)


def create_countrytyperule(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    if "c_route" not in defaults:
        defaults["c_route"] = create_routinggroup()
    if "country" not in defaults:
        defaults["country"] = create_country()
    if "type" not in defaults:
        defaults["type"] = create_type()
    return CountryTypeRule.objects.create(**defaults)


def create_countryrule(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    if "c_route" not in defaults:
        defaults["c_route"] = create_routinggroup()
    if "country" not in defaults:
        defaults["country"] = create_country()
    return CountryRule.objects.create(**defaults)


def create_regiontyperule(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    if "c_route" not in defaults:
        defaults["c_route"] = create_routinggroup()
    if "region" not in defaults:
        defaults["region"] = create_region()
    if "type" not in defaults:
        defaults["type"] = create_type()
    return RegionTypeRule.objects.create(**defaults)


def create_regionrule(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    if "c_route" not in defaults:
        defaults["c_route"] = create_routinggroup()
    if "region" not in defaults:
        defaults["region"] = create_region()
    return RegionRule.objects.create(**defaults)


def create_defaultrule(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    if "c_route" not in defaults:
        defaults["c_route"] = create_routinggroup()
    return DefaultRule.objects.create(**defaults)


class RuleViewTest(unittest.TestCase):
    '''
    Tests for Rule
    '''
    def setUp(self):
        self.client = Client()

    def test_list_rule(self):
        url = reverse('route_rule_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_rule(self):
        url = reverse('route_rule_create')
        data = {
            "status": "status",
            "route_type": "route_type",
            "weight": "weight",
            "priority": "priority",
            "provider_ratecard": create_providerratecard().pk,
            "provider_gateway_list": create_sofiagateway().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_rule(self):
        rule = create_rule()
        url = reverse('route_rule_detail', args=[rule.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_rule(self):
        rule = create_rule()
        data = {
            "status": "status",
            "route_type": "route_type",
            "weight": "weight",
            "priority": "priority",
            "provider_ratecard": create_providerratecard().pk,
            "provider_gateway_list": create_sofiagateway().pk,
        }
        url = reverse('route_rule_update', args=[rule.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class RoutingGroupViewTest(unittest.TestCase):
    '''
    Tests for RoutingGroup
    '''
    def setUp(self):
        self.client = Client()

    def test_list_routinggroup(self):
        url = reverse('route_routinggroup_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_routinggroup(self):
        url = reverse('route_routinggroup_create')
        data = {
            "name": "name",
            "status": "status",
            "status_changed": "status_changed",
            "created": "created",
            "modified": "modified",
            "description": "description",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_routinggroup(self):
        routinggroup = create_routinggroup()
        url = reverse('route_routinggroup_detail', args=[routinggroup.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_routinggroup(self):
        routinggroup = create_routinggroup()
        data = {
            "name": "name",
            "status": "status",
            "status_changed": "status_changed",
            "created": "created",
            "modified": "modified",
            "description": "description",
        }
        url = reverse('route_routinggroup_update', args=[routinggroup.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class PrefixRuleViewTest(unittest.TestCase):
    '''
    Tests for PrefixRule
    '''
    def setUp(self):
        self.client = Client()

    def test_list_prefixrule(self):
        url = reverse('route_prefixrule_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_prefixrule(self):
        url = reverse('route_prefixrule_create')
        data = {
            "prefix": "prefix",
            "destnum_length": "destnum_length",
            "c_route": create_routinggroup().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_prefixrule(self):
        prefixrule = create_prefixrule()
        url = reverse('route_prefixrule_detail', args=[prefixrule.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_prefixrule(self):
        prefixrule = create_prefixrule()
        data = {
            "prefix": "prefix",
            "destnum_length": "destnum_length",
            "c_route": create_routinggroup().pk,
        }
        url = reverse('route_prefixrule_update', args=[prefixrule.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class DestinationRuleViewTest(unittest.TestCase):
    '''
    Tests for DestinationRule
    '''
    def setUp(self):
        self.client = Client()

    def test_list_destinationrule(self):
        url = reverse('route_destinationrule_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_destinationrule(self):
        url = reverse('route_destinationrule_create')
        data = {
            "c_route": create_routinggroup().pk,
            "destination": create_destination().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_destinationrule(self):
        destinationrule = create_destinationrule()
        url = reverse('route_destinationrule_detail', args=[destinationrule.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_destinationrule(self):
        destinationrule = create_destinationrule()
        data = {
            "c_route": create_routinggroup().pk,
            "destination": create_destination().pk,
        }
        url = reverse('route_destinationrule_update', args=[destinationrule.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class CountryTypeRuleViewTest(unittest.TestCase):
    '''
    Tests for CountryTypeRule
    '''
    def setUp(self):
        self.client = Client()

    def test_list_countrytyperule(self):
        url = reverse('route_countrytyperule_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_countrytyperule(self):
        url = reverse('route_countrytyperule_create')
        data = {
            "c_route": create_routinggroup().pk,
            "country": create_country().pk,
            "type": create_type().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_countrytyperule(self):
        countrytyperule = create_countrytyperule()
        url = reverse('route_countrytyperule_detail', args=[countrytyperule.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_countrytyperule(self):
        countrytyperule = create_countrytyperule()
        data = {
            "c_route": create_routinggroup().pk,
            "country": create_country().pk,
            "type": create_type().pk,
        }
        url = reverse('route_countrytyperule_update', args=[countrytyperule.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class CountryRuleViewTest(unittest.TestCase):
    '''
    Tests for CountryRule
    '''
    def setUp(self):
        self.client = Client()

    def test_list_countryrule(self):
        url = reverse('route_countryrule_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_countryrule(self):
        url = reverse('route_countryrule_create')
        data = {
            "c_route": create_routinggroup().pk,
            "country": create_country().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_countryrule(self):
        countryrule = create_countryrule()
        url = reverse('route_countryrule_detail', args=[countryrule.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_countryrule(self):
        countryrule = create_countryrule()
        data = {
            "c_route": create_routinggroup().pk,
            "country": create_country().pk,
        }
        url = reverse('route_countryrule_update', args=[countryrule.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class RegionTypeRuleViewTest(unittest.TestCase):
    '''
    Tests for RegionTypeRule
    '''
    def setUp(self):
        self.client = Client()

    def test_list_regiontyperule(self):
        url = reverse('route_regiontyperule_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_regiontyperule(self):
        url = reverse('route_regiontyperule_create')
        data = {
            "c_route": create_routinggroup().pk,
            "region": create_region().pk,
            "type": create_type().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_regiontyperule(self):
        regiontyperule = create_regiontyperule()
        url = reverse('route_regiontyperule_detail', args=[regiontyperule.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_regiontyperule(self):
        regiontyperule = create_regiontyperule()
        data = {
            "c_route": create_routinggroup().pk,
            "region": create_region().pk,
            "type": create_type().pk,
        }
        url = reverse('route_regiontyperule_update', args=[regiontyperule.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class RegionRuleViewTest(unittest.TestCase):
    '''
    Tests for RegionRule
    '''
    def setUp(self):
        self.client = Client()

    def test_list_regionrule(self):
        url = reverse('route_regionrule_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_regionrule(self):
        url = reverse('route_regionrule_create')
        data = {
            "c_route": create_routinggroup().pk,
            "region": create_region().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_regionrule(self):
        regionrule = create_regionrule()
        url = reverse('route_regionrule_detail', args=[regionrule.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_regionrule(self):
        regionrule = create_regionrule()
        data = {
            "c_route": create_routinggroup().pk,
            "region": create_region().pk,
        }
        url = reverse('route_regionrule_update', args=[regionrule.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class DefaultRuleViewTest(unittest.TestCase):
    '''
    Tests for DefaultRule
    '''
    def setUp(self):
        self.client = Client()

    def test_list_defaultrule(self):
        url = reverse('route_defaultrule_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_defaultrule(self):
        url = reverse('route_defaultrule_create')
        data = {
            "c_route": create_routinggroup().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_defaultrule(self):
        defaultrule = create_defaultrule()
        url = reverse('route_defaultrule_detail', args=[defaultrule.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_defaultrule(self):
        defaultrule = create_defaultrule()
        data = {
            "c_route": create_routinggroup().pk,
        }
        url = reverse('route_defaultrule_update', args=[defaultrule.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


