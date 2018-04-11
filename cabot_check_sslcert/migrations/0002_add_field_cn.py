# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cabotapp', '0006_auto_20170821_1000'),
        ('cabot_check_sslcert', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='SslcertStatusCheck',
            name='common_name',
            field=models.TextField(
                help_text=b'Common name to check.',
                null=True,
                blank=True,
                default=None)
        ),
    ]
