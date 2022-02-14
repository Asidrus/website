# Generated by Django 3.2.9 on 2022-02-14 08:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checklist', '0009_alter_itemname_id_params'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemname',
            name='id_params',
        ),
        migrations.AddField(
            model_name='pages',
            name='id_params',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='checklist.params'),
        ),
    ]
