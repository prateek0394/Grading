# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='appName',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('appID', models.CharField(max_length=3)),
                ('appName', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='appOnOff',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('startDate', models.CharField(max_length=20)),
                ('endDate', models.CharField(max_length=20)),
                ('timestamp', models.CharField(default=b'<built-in method now of type object at 0x1E200528>', max_length=20)),
                ('app', models.ForeignKey(to='appSetting.appName')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
