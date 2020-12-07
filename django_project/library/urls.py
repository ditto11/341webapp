from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('?search/', SearchView.as_view(), name='search'),
]
