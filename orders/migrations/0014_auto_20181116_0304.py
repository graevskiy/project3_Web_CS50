# Generated by Django 2.0.3 on 2018-11-16 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0013_pizzasize_pizzatype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='name',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='size',
            field=models.CharField(max_length=64),
        ),
    ]