# Generated by Django 4.1 on 2022-08-10 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ENIVIDA', '0002_alter_tender_number_of_covers_alter_tender_tender_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Category_Name', models.CharField(max_length=200)),
            ],
        ),
    ]
