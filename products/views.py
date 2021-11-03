from django.shortcuts import render
from .models import Product

# Create your views here.
def home(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request,'products/home.html',context)


def product(request,product_id=None):
    product = Product.objects.get(id=product_id)
    context={'product':product}
    return render(request,'products/product.html',context)