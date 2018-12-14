from django.urls import path
from clients import views as client_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', client_views.client_list, name='client_list'),
    path('view/<int:pk>', client_views.client_show, name='client_show'),
    path('new', client_views.client_new, name='client_new'),
    path('edit/<int:pk>', client_views.client_update, name='client_edit'),
    path('delete/<int:pk>', client_views.client_delete, name='client_delete'),
]

urlpatterns += staticfiles_urlpatterns()