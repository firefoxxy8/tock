# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-12-29 20:38
from __future__ import unicode_literals

from django.db import migrations

def to_employee(apps, schema_editor):
    TimeCardPrefillData = apps.get_model('hours', 'TimeCardPrefillData')
    for tcpd in TimeCardPrefillData.objects.all():
        tcpd.employee = tcpd.user.user_data
        tcpd.save()


class Migration(migrations.Migration):

    dependencies = [
        ('hours', '0035_auto_20171229_1531'),
    ]

    operations = [
        migrations.RunPython(to_employee)
    ]