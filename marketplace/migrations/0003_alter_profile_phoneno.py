# Generated by Django 4.0.5 on 2023-01-07 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0002_remove_profile_fname_remove_profile_lname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phoneno',
            field=models.CharField(max_length=10),
        ),
    ]
