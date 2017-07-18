# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-08-16 04:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a')),
                ('active', models.BooleanField(default=True, verbose_name='\u0410\u043a\u0442\u0438\u0432\u043d\u043e\u0441\u0442\u044c')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '\u043f\u043b\u044d\u0439\u043b\u0438\u0441\u0442 \u0444\u043e\u043d\u043e\u0432\u044b\u0445 \u0440\u043e\u043b\u0438\u043a\u043e\u0432',
                'verbose_name_plural': '\u041f\u043b\u044d\u0439\u043b\u0438\u0441\u0442\u044b \u0444\u043e\u043d\u043e\u0432\u044b\u0445 \u0440\u043e\u043b\u0438\u043a\u043e\u0432',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, null=True, verbose_name='\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u0432\u0438\u0434\u0435\u043e')),
                ('file', models.FileField(upload_to='Advertisment/video/videos')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '\u0432\u0438\u0434\u0435\u043e \u0444\u043e\u043d\u043e\u0432\u044b\u0445 \u0440\u043e\u043b\u0438\u043a\u043e\u0432',
                'verbose_name_plural': '\u0412\u0438\u0434\u0435\u043e \u0444\u043e\u043d\u043e\u0432\u044b\u0445 \u0440\u043e\u043b\u0438\u043a\u043e\u0432',
            },
        ),
        migrations.AddField(
            model_name='playlist',
            name='video',
            field=models.ManyToManyField(to='relaxes.Video'),
        ),
    ]
