# Generated by Django 3.1.3 on 2020-12-30 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0068_auto_20201230_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='about_mini_description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='information',
            name='latest_description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='information',
            name='meet_description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='information',
            name='number_description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='information',
            name='service_mini_description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='information',
            name='success_description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='information',
            name='testimonial_description',
            field=models.TextField(blank=True),
        ),
    ]