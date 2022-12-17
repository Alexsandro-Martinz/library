from rest_framework import viewsets

from books.api.serializers import BooksSerializer
from books.models import Books
 
class BooksViewSets(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer