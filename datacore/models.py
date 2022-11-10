from django.db import models


class ScrappedData(models.Model):
    email = models.EmailField()


class RawFiles(models.Model):
    file = models.FileField(upload_to="files/")
