# Generated by Django 4.1 on 2022-08-12 11:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ENIVIDA', '0009_remove_user_date_of_birth'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
