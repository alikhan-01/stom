# Generated by Django 3.1.3 on 2021-01-15 12:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0097_auto_20210115_1843'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='twitter',
            new_name='telegram',
        ),
    ]
