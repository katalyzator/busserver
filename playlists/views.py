# import sys
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
#
# from .models import Bus, PlaylistAdvertisment
#
#
# # Create your views here.
#
# @csrf_exempt
# def bind_bus_to_playlist(request):
#     bus_id = request.POST.get('bus_id')
#     playlist_id = request.POST.get('playlist_id')
#
#     try:
#         bus = Bus.objects.get(id=bus_id)
#         playlist = PlaylistAdvertisment.objects.get(id=playlist_id)
#
#         playlist.bus.add(bus)
#         playlist.save()
#
#     except:
#         return JsonResponse({
#             'result': 'error',
#             'err': sys.exc_info()
#         })
#
#     return JsonResponse({
#         'result': 'success',
#         'playlist_id': playlist_id,
#         'bus_id': bus_id,
#         'playlist_title': playlist.title
#     })
#
#
# @csrf_exempt
# def unbind_bus_to_playlist(request):
#     bus_id = request.POST.get('bus_id')
#     playlist_id = request.POST.get('playlist_id')
#
#     try:
#         bus = Bus.objects.get(id=bus_id)
#         playlist = PlaylistAdvertisment.objects.get(id=playlist_id)
#
#         playlist.bus.remove(bus)
#         playlist.save()
#
#     except:
#         return JsonResponse({
#             'result': 'error',
#             'err': sys.exc_info()
#         })
#
#     return JsonResponse({
#         'result': 'success'
#     })
