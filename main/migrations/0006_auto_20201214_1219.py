# Generated by Django 3.1.3 on 2020-12-14 06:19

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20201213_2025'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tip',
            old_name='status',
            new_name='rating',
        ),
        migrations.AddField(
            model_name='tip',
            name='color',
            field=colorfield.fields.ColorField(default='#FF0000', max_length=18),
        ),
    ]
