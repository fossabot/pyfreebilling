import unittest
from django.core.urlresolvers import reverse
from django.test import Client
from .models import Ratecard, Rate, CallerNumList, ProviderRatecard, CustomerRatecard, CustomerPrefixRate, ProviderPrefixRate, CustomerDestinationRate, ProviderDestinationRate, CustomerCountryTypeRate, ProviderCountryTypeRate, CustomerCountryRate, ProviderCountryRate, CustomerRegionTypeRate, ProviderRegionTypeRate, CustomerRegionRate, ProviderRegionRate, CustomerDefaultRate, ProviderDefaultRate
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


def create_ratecard(**kwargs):
    defaults = {}
    defaults["description"] = "description"
    defaults["date_start"] = "date_start"
    defaults["date_end"] = "date_end"
    defaults.update(**kwargs)
    if "callerid_list" not in defaults:
        defaults["callerid_list"] = create_callernumlist()
    return Ratecard.objects.create(**defaults)


def create_rate(**kwargs):
    defaults = {}
    defaults["r_rate"] = "r_rate"
    defaults["r_block_min_duration"] = "r_block_min_duration"
    defaults["r_minimal_time"] = "r_minimal_time"
    defaults["r_init_block"] = "r_init_block"
    defaults["status"] = "status"
    defaults.update(**kwargs)
    return Rate.objects.create(**defaults)


