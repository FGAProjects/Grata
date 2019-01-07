from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.conf.urls import url

from clients import views as client_views
from meetings import views as meeting_views
from topics import views as topics_views
from shedules import views as shedules_views
from pdfs import views as pdfs_views
from pdfs.views import PDF

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
    path('lista_de_usuarios/<int:pk>', client_views.list_users, name='client_list'),

    #Meetings
    path('reunioes/', meeting_views.list_meeting, name='meeting_list'),
    path('detalhes_reuniao/<int:pk>', meeting_views.show_meeting, name='meeting_show'),
    path('nova_reuniao/', meeting_views.new_meeting, name='meeting_new'),
    path('editar_reuniao/<int:pk>', meeting_views.edit_meeting, name='meeting_edit'),
    path('excluir_reuniao/<int:pk>', meeting_views.delete_meeting, name='meeting_delete'),

    #Topic
    path('novo_topico/<int:pk>', topics_views.new_topic, name='topic_new'),
    path('excluir_topico/<int:pk>/<int:pk_meeting>', topics_views.delete_topic, name='topic_delete'),

    #Shedule
    path('nova_pauta/<int:pk>', shedules_views.new_shedule, name='shedule_new'),
    path('editar_pauta/<int:pk_meeting>/<int:pk_shedule>', shedules_views.edit_shedule, name='shedule_edit'),
    path('excluir_pauta/<int:pk_meeting>/<int:pk_shedule>', shedules_views.delete_shedule, name='shedule_delete'),
    path('detalhes_pauta/<int:pk_meeting>/<int:pk_shedule>', shedules_views.show_shedule, name='shedule_show'),

    #PDF
    path('pdf/<int:pk>', PDF.as_view(), name='pdf_show'),
]

urlpatterns += staticfiles_urlpatterns()