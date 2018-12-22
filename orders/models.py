from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.



class Topping(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.name}"

class PizzaType(models.Model):
    name = models.CharField(max_length=32)
    label = models.CharField(max_length=64)
    def __str__(self):
        return f"{self.label}"

class MenuItem_Pizza(models.Model):
    item_type = models.ForeignKey('PizzaType', on_delete=models.CASCADE)
    small_price = models.FloatField(default=0.0)
    large_price = models.FloatField(default=0.0)
    number_of_toppings = models.SmallIntegerField(default=0, validators=[MinValueValidator(0)])

    def __str__(self):
        return f"{self.item_type}, small: ${self.small_price}, large: ${self.large_price}, toppings: {self.number_of_toppings}"

class Pizza(models.Model):
    S = 'SMALL'
    L = 'LARGE'
    SIZES = (
            (S, 'Small'),
            (L, 'Large')
        )
    # REGULAR = 'REGULAR'
    # _1TOPPING = '_1TOPPING'
    # _2TOPPING = '_2TOPPING'
    # _3TOPPING = '_3TOPPING'
    # TYPES = (
    #         (REGULAR, 'Cheese'),
    #         (_1TOPPING, '1 Topping'),
    #         (_2TOPPING, '2 Toppings'),
    #         (_3TOPPING, '3 Toppings')
    #     )


    name = models.ForeignKey('PizzaType', on_delete=models.CASCADE)
    size = models.CharField(max_length=64, default=S, choices=SIZES)
    price = models.FloatField(default=0.0)
    toppings = models.ManyToManyField(Topping, related_name="toppings", blank=True)
    number_of_toppings = models.SmallIntegerField()

    def __str__(self):
        return f"{self.name} - {self.get_size_display()} pizza (${self.price})"

class Sub(models.Model):
    S = 'SMALL'
    L = 'LARGE'
    SIZES = (
            (S, 'Small'),
            (L, 'Large')
        )
    IT = 'IT'
    CH = 'CH'
    HC = 'HC'
    MB = 'MB'
    TN = 'TN'
    SUBS_TYPES = (
            (IT, 'Italian'),
            (CH, 'Cheese'),
            (HC, 'Ham + Cheese'),
            (MB, 'Meatball'),
            (TN, 'Tuna')
        )
    name = models.CharField(max_length=64, default=CH, choices=SUBS_TYPES)
    size = models.CharField(max_length=64, default=S, choices=SIZES)
    price = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.get_size_display()} {self.name} Sub (${self.price})"

