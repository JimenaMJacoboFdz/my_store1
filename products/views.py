from django.shortcuts import render

from .models import Product

def index(request):
    products = Product.objects.all()
    return render(request, "list_of_products.html", {"products":products})
    #return HttpResponse("<h1>Hello World</h1>")

def get_product(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'show_product.html', {'product':product})