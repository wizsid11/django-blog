# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-10 21:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_profile'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-timestamp', '-updated']},
        ),
    ]
