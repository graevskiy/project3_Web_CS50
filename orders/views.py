from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse
from .models import Pizza, Topping

# Create your views here.
def index(request):

    if not request.user.is_authenticated:
        return render(request, "orders/login.html")
    context = {
        "user": request.user,
        "pizzas": Pizza.objects.all(),
        "pizza_types": Pizza.TYPES,
        "pizza_sizes": Pizza.SIZES,
        "toppings": Topping.objects.all()
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