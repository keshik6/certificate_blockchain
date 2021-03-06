# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-04-18 16:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certificate_id', models.IntegerField(unique=True)),
                ('receiver_address', models.CharField(max_length=50)),
                ('receiver_proof', models.CharField(max_length=500)),
                ('sender_address', models.CharField(max_length=50)),
                ('sender_proof', models.CharField(max_length=500)),
                ('description', models.CharField(max_length=500)),
                ('create_time', models.IntegerField()),
            ],
        ),
    ]
