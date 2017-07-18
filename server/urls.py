"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include, patterns
from django.contrib import admin
from django.conf.urls.static import static

from playlists.api import PlaylistAdResource, VideoResource, BusResource, GroupVideoResource, ApkVersionResource
from relaxes.api import VideosResource, PlaylistsResource
from tastypie.api import Api

from server import settings


v1 = Api(api_name='v1')
v1.register(PlaylistAdResource())
v1.register(VideoResource())
v1.register(BusResource())
v1.register(GroupVideoResource())

v2 = Api(api_name='v2')
v2.register(PlaylistsResource())
v2.register(VideosResource())

v3 = Api(api_name='v3')
v3.register(BusResource())

v4 = Api(api_name='v4')
v4.register(ApkVersionResource())


urlpatterns = patterns('',
                       url(r'^jet/', include('jet.urls', 'jet')),
                       url(r'^admin/', admin.site.urls),
                       url(r'^api/', include(v1.urls)),
                       url(r'^api/', include(v2.urls)),
                       url(r'^api/', include(v3.urls)),
                       url(r'^api/', include(v4.urls)),
                       url(r'^progressbarupload/', include('progressbarupload.urls')),
                       # url(r'^admin/ajax/playlist/bind', 'playlists.views.bind_bus_to_playlist', name='bind_bus_to_playlist'),
                       # url(r'^admin/ajax/playlist/unbind', 'playlists.views.unbind_bus_to_playlist', name='unbind_bus_to_playlist'),
                       )

#if settings.DEBUG:
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
