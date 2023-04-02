from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'

    order = {
        'name': 'name',
        'min_price': 'price',
        'max_price': '-price'
    }
    sort = request.GET.get('sort', 'name')

    context = {
        'phones': [entry for entry in Phone.objects.order_by(order[sort])]
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    context = {
        'phone': Phone.objects.filter(slug=slug).first()
    }
    print(context['phone'])
    return render(request, template, context)
