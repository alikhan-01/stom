# Generated by Django 3.1.3 on 2020-12-31 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0075_projectitem_projecttype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectitem',
            name='title',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AlterField(
            model_name='projecttype',
            name='title',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
