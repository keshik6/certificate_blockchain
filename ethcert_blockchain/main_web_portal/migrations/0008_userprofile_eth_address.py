# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-04-05 17:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_web_portal', '0007_auto_20180405_2216'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='eth_address',
            field=models.CharField(default='NA', max_length=64),
        ),
    ]