# Generated by Django 3.1.3 on 2021-01-15 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0095_auto_20210115_1842'),
    ]

    operations = [
        migrations.RenameField(
            model_name='doctor',
            old_name='skype',
            new_name='whatsapp',
        ),
    ]