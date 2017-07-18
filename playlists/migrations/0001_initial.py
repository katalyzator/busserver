# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-11 12:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdvertismentVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, null=True, verbose_name='\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435 \u0432\u0438\u0434\u0435\u043e')),
                ('periodik', models.IntegerField(choices=[(5, 5), (10, 10), (15, 15), (20, 20), (30, 30)], default=10, verbose_name='\u041f\u0435\u0440\u0438\u0434\u043e\u0438\u0447\u043d\u043e\u0441\u0442\u044c(\u043c\u0438\u043d)')),
                ('active', models.BooleanField(default=True, verbose_name='\u0410\u043a\u0442\u0438\u0432\u043d\u043e\u0441\u0442\u044c')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '\u0432\u0438\u0434\u0435\u043e \u0440\u0435\u043a\u043b\u0430\u043c\u043d\u044b\u0445 \u0440\u043e\u043b\u0438\u043a\u043e\u0432',
                'verbose_name_plural': '\u0412\u0438\u0434\u0435\u043e \u0440\u0435\u043a\u043b\u0430\u043c\u043d\u044b\u0445 \u0440\u043e\u043b\u0438\u043a\u043e\u0432',
            },
        ),
        migrations.CreateModel(
            name='ApkVersion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.IntegerField(default=0)),
                ('file', models.FileField(upload_to='')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'android file',
                'verbose_name_plural': 'Apk FILE',
            },
        ),
        migrations.CreateModel(
            name='Bus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(verbose_name='\u041d\u043e\u043c\u0435\u0440 \u041c\u0430\u0440\u0448\u0440\u0443\u0442\u0430')),
                ('active', models.BooleanField(default=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '\u043d\u043e\u043c\u0435\u0440 \u0442\u0440\u043e\u043b\u043b\u0435\u0439\u0431\u0443\u0441\u0430',
                'verbose_name_plural': '\u041c\u0430\u0440\u0448\u0440\u0443\u0442\u044b',
            },
        ),
        migrations.CreateModel(
            name='GroupVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
                ('active', models.BooleanField(default=True, verbose_name='\u0410\u043a\u0442\u0438\u0432\u043d\u043e\u0441\u0442\u044c')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '\u0432\u0438\u0434\u0435\u043e \u043e\u0434\u043d\u043e\u0439 \u043a\u043e\u043c\u043f\u0430\u043d\u0438\u0438',
                'verbose_name_plural': '\u0412\u0438\u0434\u0435\u043e \u043e\u0434\u043d\u043e\u0439 \u043a\u043e\u043c\u043f\u0430\u043d\u0438\u0438',
            },
        ),
        migrations.CreateModel(
            name='PlaylistAdvertisment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('bus', models.ManyToManyField(to='playlists.Bus', verbose_name='\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u041c\u0430\u0440\u0448\u0440\u0443\u0442')),
                ('video', models.ManyToManyField(to='playlists.AdvertismentVideo', verbose_name='\u0412\u044b\u0431\u0435\u0440\u0438\u0442\u0435 \u0432\u0438\u0434\u0435\u043e \u0440\u0435\u043a\u043b\u0430\u043c\u043d\u044b\u0445 \u0440\u043e\u043b\u0438\u043a\u043e\u0432')),
            ],
            options={
                'verbose_name': '\u043f\u043b\u044d\u0439\u043b\u0438\u0441\u0442 \u0440\u0435\u043a\u043b\u0430\u043c\u043d\u044b\u0445 \u0440\u043e\u043b\u0438\u043a\u043e\u0432',
                'verbose_name_plural': '\u041f\u043b\u044d\u0439\u043b\u0438\u0441\u0442\u044b \u0440\u0435\u043a\u043b\u0430\u043c\u043d\u044b\u0445 \u0440\u043e\u043b\u0438\u043a\u043e\u0432',
            },
        ),
        migrations.AddField(
            model_name='advertismentvideo',
            name='files',
            field=models.ManyToManyField(blank=True, to='playlists.GroupVideo'),
        ),
    ]
