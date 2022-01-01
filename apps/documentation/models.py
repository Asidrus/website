from django.db import models
from ckeditor.fields import RichTextField


class Page(models.Model):
    content = RichTextField()

# Create your models here.
