# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-07-12 12:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0002_auto_20190712_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permission',
            name='is_menu',
            field=models.BooleanField(default=False, verbose_name='菜单'),
        ),
    ]
