# Generated by Django 3.2.9 on 2022-02-11 09:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checklist', '0002_alter_pages_link_page'),
    ]

    operations = [
        migrations.CreateModel(
            name='blocks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_block', models.CharField(max_length=28)),
                ('on_page', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='categorys',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=18)),
            ],
        ),
        migrations.AlterField(
            model_name='pages',
            name='importance',
            field=models.CharField(default='Null', max_length=16),
        ),
        migrations.AlterField(
            model_name='itemname',
            name='id_block',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checklist.blocks'),
        ),
        migrations.DeleteModel(
            name='category',
        ),
    ]