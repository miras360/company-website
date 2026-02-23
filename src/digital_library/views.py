from django.views.generic import ListView, DetailView
from django.contrib.postgres.search import SearchQuery, SearchRank
from .models import Book

class BookListView(ListView):
    model = Book
    template_name = 'digital_library/digital_library_catalog.html'
    context_object_name = 'books'
    paginate_by = 12

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            # 'simple' for multilang (ru/en/kk)
            search_query = SearchQuery(query, config='simple')
            
            # vector filter and relevant sort (rank)
            return Book.objects.filter(search_vector=search_query).annotate(
                rank=SearchRank('search_vector', search_query)
            ).order_by('-rank')
            
        return Book.objects.all().order_by('-created_at')

class BookDetailView(DetailView):
    model = Book
    template_name = 'digital_library/digital_library_view.html'
    context_object_name = 'book'
    # Django searching slug by default