def create_callernumlist(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["callerid_filter"] = "callerid_filter"
    defaults.update(**kwargs)
    if "destination" not in defaults:
        defaults["destination"] = create_direction_models_destination()
    return CallerNumList.objects.create(**defaults)


def create_providerratecard(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["rc_type"] = "rc_type"
    defaults["provider_prefix"] = "provider_prefix"
    defaults["estimated_quality"] = "estimated_quality"
    defaults["status"] = "status"
    defaults["status_changed"] = "status_changed"
    defaults["created"] = "created"
    defaults["modified"] = "modified"
    defaults.update(**kwargs)
    return ProviderRatecard.objects.create(**defaults)


def create_customerratecard(**kwargs):
    defaults = {}
    defaults["rc_type"] = "rc_type"
    defaults["name"] = "name"
    defaults["status"] = "status"
    defaults["status_changed"] = "status_changed"
    defaults["created"] = "created"
    defaults["modified"] = "modified"
    defaults.update(**kwargs)
    return CustomerRatecard.objects.create(**defaults)


def create_customerprefixrate(**kwargs):
    defaults = {}
    defaults["prefix"] = "prefix"
    defaults["destnum_length"] = "destnum_length"
    defaults.update(**kwargs)
    if "c_ratecard" not in defaults:
        defaults["c_ratecard"] = create_customerratecard()
    return CustomerPrefixRate.objects.create(**defaults)


def create_providerprefixrate(**kwargs):
    defaults = {}
    defaults["prefix"] = "prefix"
    defaults["destnum_length"] = "destnum_length"
    defaults.update(**kwargs)
    if "p_ratecard" not in defaults:
        defaults["p_ratecard"] = create_providerratecard()
    return ProviderPrefixRate.objects.create(**defaults)


def create_customerdestinationrate(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    if "c_ratecard" not in defaults:
        defaults["c_ratecard"] = create_customerratecard()
    if "destination" not in defaults:
        defaults["destination"] = create_destination()
    return CustomerDestinationRate.objects.create(**defaults)


def create_providerdestinationrate(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    if "p_ratecard" not in defaults:
        defaults["p_ratecard"] = create_providerratecard()
    if "destination" not in defaults:
        defaults["destination"] = create_destination()
    return ProviderDestinationRate.objects.create(**defaults)


def create_customercountrytyperate(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    if "c_ratecard" not in defaults:
        defaults["c_ratecard"] = create_customerratecard()
    if "country" not in defaults:
        defaults["country"] = create_country()
    if "type" not in defaults:
        defaults["type"] = create_type()
    return CustomerCountryTypeRate.objects.create(**defaults)


def create_providercountrytyperate(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    if "p_ratecard" not in defaults:
        defaults["p_ratecard"] = create_providerratecard()
    if "country" not in defaults:
        defaults["country"] = create_country()
    if "type" not in defaults:
        defaults["type"] = create_type()
    return ProviderCountryTypeRate.objects.create(**defaults)


def create_customercountryrate(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    if "c_ratecard" not in defaults:
        defaults["c_ratecard"] = create_customerratecard()
    if "country" not in defaults:
        defaults["country"] = create_country()
    return CustomerCountryRate.objects.create(**defaults)


def create_providercountryrate(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    if "p_ratecard" not in defaults:
        defaults["p_ratecard"] = create_providerratecard()
    if "country" not in defaults:
        defaults["country"] = create_country()
    return ProviderCountryRate.objects.create(**defaults)


def create_customerregiontyperate(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    if "c_ratecard" not in defaults:
        defaults["c_ratecard"] = create_customerratecard()
    if "region" not in defaults:
        defaults["region"] = create_region()
    if "type" not in defaults:
        defaults["type"] = create_type()
    return CustomerRegionTypeRate.objects.create(**defaults)


def create_providerregiontyperate(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    if "p_ratecard" not in defaults:
        defaults["p_ratecard"] = create_providerratecard()
    if "region" not in defaults:
        defaults["region"] = create_region()
    if "type" not in defaults:
        defaults["type"] = create_type()
    return ProviderRegionTypeRate.objects.create(**defaults)


def create_customerregionrate(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    if "c_ratecard" not in defaults:
        defaults["c_ratecard"] = create_customerratecard()
    if "region" not in defaults:
        defaults["region"] = create_region()
    return CustomerRegionRate.objects.create(**defaults)


def create_providerregionrate(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    if "p_ratecard" not in defaults:
        defaults["p_ratecard"] = create_providerratecard()
    if "region" not in defaults:
        defaults["region"] = create_region()
    return ProviderRegionRate.objects.create(**defaults)


def create_customerdefaultrate(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    if "c_ratecard" not in defaults:
        defaults["c_ratecard"] = create_customerratecard()
    return CustomerDefaultRate.objects.create(**defaults)


def create_providerdefaultrate(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    if "p_ratecard" not in defaults:
        defaults["p_ratecard"] = create_providerratecard()
    return ProviderDefaultRate.objects.create(**defaults)


class RatecardViewTest(unittest.TestCase):
    '''
    Tests for Ratecard
    '''
    def setUp(self):
        self.client = Client()

    def test_list_ratecard(self):
        url = reverse('rate_ratecard_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_ratecard(self):
        url = reverse('rate_ratecard_create')
        data = {
            "description": "description",
            "date_start": "date_start",
            "date_end": "date_end",
            "callerid_list": create_callernumlist().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_ratecard(self):
        ratecard = create_ratecard()
        url = reverse('rate_ratecard_detail', args=[ratecard.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_ratecard(self):
        ratecard = create_ratecard()
        data = {
            "description": "description",
            "date_start": "date_start",
            "date_end": "date_end",
            "callerid_list": create_callernumlist().pk,
        }
        url = reverse('rate_ratecard_update', args=[ratecard.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class RateViewTest(unittest.TestCase):
    '''
    Tests for Rate
    '''
    def setUp(self):
        self.client = Client()

    def test_list_rate(self):
        url = reverse('rate_rate_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_rate(self):
        url = reverse('rate_rate_create')
        data = {
            "r_rate": "r_rate",
            "r_block_min_duration": "r_block_min_duration",
            "r_minimal_time": "r_minimal_time",
            "r_init_block": "r_init_block",
            "status": "status",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_rate(self):
        rate = create_rate()
        url = reverse('rate_rate_detail', args=[rate.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_rate(self):
        rate = create_rate()
        data = {
            "r_rate": "r_rate",
            "r_block_min_duration": "r_block_min_duration",
            "r_minimal_time": "r_minimal_time",
            "r_init_block": "r_init_block",
            "status": "status",
        }
        url = reverse('rate_rate_update', args=[rate.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class CallerNumListViewTest(unittest.TestCase):
    '''
    Tests for CallerNumList
    '''
    def setUp(self):
        self.client = Client()

    def test_list_callernumlist(self):
        url = reverse('rate_callernumlist_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_callernumlist(self):
        url = reverse('rate_callernumlist_create')
        data = {
            "name": "name",
            "callerid_filter": "callerid_filter",
            "destination": create_direction_models_destination().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_callernumlist(self):
        callernumlist = create_callernumlist()
        url = reverse('rate_callernumlist_detail', args=[callernumlist.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_callernumlist(self):
        callernumlist = create_callernumlist()
        data = {
            "name": "name",
            "callerid_filter": "callerid_filter",
            "destination": create_direction_models_destination().pk,
        }
        url = reverse('rate_callernumlist_update', args=[callernumlist.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class ProviderRatecardViewTest(unittest.TestCase):
    '''
    Tests for ProviderRatecard
    '''
    def setUp(self):
        self.client = Client()

    def test_list_providerratecard(self):
        url = reverse('rate_providerratecard_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_providerratecard(self):
        url = reverse('rate_providerratecard_create')
        data = {
            "name": "name",
            "rc_type": "rc_type",
            "provider_prefix": "provider_prefix",
            "estimated_quality": "estimated_quality",
            "status": "status",
            "status_changed": "status_changed",
            "created": "created",
            "modified": "modified",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_providerratecard(self):
        providerratecard = create_providerratecard()
        url = reverse('rate_providerratecard_detail', args=[providerratecard.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_providerratecard(self):
        providerratecard = create_providerratecard()
        data = {
            "name": "name",
            "rc_type": "rc_type",
            "provider_prefix": "provider_prefix",
            "estimated_quality": "estimated_quality",
            "status": "status",
            "status_changed": "status_changed",
            "created": "created",
            "modified": "modified",
        }
        url = reverse('rate_providerratecard_update', args=[providerratecard.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class CustomerRatecardViewTest(unittest.TestCase):
    '''
    Tests for CustomerRatecard
    '''
    def setUp(self):
        self.client = Client()

    def test_list_customerratecard(self):
        url = reverse('rate_customerratecard_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_customerratecard(self):
        url = reverse('rate_customerratecard_create')
        data = {
            "rc_type": "rc_type",
            "name": "name",
            "status": "status",
            "status_changed": "status_changed",
            "created": "created",
            "modified": "modified",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_customerratecard(self):
        customerratecard = create_customerratecard()
        url = reverse('rate_customerratecard_detail', args=[customerratecard.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_customerratecard(self):
        customerratecard = create_customerratecard()
        data = {
            "rc_type": "rc_type",
            "name": "name",
            "status": "status",
            "status_changed": "status_changed",
            "created": "created",
            "modified": "modified",
        }
        url = reverse('rate_customerratecard_update', args=[customerratecard.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class CustomerPrefixRateViewTest(unittest.TestCase):
    '''
    Tests for CustomerPrefixRate
    '''
    def setUp(self):
        self.client = Client()

    def test_list_customerprefixrate(self):
        url = reverse('rate_customerprefixrate_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_customerprefixrate(self):
        url = reverse('rate_customerprefixrate_create')
        data = {
            "prefix": "prefix",
            "destnum_length": "destnum_length",
            "c_ratecard": create_customerratecard().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_customerprefixrate(self):
        customerprefixrate = create_customerprefixrate()
        url = reverse('rate_customerprefixrate_detail', args=[customerprefixrate.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_customerprefixrate(self):
        customerprefixrate = create_customerprefixrate()
        data = {
            "prefix": "prefix",
            "destnum_length": "destnum_length",
            "c_ratecard": create_customerratecard().pk,
        }
        url = reverse('rate_customerprefixrate_update', args=[customerprefixrate.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class ProviderPrefixRateViewTest(unittest.TestCase):
    '''
    Tests for ProviderPrefixRate
    '''
    def setUp(self):
        self.client = Client()

    def test_list_providerprefixrate(self):
        url = reverse('rate_providerprefixrate_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_providerprefixrate(self):
        url = reverse('rate_providerprefixrate_create')
        data = {
            "prefix": "prefix",
            "destnum_length": "destnum_length",
            "p_ratecard": create_providerratecard().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_providerprefixrate(self):
        providerprefixrate = create_providerprefixrate()
        url = reverse('rate_providerprefixrate_detail', args=[providerprefixrate.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_providerprefixrate(self):
        providerprefixrate = create_providerprefixrate()
        data = {
            "prefix": "prefix",
            "destnum_length": "destnum_length",
            "p_ratecard": create_providerratecard().pk,
        }
        url = reverse('rate_providerprefixrate_update', args=[providerprefixrate.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class CustomerDestinationRateViewTest(unittest.TestCase):
    '''
    Tests for CustomerDestinationRate
    '''
    def setUp(self):
        self.client = Client()

    def test_list_customerdestinationrate(self):
        url = reverse('rate_customerdestinationrate_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_customerdestinationrate(self):
        url = reverse('rate_customerdestinationrate_create')
        data = {
            "c_ratecard": create_customerratecard().pk,
            "destination": create_destination().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_customerdestinationrate(self):
        customerdestinationrate = create_customerdestinationrate()
        url = reverse('rate_customerdestinationrate_detail', args=[customerdestinationrate.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_customerdestinationrate(self):
        customerdestinationrate = create_customerdestinationrate()
        data = {
            "c_ratecard": create_customerratecard().pk,
            "destination": create_destination().pk,
        }
        url = reverse('rate_customerdestinationrate_update', args=[customerdestinationrate.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class ProviderDestinationRateViewTest(unittest.TestCase):
    '''
    Tests for ProviderDestinationRate
    '''
    def setUp(self):
        self.client = Client()

    def test_list_providerdestinationrate(self):
        url = reverse('rate_providerdestinationrate_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_providerdestinationrate(self):
        url = reverse('rate_providerdestinationrate_create')
        data = {
            "p_ratecard": create_providerratecard().pk,
            "destination": create_destination().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_providerdestinationrate(self):
        providerdestinationrate = create_providerdestinationrate()
        url = reverse('rate_providerdestinationrate_detail', args=[providerdestinationrate.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_providerdestinationrate(self):
        providerdestinationrate = create_providerdestinationrate()
        data = {
            "p_ratecard": create_providerratecard().pk,
            "destination": create_destination().pk,
        }
        url = reverse('rate_providerdestinationrate_update', args=[providerdestinationrate.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class CustomerCountryTypeRateViewTest(unittest.TestCase):
    '''
    Tests for CustomerCountryTypeRate
    '''
    def setUp(self):
        self.client = Client()

    def test_list_customercountrytyperate(self):
        url = reverse('rate_customercountrytyperate_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_customercountrytyperate(self):
        url = reverse('rate_customercountrytyperate_create')
        data = {
            "c_ratecard": create_customerratecard().pk,
            "country": create_country().pk,
            "type": create_type().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_customercountrytyperate(self):
        customercountrytyperate = create_customercountrytyperate()
        url = reverse('rate_customercountrytyperate_detail', args=[customercountrytyperate.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_customercountrytyperate(self):
        customercountrytyperate = create_customercountrytyperate()
        data = {
            "c_ratecard": create_customerratecard().pk,
            "country": create_country().pk,
            "type": create_type().pk,
        }
        url = reverse('rate_customercountrytyperate_update', args=[customercountrytyperate.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class ProviderCountryTypeRateViewTest(unittest.TestCase):
    '''
    Tests for ProviderCountryTypeRate
    '''
    def setUp(self):
        self.client = Client()

    def test_list_providercountrytyperate(self):
        url = reverse('rate_providercountrytyperate_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_providercountrytyperate(self):
        url = reverse('rate_providercountrytyperate_create')
        data = {
            "p_ratecard": create_providerratecard().pk,
            "country": create_country().pk,
            "type": create_type().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_providercountrytyperate(self):
        providercountrytyperate = create_providercountrytyperate()
        url = reverse('rate_providercountrytyperate_detail', args=[providercountrytyperate.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_providercountrytyperate(self):
        providercountrytyperate = create_providercountrytyperate()
        data = {
            "p_ratecard": create_providerratecard().pk,
            "country": create_country().pk,
            "type": create_type().pk,
        }
        url = reverse('rate_providercountrytyperate_update', args=[providercountrytyperate.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class CustomerCountryRateViewTest(unittest.TestCase):
    '''
    Tests for CustomerCountryRate
    '''
    def setUp(self):
        self.client = Client()

    def test_list_customercountryrate(self):
        url = reverse('rate_customercountryrate_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_customercountryrate(self):
        url = reverse('rate_customercountryrate_create')
        data = {
            "c_ratecard": create_customerratecard().pk,
            "country": create_country().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_customercountryrate(self):
        customercountryrate = create_customercountryrate()
        url = reverse('rate_customercountryrate_detail', args=[customercountryrate.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_customercountryrate(self):
        customercountryrate = create_customercountryrate()
        data = {
            "c_ratecard": create_customerratecard().pk,
            "country": create_country().pk,
        }
        url = reverse('rate_customercountryrate_update', args=[customercountryrate.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class ProviderCountryRateViewTest(unittest.TestCase):
    '''
    Tests for ProviderCountryRate
    '''
    def setUp(self):
        self.client = Client()

    def test_list_providercountryrate(self):
        url = reverse('rate_providercountryrate_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_providercountryrate(self):
        url = reverse('rate_providercountryrate_create')
        data = {
            "p_ratecard": create_providerratecard().pk,
            "country": create_country().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_providercountryrate(self):
        providercountryrate = create_providercountryrate()
        url = reverse('rate_providercountryrate_detail', args=[providercountryrate.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_providercountryrate(self):
        providercountryrate = create_providercountryrate()
        data = {
            "p_ratecard": create_providerratecard().pk,
            "country": create_country().pk,
        }
        url = reverse('rate_providercountryrate_update', args=[providercountryrate.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class CustomerRegionTypeRateViewTest(unittest.TestCase):
    '''
    Tests for CustomerRegionTypeRate
    '''
    def setUp(self):
        self.client = Client()

    def test_list_customerregiontyperate(self):
        url = reverse('rate_customerregiontyperate_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_customerregiontyperate(self):
        url = reverse('rate_customerregiontyperate_create')
        data = {
            "c_ratecard": create_customerratecard().pk,
            "region": create_region().pk,
            "type": create_type().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_customerregiontyperate(self):
        customerregiontyperate = create_customerregiontyperate()
        url = reverse('rate_customerregiontyperate_detail', args=[customerregiontyperate.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_customerregiontyperate(self):
        customerregiontyperate = create_customerregiontyperate()
        data = {
            "c_ratecard": create_customerratecard().pk,
            "region": create_region().pk,
            "type": create_type().pk,
        }
        url = reverse('rate_customerregiontyperate_update', args=[customerregiontyperate.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class ProviderRegionTypeRateViewTest(unittest.TestCase):
    '''
    Tests for ProviderRegionTypeRate
    '''
    def setUp(self):
        self.client = Client()

    def test_list_providerregiontyperate(self):
        url = reverse('rate_providerregiontyperate_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_providerregiontyperate(self):
        url = reverse('rate_providerregiontyperate_create')
        data = {
            "p_ratecard": create_providerratecard().pk,
            "region": create_region().pk,
            "type": create_type().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_providerregiontyperate(self):
        providerregiontyperate = create_providerregiontyperate()
        url = reverse('rate_providerregiontyperate_detail', args=[providerregiontyperate.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_providerregiontyperate(self):
        providerregiontyperate = create_providerregiontyperate()
        data = {
            "p_ratecard": create_providerratecard().pk,
            "region": create_region().pk,
            "type": create_type().pk,
        }
        url = reverse('rate_providerregiontyperate_update', args=[providerregiontyperate.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class CustomerRegionRateViewTest(unittest.TestCase):
    '''
    Tests for CustomerRegionRate
    '''
    def setUp(self):
        self.client = Client()

    def test_list_customerregionrate(self):
        url = reverse('rate_customerregionrate_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_customerregionrate(self):
        url = reverse('rate_customerregionrate_create')
        data = {
            "c_ratecard": create_customerratecard().pk,
            "region": create_region().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_customerregionrate(self):
        customerregionrate = create_customerregionrate()
        url = reverse('rate_customerregionrate_detail', args=[customerregionrate.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_customerregionrate(self):
        customerregionrate = create_customerregionrate()
        data = {
            "c_ratecard": create_customerratecard().pk,
            "region": create_region().pk,
        }
        url = reverse('rate_customerregionrate_update', args=[customerregionrate.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class ProviderRegionRateViewTest(unittest.TestCase):
    '''
    Tests for ProviderRegionRate
    '''
    def setUp(self):
        self.client = Client()

    def test_list_providerregionrate(self):
        url = reverse('rate_providerregionrate_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_providerregionrate(self):
        url = reverse('rate_providerregionrate_create')
        data = {
            "p_ratecard": create_providerratecard().pk,
            "region": create_region().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_providerregionrate(self):
        providerregionrate = create_providerregionrate()
        url = reverse('rate_providerregionrate_detail', args=[providerregionrate.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_providerregionrate(self):
        providerregionrate = create_providerregionrate()
        data = {
            "p_ratecard": create_providerratecard().pk,
            "region": create_region().pk,
        }
        url = reverse('rate_providerregionrate_update', args=[providerregionrate.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class CustomerDefaultRateViewTest(unittest.TestCase):
    '''
    Tests for CustomerDefaultRate
    '''
    def setUp(self):
        self.client = Client()

    def test_list_customerdefaultrate(self):
        url = reverse('rate_customerdefaultrate_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_customerdefaultrate(self):
        url = reverse('rate_customerdefaultrate_create')
        data = {
            "c_ratecard": create_customerratecard().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_customerdefaultrate(self):
        customerdefaultrate = create_customerdefaultrate()
        url = reverse('rate_customerdefaultrate_detail', args=[customerdefaultrate.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_customerdefaultrate(self):
        customerdefaultrate = create_customerdefaultrate()
        data = {
            "c_ratecard": create_customerratecard().pk,
        }
        url = reverse('rate_customerdefaultrate_update', args=[customerdefaultrate.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


class ProviderDefaultRateViewTest(unittest.TestCase):
    '''
    Tests for ProviderDefaultRate
    '''
    def setUp(self):
        self.client = Client()

    def test_list_providerdefaultrate(self):
        url = reverse('rate_providerdefaultrate_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_providerdefaultrate(self):
        url = reverse('rate_providerdefaultrate_create')
        data = {
            "p_ratecard": create_providerratecard().pk,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_providerdefaultrate(self):
        providerdefaultrate = create_providerdefaultrate()
        url = reverse('rate_providerdefaultrate_detail', args=[providerdefaultrate.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_providerdefaultrate(self):
        providerdefaultrate = create_providerdefaultrate()
        data = {
            "p_ratecard": create_providerratecard().pk,
        }
        url = reverse('rate_providerdefaultrate_update', args=[providerdefaultrate.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
