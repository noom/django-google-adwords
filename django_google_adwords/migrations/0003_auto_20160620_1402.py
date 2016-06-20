# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_google_adwords', '0002_auto_20160502_1136'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dailyadgroupmetrics',
            name='max_cpa_converted_clicks',
        ),
        migrations.RemoveField(
            model_name='dailyadgroupmetrics',
            name='max_cpa_converted_clicks_currency',
        ),
    ]
