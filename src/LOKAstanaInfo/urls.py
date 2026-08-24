from django.urls import path
from . import views

urlpatterns = [
    path('', views.lok_astana_view, name='lok-astana'),
]