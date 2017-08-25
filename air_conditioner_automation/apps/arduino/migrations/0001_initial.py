# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-25 10:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Arduino',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('mac_address', models.CharField(max_length=12, unique=True)),
                ('ip_address', models.GenericIPAddressField(null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
