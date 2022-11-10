from django.urls import path, include
from .views import RawFilesViewset

urlpatterns = [path("", RawFilesViewset().as_view())]
