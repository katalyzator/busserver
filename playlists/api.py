from tastypie.constants import ALL_WITH_RELATIONS
from tastypie.contrib.gis.resources import ModelResource

from tastypie import fields

from .models import PlaylistAdvertisment, AdvertismentVideo, Bus, GroupVideo, ApkVersion

api_object_playlist = PlaylistAdvertisment.objects.all()
api_object_video = AdvertismentVideo.objects.all()
api_object_bus = Bus.objects.all()
api_object_group_video = GroupVideo.objects.all()
api_object_apk_version = ApkVersion.objects.all()


class PlaylistAdResource(ModelResource):
    class Meta:
        queryset = api_object_playlist
        name = 'PlaylistAd'
        filtering = {
            'bus': ALL_WITH_RELATIONS,
        }
	limit = 200
    
    bus = fields.ToManyField('playlists.api.BusResource', 'bus', full=True, null=True)
    video = fields.ToManyField('playlists.api.VideoResource', 'video', full=True, null=True)


class VideoResource(ModelResource):
    files = fields.ToManyField('playlists.api.GroupVideoResource', 'files', full=True, null=True)

    class Meta:
        queryset = api_object_video
        name = 'video'
	limit = 200
        # def dehydrate(self, bundle):
        #     bundle.data['file'] = ', '.join([a.file.__str__() for a in bundle.obj.files.all()])
        #     return bundle


class BusResource(ModelResource):
    class Meta:
        queryset = api_object_bus
        name = 'bus'
        filtering = {
            'number': ALL_WITH_RELATIONS,
        }
	limit = 200

class GroupVideoResource(ModelResource):
    class Meta:
        queryset = api_object_group_video
        resource_name = 'files'
        excludes = 'resource_uri'.split()


    def dehydrate(self, bundle):
        file = bundle.data['file']
        bundle.data['file'] = file[1:]
        return bundle


class ApkVersionResource(ModelResource):
    class Meta:
        queryset = api_object_apk_version
        resource_name = 'apk'
	limit = 200
