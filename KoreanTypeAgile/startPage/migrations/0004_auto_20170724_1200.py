# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-24 03:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startPage', '0003_auto_20170723_2341'),
    ]

    operations = [
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue_name', models.CharField(max_length=40)),
                ('issue_contents', models.CharField(max_length=40)),
                ('person_created', models.CharField(max_length=40)),
                ('commit', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(default='', max_length=40)),
                ('project_member', models.CharField(default='', max_length=40)),
            ],
        ),
        migrations.RemoveField(
            model_name='todo',
            name='userId',
        ),
        migrations.AddField(
            model_name='todo',
            name='create',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='todo',
            name='do',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='todo',
            name='done',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='todo',
            name='performer',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AddField(
            model_name='todo',
            name='person_created',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AddField(
            model_name='todo',
            name='progress',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='todo',
            name='project_name',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AddField(
            model_name='todo',
            name='todo',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='project',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AlterField(
            model_name='todo',
            name='todoContents',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AlterField(
            model_name='todo',
            name='todoName',
            field=models.CharField(default='', max_length=40),
        ),
    ]
