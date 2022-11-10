from rest_framework.generics import ListCreateAPIView
from .serializers import RawFilesSerializer
from rest_framework.response import Response
from .models import RawFiles
from rest_framework import status
from .scrap import DataScrap


class RawFilesViewset(ListCreateAPIView):
    serializer_class = RawFilesSerializer
    queryset = RawFiles.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = RawFilesSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        print(serializer.validated_data)
        data_obj = DataScrap(serializer.validated_data["file"])
        data = data_obj.get_data()

        print(data)
        #!do something

        return Response(serializer.data, status=status.HTTP_201_CREATED)
