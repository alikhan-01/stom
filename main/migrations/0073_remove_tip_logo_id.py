# Generated by Django 3.1.3 on 2020-12-30 14:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0072_service_icon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tip',
            name='logo_id',
        ),
    ]
