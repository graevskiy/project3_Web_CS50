from django.db import models

# Create your models here.



class Topping(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.name}"

class PizzaSize(models.Model):
    name = models.CharField(max_length=32)
    label = models.CharField(max_length=64)

class PizzaType(models.Model):
    name = models.CharField(max_length=32)
    label = models.CharField(max_length=64)

class Pizza(models.Model):
    # S = 'SMALL'
    # L = 'LARGE'
    # SIZES = (
    #         (S, 'Small'),
    #         (L, 'Large')
    #     )
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

    
    tmp_list = [ (_size.name, _size.label) for _size in PizzaSize.objects.all()]
    SIZES = tuple(tmp_list)

    tmp_list = [ (_type.name, _type.label) for _type in PizzaType.objects.all()]
    TYPES = tuple(tmp_list)

    name = models.CharField(max_length=64, default=TYPES[0][0], choices=TYPES)
    size = models.CharField(max_length=64, default=SIZES[0][0], choices=SIZES)
    price = models.FloatField(default=0.0)
    toppings = models.ManyToManyField(Topping, related_name="in_pizza", blank=True)

    def __str__(self):
        return f"{self.get_name_display()} - {self.get_size_display()} pizza (${self.price})"

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

