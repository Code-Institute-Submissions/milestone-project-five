# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-01-24 21:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bugs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bugcomment',
            name='author_avatar',
            field=models.CharField(blank=True, default='images/user.jpg', max_length=200),
        ),
    ]
