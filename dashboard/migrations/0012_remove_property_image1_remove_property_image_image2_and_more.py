# Generated by Django 4.0.5 on 2023-03-28 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0011_property_image1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='property',
            name='image1',
        ),
        migrations.RemoveField(
            model_name='property_image',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='property_image',
            name='image3',
        ),
        migrations.RemoveField(
            model_name='property_image',
            name='image4',
        ),
        migrations.RemoveField(
            model_name='property_image',
            name='image5',
        ),
        migrations.AlterField(
            model_name='property_image',
            name='image1',
            field=models.ImageField(default='', upload_to='images/'),
        ),
    ]
