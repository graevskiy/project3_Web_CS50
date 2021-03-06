# Generated by Django 2.0.3 on 2018-11-20 01:18

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0014_auto_20181116_0304'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItem_Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('small_price', models.FloatField(default=0.0)),
                ('large_price', models.FloatField(default=0.0)),
                ('number_of_toppings', models.SmallIntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('item_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.PizzaType')),
            ],
        ),
        migrations.DeleteModel(
            name='PizzaSize',
        ),
        migrations.AddField(
            model_name='pizza',
            name='number_of_toppings',
            field=models.SmallIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pizza',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.PizzaType'),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='size',
            field=models.CharField(choices=[('SMALL', 'Small'), ('LARGE', 'Large')], default='SMALL', max_length=64),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='toppings',
            field=models.ManyToManyField(blank=True, related_name='toppings', to='orders.Topping'),
        ),
    ]
