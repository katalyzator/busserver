# coding=utf-8
from __future__ import unicode_literals

from django.db import models

from playlists.helper import transform

DURATION_CHOICES = (
    (5, 5),
    (10, 10),
    (15, 15),	
    (20, 20),
    (30, 30),
)

path = 'Advertisment/video/'
path_apk = 'Advertisment/apk/'


class PlaylistAdvertisment(models.Model):
    class Meta:
        verbose_name_plural = 'Плэйлисты рекламных роликов'
        verbose_name = 'плэйлист рекламных роликов'

    title = models.CharField(max_length=120, verbose_name='Заголовок')
    bus = models.ManyToManyField('Bus', verbose_name='Выберите Маршрут')
    video = models.ManyToManyField('AdvertismentVideo', verbose_name='Выберите видео рекламных роликов')
    # timestart = models.DateField(verbose_name='Дата Начала Плэйлиста', null=False)
    # timefinish = models.DateField(verbose_name='Дата Окончания Плэйлиста', null=False)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.title


class Bus(models.Model):
    class Meta:
        verbose_name_plural = 'Маршруты'
        verbose_name = 'номер троллейбуса'

    number = models.IntegerField(verbose_name='Номер Маршрута')
    active = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return str(self.number)


class AdvertismentVideo(models.Model):
    class Meta:
        verbose_name_plural = 'Видео рекламных роликов'
        verbose_name = 'видео рекламных роликов'

    name = models.CharField(max_length=120, null=True, verbose_name='Наименование видео')
    files = models.ManyToManyField('GroupVideo', blank=True)
    periodik = models.IntegerField(default=10, choices=DURATION_CHOICES, verbose_name='Перидоичность(мин)')
    active = models.BooleanField(default=True, verbose_name='Активность')
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.name


class GroupVideo(models.Model):
    class Meta:
        verbose_name_plural = 'Видео одной компании'
        verbose_name = 'видео одной компании'

    # name = models.CharField(max_length=120, null=True, verbose_name='Наименование видео')
    file = models.FileField(null=False, upload_to=transform(path))
    active = models.BooleanField(default=True, verbose_name='Активность')
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return str(self.id)


class ApkVersion(models.Model):
    class Meta:
        verbose_name_plural = 'Apk FILE'
        verbose_name = 'android file'

    version = models.IntegerField(default=0)
    file = models.FileField(upload_to=transform(path_apk))
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
