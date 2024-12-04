from django.shortcuts import render, get_object_or_404
from .models import Product
from django.http import Http404
from django.db.models import Avg


# Create your views here.

def product_list(request):
    products = Product.objects.all()
    n_of_products = products.count()
    avg_rating = products.aggregate(Avg('rating'))
    return render(request, 'product_module/product_list.html', {
        'products': products,
        'total_number_of_products': n_of_products,
        'average_ratings': avg_rating
    })


def product_detail(request, slug):
    try:
        product = Product.objects.get(slug=slug)
    except Exception:
        return Http404()
    #product = get_object_or_404(Product, slug)
    return render(request, 'product_module/product_detail.html', {'product': product})
