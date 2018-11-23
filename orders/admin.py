from django.contrib import admin

from .models import Pizza, Topping, Sub, PizzaType, MenuItem_Pizza

# Register your models here.

admin.site.register(Topping)
admin.site.register(PizzaType)
admin.site.register(MenuItem_Pizza)
# admin.site.register(Pizza)

admin.site.register(Sub)