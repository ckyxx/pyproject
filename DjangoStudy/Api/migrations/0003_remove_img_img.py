# Generated by Django 2.0 on 2019-05-24 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0002_auto_20190524_2210'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='img',
            name='img',
        ),
    ]
