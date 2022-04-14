from django.urls import path

from .views import Convert

urlpatterns = [
    path('convert/', Convert.as_view())
]
