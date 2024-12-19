from django.shortcuts import render
from .models import Product
from django.http import Http404

# Create your views here.
def product_list(request):
    products = Product.objects.all()
    n_of_products = products.count()
    return render(request, 'product_module/product_list.html', {
        'products': products,
        'total_number_of_products': n_of_products
    })


def product_detail(request, slug):
    try:
        product = Product.objects.get(slug=slug)
    except Exception:
        return Http404()
    #product = get_object_or_404(Product, slug)
    return render(request, 'product_module/product_detail.html', {'product': product})
