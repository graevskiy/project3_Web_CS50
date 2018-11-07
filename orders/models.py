from django.db import models

# Create your models here.


class Pizza(models.Model):
    
    name = models.CharField(max_length=64)
    size = models.CharField(max_length=64)
    price = models.FloatField()    

    def __str__(self):
        return f"{self.size} pizza (${self.price})"

class Topping(models.Model):

    name = models.CharField(max_length=128)    
    pizzas = models.ManyToManyField(Pizza, blank=True, related_name="toppings")

    def __str__(self):
        return f"{self.name}"

class Sub(models.Model):
    name = models.CharField(max_length=64)
    price = models.FloatField()

    def __str__(self):
        return f"{self.name}"