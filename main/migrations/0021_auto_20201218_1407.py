# Generated by Django 3.1.3 on 2020-12-18 08:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_auto_20201218_1405'),
    ]

    operations = [
        migrations.RenameField(
            model_name='information',
            old_name='short_description',
            new_name='meet_description',
        ),
    ]