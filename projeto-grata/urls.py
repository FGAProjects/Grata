from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path
from clients import views as client_views

urlpatterns = [
    path('', client_views.client_list, name='client_list'),
    path('view/<int:pk>', client_views.client_show, name='client_show'),
    path('new', client_views.client_new, name='client_new'),
    path('edit/<int:pk>', client_views.client_update, name='client_edit'),
    path('delete/<int:pk>', client_views.client_delete, name='client_delete'),
]