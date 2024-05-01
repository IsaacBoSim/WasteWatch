from django.db import models

from django.conf import settings
from django.utils import timezone
from storages.backends.s3boto3 import S3Boto3Storage
from django.contrib.auth.models import User


class Report(models.Model):
    id = models.AutoField(primary_key=True, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.TextField()
    description = models.TextField()
    text_file = models.FileField()
    image_file = models.ImageField()
    date = models.DateField(default=timezone.now)

    REPORTSTATUS = (
        (0, 'New'),
        (1, 'In Progress'),
        (2, 'Resolved'),
    )
    status = models.PositiveSmallIntegerField(choices=REPORTSTATUS, default=0)
    resolve_explanation = models.TextField(null=True)



class ReportStorage(S3Boto3Storage):
    location = 'reports'
    default_acl = 'public-read'
    file_overwrite = False
