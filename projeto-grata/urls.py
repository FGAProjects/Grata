from django.urls import path
from clients import views as client_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', client_views.client_list, name='client_list'),
    path('perfil/<int:pk>', client_views.client_show, name='client_show'),
    path('novo_usuario', client_views.new_clients, name='client_new'),
    path('alterar_cliente/<int:pk>', client_views.client_update, name='client_edit'),
    path('excluir_perfil/<int:pk>', client_views.client_delete, name='client_delete'),
]

urlpatterns += staticfiles_urlpatterns()