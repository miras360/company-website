from django.shortcuts import render

def index(request):
    # Create your views here.
    return render(request, 'shipazhai/shipazhai_2026.html')
