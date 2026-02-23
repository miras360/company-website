from django.urls import path
from . import views
from django.views.generic import RedirectView

app_name = 'digital_library'

#urlpatterns = [
#    path('', views.BookListView.as_view(), name='book_list'),
#    path('<slug:slug>/', views.BookDetailView.as_view(), name='book_detail'),
#]   # Старые рабочие пути на случай, если проект возобновят

urlpatterns = [
    # Все старые имена теперь ведут на одну страницу ошибки
    path('', RedirectView.as_view(url='/error/'), name='book_list'),
    path('<slug:slug>/', RedirectView.as_view(url='/error/'), name='book_detail'),
]