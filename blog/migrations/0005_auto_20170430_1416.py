# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-04-30 06:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='tags',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='label',
            field=models.TextField(),
        ),
    ]
