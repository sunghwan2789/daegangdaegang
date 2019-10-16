"""daegang URL Configuration

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
import home.views
import account.views
import data.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home.views.index, name='index'),
    path('home/mypage', home.views.mypage, name='mypage'),
    path('account/signup', account.views.signup, name='signup'),
    path('account/login', account.views.login, name='login'),
    path('account/logout', account.views.logout, name='logout'),
    path('data/info_me', data.views.info_me, name='info_me'), #미랩 인포
    path('data/info_cul', data.views.info_cul, name='info_cul'), #인문대 인포
    path('data/info_na', data.views.info_na, name='info_na'), #자대 인포
    path('data/<int:room_id>/', data.views.detail, name='detail'),
    ]
