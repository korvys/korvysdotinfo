# landing/urls.py
from django.urls import path
from .views import landingpage_view

urlpatterns = [
    path('', landingpage_view, name='landingpage'),
]