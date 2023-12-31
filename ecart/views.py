from django.shortcuts import render

from ecart.settings import BASE_DIR, STATICFILES_DIRS
from store.models import Product

def home(request):
    products = Product.objects.all().filter(is_available=True)[:4]
    context = { "products": products }
    return render(request, 'home.html', context)