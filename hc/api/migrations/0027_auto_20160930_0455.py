# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-30 04:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0026_auto_20160415_1824'),
    ]

    operations = [
        migrations.AddField(
            model_name='channel',
            name='telegram_id',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='channel',
            name='kind',
            field=models.CharField(choices=[('email', 'Email'), ('webhook', 'Webhook'), ('hipchat', 'HipChat'), ('telegram', 'Telegram'), ('slack', 'Slack'), ('pd', 'PagerDuty'), ('po', 'Pushover'), ('victorops', 'VictorOps')], max_length=20),
        ),
    ]
