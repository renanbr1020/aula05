# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-22 00:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50, verbose_name='nome')),
                ('descricao', models.TextField()),
                ('data_nascimento', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
