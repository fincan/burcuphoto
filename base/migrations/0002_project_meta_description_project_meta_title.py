# Generated by Django 4.0.2 on 2022-02-27 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='meta_description',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Meta Description'),
        ),
        migrations.AddField(
            model_name='project',
            name='meta_title',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Meta Title'),
        ),
    ]
