# Generated by Django 3.1.3 on 2021-01-05 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0084_information_con_us_mini_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('phone', models.CharField(max_length=300)),
                ('email', models.EmailField(blank=True, max_length=300)),
                ('message', models.TextField(blank=True)),
            ],
        ),
    ]
