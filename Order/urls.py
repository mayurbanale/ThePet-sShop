
from django.contrib import admin
from django.urls import path
from . import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('addcart/<int:id>', v.addCart, name='addcart'),
    path('cartlist', v.cartlist, name='cartlist'),
    path('myorder', v.my_order, name='myorder'),
    path('del/<int:id>/', v.delete, name='delete')
]
