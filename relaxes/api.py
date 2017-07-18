from tastypie.contrib.gis.resources import ModelResource

from tastypie import fields

from .models import Video, Playlist

api_object_playlist = Playlist.objects.all()
api_object_video = Video.objects.all()


class PlaylistsResource(ModelResource):
    class Meta:
        queryset = api_object_playlist
        name = 'Playlist'

    video = fields.ToManyField('relaxes.api.VideosResource', 'video', full=True, null=True)


class VideosResource(ModelResource):
    class Meta:
        queryset = api_object_video
        name = 'video'

    def dehydrate(self, bundle):
        file = bundle.data['file']
        bundle.data['file'] = file[1:]
        return bundle
