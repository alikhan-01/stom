# Generated by Django 3.1.3 on 2020-12-30 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0073_remove_tip_logo_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='tip',
            name='icon',
            field=models.CharField(default='default icon', max_length=300),
            preserve_default=False,
        ),
    ]
