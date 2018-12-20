from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.conf.urls import url

from clients import views as client_views
from meetings import views as meeting_views

urlpatterns = [

    #Admin
    url(r'^admin/', admin.site.urls),

    #Login
    url(r'^$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    #Users
    path('perfil/', client_views.client_show, name='client_show'),
    path('novo_usuario', client_views.new_client, name='client_new'),
    path('editar_perfil/', client_views.client_update, name='client_edit'),
    url(r'^excluir_perfil/(?P<pk>\d+)$', client_views.ClientDelete.as_view(), name='client_delete'),

    #Meetings
    path('reuniao/', meeting_views.meeting_show, name='meeting_show'),
    path('reunioes/', meeting_views.meeting_list, name='meeting_list'),
]

urlpatterns += staticfiles_urlpatterns()