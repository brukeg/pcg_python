"""
todo_list urls.py
"""

from django.urls import path
from . import views

app_name = 'urlshorten'  # for name spacing
urlpatterns = [
    path('', views.index, name='index'),
    path('urlshorten/shorten', views.shorten, name='shorten'),
    path('<short_url>', views.redirectr, name='redirect'),
    ]
