# Generated by Django 4.1 on 2022-08-12 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ENIVIDA', '0020_rename_biddr_email_user_bidder_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Bidder_Email',
            field=models.EmailField(max_length=50, null=True),
        ),
    ]
