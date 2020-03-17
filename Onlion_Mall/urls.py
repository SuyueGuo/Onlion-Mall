"""Onlion_Mall URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from user import views as user_views
from commodity import views as commodity_views
from trade import views as trade_views
from comment import views as comment_views
from shopping_cart import views as shopping_cart_views
from history import views as history_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register-form/', user_views.register_form),
    path('user/', user_views.user),
    path('login-form/', user_views.login_form),
    path('home/', user_views.home_page),
    path('commodity/', commodity_views.commodity),
    path('add-commodity/', commodity_views.add_commodity),
    path('shopping_cart/', shopping_cart_views.shopping_cart),
    path('trade/', trade_views.trade),
    path('comment/', comment_views.comment),
    path('history/', history_views.history),
]

handler404 = user_views.page_not_found
