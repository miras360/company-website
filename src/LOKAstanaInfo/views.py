from django.shortcuts import render
from .models import LOKGeneralInfo, LOKRoom, LOKService

def lok_astana_view(request):
    general_info = LOKGeneralInfo.objects.first()
    rooms = LOKRoom.objects.prefetch_related('gallery').all()
    services = LOKService.objects.all()

    context = {
        'general': general_info,
        'rooms': rooms,
        'services': services,
    }
    return render(request, 'LOKAstanaInfo/lok_astana.html', context)