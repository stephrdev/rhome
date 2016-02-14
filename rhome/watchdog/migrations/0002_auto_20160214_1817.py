# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models  # noqa


class Migration(migrations.Migration):

    dependencies = [
        ('watchdog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='watchdog',
            options={'verbose_name_plural': 'Watchdogs', 'ordering': ('metric',), 'permissions': (('check_watchdog', 'Can check Watchdog'),), 'verbose_name': 'Watchdog'},
        ),
    ]
