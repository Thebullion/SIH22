# Generated by Django 4.1 on 2022-08-26 09:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ENIVIDA', '0042_remove_tender_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='etender',
            old_name='Tender_Category',
            new_name='Bid_Category',
        ),
        migrations.RenameField(
            model_name='etender',
            old_name='Tender_ID',
            new_name='Bid_ID',
        ),
        migrations.RenameField(
            model_name='etender',
            old_name='Tender_Type',
            new_name='Bid_Type',
        ),
    ]