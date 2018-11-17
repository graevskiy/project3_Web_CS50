from django.contrib import admin

from .models import Pizza, Topping, Sub, PizzaSize, PizzaType

# Register your models here.

admin.site.register(PizzaSize)
admin.site.register(PizzaType)
admin.site.register(Pizza)
admin.site.register(Topping)
admin.site.register(Sub)