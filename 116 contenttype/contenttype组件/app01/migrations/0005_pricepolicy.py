# -*- coding: utf-8 -*-
# Generated by Django 1.11.23 on 2019-10-21 02:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('app01', '0004_auto_20191021_0242'),
    ]

    operations = [
        migrations.CreateModel(
            name='PricePolicy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('period', models.IntegerField()),
                ('object_id', models.IntegerField(verbose_name='关联表数据ID')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType', verbose_name='关联表名称')),
            ],
        ),
    ]
