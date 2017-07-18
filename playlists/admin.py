# coding=utf-8
import os

from django.contrib import admin
from django import forms
from django.forms import ModelForm
from django.forms.utils import ErrorList
from django.template import Context, Template

from .models import AdvertismentVideo, PlaylistAdvertisment, Bus, GroupVideo, ApkVersion

# Register your models here.

PATH = os.path.dirname(os.path.dirname(__file__))


#
# def filter():
#     playlists = PlaylistAdvertisment.objects.all()
#     buses = Bus.objects.all()
#
#     filtered_buses = []
#     linked = False
#
#     for bus in buses:
#         for playlist in playlists:
#             if bus in playlist.bus.all():
#                 linked = True
#                 break
#
#         if not linked:
#             filtered_buses.append(bus)
#
#         linked = False
#
#     return Bus.objects.filter(number__in=[item.number for item in filtered_buses])
#
# filtered = filter()

#
# class PlaylistAdminForm(ModelForm):
#     bus = forms.ModelMultipleChoiceField(queryset=filtered)


class PlaylistAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_filter = ['title', 'timestamp']

    # form = PlaylistAdminForm

    class Meta:
        model = PlaylistAdvertisment


class BusAdmin(admin.ModelAdmin):
    list_display = ['number', 'playlist']

    def playlist(self, obj):
        playlists = PlaylistAdvertisment.objects.filter(bus=obj)
        f = open(os.path.join(PATH, 'playlists/templates/admin_list_editable_field.html'))

        content = f.read()
        f.close()
        context = Context(dict(playlist=playlists, bus_id=obj.id))
        template = Template(content)
        return template.render(context)

    playlist.short_description = 'Плэйлисты'

    class Meta:
        model = Bus


class AdvertismentVideoAdminForm(ModelForm):

    def __init__(self, data=None, files=None, auto_id='id_%s', prefix=None, initial=None, error_class=ErrorList,
                 label_suffix=None, empty_permitted=False, instance=None):
        super(AdvertismentVideoAdminForm, self).__init__(data, files, auto_id, prefix, initial, error_class,
                                                         label_suffix, empty_permitted, instance)

        group_videos = GroupVideo.objects.all()
        advertisment_videos = AdvertismentVideo.objects.all()
        filtered = []
        is_busy = False

        if instance is not None:
            for instance_group_video in instance.files.all():
                filtered.append(instance_group_video.id)

        for group_video in group_videos:
            for advertisment_video in advertisment_videos:
                if group_video in advertisment_video.files.all():
                    is_busy = True

            if not is_busy:
                filtered.append(group_video.id)
            is_busy = False

        self.fields['files'].queryset = GroupVideo.objects.filter(id__in=filtered)


class AdvertismentVideoAdmin(admin.ModelAdmin):

    class Meta:
        model = AdvertismentVideo
        exclude = []

    form = AdvertismentVideoAdminForm


class GroupVideoAdmin(admin.ModelAdmin):
    class Meta:
        model = GroupVideo
        exclude = []

    change_form_template = 'progressbarupload/change_form.html'
    add_form_template = 'progressbarupload/change_form.html'

    class Media:
        js = ("http://code.jquery.com/jquery.min.js",)


class ApkVersionAdmin(admin.ModelAdmin):
    class Meta:
        model = ApkVersion
        exclude = []

    change_form_template = 'progressbarupload/change_form.html'
    add_form_template = 'progressbarupload/change_form.html'

    class Media:
        js = ("http://code.jquery.com/jquery.min.js",)


admin.site.register(PlaylistAdvertisment, PlaylistAdmin)

admin.site.register(AdvertismentVideo, AdvertismentVideoAdmin)

admin.site.register(GroupVideo, GroupVideoAdmin)

admin.site.register(Bus, BusAdmin)

admin.site.register(ApkVersion, ApkVersionAdmin)
