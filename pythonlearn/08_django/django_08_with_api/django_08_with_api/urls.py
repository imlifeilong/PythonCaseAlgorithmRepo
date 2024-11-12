"""django_08_with_api URL Configuration

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
from app import views as app_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('book-api-view/', app_views.BookAPIView.as_view()),
    path('book-django-paginator-api-view/', app_views.BookDjangoPaginatorAPIView.as_view()),
    path('book-drf-pagination-api-view/', app_views.BookDRFPaginationAPIView.as_view()),
    path('book-list-api-view/', app_views.BookListAPIView.as_view()),
    path('book-mixin-generic-api-view/', app_views.BookMixinGenericAPIView.as_view()),
    # path('book-viewset-api-view/', app_views.BookViewSet.as_view()),
]
