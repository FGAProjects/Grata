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
    path('excluir_perfil/', client_views.client_delete, name='client_delete'),

    #Meetings
    path('reunioes/', meeting_views.list_meeting, name='meeting_list'),
    path('detalhes_reuniao/<int:pk>', meeting_views.show_meeting, name='meeting_view'),
    path('nova_reuniao/', meeting_views.new_meeting, name='meeting_new'),
    path('editar_reuniao/<int:pk>', meeting_views.edit_meeting, name='meeting_edit'),
    path('delete/<int:pk>', meeting_views.delete_meeting, name='meeting_delete'),
]


urlpatterns += staticfiles_urlpatterns()