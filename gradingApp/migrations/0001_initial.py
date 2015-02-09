# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import gradingApp.models


class Migration(migrations.Migration):

    dependencies = [
        ('finalauth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('courseCode', models.CharField(max_length=10)),
                ('title', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='duration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('semester', models.IntegerField(max_length=1)),
                ('year', models.IntegerField(max_length=4)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='markList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('midSemGrade', models.CharField(max_length=1)),
                ('endSemGrade', models.CharField(max_length=1)),
                ('evalData', models.TextField()),
                ('midsemReport', models.FileField(upload_to=gradingApp.models.namefile)),
                ('midsemAntiPlag', models.FileField(upload_to=gradingApp.models.namefile)),
                ('endsemReport', models.FileField(upload_to=gradingApp.models.namefile)),
                ('endsemAntiPlag', models.FileField(upload_to=gradingApp.models.namefile)),
                ('course', models.ForeignKey(to='gradingApp.course')),
                ('dur', models.ForeignKey(to='gradingApp.duration')),
                ('faculty', models.ForeignKey(to='finalauth.facultyData')),
                ('student', models.ForeignKey(to='finalauth.studentData')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='reminder_details',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reciever', models.CharField(max_length=30)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('timestamp', models.CharField(default=b'<built-in method now of type object at 0x1E200528>', max_length=20)),
                ('userid', models.ForeignKey(to='finalauth.userData')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='reportGeneration',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('reportDesc', models.TextField()),
                ('timestamp', models.CharField(default=b'<built-in method now of type object at 0x1E200528>', max_length=20)),
                ('userid', models.ForeignKey(to='finalauth.userData')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='duration',
            unique_together=set([('semester', 'year')]),
        ),
    ]
