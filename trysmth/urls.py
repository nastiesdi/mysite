"""trysmth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from first import views
from django.urls import re_path

urlpatterns = [
    path('', views.index, name='home'),
    path('catalog', views.catalog, name='catalog'),
    path('about', views.about, name='about'),
    path('delivery', views.delivery, name='delivery'),
    re_path(r'^category/(?P<category_name>\w+)/', views.category),
    re_path(r'category/$', views.category),
    path('product/<str:product_id>', views.product),
    re_path(r'product/$', views.product),
    path('admin/', admin.site.urls),
]
