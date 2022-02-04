from django.db import models

# Create your models here.


class CRM(models.Model):
    name = models.CharField(max_length=20)
    url = models.CharField(max_length=100, verbose_name="url prod CRM")
    mrm = models.CharField(max_length=50, default='')
    prod = models.CharField(max_length=50, verbose_name="PHPSSID prod")
    dev = models.CharField(max_length=50, verbose_name="PHPSSID dev")
    manager = models.CharField(max_length=10, verbose_name="tester manager id", default='')
