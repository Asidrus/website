# Generated by Django 3.2.9 on 2022-01-14 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checklist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pages',
            name='link_page',
            field=models.CharField(max_length=80),
        ),
    ]