# Generated by Django 4.1 on 2022-08-26 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ENIVIDA', '0040_rename_bid_validity_tender_budget_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='administrater',
            old_name='Admin_Mobile',
            new_name='AEmail',
        ),
        migrations.RenameField(
            model_name='administrater',
            old_name='Admin_Name',
            new_name='AName',
        ),
        migrations.RenameField(
            model_name='administrater',
            old_name='Admin_Password',
            new_name='APassword',
        ),
        migrations.RenameField(
            model_name='administrater',
            old_name='Admin_Email',
            new_name='AUID',
        ),
        migrations.AddField(
            model_name='administrater',
            name='AMobile',
            field=models.IntegerField(default=0),
        ),
    ]
