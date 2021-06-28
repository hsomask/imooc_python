"""imooc_python URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls import include, url
from scanhosts.views import *

# 相当于是一个全局配置，请求发送的路由，都要通过这里转发到各个app里面去

urlpatterns = [
    path('admin/', admin.site.urls),
    # path(r"^getinfos/$",user_history),
    # path('getinfos/', user_history),
    # path('sendinfos/', user_info)
    path('scanhosts/', include('scanhosts.urls')),

]
