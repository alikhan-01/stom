# Generated by Django 3.1.3 on 2020-12-28 12:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0060_information_make_about_description'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register',
            old_name='description',
            new_name='message',
        ),
    ]
