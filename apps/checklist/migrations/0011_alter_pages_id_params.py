# Generated by Django 3.2.9 on 2022-02-14 08:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checklist', '0010_auto_20220214_1152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pages',
            name='id_params',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='checklist.params'),
        ),
    ]
