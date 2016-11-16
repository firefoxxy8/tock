# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-16 20:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0016_userdata_profit_loss_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='profit_loss_account',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='projects.ProfitLossAccount', verbose_name='Profit/loss Accounting String'),
        ),
    ]
