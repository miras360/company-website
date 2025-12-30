import os
from django.shortcuts import render
from .models import Ads, Files
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
# Create your views here.
def ads(request):
    ads = Ads.objects.order_by('-id')
    for ad in ads:
        files = Files.objects.filter(ads_id = ad.pk)
        ad.files = files
    return render(request, 'infoPages/advertisement.html', {'ads':ads})

def download_file(request, file_id):
    file_obj = get_object_or_404(Files, pk=file_id)
    file_name = os.path.basename(file_obj.name)
    file_extension = file_obj.type
    file = f'{file_name.encode("utf-8").decode("ISO-8859-1")}.{file_extension}'
    print("file : ", file)
    response = HttpResponse(file_obj.file, content_type='application/octet-stream')
    response['Content-Disposition'] = f'attachment; filename="{file}"'
    return response