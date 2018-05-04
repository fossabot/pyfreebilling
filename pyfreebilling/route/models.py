# Copyright 2018 Mathias WOLFF
# This file is part of pyfreebilling.
#
# pyfreebilling is free software: you can redistribute it and/or modify
# it under the terms of the Affero GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pyfreebilling is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with pyfreebilling.  If not, see <http://www.gnu.org/licenses/>

from django.core.validators import MaxValueValidator
from django.core.urlresolvers import reverse
from django.db import models as models
from django.db.models import *
from django.conf import settings
from django.contrib.postgres.fields import DateTimeRangeField
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from django_extensions.db import fields as extension_fields
from django_extensions.db.fields import AutoSlugField

from model_utils.models import StatusModel, TimeStampedModel
from model_utils import Choices

from partial_index import PartialIndex

from pyfreebilling.direction.models import Country, Destination, Region, Type
from pyfreebilling.pyfreebill.models import SofiaGateway
from pyfreebilling.rate.models import ProviderRatecard


class RoutingGroup(StatusModel, TimeStampedModel):

    # Choices
    STATUS = Choices(
        ('enabled', _(u"Enabled")),
        ('disabled', _(u"Disabled")),
    )

    # Fields
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField(_(u'description'), blank=True)


    class Meta:
        db_table = 'route_routinggroup'
        app_label = 'route'
        ordering = ('name',)

    def __unicode__(self):
        return u'%s' % self.name

    def get_absolute_url(self):
        return reverse('route_routinggroup_detail', args=(self.slug,))


    def get_update_url(self):
        return reverse('route_routinggroup_update', args=(self.slug,))


class RuleModel(models.Model):

    # Choices
    LCR_TYPE_CHOICES = Choices(
        ('LCR', _(u"Least cost")),
        ('PRIO', _(u"Priority")),
        ('WEIGHT', _(u"Weight")),
        ('QUALITY', _(u"Quality")),
    )
    STATUS_CHOICES = Choices(
        ('enabled', _(u"Enabled")),
        ('disabled', _(u"Disabled")),
        ('blocked', _(u"Blocked")),
    )

    # Fields
    status = models.CharField(_(u"Status"), max_length=20, default=STATUS_CHOICES.enabled, choices=STATUS_CHOICES, help_text=_(u"State of the rate : enabled / blocked - calls to this destination are blocked / disabled"))
    route_type = models.CharField(_(u"route type"), max_length=10, choices=LCR_TYPE_CHOICES, default=LCR_TYPE_CHOICES.LCR)
    weight = models.PositiveIntegerField(default=1)
    priority = models.PositiveIntegerField(default=1)

    # Relationship Fields
    provider_ratecard = models.ForeignKey(
        ProviderRatecard,
        on_delete=models.PROTECT
    )
    provider_gateway_list = models.ManyToManyField(SofiaGateway)

    class Meta:
        abstract = True


