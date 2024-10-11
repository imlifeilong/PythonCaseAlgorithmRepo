"""django_02_with_auth URL Configuration

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
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from account.views import protected_view, ProtectedView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/token-auth/', obtain_jwt_token),   # 用户登录获取 JWT
    path('api/token-refresh/', refresh_jwt_token),  # 刷新 JWT
    path('api/token-verify/', verify_jwt_token),    # 验证 JWT 是否有效
    path('api/protected/', protected_view),  # 示例保护视图
    path('api/protected-class/', ProtectedView.as_view()),  # 示例保护类视图
]
