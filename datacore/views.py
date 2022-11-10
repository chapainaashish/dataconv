from rest_framework.generics import ListCreateAPIView
from .serializers import RawFilesSerializer
from .models import RawFiles


class RawFilesViewset(ListCreateAPIView):
    serializer_class = RawFilesSerializer
    queryset = RawFiles.objects.all()
