from django.contrib import admin
from django.urls import path, include
from .views import signup
from .views import user_login

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', user_login, name='login'),
]
