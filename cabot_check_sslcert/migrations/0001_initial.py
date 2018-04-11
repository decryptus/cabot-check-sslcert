# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cabotapp', '0006_auto_20170821_1000'),
    ]

    operations = [
        migrations.CreateModel(
            name='SslcertStatusCheck',
            fields=[
                ('statuscheck_ptr',
                 models.OneToOneField(
                    auto_created=True,
                    on_delete=django.db.models.deletion.CASCADE,
                    parent_link=True,
                    primary_key=True,
                    serialize=False,
                    to='cabotapp.StatusCheck')),
                ('host',
                 models.TextField(
                    help_text=b'Host to check.',
                    null=False,
                    blank=False)),
                ('port',
                 models.PositiveIntegerField(
                    help_text=b'Port to check.',
                    null=False,
                    blank=False,
                    default=443)),
                ('common_name',
                 models.TextField(
                    help_text=b'Common name to check.',
                    null=True,
                    blank=True,
                    default=None)),
                ('days',
                 models.PositiveIntegerField(
                    help_text=b'Days before expiration.',
                    null=False,
                    blank=False,
                    default=60)),
            ],
            options={
                'abstract': False,
            },
            bases=('cabotapp.statuscheck',),
        ),
    ]
