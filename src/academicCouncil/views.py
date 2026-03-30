from django.shortcuts import render
from .models import AcademicCouncilInfo, AcademicCouncilDoc, AcademicCouncilMeetings

def council_main(request):
    # Берем первую запись с инфой
    info = AcademicCouncilInfo.objects.first()
    # Все документы для скачивания
    docs = AcademicCouncilDoc.objects.all()
    # Все протоколы заседаний
    meetings = AcademicCouncilMeetings.objects.all()
    
    context = {
        'info': info,
        'docs': docs,
        'meetings': meetings,
    }
    return render(request, 'academicCouncil/main.html', context)

def council_pdf_detail(request, pk):
    # Это для открытия PDF в iframe (твоя страница doc-details.html)
    meeting = AcademicCouncilMeetings.objects.get(id=pk)
    return render(request, 'academicCouncil/doc-details.html', {'file': meeting.document})