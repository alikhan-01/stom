# Generated by Django 3.1.3 on 2020-12-19 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0033_success_mini_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='mini_logo',
            field=models.ImageField(default='default mini_logo', upload_to='upload'),
            preserve_default=False,
        ),
    ]
