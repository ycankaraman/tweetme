# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2019-08-13 11:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('content1', models.TextField()),
                ('content2', models.TextField()),
            ],
        ),
    ]
