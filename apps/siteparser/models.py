from django.db import models
from django.conf import settings

from django.contrib.auth.models import User


class Parser(models.Model):
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
    fileName = models.CharField('имя файла', max_length=50)



