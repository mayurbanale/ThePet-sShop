
from django.contrib import admin
from django.urls import path, include
from Account import views as v
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', v.home),
    path('products-', include(('Product.urls', 'Product'), namespace='Product')),
    path('accounts-', include(('Account.urls', 'Account'), namespace='Account')),
    path('Orders-', include(('Order.urls', 'Order'), namespace='Order'))
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
