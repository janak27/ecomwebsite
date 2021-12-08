"""ecom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path,include
from shop import views
from django.views.generic import TemplateView

from django.views.static import serve
from django.conf.urls import url
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls, name="adminw"),
    path('login/', views.Login.as_view(), name="login_custom"),
    path('Register/', views.Register.as_view(), name="Register"),
    path('cart/', views.cart, name="cart"),
    path("", views.index, name="index"),
    path("logout", views.logout_view, name="logout_custom"),
    path("test/", TemplateView.as_view(template_name="shop/test.html"), name="test"),
    path("about/", TemplateView.as_view(template_name="shop/about.html"), name="about"),
    path('<int:obj_id>',views.detail, name="detail"),
    path("checkout/",views.checkout, name="checkout"),
    path("product_list/",views.product_list, name="product_list"),
    path('accounts/', include('django.contrib.auth.urls')),
    
]