class PrefixRule(TimeStampedModel, RuleModel):

    # Fields
    prefix = models.CharField(_(u'numeric prefix'), max_length=30, db_index=True)
    destnum_length = models.PositiveSmallIntegerField(_(u'Destination number length'), default=0, help_text=_(u"If value > 0, then destination number must match tsi length"))

    # Relationship Fields
    c_route = models.ForeignKey(RoutingGroup, on_delete=models.CASCADE)

    class Meta:
        db_table = 'route_prefix_rule'
        app_label = 'route'
        ordering = ('prefix', '-destnum_length')
        unique_together = [
            ['c_route', 'prefix', 'destnum_length', 'provider_ratecard'],
        ]
        indexes = [
            PartialIndex(
                fields=['c_route', 'prefix', 'destnum_length', 'provider_ratecard'],
                unique=True,
                where='status <> \'disabled\''
            ),
        ]

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('route_prefixrule_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('route_prefixrule_update', args=(self.pk,))


class DestinationRule(TimeStampedModel, RuleModel):


    # Relationship Fields
    c_route = models.ForeignKey(RoutingGroup, on_delete=models.CASCADE)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)

    class Meta:
        db_table = 'route_destination_rule'
        app_label = 'route'
        ordering = ('destination',)
        unique_together = [
            ['c_route', 'destination', 'provider_ratecard'],
        ]
        indexes = [
            PartialIndex(
                fields=['c_route', 'destination', 'provider_ratecard'],
                unique=True,
                where='status <> \'disabled\''
            ),
        ]

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('route_destinationrule_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('route_destinationrule_update', args=(self.pk,))


class CountryTypeRule(TimeStampedModel, RuleModel):


    # Relationship Fields
    c_route = models.ForeignKey(RoutingGroup, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)

    class Meta:
        db_table = 'route_countrytype_rule'
        app_label = 'route'
        ordering = ('country', 'type')
        unique_together = [
            ['c_route', 'country', 'type', 'provider_ratecard'],
        ]
        indexes = [
            PartialIndex(
                fields=['c_route', 'country', 'type', 'provider_ratecard'],
                unique=True,
                where='status <> \'disabled\''
            ),
        ]

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('route_countrytyperule_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('route_countrytyperule_update', args=(self.pk,))


class CountryRule(TimeStampedModel, RuleModel):


    # Relationship Fields
    c_route = models.ForeignKey(RoutingGroup, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    class Meta:
        db_table = 'route_countryrule'
        app_label = 'route'
        ordering = ('country',)
        unique_together = [
            ['c_route', 'country', 'provider_ratecard'],
        ]
        indexes = [
            PartialIndex(
                fields=['c_route', 'country', 'provider_ratecard'],
                unique=True,
                where='status <> \'disabled\''
            ),
        ]

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('route_countryrule_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('route_countryrule_update', args=(self.pk,))


class RegionTypeRule(TimeStampedModel, RuleModel):


    # Relationship Fields
    c_route = models.ForeignKey(RoutingGroup, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE)

    class Meta:
        db_table = 'route_regiontype_rule'
        app_label = 'route'
        ordering = ('region', 'type')
        unique_together = [
            ['c_route', 'region', 'type', 'provider_ratecard'],
        ]
        indexes = [
            PartialIndex(
                fields=['c_route', 'region', 'type', 'provider_ratecard'],
                unique=True,
                where='status <> \'disabled\''
            ),
        ]

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('route_regiontyperule_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('route_regiontyperule_update', args=(self.pk,))


class RegionRule(TimeStampedModel, RuleModel):


    # Relationship Fields
    c_route = models.ForeignKey(RoutingGroup, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    class Meta:
        db_table = 'route_region_rule'
        app_label = 'route'
        ordering = ('region',)
        unique_together = [
            ['c_route', 'region', 'provider_ratecard'],
        ]
        indexes = [
            PartialIndex(
                fields=['c_route', 'region', 'provider_ratecard'],
                unique=True,
                where='status <> \'disabled\''
            ),
        ]

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('route_regionrule_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('route_regionrule_update', args=(self.pk,))


class DefaultRule(TimeStampedModel, RuleModel):


    # Relationship Fields
    c_route = models.ForeignKey(RoutingGroup, on_delete=models.CASCADE)

    class Meta:
        db_table = 'route_default_rule'
        app_label = 'route'
        ordering = ('-pk',)
        unique_together = [
            ['c_route', 'provider_ratecard'],
            # Pour une destination, le route_type doit-etre identique
        ]
        indexes = [
            PartialIndex(
                fields=['c_route', 'provider_ratecard'],
                unique=True,
                where='status <> \'disabled\''
            ),
        ]

    def __unicode__(self):
        return u'%s' % self.pk

    def get_absolute_url(self):
        return reverse('route_defaultrule_detail', args=(self.pk,))


    def get_update_url(self):
        return reverse('route_defaultrule_update', args=(self.pk,))
