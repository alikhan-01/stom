# Generated by Django 3.1.3 on 2020-12-26 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0051_auto_20201226_1244'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='quote_3',
            field=models.CharField(default='default quote_3', max_length=200),
            preserve_default=False,
        ),
    ]
