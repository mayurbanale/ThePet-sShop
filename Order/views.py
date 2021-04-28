from django.shortcuts import render, redirect
from .models import Cart, product, User, Order
from Product.models import category


def addCart(request, id):
    uid = request.session.get('uid')
    c = Cart()
    products = product.objects.get(id=id)
    user = User.objects.get(id=uid)
    c.product = products
    c.user = user
    c.save()
    return redirect('/')


def cartlist(request):
    uid = request.session.get('uid')
    cr = Cart.objects.filter(user=uid)
    cl = category.objects.all()
    if request.method == 'POST':
        odr = Order()
        total = request.POST.get('totalbill')
        odr.totalbill = int(total)
        odr.user = User.objects.get(id=uid)
        odr.save()
        for i in cr:
            i.delete()

        return redirect('/')
    else:
        totalbill = 0
        for i in cr:
            totalbill = totalbill+i.product.price
        d = {'cr': cr, 'cl': cl, 'total': totalbill}
        return render(request, 'cartlist.html', d)


def my_order(request):
    uid = request.session.get('uid')
    odr = Order.objects.filter(user=uid)
    cl = category.objects.all()
    d = {'cl': cl, 'odr': odr}
    return render(request, 'myorder.html', d)


def delete(request, id):
    cr = Cart.objects.filter(id=id)
    cr.delete()
    return render(request, 'cartlist.html')
