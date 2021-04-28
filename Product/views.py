from django.shortcuts import render, redirect
from .models import category, product


def get_by_category(request, id):
    cl = category.objects.all()
    pl = product.objects.filter(category=id)
    d = {'cl': cl, 'pl': pl}
    return render(request, 'home.html', d)


def search_product(request):
    cl = category.objects.all()
    if request.method == 'POST':
        srch = request.POST.get('srch')
        pl = product.objects.filter(name__contains=srch)
        d = {'cl': cl, 'pl': pl}
        return render(request, 'search.html', d)
    else:
        pl = product.objects.all()
        d = {'cl': cl, 'pl': pl}
        return render(request, 'search.html', d)


def product_details(request, id):
    cl = category.objects.all()
    pl = product.objects.filter(id=id)
    d = {'cl': cl, 'pl': pl}

    return render(request, 'details.html', d)
