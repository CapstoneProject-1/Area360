# Generated by Django 4.0.5 on 2023-03-26 15:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_rename_dynamic_fileds_property_dynamic_fields'),
    ]

    operations = [
        migrations.RenameField(
            model_name='property_image',
            old_name='image',
            new_name='image1',
        ),
        migrations.AddField(
            model_name='property_image',
            name='image2',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='images/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='property_image',
            name='image3',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='images/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='property_image',
            name='image4',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='images/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='property_image',
            name='image5',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='images/'),
            preserve_default=False,
        ),
    ]
