# Generated by Django 2.0.3 on 2018-11-09 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_auto_20181110_0143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='size',
            field=models.CharField(choices=[('select', (('SMALL', 'Small'), ('LARGE', 'Large')))], max_length=64),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='toppings',
            field=models.ManyToManyField(related_name='in_pizza', to='orders.Topping'),
        ),
    ]
