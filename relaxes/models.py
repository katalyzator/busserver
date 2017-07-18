# coding=utf-8
from __future__ import unicode_literals

from django.db import models

from playlists.helper import transform

path = 'Advertisment/video/videos'


class Playlist(models.Model):
    class Meta:
        verbose_name_plural = 'Плэйлисты фоновых роликов'
        verbose_name = 'плэйлист фоновых роликов'

    video = models.ManyToManyField('Video')
    title = models.CharField(max_length=120, verbose_name='Заголовок')
    active = models.BooleanField(default=True, verbose_name='Активность')
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return self.title


class Video(models.Model):
    class Meta:
        verbose_name_plural = 'Видео фоновых роликов'
        verbose_name = 'видео фоновых роликов'

    name = models.CharField(max_length=120, null=True, verbose_name='Наименование видео')
    file = models.FileField(null=False, upload_to=transform(path))
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return "Видео %s" % (self.name)

