# Generated by Django 3.1.3 on 2020-12-18 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0028_auto_20201218_2014'),
    ]

    operations = [
        migrations.RenameField(
            model_name='information',
            old_name='short_description2',
            new_name='success_description',
        ),
    ]
