# Generated by Django 3.1.3 on 2020-12-18 08:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0024_auto_20201218_1418'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prize',
            name='short_description',
        ),
        migrations.RemoveField(
            model_name='prize',
            name='status',
        ),
    ]