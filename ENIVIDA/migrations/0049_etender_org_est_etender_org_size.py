# Generated by Django 4.1 on 2022-08-26 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ENIVIDA', '0048_remove_etender_organization_size_remove_etender_orgy'),
    ]

    operations = [
        migrations.AddField(
            model_name='etender',
            name='Org_est',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='etender',
            name='Org_size',
            field=models.IntegerField(default=0),
        ),
    ]
