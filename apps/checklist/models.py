from django.db import models

class categorys(models.Model):
    id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=18)


class blocks(models.Model):
    id = models.AutoField(primary_key=True)
    title_block = models.CharField(max_length=28)
    on_page = models.BooleanField(default=False)
    id_category = models.ForeignKey(categorys, on_delete=models.CASCADE, default='')


class params(models.Model):
    id = models.AutoField(primary_key=True)
    importance = models.CharField(max_length=18)

class itemName(models.Model):
    id = models.AutoField(primary_key=True)
    general_heading_items = models.CharField(max_length=80)
    id_block = models.ForeignKey(blocks, on_delete=models.CASCADE)
    id_params = models.ForeignKey(params, on_delete=models.CASCADE, default='')


class pages(models.Model):
    id = models.AutoField(primary_key=True)
    title_link = models.CharField(max_length=80) 
    link_page = models.CharField(max_length=80) 
    id_block = models.ForeignKey(itemName, on_delete=models.CASCADE)



# Create your models here.
