from rest_framework import serializers
from .models import RawFiles


class RawFilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = RawFiles
        fields = ["file"]
