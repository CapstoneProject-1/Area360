# Generated by Django 4.0.5 on 2023-04-16 09:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0011_delete_buyer'),
        ('dashboard', '0017_alter_property_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='user_seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marketplace.profile'),
        ),
    ]