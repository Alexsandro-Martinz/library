from django.contrib import admin
from django.urls import path, include

from rest_framework import routers

from books.api.viewsets import BooksViewSets

from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter()
router.register('books', BooksViewSets, basename='Books')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
