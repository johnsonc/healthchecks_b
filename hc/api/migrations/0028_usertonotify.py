# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-11 09:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0027_auto_20160930_0455'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserToNotify',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Check')),
                ('recepient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
