# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-26 15:21
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
                ('userId', models.AutoField(primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=45, unique=True)),
                ('userPassword', models.CharField(max_length=30)),
                ('userMobile', models.IntegerField(max_length=11, unique=True)),
                ('userEmail', models.IntegerField(max_length=45, unique=True)),
                ('userType', models.IntegerField(default='0', max_length=2)),
                ('userFlag', models.IntegerField(default='1', max_length=2)),
            ],
        ),
    ]
