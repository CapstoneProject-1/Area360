# Generated by Django 4.0.5 on 2023-03-07 04:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0006_alter_profile_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={'permissions': {('buyer', 'buyer'), ('builder', 'builder'), ('seller', 'seller')}},
        ),
    ]
