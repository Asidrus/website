from django.db import models

# Create your models here.


class CRM(models.Model):
    name = models.CharField(max_length=20)
    url = models.TextField(verbose_name="url prod CRM")
    prod = models.TextField(verbose_name="PHPSSID prod")
    dev = models.TextField(verbose_name="PHPSSID dev")
    manager = models.TextField(verbose_name="tester manager id", default='')
