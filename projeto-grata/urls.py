from django.urls import path
from clients import views as client_views
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.conf.urls import url

urlpatterns = [

    url(r'^admin/', admin.site.urls),

    # path('',accounts_views.login_view, name='login'),
    url(r'^$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    path('perfil/', client_views.client_show, name='client_show'),
    path('novo_usuario', client_views.new_client, name='client_new'),
    # path('alterar_cliente/<int:pk>', client_views.client_update, name='client_edit'),
    # path('excluir_perfil/<int:pk>', client_views.client_delete, name='client_delete'),
]

urlpatterns += staticfiles_urlpatterns()