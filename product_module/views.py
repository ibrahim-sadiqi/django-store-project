from django.db.models import Count
from django.shortcuts import render, redirect

from site_module.models import SiteBanner
from .models import Product, ProductCategory, ProductBrand
from django.http import Http404, HttpRequest
from django.views.generic.base import TemplateView, View
from django.views.generic import ListView, DetailView


class ProductListView(ListView):
    template_name = 'product_module/product_list.html'
    model = Product
    context_object_name = 'products'
    ordering = ['price']
    paginate_by = 1

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductListView, self).get_context_data()
        query = Product.objects.all()
        product: Product = query.order_by('-price').first()
        db_max_price = product.price if product is not None else 0
        context['db_max_price'] = db_max_price
        context['start_price'] = self.request.GET.get('start_price') or 0
        context['end_price'] = self.request.GET.get('end_price') or db_max_price
        context['banners'] = SiteBanner.objects.filter(is_active=True, position__iexact=SiteBanner.SiteBannerPosition.product_list)
        return context

    def get_queryset(self):
        base_query = super(ProductListView, self).get_queryset()
        category_name = self.kwargs.get('cat')
        brand_name = self.kwargs.get('brand')
        start_price = self.request.GET.get('start_price')
        end_price = self.request.GET.get('end_price')
        if start_price is not None:
            base_query = base_query.filter(price__gte=start_price)

        if end_price is not None:
            base_query = base_query.filter(price__lte=end_price)

        if brand_name is not None:
            base_query = base_query.filter(brand__url_title__iexact=brand_name)

        if category_name is not None:
            base_query = base_query.filter(category__url_title__iexact=category_name)
        return base_query


class ProductDetailView(DetailView):
    template_name = 'product_module/product_detail.html'
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        f_product_id = self.request.session.get('product_favorite')
        context['is_favorite'] = f_product_id == str(self.object.id)
        context['banners'] = SiteBanner.objects.filter(is_active=True, position__iexact=SiteBanner.SiteBannerPosition.product_detail)
        return context


class AddProductFavorite(View):
    def post(self, request):
        product_id = request.POST['product_id']
        product = Product.objects.get(pk=product_id)
        request.session['product_favorite'] = product_id
        return redirect(product.get_absolute_url())


def product_categories_component(request: HttpRequest):
    context = {
        'categories': ProductCategory.objects.filter(is_active=True, is_delete=False)
    }
    return render(request, 'product_module/components/product_catogory_component.html', context)


def product_list_by_brand_component(request: HttpRequest):
    product_brand = ProductBrand.objects.annotate(products_brand=Count('product')).filter(is_active=True)
    context = {
        'brands': product_brand
    }
    return render(request, 'product_module/components/product_brands_components.html', context)

