# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-10 12:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contest', '0014_auto_20160310_1917'),
    ]

    operations = [
        migrations.AddField(
            model_name='contestproblem',
            name='spj',
            field=models.BooleanField(default=False),
        ),
    ]