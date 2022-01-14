from django.db import models

class category(models.Model):
    title_block = models.CharField(max_length=28)

class itemName(models.Model):
    general_heading_items = models.CharField(max_length=80)
    id_block = models.ForeignKey(category, on_delete=models.CASCADE)

class pages(models.Model):
    title_link = models.CharField(max_length=80) 
    link_page = models.CharField(max_length=80) 
    id_block = models.ForeignKey(itemName, on_delete=models.CASCADE)
    importance = models.CharField(max_length=16)

# class Example(models.Model):
#     id = models.Model.pk()

# Create your models here.
