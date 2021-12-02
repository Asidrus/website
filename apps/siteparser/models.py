from django.db import models
from django.conf import settings

from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
import time

class Parser(models.Model):
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    fileName = models.CharField('имя файла', max_length=50)
    datetime = models.DateTimeField('Datetime', auto_now=True)
    patterns = models.CharField(max_length=200, default='')
    site = models.CharField(max_length=256, default='')



