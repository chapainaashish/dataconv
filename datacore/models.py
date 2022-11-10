from django.db import models


class ScrappedData(models.Model):
    email = models.EmailField()
