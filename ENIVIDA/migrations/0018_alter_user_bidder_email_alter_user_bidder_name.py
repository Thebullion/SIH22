# Generated by Django 4.1 on 2022-08-12 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ENIVIDA', '0017_alter_user_bidder_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Bidder_Email',
            field=models.EmailField(default=0, max_length=25),
        ),
        migrations.AlterField(
            model_name='user',
            name='Bidder_Name',
            field=models.CharField(default=0, max_length=500),
        ),
    ]