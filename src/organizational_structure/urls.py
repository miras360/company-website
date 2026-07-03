from django.urls import path
from . import views

urlpatterns = [
    path('', views.orgStruct, name='orgStruct'),
    path('department/<int:pk>/', views.department_detail, name='department_detail'),
]