from django.shortcuts import render
from .models import *
# Create your views here.

def scienceInfo(request):
    #info = ScienceAchievments.objects.order_by('-id').first()

    #return render(request, 'sciencificBlock/scienceAcievments.html', {'science':info})
    infos = ScienceAchievments.objects.order_by('-id')

    # Для отладки (можете удалить потом)
    print(f"Всего документов: {infos.count()}")

    return render(request, 'sciencificBlock/scienceAcievments.html', {'sciences': infos})
def scienceDev(request):
    infos = Science.objects.order_by('id')
    datas = []
    for info in infos:
        data = {
            'title': info.title if info.title else None,
            'addInfoTitle': info.addInfoTitle if info.addInfoTitle else None,
            'addInfo': info.addInfo.split('\n') if info.addInfo else None,
        }
        datas.append(data)
    
    return render(request, 'sciencificBlock/scienceDev.html', {'datas': datas})


def scienceSovet(request):
    infos = ScienceSovet.objects.order_by('id').first()
    plans = ScienceSovetPlans.objects.filter(sovet_id=infos.pk)
    meetings = ScienceSovetMeetings.objects.order_by('id')
    regulations = ScienceSovetRegulation.objects.order_by('id')
    datas = {
        'pk': infos.pk if infos else None,
        'title': infos.title if infos else None,
        'description': infos.description.split('\n') if infos.description else None,
        'creation_name': infos.creation_title if infos else None,
        'creation': infos.creation if infos else None,
    }
    
    return render(request, 'sciencificBlock/scienceSovet.html', {'datas': datas, 'plans': plans, 'meetings': meetings, 'regulations' : regulations})

def creation_details(request, fid):
    data = ScienceSovet.objects.get(id = fid)
    file = data.creation
    return render(request, 'sciencificBlock/doc-details.html', {'file':file})

def regulation_details(request, fid):
    data = ScienceSovetRegulation.objects.get(id = fid)
    file = data.document
    return render(request, 'sciencificBlock/doc-details.html', {'file':file})

def plan_detail(request, fid):
    data = ScienceSovetPlans.objects.get(id = fid)
    file = data.document
    return render(request, 'sciencificBlock/doc-details.html', {'file':file})

def sciencePlans(request):
    infos = SciencePlans.objects.order_by('id').first()
    datas = {
        'title': infos.title if infos else None,
        'content': infos.content if infos else None,
    }
    
    return render(request, 'sciencificBlock/sciencePlans.html', {'datas': datas})

def meetings_detail(request, fid):
    data = ScienceSovetMeetings.objects.get(id = fid)
    file = data.document
    return render(request, 'sciencificBlock/doc-details.html', {'file':file})

