from django.shortcuts import render

from .models import Product

def index(request):
    products = Product.objects.all()
    return render(request, "list_of_products.html", {"products":products})
    #return HttpResponse("<h1>Hello World</h1>")