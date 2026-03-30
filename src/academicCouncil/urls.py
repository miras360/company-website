from django.urls import path
from . import views

urlpatterns = [
    path('', views.council_main, name='council_main'),
    # Меняем name на council_pdf_view
    path('meeting/<int:pk>/', views.council_pdf_detail, name='council_pdf_view'), 
]