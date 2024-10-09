from django.urls import path
from . import views
app_name = 'account'
urlpatterns = [
    # 模板
    path('login', views.login, name="login"),
]
