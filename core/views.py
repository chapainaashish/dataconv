from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response

from .models import RawFiles, ScrappedData
from .scrapper import DataScrap
from .serializers import RawFilesSerializer


@api_view(["POST"])
def file_post(self, request, *args, **kwargs):
    serializer = RawFilesSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    data_obj = DataScrap(serializer.validated_data["file"])
    data = data_obj.get_data()

    model_instances = [ScrappedData(email=field.email) for field in data.itertuples()]
    ScrappedData.objects.bulk_create(model_instances)

    return Response(
        {
            "message": "successfully created",
            "emails": data.to_dict(),
        },
        status=status.HTTP_201_CREATED,
    )
