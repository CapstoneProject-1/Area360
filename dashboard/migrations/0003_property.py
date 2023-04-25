# Generated by Django 4.0.5 on 2023-03-19 03:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0002_remove_property_image_property_delete_property'),
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_purpose', models.CharField(choices=[('Rent', 'Rent'), ('Sell', 'Sell')], max_length=10)),
                ('property_type', models.CharField(max_length=50)),
                ('property_posting', models.CharField(blank=True, choices=[('Full House', 'Full House'), ('On sharing basis', 'On sharing basis')], default='On sharing basis', max_length=30, null=True)),
                ('property_state', models.CharField(max_length=100)),
                ('property_city', models.CharField(max_length=100)),
                ('property_age_of_construction', models.CharField(blank=True, choices=[('less than 5 years', 'less than 5 years'), ('5 to 10 years', '5 to 10 years'), ('10 to 20 years', '10 to 20 years'), ('More than 20', 'More than 20')], max_length=100, null=True)),
                ('property_bountry_wall', models.CharField(blank=True, max_length=20, null=True)),
                ('property_furnished_status', models.CharField(blank=True, choices=[('Full Furnished', 'Full Furnished'), ('No Furnished', 'No Furnished')], max_length=50, null=True)),
                ('dynamic_fileds', models.JSONField(default=None)),
                ('user_seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]