"""bookstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import home_page,footer, wish_size

urlpatterns = [
    path('', home_page),
    path('wish-size', wish_size, name='wish_size'),
    path('',include('bookstore_account.urls')),
    path('',include('bookstore_products.urls')),
    path('',include('bookstore_contact_us.urls')),
    path('',include('bookstore_wishlist.urls')),
    path('footer',footer,name='footer'),
    path('admin/', admin.site.urls),
    # path('admin_tools_stats/', include('admin_tools_stats.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)