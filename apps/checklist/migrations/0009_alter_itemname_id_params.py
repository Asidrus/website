# Generated by Django 3.2.9 on 2022-02-14 08:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checklist', '0008_auto_20220214_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemname',
            name='id_params',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='checklist.params'),
        ),
    ]
