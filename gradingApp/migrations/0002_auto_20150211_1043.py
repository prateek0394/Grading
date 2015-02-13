# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gradingApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='courseTemplates',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('keyDev', models.IntegerField(max_length=2)),
                ('courseN', models.ForeignKey(to='gradingApp.course')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='course',
            name='courseCode',
            field=models.CharField(unique=True, max_length=10),
        ),
        migrations.AlterField(
            model_name='marklist',
            name='endSemGrade',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='marklist',
            name='midSemGrade',
            field=models.CharField(max_length=5),
        ),
    ]
