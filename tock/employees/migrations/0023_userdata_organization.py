# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-12-26 18:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0001_initial'),
        ('employees', '0022_remove_userdata_float_people_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='organization',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='organizations.Organization'),
        ),
    ]
