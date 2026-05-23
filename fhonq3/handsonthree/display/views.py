from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Product

#Part 2: Views
def product_list(request):
    #Retrieve all products from the database
    products = Product.objects.all()

    #Pass the products to the template
    context = {
        'products': products
    }
    return render(request, 'product_list.html', context)