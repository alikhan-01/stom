# Generated by Django 3.1.3 on 2020-12-30 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0063_auto_20201230_1925'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='history_title',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]