# coding=utf-8
from django.contrib import admin

from .models import Video, Playlist


# Register your models here.


class PlaylistAdmin(admin.ModelAdmin):
    class Meta:
        model = Playlist


class VideoAdmin(admin.ModelAdmin):
    class Meta:
        model = Video
        exclude = []


class UploadFileAdmin(admin.ModelAdmin):
    change_form_template = 'progressbarupload/change_form.html'
    add_form_template = 'progressbarupload/change_form.html'

    class Media:
        js = ("http://code.jquery.com/jquery.min.js",)


admin.site.register(Playlist, PlaylistAdmin)

admin.site.register(Video, UploadFileAdmin)
