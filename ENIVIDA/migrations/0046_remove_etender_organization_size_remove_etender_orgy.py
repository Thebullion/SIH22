# Generated by Django 4.1 on 2022-08-26 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ENIVIDA', '0045_rename_organization_established_year_etender_orgy'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='etender',
            name='Organization_size',
        ),
        migrations.RemoveField(
            model_name='etender',
            name='orgy',
        ),
    ]
