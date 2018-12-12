from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from restaurants.views import home,about,contact

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',home), #ROOT
    url(r'about/$',about),
    url(r'contact/$',contact),
]
