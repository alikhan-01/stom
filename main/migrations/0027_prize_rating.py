# Generated by Django 3.1.3 on 2020-12-18 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_auto_20201218_1421'),
    ]

    operations = [
        migrations.AddField(
            model_name='prize',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]