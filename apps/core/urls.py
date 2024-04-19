from django.urls import path
from django.contrib.auth.views import (
    LogoutView,
    LoginView
)
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]