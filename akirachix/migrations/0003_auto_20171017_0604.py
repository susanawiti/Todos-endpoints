# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-17 06:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('akirachix', '0002_auto_20170926_1003'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userId', models.IntegerField(default=1)),
                ('tiltle', models.CharField(default='Default Title', max_length=200)),
                ('body', models.TextField(default='Body of post goes here')),
            ],
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
