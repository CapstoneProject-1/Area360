# Generated by Django 4.0.5 on 2023-03-19 03:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property_image',
            name='property',
        ),
        migrations.DeleteModel(
            name='Property',
        ),
    ]
