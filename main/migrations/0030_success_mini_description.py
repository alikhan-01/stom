# Generated by Django 3.1.3 on 2020-12-18 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0029_auto_20201218_2016'),
    ]

    operations = [
        migrations.AddField(
            model_name='success',
            name='mini_description',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
