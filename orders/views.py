from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse
from django.core import serializers
from .models import Pizza, Topping, MenuItem_Pizza, PizzaType

# Create your views here.
def index(request):

    if not request.user.is_authenticated:
        return render(request, "orders/login.html")

    context = {
        "user": request.user,
        "toppings": Topping.objects.all(),
        "pizza_items": MenuItem_Pizza.objects.all(),
        "pizza_sizes": Pizza.SIZES
    }
    return render(request, "orders/index.html", context)
    # return HttpResponse("Project 3: TODO")

def login_view(request):
    username = request.POST["user"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "orders/login.html", {"message": "Invalid credentials."})

def logout_view(request):
    logout(request)
    return render(request, "orders/login.html", {"message": "You were logged out."})

def cart_update(request):
    """ update Cart model """

    _type = PizzaType.objects.get(name=request.POST['pizza_type'])
    menu_item = MenuItem_Pizza.objects.get(pk=request.POST['pizza_id'])
    size = request.POST['pizza_size_'+_type.name]
    number_of_toppings = request.POST.get('topping_'+_type.name, 0)
    #price = menu_item._meta.get_field(size+'_price')
    pizza = Pizza.objects.create(name=_type, size=size, number_of_toppings=number_of_toppings)

    return HttpResponse(serializers.serialize("json", [pizza,menu_item]), content_type="application/json")