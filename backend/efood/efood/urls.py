from django.contrib import admin
from django.urls import path

from test_api.views import BookView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', BookView.as_view()),
]
