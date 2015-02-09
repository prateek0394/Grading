# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import finalauth.models


class Migration(migrations.Migration):

    dependencies = [
        ('finalauth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='uploadDelete',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('operation', models.CharField(max_length=30)),
                ('uploadFile', models.FileField(upload_to=finalauth.models.namefile)),
                ('timestamp', models.CharField(default=b'<built-in method now of type object at 0x1E200528>', max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
