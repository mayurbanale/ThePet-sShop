
from django.contrib import admin
from django.urls import path
from . import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', v.register, name="register"),
    path('login/', v.login, name="login"),
    path('logedout/', v.logout_view, name='logout')
]
