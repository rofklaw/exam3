# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-01 17:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logreg', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='alias',
            field=models.CharField(default='Clrak', max_length=50),
            preserve_default=False,
        ),
    ]
