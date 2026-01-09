from django.shortcuts import render

from .models import CeoDatas
# Create your views here.
def ceoInfo(request):
    datas = CeoDatas.objects.order_by('sort_order','id')
    ceo_list=[]
    for data in datas:
        ceo_data = {
            'name': data.name if data.name else None,
            'date_of_birth' : data.dateOfBirth if data.dateOfBirth else None,
            'post' : data.post if data.post else None,
            'edu_parts': data.education.split('\n') if data.education else None,
            'spec_parts':  data.scientific.split('\n') if data.scientific else None,
            'work': data.work.split('\n') if data.work else None,
            'positions':  data.positions.split('\n') if data.positions else None,
            'awards_parts':  data.awards.split('\n') if data.awards else None,
            'sertif_parts':  data.sertificates.split('\n') if data.sertificates else None,
            'public_parts':  data.publications.split('\n') if data.publications else None,
            'photo': data.photo if data.photo else None,
        }
        ceo_list.append(ceo_data)
    return render(request, 'ceoInfo/ceoInfoPage.html', {'datas': ceo_list})
