# Generated by Django 2.0.3 on 2018-11-08 21:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20181109_0018'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topping',
            name='price',
        ),
    ]
