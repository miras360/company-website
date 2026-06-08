from django.urls import path
from . import views

urlpatterns = [
    # Именно этот 'name' ищет тег {% url %}
    path('', views.index, name='shipazhai_2026'), 
]