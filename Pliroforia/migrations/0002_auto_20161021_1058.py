# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-21 15:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pliroforia', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='catalizador',
            name='familia',
            field=models.CharField(default='null', max_length=30),
        ),
        migrations.AddField(
            model_name='catalizador',
            name='imagen',
            field=models.CharField(default='null', max_length=50),
        ),
        migrations.AlterField(
            model_name='catalizador',
            name='id',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='catalizador',
            name='marca',
            field=models.CharField(default='null', max_length=20),
        ),
    ]
