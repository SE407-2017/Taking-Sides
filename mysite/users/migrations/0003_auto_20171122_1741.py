# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-22 09:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_voted_questions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='voted_questions',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
