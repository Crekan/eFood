from django.contrib import admin
from django.urls import path

from test_app.views import BooksView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/books/', BooksView.as_view(), name='books_list')
]
