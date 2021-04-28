from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth import login as dj_login, logout, authenticate

from Product.models import category, product
from .models import UserInfo, UserForm, UserCreationForm, User, LoginForm


def home(request):
    cl = category.objects.all()
    pl = product.objects.all()
    d = {'cl': cl, 'pl': pl}
    return render(request, 'home.html', d)


def register(request):
    cl = category.objects.all()
    pl = product.objects.all()
    if request.method == 'POST':
        f = UserForm(request.POST)
        f.save()
        return redirect('/')
    else:
        f = UserForm
        d = {'cl': cl, 'pl': pl, 'form': f}
        return render(request, 'form.html', d)


def login(request):
    cl = category.objects.all()
    pl = product.objects.all()
    if request.method == 'POST':
        uname = request.POST.get('UserName')
        passw = request.POST.get('Password')
        user = authenticate(request, username=uname, password=passw)
        if user is not None:
            request.session['uid'] = user.id
            dj_login(request, user)
            return redirect('/')
        else:
            return HttpResponse('<h2>Invalid username or password</h2>')
    else:
        f = LoginForm
        d = {'cl': cl, 'pl': pl, 'form': f}
        return render(request, 'form.html', d)


def logout_view(request):
    logout(request)
    return redirect('/')
