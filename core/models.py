from django.db import models
from django.core.validators import FileExtensionValidator


class ScrappedData(models.Model):
    email = models.EmailField()


class RawFiles(models.Model):
    file = models.FileField(
        upload_to="uploads/",
        validators=[FileExtensionValidator(allowed_extensions=["csv", "xlsx"])],
    )
