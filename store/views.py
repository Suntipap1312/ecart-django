from django.shortcuts import get_object_or_404, render

from category.models import Category
from .models import Product
# Create your views here.
def store(request, category_slug=None):
    categories = None
    products = None
    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
    else:
        products = Product.objects.all().filter(is_available=True)

    products_count = products.count()
    context = { "products": products, "products_count": products_count }
    return render(request, 'store/store.html', context)

def product_detail(request, category_slug, product_slug):
    product = None
    try:
        # category__slug = double undescore is looking up for Product.Category.slug
        product = Product.objects.get(slug=product_slug, category__slug=category_slug)
    except Exception as e:
        print("Something went wrong:", e)
    context = { "product": product }
    return render(request, 'store/product_detail.html', context)