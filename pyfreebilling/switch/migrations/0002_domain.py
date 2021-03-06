# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-11-16 17:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('switch', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.CharField(help_text='SIP domain', max_length=64, verbose_name='Domain')),
                ('did', models.CharField(help_text='Unique identifier for the domain.', max_length=64, verbose_name='Domain identifier')),
                ('flags', models.IntegerField(choices=[(0, 'Default'), (1, 'Disabled'), (2, 'Canonical'), (3, 'Allowed_to'), (4, 'Allowed_From'), (5, 'For_serweb'), (6, 'Pending'), (7, 'Deleted'), (8, 'Caller_deleted'), (9, 'Calle_deleted')], default=b'0', help_text='Kamailio flags.', verbose_name='flags')),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='date added')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='date modified')),
            ],
            options={
                'ordering': ('domain',),
                'db_table': 'uid_domain',
                'verbose_name': 'SIP domain',
                'verbose_name_plural': 'SIP domains',
            },
        ),
    ]
