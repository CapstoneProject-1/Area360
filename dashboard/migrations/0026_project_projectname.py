# Generated by Django 4.0.5 on 2023-04-26 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0025_project_companyname_delete_builderprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='projectname',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]