# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-15 23:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('email', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('password', models.CharField(default='password', max_length=255)),
            ],
        ),
    ]
