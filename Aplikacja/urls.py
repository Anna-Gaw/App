"""Aplikacja URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app.views import OrderView, CustomerDetailView,  BaseView, UserLoginView, UserLogoutView, NewUserView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^restauracja$', BaseView.as_view(), name= 'base'),
    url(r'^login$', UserLoginView.as_view(), name ='login'),
    url(r'^logout$', UserLogoutView.as_view(), name = 'logout'),
    url(r'^new_user$', NewUserView.as_view(), name = 'new'),
    url(r'^customers_detail/(?P<user_id>(\d)+)', CustomerDetailView.as_view(), name = 'detale'),
    url(r'^new_order', OrderView.as_view(), name = 'order')
]
