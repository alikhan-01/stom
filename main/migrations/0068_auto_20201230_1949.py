# Generated by Django 3.1.3 on 2020-12-30 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0067_information_service_item_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='service_item_description',
            field=models.TextField(blank=True),
        ),
    ]
