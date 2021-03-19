"""
    App Urls
"""
from django.urls import path
from .views import index_api

urlpatterns = [
    path('', index_api, name='index'),
]
