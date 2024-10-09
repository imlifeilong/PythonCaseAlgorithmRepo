"""django_01_with_route URL Configuration

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
from django.urls import path
from django.urls import include

"""
为什么需要命名空间？
在Django项目中，URL名称（也称为URL别名或URL标识符）用于在视图中引用URL。
如果没有命名空间，那么当多个应用或应用的多个部分尝试使用相同的URL名称时，就会发生冲突。
命名空间允许你通过前缀来区分这些名称，从而避免冲突。可以通过在include()函数中指定namespace参数来设置命名空间。
"""
urlpatterns = [
    path('admin/', admin.site.urls),

    path('app/', include('app.urls')),
    path('account/', include('account.urls', namespace="account")),
]
