# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-17 18:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Catalizador',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('código', models.CharField(max_length=30)),
                ('precio', models.IntegerField(default=0)),
                ('marca', models.CharField(max_length=20)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
