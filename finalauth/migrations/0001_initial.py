# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='facultyData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='logForUsers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.CharField(default=b'<built-in method now of type object at 0x1E200528>', max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='studentData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='userData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('userid', models.CharField(max_length=10)),
                ('bitsid', models.CharField(max_length=14)),
                ('name', models.CharField(max_length=50)),
                ('userType', models.IntegerField(max_length=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='studentdata',
            name='user',
            field=models.ForeignKey(to='finalauth.userData'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='logforusers',
            name='user',
            field=models.ForeignKey(to='finalauth.userData'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='facultydata',
            name='user',
            field=models.ForeignKey(to='finalauth.userData'),
            preserve_default=True,
        ),
    ]
