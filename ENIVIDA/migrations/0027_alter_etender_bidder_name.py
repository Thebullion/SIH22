# Generated by Django 4.1 on 2022-08-17 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ENIVIDA', '0026_etender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etender',
            name='Bidder_Name',
            field=models.CharField(max_length=200),
        ),
    ]