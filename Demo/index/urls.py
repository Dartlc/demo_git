"""
    App Urls
"""
from django.urls import path
from .views import index_api, sample_api

urlpatterns = [
    path('', index_api, name='index'),
    path('sample/', sample_api, name='sample'),
]
