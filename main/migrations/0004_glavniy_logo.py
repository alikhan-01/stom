# Generated by Django 3.1.3 on 2020-12-13 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20201212_2304'),
    ]

    operations = [
        migrations.AddField(
            model_name='glavniy',
            name='logo',
            field=models.ImageField(default='default logo', upload_to='upload'),
            preserve_default=False,
        ),
    ]
