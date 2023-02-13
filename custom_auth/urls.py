from django.urls import path, include
from .views import *
urlpatterns = [
        path('signup-form/', UserCreateView.as_view(), name='user_create_form'),
]