# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-29 16:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eighth', '0051_auto_20170203_1310'),
    ]

    operations = [
        migrations.AddField(
            model_name='eighthsponsor',
            name='contracted_eighth',
            field=models.BooleanField(default=True),),
        migrations.AddField(
            model_name='historicaleighthsponsor',
            name='contracted_eighth',
            field=models.BooleanField(default=True),),
    ]
