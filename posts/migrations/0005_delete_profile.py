# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-11 05:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_post_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
